# Changelog

All notable changes to this project will be documented in this file.

This project follows a simple changelog structure inspired by [Keep a Changelog](https://keepachangelog.com/), with unreleased changes recorded first.

---

## [Unreleased]

### Added

* Added `docs/defense-court-protocol.md` as the core documentation for the Defense Court Protocol.

* Added `docs/defense-trace-protocol.md`, defining the traceability, accountability, verification, recovery, governance, and human review model for defensive AI actions.

* Added `docs/defense-agent-rank-architecture.md`, defining the AI Twelve-Rank Defense Agent Architecture, including defensive roles, authority scopes, responsibility boundaries, trace requirements, and human review triggers.

* Added `docs/cyber-defense-seventeen-articles.md`, defining the Seventeen-Article Cyber Defense Charter as the behavioral constitution of the Defense Court Protocol.

* Added `schemas/defense-trace-record.schema.json` for validating Defense Trace Records.

* Added `examples/defense-trace-record.example.yaml` as a valid emergency containment trace record example.

* Added `schemas/defense-agent-rank.schema.json` for validating the AI Twelve-Rank Defense Agent Architecture.

* Added `examples/defense-agent-rank.example.yaml` as a valid defensive agent rank example, including ranks, roles, authority scopes, allowed actions, trace requirements, and human review triggers.

* Added `schemas/cyber-defense-constitution.schema.json` for validating the AI Seventeen-Article Cyber Defense Charter.

* Added `examples/cyber-defense-constitution.example.yaml` as a valid cyber defense constitution example, including modules, articles, trace requirements, and human review triggers.

* Added `scripts/validate_examples.py` to validate YAML examples against JSON Schemas.

* Added `.github/workflows/validate-examples.yml` to run schema validation through GitHub Actions.

### Changed

* Updated `README.md` with the Defense Court Protocol overview, core principles, key documents, repository structure, validation instructions, GitHub Actions workflow, and roadmap.
* Updated the documentation structure to reflect the three core Defense Court Protocol pillars:

  * Trace
  * Rank
  * Articles

### Fixed

* Updated `schemas/cyber-defense-constitution.schema.json` to allow `severity` as a valid trace requirement.
* Resolved schema validation mismatch between `cyber-defense-constitution.example.yaml` and `cyber-defense-constitution.schema.json`.

---

## [0.1.0-candidate] - 2026-06-08

### Added

* Initial candidate structure for the Defense Court Protocol.
* Defined the Defense Court Protocol as a governance kernel for AI cyber defense.
* Introduced the core operating model:

```text
Rank defines responsibility.
Articles define behavior.
Trace defines accountability.
Governance defines safety.
Human Review defines legitimacy.
```

* Introduced the Inner Loop / Outer Loop model:

  * Inner Loop: AI immediate, scoped, traceable emergency response.
  * Outer Loop: human review, governance, legal assessment, recovery approval, and policy correction.

* Introduced the three validated protocol pillars:

  * Defense Trace Record
  * Defense Agent Rank
  * Cyber Defense Constitution

* Introduced the core defense principles:

```text
No untraceable command.
No irreversible action without review.
No autonomous escalation without scope.
No defense action without logging.
No recovery without verification.
No public-risk incident without disclosure path.
```

### Documentation

* Added the core Defense Court Protocol documentation.
* Added trace protocol documentation.
* Added rank architecture documentation.
* Added cyber defense Seventeen Articles documentation.
* Added README documentation for repository structure, validation, roadmap, and design philosophy.

### Validation

* Added JSON Schema validation for:

  * `examples/defense-trace-record.example.yaml`
  * `examples/defense-agent-rank.example.yaml`
  * `examples/cyber-defense-constitution.example.yaml`

* Added GitHub Actions workflow for automated validation.

---

## Notes

The Defense Court Protocol is defensive, governance-oriented, traceable, and human-reviewed.

This repository does not provide:

* offensive cyber techniques
* exploit instructions
* malware behavior
* intrusion guidance
* evasion methods
* unauthorized access methods
* fully autonomous legal judgment
* fully autonomous public disclosure
* fully autonomous irreversible action

The purpose of this project is to define a structured governance model for AI cyber defense systems that can respond quickly without becoming lawless, and remain governed without becoming too slow.
