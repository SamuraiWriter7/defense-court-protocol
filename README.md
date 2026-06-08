# Defense Court Protocol

**Defense Court Protocol** is a governance kernel for AI cyber defense.

It defines a structured defensive operating model for multi-agent AI systems by integrating:

* defensive agent ranks
* a Seventeen-Article Cyber Defense Charter
* traceability
* emergency containment
* governance review
* semantic alignment checks
* human oversight

The goal is not to create a status hierarchy among AI agents.

The goal is to define **responsibility, authority, traceability, review, safe defensive coordination, and institutional consistency**.

---

## Overview

Modern cyber defense increasingly faces high-speed, automated, and AI-assisted threats.

Traditional IT operations often emphasize continuity and availability:

```text
Keep systems running.
Avoid shutdown.
Wait for human approval.
Escalate through slow review paths.
```

However, fast-moving cyber incidents require a different operating model.

The Defense Court Protocol introduces the principle of:

```text
The courage to stop.
```

Under clearly defined emergency conditions, AI defense agents may perform limited, scoped, reversible, and traceable containment actions before full human review.

Human review still preserves final legitimacy.

In short:

```text
AI may contain.
Verification must review.
Governance may pause.
Humans finalize legitimacy.
```

---

## Core Concept

The Defense Court Protocol is built on five layers:

```text
Rank Layer
  Defines defensive agent roles, authority scopes, and responsibility boundaries.

Article Layer
  Defines behavioral, procedural, ethical, traceability, and safety rules.

Defense Kernel
  Defines emergency detection, containment, isolation, and recovery rules.

Trace Layer
  Records actions, decisions, evidence, safeguards, review status, and responsibility.

Human Review Layer
  Preserves final human responsibility, legitimacy, and governance oversight.
```

The core structure can be summarized as:

```text
Rank defines responsibility.
Articles define behavior.
Trace defines accountability.
Governance defines safety.
Human Review defines legitimacy.
```

---

## Core Principles

The Defense Court Protocol follows these principles:

```text
No untraceable command.
No irreversible action without review.
No autonomous escalation without scope.
No defense action without logging.
No recovery without verification.
No public-risk incident without disclosure path.
```

These principles ensure that AI cyber defense can be fast without becoming lawless.

---

## Key Documents

* [Defense Court Protocol](docs/defense-court-protocol.md)
  Defines the overall cyber defense governance kernel for multi-agent AI systems.

* [Defense Trace Protocol](docs/defense-trace-protocol.md)
  Defines the traceability, accountability, verification, recovery, governance, and human review model for defensive AI actions.

* [Defense Agent Rank Architecture](docs/defense-agent-rank-architecture.md)
  Defines the defensive AI agent rank system, including roles, authority scopes, responsibility boundaries, trace requirements, and human review triggers.

* [Cyber Defense Seventeen Articles](docs/cyber-defense-seventeen-articles.md)
  Defines the Seventeen-Article Cyber Defense Charter as the behavioral, procedural, ethical, traceability, and safety constitution of the Defense Court Protocol.

* [Constitution Alignment Model](docs/constitution-alignment-model.md)
  Defines the semantic validation layer of the Defense Court Protocol, checking institutional consistency among Trace Records, Agent Ranks, and the Cyber Defense Constitution.

---

## Core Pillars

The protocol currently has three validated pillars.

### 1. Defense Trace Record

The Defense Trace Record defines how defensive actions are recorded.

It answers:

```text
What happened?
Who acted?
Why was action taken?
Which authority was used?
Which articles applied?
Was the action reversible?
Were safeguards applied?
Was human review required?
What must happen next?
```

Files:

```text
schemas/defense-trace-record.schema.json
examples/defense-trace-record.example.yaml
```

---

### 2. Defense Agent Rank

The Defense Agent Rank model defines defensive AI roles and authority scopes.

It adapts a twelve-rank structure into a cyber defense context.

The ranks include:

```text
Daitoku  = Defense Grand Orchestrator
Shotoku  = Incident Coordinator
Daijin   = Human Impact Agent
Shojin   = User Context Agent
Dairei   = Defense Protocol Agent
Shorei   = Procedure Agent
Daishin  = Forensic Verification Agent
Shoshin  = Detection Test Agent
Daigi    = Cyber Governance Agent
Shogi    = Risk Filter Agent
Daichi   = Threat Strategy Agent
Shochi   = Threat Research Agent
```

Files:

```text
schemas/defense-agent-rank.schema.json
examples/defense-agent-rank.example.yaml
```

---

### 3. Cyber Defense Constitution

The Cyber Defense Constitution defines the Seventeen-Article Cyber Defense Charter.

It provides behavioral and procedural discipline for defensive AI agents.

The Articles are grouped into five modules:

```text
Synchronization Module
Authority Module
Protocol Module
Trace and Trust Module
Safety and Containment Module
```

Files:

```text
schemas/cyber-defense-constitution.schema.json
examples/cyber-defense-constitution.example.yaml
```

---

## Architecture

The Defense Court Protocol can be understood as an AI cyber defense institution.

```text
Human / Orchestrator
        ↓
Defense Grand Orchestrator
        ↓
Defense Agent Ranks
        ↓
Cyber Defense Seventeen Articles
        ↓
Defense Kernel
        ↓
Defense Trace Log
        ↓
Verification / Governance Review
        ↓
Human Review
        ↓
Recovery / Disclosure / Improvement
```

This structure allows AI agents to act quickly while remaining reviewable, bounded, and human-legitimate.

---

## Inner Loop and Outer Loop

The protocol separates emergency response into two loops.

### Inner Loop

The Inner Loop is the AI immediate response layer.

Typical actions include:

```text
observe
warn
contain
quarantine
suspend
preserve evidence
notify governance
notify human reviewers
```

Inner Loop actions must be:

* scoped
* logged
* justified
* reversible when possible
* automatically reported
* subject to later human review

### Outer Loop

The Outer Loop is the human review and governance layer.

Typical actions include:

```text
review incident evidence
confirm or reject containment
approve recovery
assess legal obligations
notify users or stakeholders if needed
update protocols and detection rules
record contribution and correction events
```

The separation is simple:

```text
AI may perform emergency containment.
AI must not finalize legitimacy.
Human review determines legitimacy.
Verification determines recovery readiness.
Governance determines boundary compliance.
```

---

## Repository Structure

```text
docs/
  defense-court-protocol.md
  defense-trace-protocol.md
  defense-agent-rank-architecture.md
  cyber-defense-seventeen-articles.md
  constitution-alignment-model.md

schemas/
  defense-trace-record.schema.json
  defense-agent-rank.schema.json
  cyber-defense-constitution.schema.json

examples/
  defense-trace-record.example.yaml
  defense-agent-rank.example.yaml
  cyber-defense-constitution.example.yaml

scripts/
  validate_examples.py
  check_constitution_alignment.py

.github/
  workflows/
    validate-examples.yml
```

---

## Validation

This repository performs two layers of validation:

```text
Schema Validation
  Checks whether YAML examples conform to JSON Schemas.

Semantic Validation
  Checks whether the Trace, Rank, and Constitution examples are institutionally aligned.
```

Together, these validations ensure both structural correctness and governance consistency.

---

## Schema Validation

Schema validation checks whether each YAML example matches its corresponding JSON Schema.

Required Python packages:

```text
PyYAML
jsonschema
```

Install dependencies:

```bash
pip install pyyaml jsonschema
```

Run schema validation:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
Validating target: Defense Trace Record
Validation passed.

Validating target: Defense Agent Rank
Validation passed.

Validating target: Cyber Defense Constitution
Validation passed.

All validations passed.
```

Current schema validation targets:

```text
Defense Trace Record
  Schema:  schemas/defense-trace-record.schema.json
  Example: examples/defense-trace-record.example.yaml

Defense Agent Rank
  Schema:  schemas/defense-agent-rank.schema.json
  Example: examples/defense-agent-rank.example.yaml

Cyber Defense Constitution
  Schema:  schemas/cyber-defense-constitution.schema.json
  Example: examples/cyber-defense-constitution.example.yaml
```

---

## Semantic Validation

Semantic validation checks whether the validated examples are meaningfully aligned as a governance system.

It is performed by:

```text
scripts/check_constitution_alignment.py
```

This script checks consistency across:

```text
examples/defense-trace-record.example.yaml
examples/defense-agent-rank.example.yaml
examples/cyber-defense-constitution.example.yaml
```

It verifies conditions such as:

```text
Trace Record applicable article IDs exist in the Cyber Defense Constitution.
Trace Record applicable article names match the Constitution article titles.
Trace Record acting_agent.rank exists in the Defense Agent Rank document.
Trace Record rank_authority matches acting_agent.rank.
Emergency containment references the required Articles 5, 6, and 9.
Critical incidents do not bypass human review.
Recovery actions require proper governance approval.
Constitution module definitions match article module declarations.
```

For the conceptual model behind semantic validation, see:

* [Constitution Alignment Model](docs/constitution-alignment-model.md)

Run semantic validation:

```bash
python scripts/check_constitution_alignment.py
```

Expected output:

```text
Checking Defense Court Protocol constitution alignment...

Constitution alignment passed.

Errors: 0
Warnings: 0

All constitution alignment checks passed.
```

Warnings can be treated as errors by running:

```bash
python scripts/check_constitution_alignment.py --strict-warnings
```

Semantic validation is important because JSON Schema can verify document shape, but it cannot fully verify institutional meaning.

In short:

```text
Schema Validation
  = checks whether the documents are structurally valid.

Semantic Validation
  = checks whether the documents agree with each other as a governance system.
```

This gives the Defense Court Protocol both a gatekeeper and a magistrate.

---

## GitHub Actions

The repository includes a GitHub Actions workflow:

```text
.github/workflows/validate-examples.yml
```

The workflow runs on:

```text
push
pull_request
workflow_dispatch
```

It performs:

```text
1. Schema validation
2. Constitution alignment validation
```

Workflow checks:

```bash
python scripts/validate_examples.py
python scripts/check_constitution_alignment.py
```

This ensures that changes to schemas, examples, ranks, articles, or trace records remain both structurally valid and institutionally aligned.

---

## Validated Files

Current validation targets:

```text
Defense Trace Record
  Schema:  schemas/defense-trace-record.schema.json
  Example: examples/defense-trace-record.example.yaml

Defense Agent Rank
  Schema:  schemas/defense-agent-rank.schema.json
  Example: examples/defense-agent-rank.example.yaml

Cyber Defense Constitution
  Schema:  schemas/cyber-defense-constitution.schema.json
  Example: examples/cyber-defense-constitution.example.yaml
```

Current semantic alignment inputs:

```text
Trace Example:
  examples/defense-trace-record.example.yaml

Rank Example:
  examples/defense-agent-rank.example.yaml

Constitution Example:
  examples/cyber-defense-constitution.example.yaml
```

---

## Design Philosophy

The Defense Court Protocol is based on the idea that cyber defense should be:

```text
fast but bounded
automated but reviewable
structured but adaptable
traceable but not bureaucratic
human-supervised but not paralyzed
```

In emergency conditions, waiting too long can increase harm.

But unrestricted automation can also create new harm.

The protocol therefore balances speed and restraint.

```text
Contain fast.
Recover carefully.
Review honestly.
Record everything significant.
```

---

## Non-Goals

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

The Defense Court Protocol is defensive, governance-oriented, traceable, and human-reviewed.

---

## Relationship to Royalty OS

The Defense Court Protocol can connect to Royalty OS by recording defensive contribution and correction events.

Potential contribution events include:

```text
detection contribution
containment contribution
forensic contribution
governance contribution
recovery contribution
documentation contribution
research contribution
risk reduction event
```

Potential correction events include:

```text
false positive correction
over-containment prevention
missed signal review
protocol correction
recovery improvement
governance refinement
```

This allows defense value to be recorded without rewarding only dramatic action.

A mature defense system should recognize quiet prevention, careful verification, and honest correction.

---

## Roadmap

Planned future work:

```text
v0.2
  - richer incident classification
  - expanded severity model
  - incident lifecycle status
  - evidence reference fields
  - expanded semantic alignment checks

v0.3
  - authority matrix between ranks and action classes
  - escalation path validation
  - recovery gate validation

v0.4
  - signature and provenance fields
  - agent identity / AOC integration
  - command authentication evidence

v0.5
  - Royalty OS contribution event integration
  - fault and correction event model

v1.0
  - formal conformance profile
  - operational implementation guide
  - governance review checklist
```

---

## Summary

Defense Court Protocol is a governance kernel for AI cyber defense.

It defines:

```text
Rank for responsibility.
Articles for behavior.
Defense Kernel for emergency response.
Trace for accountability.
Governance for safety.
Human Review for legitimacy.
Semantic Validation for institutional consistency.
```

In this model:

```text
The Twelve-Rank structure forms the defensive organization.
The Seventeen-Article Charter forms the defensive discipline.
The Trace Protocol forms the battle record.
The Governance Layer prevents overreach.
The Human Review Layer preserves final responsibility.
The Semantic Alignment Checker verifies institutional consistency.
```

The result is an AI cyber defense system that can act quickly without becoming lawless, and remain governed without becoming too slow.
