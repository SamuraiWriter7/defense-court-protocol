#!/usr/bin/env python3
"""
Check semantic alignment among Defense Court Protocol examples.

This script checks consistency across:

- examples/defense-trace-record.example.yaml
- examples/defense-agent-rank.example.yaml
- examples/cyber-defense-constitution.example.yaml

Unlike scripts/validate_examples.py, this script does not only check
schema shape. It checks whether the validated documents are institutionally
aligned.

Usage:
    python scripts/check_constitution_alignment.py

Optional:
    python scripts/check_constitution_alignment.py --strict-warnings
"""

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError as exc:
    print("Missing dependency: PyYAML")
    print("Install with: pip install pyyaml")
    raise SystemExit(1) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]

TRACE_EXAMPLE = REPO_ROOT / "examples/defense-trace-record.example.yaml"
RANK_EXAMPLE = REPO_ROOT / "examples/defense-agent-rank.example.yaml"
CONSTITUTION_EXAMPLE = REPO_ROOT / "examples/cyber-defense-constitution.example.yaml"


@dataclass
class Issue:
    level: str
    code: str
    message: str


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file and ensure the root is a mapping."""
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


def require_mapping(data: dict[str, Any], key: str, source_name: str) -> dict[str, Any]:
    """Return a required mapping from a root object."""
    value = data.get(key)

    if not isinstance(value, dict):
        raise RuntimeError(f"Missing or invalid root key '{key}' in {source_name}")

    return value


def build_article_map(
    constitution: dict[str, Any],
    issues: list[Issue],
) -> dict[int, dict[str, Any]]:
    """Build an article map from the cyber defense constitution."""
    articles = constitution.get("articles", [])

    if not isinstance(articles, list):
        issues.append(
            Issue(
                "ERROR",
                "constitution.articles.invalid",
                "cyber_defense_constitution.articles must be a list.",
            )
        )
        return {}

    article_map: dict[int, dict[str, Any]] = {}

    for article in articles:
        if not isinstance(article, dict):
            issues.append(
                Issue(
                    "ERROR",
                    "constitution.article.invalid",
                    "Each article must be an object/map.",
                )
            )
            continue

        article_id = article.get("id")

        if not isinstance(article_id, int):
            issues.append(
                Issue(
                    "ERROR",
                    "constitution.article.id.invalid",
                    "Each article must have an integer id.",
                )
            )
            continue

        if article_id in article_map:
            issues.append(
                Issue(
                    "ERROR",
                    "constitution.article.id.duplicate",
                    f"Duplicate article id found: {article_id}",
                )
            )
            continue

        article_map[article_id] = article

    expected_ids = set(range(1, 18))
    actual_ids = set(article_map)

    missing_ids = sorted(expected_ids - actual_ids)
    extra_ids = sorted(actual_ids - expected_ids)

    if missing_ids:
        issues.append(
            Issue(
                "ERROR",
                "constitution.article.id.missing",
                f"Missing article ids: {missing_ids}",
            )
        )

    if extra_ids:
        issues.append(
            Issue(
                "ERROR",
                "constitution.article.id.extra",
                f"Unexpected article ids: {extra_ids}",
            )
        )

    return article_map


def build_rank_map(
    rank_document: dict[str, Any],
    issues: list[Issue],
) -> dict[str, dict[str, Any]]:
    """Build a rank map from the defense agent rank document."""
    ranks = rank_document.get("ranks", [])

    if not isinstance(ranks, list):
        issues.append(
            Issue(
                "ERROR",
                "rank.ranks.invalid",
                "defense_agent_rank.ranks must be a list.",
            )
        )
        return {}

    rank_map: dict[str, dict[str, Any]] = {}

    for rank_entry in ranks:
        if not isinstance(rank_entry, dict):
            issues.append(
                Issue(
                    "ERROR",
                    "rank.entry.invalid",
                    "Each rank entry must be an object/map.",
                )
            )
            continue

        rank_name = rank_entry.get("rank")

        if not isinstance(rank_name, str):
            issues.append(
                Issue(
                    "ERROR",
                    "rank.name.invalid",
                    "Each rank entry must have a string rank.",
                )
            )
            continue

        if rank_name in rank_map:
            issues.append(
                Issue(
                    "ERROR",
                    "rank.name.duplicate",
                    f"Duplicate rank found: {rank_name}",
                )
            )
            continue

        rank_map[rank_name] = rank_entry

    if len(rank_map) != 12:
        issues.append(
            Issue(
                "ERROR",
                "rank.count.invalid",
                f"Expected 12 defense ranks, found {len(rank_map)}.",
            )
        )

    return rank_map


def check_module_alignment(
    constitution: dict[str, Any],
    article_map: dict[int, dict[str, Any]],
    issues: list[Issue],
) -> None:
    """Check whether module definitions align with article declarations."""
    modules = constitution.get("modules", {})

    if not isinstance(modules, dict):
        issues.append(
            Issue(
                "ERROR",
                "constitution.modules.invalid",
                "cyber_defense_constitution.modules must be an object/map.",
            )
        )
        return

    for module_name, module_data in modules.items():
        if not isinstance(module_data, dict):
            issues.append(
                Issue(
                    "ERROR",
                    "constitution.module.invalid",
                    f"Module '{module_name}' must be an object/map.",
                )
            )
            continue

        article_ids = module_data.get("article_ids", [])

        if not isinstance(article_ids, list):
            issues.append(
                Issue(
                    "ERROR",
                    "constitution.module.article_ids.invalid",
                    f"Module '{module_name}' article_ids must be a list.",
                )
            )
            continue

        for article_id in article_ids:
            article = article_map.get(article_id)

            if article is None:
                issues.append(
                    Issue(
                        "ERROR",
                        "constitution.module.article_id.unknown",
                        f"Module '{module_name}' references unknown article id {article_id}.",
                    )
                )
                continue

            article_module = article.get("module")

            if article_module != module_name:
                issues.append(
                    Issue(
                        "ERROR",
                        "constitution.module.article_mismatch",
                        (
                            f"Article {article_id} is listed under module '{module_name}' "
                            f"but declares module '{article_module}'."
                        ),
                    )
                )


def check_trace_articles(
    trace_record: dict[str, Any],
    article_map: dict[int, dict[str, Any]],
    issues: list[Issue],
) -> set[int]:
    """Check trace applicable article references against the constitution."""
    constitutional_basis = trace_record.get("constitutional_basis", {})

    if not isinstance(constitutional_basis, dict):
        issues.append(
            Issue(
                "ERROR",
                "trace.constitutional_basis.invalid",
                "defense_trace_record.constitutional_basis must be an object/map.",
            )
        )
        return set()

    applicable_articles = constitutional_basis.get("applicable_articles", [])

    if not isinstance(applicable_articles, list):
        issues.append(
            Issue(
                "ERROR",
                "trace.applicable_articles.invalid",
                "constitutional_basis.applicable_articles must be a list.",
            )
        )
        return set()

    referenced_article_ids: set[int] = set()

    for item in applicable_articles:
        if not isinstance(item, dict):
            issues.append(
                Issue(
                    "ERROR",
                    "trace.applicable_article.invalid",
                    "Each applicable article reference must be an object/map.",
                )
            )
            continue

        article_id = item.get("id")
        article_name = item.get("name")

        if not isinstance(article_id, int):
            issues.append(
                Issue(
                    "ERROR",
                    "trace.applicable_article.id.invalid",
                    "Each applicable article must have an integer id.",
                )
            )
            continue

        referenced_article_ids.add(article_id)

        constitution_article = article_map.get(article_id)

        if constitution_article is None:
            issues.append(
                Issue(
                    "ERROR",
                    "trace.applicable_article.unknown",
                    f"Trace references unknown article id {article_id}.",
                )
            )
            continue

        constitution_title = constitution_article.get("title")

        if article_name != constitution_title:
            issues.append(
                Issue(
                    "ERROR",
                    "trace.applicable_article.name_mismatch",
                    (
                        f"Trace article id {article_id} name mismatch: "
                        f"trace='{article_name}', constitution='{constitution_title}'."
                    ),
                )
            )

    return referenced_article_ids


def action_allowed_by_rank(action_type: str, allowed_actions: list[Any]) -> bool:
    """Check whether a trace action is compatible with a rank's allowed actions."""
    allowed = {item for item in allowed_actions if isinstance(item, str)}

    if action_type in allowed:
        return True

    # emergency_containment is a composite action. It may be permitted when
    # the rank can perform containment-like actions.
    if action_type == "emergency_containment":
        return bool({"contain", "quarantine", "suspend", "emergency_containment"} & allowed)

    return False


def check_trace_rank_alignment(
    trace_record: dict[str, Any],
    rank_map: dict[str, dict[str, Any]],
    issues: list[Issue],
) -> None:
    """Check acting_agent and rank_authority against the rank architecture."""
    acting_agent = trace_record.get("acting_agent", {})
    constitutional_basis = trace_record.get("constitutional_basis", {})
    action = trace_record.get("action", {})

    if not isinstance(acting_agent, dict):
        issues.append(
            Issue(
                "ERROR",
                "trace.acting_agent.invalid",
                "defense_trace_record.acting_agent must be an object/map.",
            )
        )
        return

    if not isinstance(constitutional_basis, dict):
        issues.append(
            Issue(
                "ERROR",
                "trace.constitutional_basis.invalid",
                "defense_trace_record.constitutional_basis must be an object/map.",
            )
        )
        return

    if not isinstance(action, dict):
        issues.append(
            Issue(
                "ERROR",
                "trace.action.invalid",
                "defense_trace_record.action must be an object/map.",
            )
        )
        return

    acting_rank = acting_agent.get("rank")
    acting_role = acting_agent.get("role")
    rank_authority = constitutional_basis.get("rank_authority")
    action_type = action.get("type")

    if acting_rank not in rank_map:
        issues.append(
            Issue(
                "ERROR",
                "trace.acting_agent.rank.unknown",
                f"Trace acting_agent.rank is not defined in Defense Agent Rank: {acting_rank}",
            )
        )
        return

    if rank_authority not in rank_map:
        issues.append(
            Issue(
                "ERROR",
                "trace.rank_authority.unknown",
                f"Trace rank_authority is not defined in Defense Agent Rank: {rank_authority}",
            )
        )

    if acting_rank != rank_authority:
        issues.append(
            Issue(
                "ERROR",
                "trace.rank_authority.mismatch",
                (
                    f"acting_agent.rank '{acting_rank}' does not match "
                    f"constitutional_basis.rank_authority '{rank_authority}'."
                ),
            )
        )

    rank_definition = rank_map[acting_rank]
    expected_role = rank_definition.get("role")

    if acting_role != expected_role:
        issues.append(
            Issue(
                "WARNING",
                "trace.acting_agent.role_mismatch",
                (
                    f"acting_agent.role '{acting_role}' differs from rank definition "
                    f"role '{expected_role}' for rank '{acting_rank}'."
                ),
            )
        )

    allowed_actions = rank_definition.get("allowed_actions", [])

    if not isinstance(action_type, str):
        issues.append(
            Issue(
                "ERROR",
                "trace.action.type.invalid",
                "defense_trace_record.action.type must be a string.",
            )
        )
        return

    if not isinstance(allowed_actions, list):
        issues.append(
            Issue(
                "ERROR",
                "rank.allowed_actions.invalid",
                f"Rank '{acting_rank}' allowed_actions must be a list.",
            )
        )
        return

    if not action_allowed_by_rank(action_type, allowed_actions):
        issues.append(
            Issue(
                "ERROR",
                "trace.action.not_allowed_by_rank",
                (
                    f"Action type '{action_type}' is not allowed by rank '{acting_rank}'. "
                    f"Allowed actions: {allowed_actions}"
                ),
            )
        )


def check_emergency_containment_rules(
    trace_record: dict[str, Any],
    referenced_article_ids: set[int],
    issues: list[Issue],
) -> None:
    """Check special requirements for emergency containment traces."""
    action = trace_record.get("action", {})
    safeguards = trace_record.get("safeguards", {})

    if not isinstance(action, dict):
        return

    action_type = action.get("type")

    if action_type != "emergency_containment":
        return

    required_articles = {5, 6, 9}
    missing_articles = sorted(required_articles - referenced_article_ids)

    if missing_articles:
        issues.append(
            Issue(
                "ERROR",
                "trace.emergency_containment.required_articles_missing",
                (
                    "Emergency containment should reference Articles 5, 6, and 9. "
                    f"Missing: {missing_articles}"
                ),
            )
        )

    if 17 not in referenced_article_ids:
        issues.append(
            Issue(
                "WARNING",
                "trace.emergency_containment.collective_review_missing",
                (
                    "Emergency containment should usually reference Article 17 "
                    "when major review is required."
                ),
            )
        )

    reversible = action.get("reversible")

    if reversible is not True:
        issues.append(
            Issue(
                "WARNING",
                "trace.emergency_containment.not_reversible",
                "Emergency containment should be reversible whenever possible.",
            )
        )

    if not isinstance(safeguards, dict):
        issues.append(
            Issue(
                "ERROR",
                "trace.safeguards.invalid",
                "defense_trace_record.safeguards must be an object/map.",
            )
        )
        return

    expected_safeguards = {
        "command_authentication": "passed",
        "scope_check": "passed",
        "blast_radius_limit": "enabled",
        "rollback_plan": "available",
        "human_notification": "sent",
    }

    for key, expected_value in expected_safeguards.items():
        actual_value = safeguards.get(key)

        if actual_value != expected_value:
            issues.append(
                Issue(
                    "ERROR",
                    "trace.emergency_containment.safeguard_invalid",
                    (
                        f"Emergency containment safeguard '{key}' should be "
                        f"'{expected_value}', found '{actual_value}'."
                    ),
                )
            )


def check_review_rules(
    trace_record: dict[str, Any],
    rank_map: dict[str, dict[str, Any]],
    issues: list[Issue],
) -> None:
    """Check review and human review consistency."""
    severity = trace_record.get("severity")
    review = trace_record.get("review", {})
    acting_agent = trace_record.get("acting_agent", {})
    action = trace_record.get("action", {})

    if not isinstance(review, dict):
        issues.append(
            Issue(
                "ERROR",
                "trace.review.invalid",
                "defense_trace_record.review must be an object/map.",
            )
        )
        return

    human_review_status = review.get("human_review_status")
    governance_status = review.get("governance_status")

    if severity == "critical" and human_review_status == "not_required":
        issues.append(
            Issue(
                "ERROR",
                "trace.critical.human_review_not_required",
                "Critical incidents must not set human_review_status to 'not_required'.",
            )
        )

    acting_rank = acting_agent.get("rank") if isinstance(acting_agent, dict) else None
    rank_definition = rank_map.get(acting_rank)

    if severity == "critical" and rank_definition:
        triggers = rank_definition.get("requires_human_review_for", [])

        if isinstance(triggers, list) and "critical_incident" not in triggers:
            issues.append(
                Issue(
                    "WARNING",
                    "rank.critical_review_trigger.missing",
                    (
                        f"Rank '{acting_rank}' does not list 'critical_incident' "
                        "in requires_human_review_for."
                    ),
                )
            )

    action_type = action.get("type") if isinstance(action, dict) else None

    if action_type == "recover" and governance_status != "recovery_approved":
        issues.append(
            Issue(
                "ERROR",
                "trace.recover.governance_not_approved",
                (
                    "Recovery actions require review.governance_status "
                    "to be 'recovery_approved'."
                ),
            )
        )

    if action_type == "recover" and human_review_status not in {"approved", "not_required"}:
        issues.append(
            Issue(
                "WARNING",
                "trace.recover.human_review_pending",
                (
                    "Recovery action has not been clearly approved by human review. "
                    f"human_review_status='{human_review_status}'."
                ),
            )
        )


def check_alignment() -> list[Issue]:
    """Run all semantic alignment checks."""
    issues: list[Issue] = []

    trace_root = load_yaml(TRACE_EXAMPLE)
    rank_root = load_yaml(RANK_EXAMPLE)
    constitution_root = load_yaml(CONSTITUTION_EXAMPLE)

    trace_record = require_mapping(
        trace_root,
        "defense_trace_record",
        "examples/defense-trace-record.example.yaml",
    )
    rank_document = require_mapping(
        rank_root,
        "defense_agent_rank",
        "examples/defense-agent-rank.example.yaml",
    )
    constitution = require_mapping(
        constitution_root,
        "cyber_defense_constitution",
        "examples/cyber-defense-constitution.example.yaml",
    )

    article_map = build_article_map(constitution, issues)
    rank_map = build_rank_map(rank_document, issues)

    check_module_alignment(constitution, article_map, issues)
    referenced_article_ids = check_trace_articles(trace_record, article_map, issues)
    check_trace_rank_alignment(trace_record, rank_map, issues)
    check_emergency_containment_rules(trace_record, referenced_article_ids, issues)
    check_review_rules(trace_record, rank_map, issues)

    return issues


def print_issues(issues: list[Issue]) -> None:
    """Print alignment issues."""
    if not issues:
        print("Constitution alignment passed.")
        return

    for issue in issues:
        print(f"[{issue.level}] {issue.code}")
        print(f"  {issue.message}")


def main() -> int:
    """Run semantic alignment checks."""
    parser = argparse.ArgumentParser(
        description="Check semantic alignment across Defense Court Protocol examples."
    )
    parser.add_argument(
        "--strict-warnings",
        action="store_true",
        help="Treat warnings as errors.",
    )

    args = parser.parse_args()

    print("Checking Defense Court Protocol constitution alignment...")
    print(f"Trace example:        {TRACE_EXAMPLE.relative_to(REPO_ROOT)}")
    print(f"Rank example:         {RANK_EXAMPLE.relative_to(REPO_ROOT)}")
    print(f"Constitution example: {CONSTITUTION_EXAMPLE.relative_to(REPO_ROOT)}")
    print()

    try:
        issues = check_alignment()
    except RuntimeError as exc:
        print("Constitution alignment failed.")
        print(str(exc))
        return 1

    print_issues(issues)

    errors = [issue for issue in issues if issue.level == "ERROR"]
    warnings = [issue for issue in issues if issue.level == "WARNING"]

    print()
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print()
        print("Constitution alignment failed.")
        return 1

    if warnings and args.strict_warnings:
        print()
        print("Constitution alignment failed because --strict-warnings is enabled.")
        return 1

    print()
    print("All constitution alignment checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
