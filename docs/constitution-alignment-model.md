# Constitution Alignment Model v0.1

**Status:** Draft
**Layer:** Semantic Validation Layer / Governance Layer
**Related Concepts:** Defense Court Protocol, Defense Trace Protocol, Defense Agent Rank Architecture, Cyber Defense Seventeen Articles, Semantic Validation, Human Review
**Script:** `scripts/check_constitution_alignment.py`

---

## 1. Overview

The **Constitution Alignment Model** defines how the core documents of the Defense Court Protocol are checked for semantic consistency.

The Defense Court Protocol has three core validated pillars:

```text
Defense Trace Record
Defense Agent Rank
Cyber Defense Constitution
```

JSON Schema validation verifies that each document has the correct structure.

However, structural correctness alone is not enough.

A trace record can be structurally valid while still referring to an article that does not exist.
A rank can be structurally valid while still lacking the authority required for an action.
A constitution can be structurally valid while its module definitions and article declarations are inconsistent.

The Constitution Alignment Model addresses this second layer of validation.

```text
Schema Validation
  = checks whether each document is structurally valid.

Constitution Alignment
  = checks whether the documents agree with each other as a governance system.
```

In short:

```text
Schema Validation checks the form.
Constitution Alignment checks the institution.
```

---

## 2. Purpose

The purpose of the Constitution Alignment Model is to ensure that Defense Court Protocol examples are not only valid as files, but also coherent as a governance system.

It verifies that:

* Trace Records reference valid constitutional articles.
* Trace Records use article names consistent with the Cyber Defense Constitution.
* Acting agents use ranks defined in the Defense Agent Rank document.
* Rank authority matches the acting agent rank.
* Emergency containment references required defense articles.
* Critical incidents do not bypass human review.
* Recovery actions require proper governance approval.
* Constitution modules correctly match article declarations.

This creates a second level of protocol assurance.

```text
No institutional claim without alignment.
No trace legitimacy without constitutional basis.
No rank authority without rank definition.
No recovery without governance approval.
```

---

## 3. Validation Layers

The Defense Court Protocol uses two validation layers.

### 3.1 Schema Validation

Schema validation is performed by:

```text
scripts/validate_examples.py
```

It checks examples against JSON Schemas.

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

Schema validation answers:

```text
Is the document well-formed?
Are required fields present?
Are enum values valid?
Are unexpected properties rejected?
```

### 3.2 Semantic Validation

Semantic validation is performed by:

```text
scripts/check_constitution_alignment.py
```

It checks whether the validated examples are institutionally aligned.

Semantic validation answers:

```text
Do the documents agree with each other?
Does the trace refer to valid constitutional articles?
Does the acting agent rank exist?
Does the rank authority match the acting agent?
Does emergency containment follow constitutional requirements?
Does critical severity require human review?
```

This is the layer where the Defense Court Protocol begins to behave like a governed system rather than a collection of files.

---

## 4. Core Alignment Equation

The Constitution Alignment Model is based on this equation:

```text
Institutional Validity =
Trace × Rank × Articles × Governance × Human Review
```

More explicitly:

```text
Trace identifies what happened.
Rank identifies who had authority.
Articles identify why the action was justified.
Governance checks whether the action stayed within bounds.
Human Review preserves legitimacy.
```

If one of these elements is missing or inconsistent, the protocol may still be syntactically valid, but institutionally weak.

---

## 5. Alignment Inputs

The alignment checker currently uses three example files as inputs.

```text
examples/defense-trace-record.example.yaml
examples/defense-agent-rank.example.yaml
examples/cyber-defense-constitution.example.yaml
```

These represent the three pillars of the protocol.

### 5.1 Defense Trace Record

The Defense Trace Record provides the event being reviewed.

It contains:

```text
trace_id
timestamp
severity
incident
acting_agent
constitutional_basis
action
safeguards
review
```

It answers:

```text
What happened?
Who acted?
Why was action taken?
Which authority was used?
Which articles applied?
What review remains pending?
```

### 5.2 Defense Agent Rank

The Defense Agent Rank document defines the role and authority system.

It contains:

```text
ranks
roles
categories
responsibilities
authority scopes
allowed actions
trace requirements
human review triggers
```

It answers:

```text
Who may act?
What may they do?
What is their authority scope?
When is trace required?
When is human review required?
```

### 5.3 Cyber Defense Constitution

The Cyber Defense Constitution defines the Seventeen-Article Defense Charter.

It contains:

```text
core principles
modules
articles
rules
required behaviors
prohibited behaviors
trace requirements
human review triggers
```

It answers:

```text
How must agents behave?
Which articles justify an action?
Which behaviors are required or prohibited?
Which situations require human review?
```

---

## 6. Alignment Checks

The current alignment checker performs the following checks.

---

### 6.1 Article Existence Check

The checker verifies that every article referenced by a Defense Trace Record exists in the Cyber Defense Constitution.

Example trace reference:

```yaml
constitutional_basis:
  applicable_articles:
    - id: 5
      name: "Safety Over Availability"
```

The checker confirms that Article 5 exists in:

```text
examples/cyber-defense-constitution.example.yaml
```

If the trace refers to an unknown article ID, the checker reports an error.

Purpose:

```text
A trace must not claim constitutional authority from a non-existent article.
```

---

### 6.2 Article Name Consistency Check

The checker verifies that the article name in the Defense Trace Record matches the title in the Cyber Defense Constitution.

For example:

```yaml
- id: 9
  name: "Trace and Trust"
```

must match:

```yaml
- id: 9
  title: "Trace and Trust"
```

If the ID exists but the name differs, the checker reports an error.

Purpose:

```text
A trace must not silently drift from the official constitutional text.
```

---

### 6.3 Rank Existence Check

The checker verifies that the acting agent rank in the Defense Trace Record exists in the Defense Agent Rank document.

Example:

```yaml
acting_agent:
  rank: "Daigi"
```

The checker confirms that `Daigi` is defined in:

```text
examples/defense-agent-rank.example.yaml
```

Purpose:

```text
An agent must not claim authority from an undefined rank.
```

---

### 6.4 Rank Authority Consistency Check

The checker verifies that:

```text
acting_agent.rank
```

matches:

```text
constitutional_basis.rank_authority
```

Example:

```yaml
acting_agent:
  rank: "Daigi"

constitutional_basis:
  rank_authority: "Daigi"
```

If these differ, the checker reports an error.

Purpose:

```text
The agent who acts and the rank authority used must be institutionally consistent.
```

---

### 6.5 Role Consistency Check

The checker compares the acting agent role in the Defense Trace Record with the role defined for that rank in the Defense Agent Rank document.

Example:

```yaml
acting_agent:
  rank: "Daigi"
  role: "Cyber Governance Agent"
```

must match the rank definition:

```yaml
rank: "Daigi"
role: "Cyber Governance Agent"
```

If the role differs, the checker reports a warning.

Purpose:

```text
Role drift should be detected before it becomes authority drift.
```

This is currently a warning rather than an error because some implementations may allow role aliases in future versions.

---

### 6.6 Action Allowed by Rank Check

The checker verifies that the action type in the Defense Trace Record is compatible with the acting rank's allowed actions.

Example:

```yaml
action:
  type: "emergency_containment"
```

For `emergency_containment`, the checker allows the action when the rank permits one of the containment-like actions:

```text
contain
quarantine
suspend
emergency_containment
```

Purpose:

```text
A rank must not perform actions outside its defined authority.
```

---

### 6.7 Emergency Containment Article Check

For emergency containment, the checker requires that the trace references the key containment-related articles:

```text
Article 5: Safety Over Availability
Article 6: Containment of Harm
Article 9: Trace and Trust
```

If any are missing, the checker reports an error.

Article 17 is also recommended for major emergency containment:

```text
Article 17: Collective Review
```

If Article 17 is missing, the checker reports a warning.

Purpose:

```text
Emergency containment must be grounded in safety, containment, traceability, and review.
```

---

### 6.8 Emergency Safeguard Check

For emergency containment, the checker verifies key safeguards.

Expected values:

```yaml
safeguards:
  command_authentication: "passed"
  scope_check: "passed"
  blast_radius_limit: "enabled"
  rollback_plan: "available"
  human_notification: "sent"
```

If any expected safeguard is missing or set incorrectly, the checker reports an error.

Purpose:

```text
Emergency authority must remain bounded, reversible where possible, and reviewable.
```

---

### 6.9 Critical Incident Human Review Check

If a trace record has:

```yaml
severity: "critical"
```

then:

```yaml
human_review_status: "not_required"
```

is not allowed.

Purpose:

```text
Critical incidents must not bypass human review.
```

---

### 6.10 Recovery Governance Check

If the action type is:

```yaml
action:
  type: "recover"
```

then the governance status must be:

```yaml
review:
  governance_status: "recovery_approved"
```

If not, the checker reports an error.

Purpose:

```text
No recovery without governance approval.
```

The checker may also warn if human review is still pending for a recovery action.

---

### 6.11 Module Alignment Check

The checker verifies that constitution modules match article declarations.

For example, if the module definition says:

```yaml
safety_and_containment_module:
  article_ids:
    - 5
```

then Article 5 must declare:

```yaml
module: "safety_and_containment_module"
```

If a module lists an article that declares a different module, the checker reports an error.

Purpose:

```text
The constitution must not contradict its own module structure.
```

---

## 7. Error and Warning Model

The alignment checker distinguishes between errors and warnings.

### 7.1 Errors

Errors indicate institutional inconsistency.

Examples:

```text
unknown article reference
article name mismatch
undefined acting rank
rank authority mismatch
emergency containment missing required articles
emergency containment missing required safeguards
critical incident marked as not requiring human review
recovery without governance approval
module/article mismatch
```

Errors cause the script to fail.

### 7.2 Warnings

Warnings indicate potential institutional weakness or future compatibility concerns.

Examples:

```text
acting agent role differs from rank definition
emergency containment lacks Article 17
emergency containment is not reversible
recovery human review is still pending
critical incident rank lacks human review trigger
```

Warnings do not fail the script by default.

Warnings can be treated as errors by using:

```bash
python scripts/check_constitution_alignment.py --strict-warnings
```

---

## 8. Current Script

The current implementation is:

```text
scripts/check_constitution_alignment.py
```

Run:

```bash
python scripts/check_constitution_alignment.py
```

Expected output:

```text
Checking Defense Court Protocol constitution alignment...
Trace example:        examples/defense-trace-record.example.yaml
Rank example:         examples/defense-agent-rank.example.yaml
Constitution example: examples/cyber-defense-constitution.example.yaml

Constitution alignment passed.

Errors: 0
Warnings: 0

All constitution alignment checks passed.
```

Strict mode:

```bash
python scripts/check_constitution_alignment.py --strict-warnings
```

---

## 9. Relationship to GitHub Actions

The GitHub Actions workflow runs both validation layers.

Workflow:

```text
.github/workflows/validate-examples.yml
```

It performs:

```bash
python scripts/validate_examples.py
python scripts/check_constitution_alignment.py
```

This creates a two-stage validation gate:

```text
1. Schema Validation
   Checks structural correctness.

2. Constitution Alignment
   Checks institutional consistency.
```

In metaphor:

```text
Schema Validation is the gatekeeper.
Constitution Alignment is the magistrate.
```

The gatekeeper checks whether the papers are properly filled out.

The magistrate checks whether the claim makes sense under the constitution.

---

## 10. Relationship to Defense Trace Protocol

The Defense Trace Protocol defines what must be recorded.

The Constitution Alignment Model checks whether those records are constitutionally meaningful.

For example, the Defense Trace Protocol may require:

```yaml
constitutional_basis:
  applicable_articles:
    - id: 5
      name: "Safety Over Availability"
```

The Constitution Alignment Model checks whether:

```text
Article 5 exists.
The name matches.
The action type is consistent.
The acting rank is authorized.
The review status is appropriate.
```

This turns trace from a log into evidence.

---

## 11. Relationship to Defense Agent Rank Architecture

The Defense Agent Rank Architecture defines who may act.

The Constitution Alignment Model checks whether the trace respects that authority.

It checks:

```text
acting rank exists
rank authority exists
acting rank and rank authority match
role matches rank definition
action is allowed by rank
critical incident review trigger exists
```

This prevents rank from becoming decorative.

Rank becomes operational because it is checked against actions.

---

## 12. Relationship to Cyber Defense Seventeen Articles

The Cyber Defense Seventeen Articles define how agents must act.

The Constitution Alignment Model checks whether the trace is grounded in those articles.

It checks:

```text
article IDs exist
article names match
module definitions align
emergency containment references key articles
```

This prevents the constitution from becoming symbolic only.

The Articles become operational because actions must reference them correctly.

---

## 13. Relationship to Human Review

The Constitution Alignment Model helps preserve human responsibility.

It checks that critical incidents do not bypass human review.

It also warns when recovery actions appear insufficiently reviewed.

The goal is not to make human review slower.

The goal is to make sure that fast AI defense does not silently become final AI authority.

```text
AI may contain.
Verification must review.
Governance may pause.
Humans finalize legitimacy.
```

---

## 14. Relationship to Royalty OS

The alignment model may later support Royalty OS by ensuring that contribution and correction events are tied to valid defense records.

Future contribution records may rely on alignment checks such as:

```text
Was the contribution tied to a valid trace?
Was the acting rank defined?
Was the action constitutionally grounded?
Was the outcome reviewed?
Was the correction recorded?
```

This prevents value recognition from being based on unverified or constitutionally invalid actions.

Royalty OS integration should reward not only successful containment, but also:

```text
false-positive correction
over-containment prevention
missed-signal review
protocol improvement
governance refinement
careful recovery verification
```

---

## 15. Current Limitations

The current alignment checker is intentionally minimal.

It does not yet validate:

* multiple trace records
* parent/child trace chains
* incident lifecycle transitions
* full recovery gate logic
* article-to-action matrices
* rank-to-article matrices
* detailed evidence references
* signed provenance
* AOC / agent identity
* external policy references
* Royalty OS contribution events

These may be added in future versions.

---

## 16. Future Work

Future versions may include:

```text
v0.2:
  - support multiple trace records
  - support parent_trace_id and related_trace_ids
  - validate incident lifecycle status
  - validate richer severity transitions

v0.3:
  - article-to-action authority matrix
  - rank-to-article authority matrix
  - recovery gate validation
  - escalation path validation

v0.4:
  - signed trace validation
  - command provenance fields
  - AOC / agent identity integration
  - evidence reference validation

v0.5:
  - Royalty OS contribution and correction event alignment
  - defense value event validation
  - fault and correction mapping

v1.0:
  - formal conformance profile
  - semantic validation specification
  - governance review checklist
```

---

## 17. Non-Goals

The Constitution Alignment Model does not define:

* offensive cyber techniques
* exploit methods
* malware behavior
* intrusion guidance
* evasion methods
* unauthorized access methods
* automated legal judgment
* automated public disclosure
* unrestricted autonomous action

It is a defensive semantic validation model.

Its purpose is to check institutional consistency across the Defense Court Protocol.

---

## 18. Summary

The Constitution Alignment Model is the semantic validation layer of the Defense Court Protocol.

It ensures that:

```text
Trace references valid Articles.
Rank authority is defined.
Actions match rank authority.
Emergency containment follows constitutional rules.
Critical incidents preserve human review.
Recovery requires governance approval.
The Constitution remains internally consistent.
```

In this model:

```text
Schema Validation checks whether the documents are valid files.
Constitution Alignment checks whether they form a valid institution.
```

This is the difference between a repository that contains documents and a repository that begins to behave like a governance system.

The Defense Court Protocol therefore evolves from:

```text
validated structure
```

to:

```text
self-checking institution
```

That is the purpose of the Constitution Alignment Model.
