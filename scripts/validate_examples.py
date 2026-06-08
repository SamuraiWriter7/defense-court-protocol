#!/usr/bin/env python3
"""
Validate example YAML files against JSON Schema files.

Required Python packages:
- PyYAML
- jsonschema

Usage:
    python scripts/validate_examples.py
"""

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print("Missing dependency: PyYAML")
    print("Install with: pip install pyyaml")
    raise SystemExit(1) from exc

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError as exc:
    print("Missing dependency: jsonschema")
    print("Install with: pip install jsonschema")
    raise SystemExit(1) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]


VALIDATION_TARGETS = [
       {
        "name": "Defense Trace Record",
        "schema": "schemas/defense-trace-record.schema.json",
        "example": "examples/defense-trace-record.example.yaml",
    },
    {
        "name": "Defense Agent Rank",
        "schema": "schemas/defense-agent-rank.schema.json",
        "example": "examples/defense-agent-rank.example.yaml",
    },
    {
        "name": "Cyber Defense Constitution",
        "schema": "schemas/cyber-defense-constitution.schema.json",
        "example": "examples/cyber-defense-constitution.example.yaml",
    },
]


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in {path}: {exc}") from exc


def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"YAML file not found: {path}") from exc
    except yaml.YAMLError as exc:
        raise RuntimeError(f"Invalid YAML in {path}: {exc}") from exc

    if data is None:
        raise RuntimeError(f"YAML file is empty: {path}")

    if not isinstance(data, dict):
        raise RuntimeError(f"YAML root must be an object/map: {path}")

    return data


def format_error_path(error: ValidationError) -> str:
    """Return a readable JSON path for a validation error."""
    if not error.absolute_path:
        return "$"

    path_parts = ["$"]

    for part in error.absolute_path:
        if isinstance(part, int):
            path_parts.append(f"[{part}]")
        else:
            path_parts.append(f".{part}")

    return "".join(path_parts)


def validate_target(target: dict) -> bool:
    """Validate one example file against one schema file."""
    name = target["name"]
    schema_path = REPO_ROOT / target["schema"]
    example_path = REPO_ROOT / target["example"]

    print(f"Validating target: {name}")
    print(f"Validating example: {target['example']}")
    print(f"Using schema: {target['schema']}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    try:
        Draft202012Validator.check_schema(schema)
    except SchemaError as exc:
        raise RuntimeError(f"Invalid JSON Schema in {schema_path}: {exc}") from exc

    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )

    errors = sorted(
        validator.iter_errors(example),
        key=lambda error: list(error.absolute_path),
    )

    if errors:
        print()
        print("Validation failed.")
        print(f"Target: {name}")

        for error in errors:
            print(f"- Path: {format_error_path(error)}")
            print(f"  Error: {error.message}")

        print()
        return False

    print("Validation passed.")
    print()
    return True


def main() -> int:
    """Run all validation targets."""
    all_passed = True

    if not VALIDATION_TARGETS:
        print("No validation targets defined.")
        return 0

    for target in VALIDATION_TARGETS:
        try:
            passed = validate_target(target)
        except RuntimeError as exc:
            print()
            print("Validation failed.")
            print(str(exc))
            print()
            passed = False

        if not passed:
            all_passed = False

    if not all_passed:
        return 1

    print("All validations passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
