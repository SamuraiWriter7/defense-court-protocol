# Defense Trace Protocol v0.1

**Status:** Draft
**Layer:** Trace Layer / Governance Layer
**Related Concepts:** Defense Court Protocol, Defense Trace Record, AI Twelve-Rank Defense Agent Architecture, AI Seventeen-Article Cyber Defense Charter, Human Review, Royalty OS
**Schema:** `schemas/defense-trace-record.schema.json`
**Example:** `examples/defense-trace-record.example.yaml`

---

## 1. Overview

The **Defense Trace Protocol** defines how cyber defense actions performed by AI agents are recorded, reviewed, verified, and connected to human responsibility.

It is a core component of the **Defense Court Protocol**.

The Defense Court Protocol defines:

```text
Rank for responsibility.
Articles for behavior.
Defense Kernel for emergency response.
Trace for accountability.
Governance for safety.
Human Review for legitimacy.
```

Within this structure, the Defense Trace Protocol provides the record layer.

It answers the following questions:

```text
What happened?
Who acted?
Why was action taken?
Which authority was used?
Which constitutional articles applied?
Was the action reversible?
Were safeguards applied?
Who verified the result?
Was human review required?
What must happen next?
```

The protocol exists because high-speed cyber defense cannot rely on memory, verbal reports, or informal assumptions.

In emergency defense, **trace is the source of truth**.

---

## 2. Purpose

The purpose of the Defense Trace Protocol is to ensure that every significant cyber defense action is:

* Recorded
* Verifiable
* Reviewable
* Governed
* Connected to human responsibility
* Usable for future correction and improvement

This protocol does not exist merely to create logs.

It exists to convert defensive action into structured accountability.

```text
No defense action without logging.
No recovery without verification.
No legitimacy without human review.
```

---

## 3. Design Philosophy

The Defense Trace Protocol is based on five principles.

### 3.1 Trace Before Claim

No agent should claim that a defense action occurred unless a trace record exists.

A defense claim without trace is only an assertion.

A defense claim with trace becomes reviewable evidence.

### 3.2 Protocol Before Execution

Defense agents must act according to defined rules, not improvisation.

When emergency action is required, the trace record must show which protocol, rank authority, and constitutional articles justified the action.

### 3.3 Containment Before Expansion

During active incidents, trace records should support scoped containment.

The record should show:

* What was affected
* What was contained
* Why the containment was necessary
* Whether the action was reversible
* What blast-radius limitation was used

### 3.4 Verification Before Recovery

Recovery must not occur only because availability pressure is high.

Before recovery, trace records should provide enough evidence for verification agents, governance agents, and human reviewers to determine whether recovery is safe.

### 3.5 Human Responsibility Before Finalization

AI agents may support emergency containment.

AI agents may not finalize legitimacy.

Human review preserves final responsibility for critical incidents, public-risk incidents, irreversible actions, legal notification, disclosure, and recovery from critical compromise.

---

## 4. Scope

The Defense Trace Protocol applies to significant cyber defense actions, including:

* Threat detection
* Warning
* Emergency containment
* Quarantine
* Workflow suspension
* Recovery recommendation
* Recovery approval
* Governance escalation
* Public-risk escalation
* Evidence preservation
* False-positive correction
* Protocol correction
* Defense contribution recording

This protocol does not apply to trivial monitoring events unless they are escalated or connected to an incident.

---

## 5. Defense Trace Record

A **Defense Trace Record** is a structured record of a defense action.

The canonical schema is:

```text
schemas/defense-trace-record.schema.json
```

The canonical example is:

```text
examples/defense-trace-record.example.yaml
```

A Defense Trace Record should include:

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

These fields allow the system to determine:

```text
identity
time
severity
scope
authority
decision
reason
safeguards
verification state
governance state
human review state
next required action
```

---

## 6. Required Record Structure

### 6.1 Root Object

A Defense Trace Record uses the following root key:

```yaml
defense_trace_record:
```

This root object contains the full defense action record.

### 6.2 Required Top-Level Fields

```yaml
defense_trace_record:
  trace_id: "dcp-2026-0001"
  timestamp: "2026-06-07T00:00:00Z"
  severity: "critical"
  incident: {}
  acting_agent: {}
  constitutional_basis: {}
  action: {}
  safeguards: {}
  review: {}
```

Each significant defense action should include these fields.

---

## 7. Field Definitions

### 7.1 trace_id

The `trace_id` uniquely identifies the defense trace record.

Recommended format:

```text
dcp-YYYY-NNNN
```

Example:

```yaml
trace_id: "dcp-2026-0001"
```

The trace ID should be stable and should not be reused.

---

### 7.2 timestamp

The `timestamp` records when the action occurred.

Example:

```yaml
timestamp: "2026-06-07T00:00:00Z"
```

Timestamps should use RFC3339 / ISO 8601 date-time format.

---

### 7.3 severity

The `severity` field identifies incident severity.

Allowed values:

```text
info
low
medium
high
critical
```

Example:

```yaml
severity: "critical"
```

Severity should influence containment urgency, review requirements, and escalation path.

---

### 7.4 incident

The `incident` object describes the suspected or confirmed incident.

Required fields:

```yaml
incident:
  type: "suspected_ai_accelerated_intrusion"
  summary: "Abnormal privilege escalation and lateral movement indicators were detected."
  affected_scope:
    - "internal_api_gateway"
    - "agent_runtime_cluster"
```

The `affected_scope` field should identify affected systems, services, agents, APIs, routes, workflows, or infrastructure.

---

### 7.5 acting_agent

The `acting_agent` object identifies the agent that performed the action.

Example:

```yaml
acting_agent:
  agent_id: "shield-agent-01"
  rank: "Daigi"
  role: "Cyber Governance Agent"
```

The `rank` field should use one of the Defense Court Protocol rank names:

```text
Daitoku
Shotoku
Daijin
Shojin
Dairei
Shorei
Daishin
Shoshin
Daigi
Shogi
Daichi
Shochi
```

Rank does not represent status.

Rank represents responsibility scope.

---

### 7.6 constitutional_basis

The `constitutional_basis` object identifies the authority and principles behind the action.

Example:

```yaml
constitutional_basis:
  rank_authority: "Daigi"
  applicable_articles:
    - id: 3
      name: "Authorized Command"
    - id: 5
      name: "Safety Over Availability"
    - id: 6
      name: "Containment of Harm"
    - id: 9
      name: "Trace and Trust"
    - id: 17
      name: "Collective Review"
```

This field connects the action to the Cyber Defense Constitution.

A defense action should not be treated as legitimate merely because it was fast.

It must also be constitutionally grounded and reviewable.

---

### 7.7 action

The `action` object describes what was done.

Example:

```yaml
action:
  type: "emergency_containment"
  decision: "isolate_affected_services"
  reversible: true
  automation_level: "inner_loop_ai"
  reason: "Fast-moving attack progression was suspected and scoped containment was required."
```

Allowed action types include:

```text
observe
warn
contain
quarantine
suspend
recover
disclose
emergency_containment
```

Allowed automation levels include:

```text
manual
inner_loop_ai
outer_loop_human
hybrid
```

---

### 7.8 safeguards

The `safeguards` object records whether defensive safety checks were applied.

Example:

```yaml
safeguards:
  command_authentication: "passed"
  scope_check: "passed"
  blast_radius_limit: "enabled"
  rollback_plan: "available"
  human_notification: "sent"
```

Safeguards are essential because defense can itself become dangerous if it expands without limits.

The protocol therefore requires evidence of:

```text
command authentication
scope checking
blast-radius limitation
rollback planning
human notification
```

---

### 7.9 review

The `review` object records verification, governance, human review, and next action.

Example:

```yaml
review:
  verification_agent: "forensic-agent-01"
  governance_status: "containment_approved"
  human_review_status: "pending"
  next_required_action: "forensic_review_before_recovery"
```

The review section determines whether the action is complete, blocked, pending, or awaiting human decision.

---

## 8. Trace and the Inner Loop / Outer Loop Model

The Defense Court Protocol separates incident response into two loops.

### 8.1 Inner Loop

The Inner Loop is the fast AI response layer.

It may perform scoped actions such as:

```text
observe
warn
contain
quarantine
suspend
```

Inner Loop actions must be:

* Scoped
* Logged
* Justified
* Reported
* Reversible when possible
* Subject to later review

Trace records are mandatory for significant Inner Loop actions.

### 8.2 Outer Loop

The Outer Loop is the human review and governance layer.

It handles:

```text
legitimacy
legal assessment
public disclosure
critical recovery approval
policy correction
compensation or contribution decisions
```

Outer Loop decisions should refer back to Defense Trace Records.

### 8.3 Loop Rule

```text
AI may contain.
Verification must review.
Governance may pause.
Humans finalize legitimacy.
```

---

## 9. Trace and Governance

Governance agents use Defense Trace Records to determine whether:

* The action was within scope
* The acting agent had proper authority
* The action was reversible
* The blast radius was limited
* Human notification occurred
* Recovery should be blocked
* Public-risk escalation is needed
* Legal or policy review is required

A governance agent may pause execution even if an orchestrator approved the action.

A verification agent may block recovery even if containment succeeded.

This prevents defensive overreach.

---

## 10. Trace and Recovery

Recovery must be trace-driven.

Before recovery, the trace record should support answers to these questions:

```text
What was affected?
What was contained?
Was the attack path understood?
Were credentials or permissions compromised?
Were logs preserved?
Was the recovery target verified?
Was governance review completed?
Is human review required?
```

The recovery rule is:

```text
No recovery without verification.
```

This prevents premature restoration of compromised systems.

---

## 11. Trace and Human Review

Human review is required for major decisions, including:

* Irreversible action
* Critical incident
* Public disclosure
* Legal notification
* Production-wide shutdown
* Permanent sanction
* Recovery from critical compromise
* Cross-system credential revocation
* Public-risk incident
* Major containment action
* Major recovery action

Human reviewers should rely on trace records rather than informal incident summaries.

The trace record does not replace human judgment.

It gives human judgment a structured evidentiary basis.

---

## 12. Trace and the Cyber Defense Constitution

The Cyber Defense Constitution defines the behavioral rules of the defense system.

The Defense Trace Protocol records which articles apply to each action.

Example:

```yaml
applicable_articles:
  - id: 3
    name: "Authorized Command"
  - id: 5
    name: "Safety Over Availability"
  - id: 9
    name: "Trace and Trust"
```

This makes each action constitutionally reviewable.

In practical terms:

```text
Article 3 checks command legitimacy.
Article 5 justifies scoped containment.
Article 9 requires traceability.
Article 17 requires review for major decisions.
```

---

## 13. Trace and Defense Agent Ranks

The Defense Agent Rank system defines agent roles and authority scopes.

Trace records must show:

```text
agent_id
rank
role
rank_authority
authority_scope
```

This prevents unclear responsibility.

For example:

```yaml
acting_agent:
  agent_id: "shield-agent-01"
  rank: "Daigi"
  role: "Cyber Governance Agent"
```

This means the action was performed by a governance agent, not a research agent, coordinator, or recovery agent.

Rank-based traceability prevents role confusion during emergencies.

---

## 14. Trace and Royalty OS Integration

Defense actions may create value.

A trace record can later support Royalty OS contribution events such as:

```text
detection contribution
containment contribution
forensic contribution
recovery contribution
runbook improvement
false-positive correction
governance improvement
risk reduction event
```

However, the protocol must record both success and correction.

Royalty OS integration should not reward only successful containment.

It should also recognize:

```text
false-positive correction
over-containment prevention
missed-signal analysis
recovery improvement
policy correction
protocol refinement
```

This prevents the defense system from becoming self-congratulatory.

A mature defense system must reward learning, not just victory.

---

## 15. Minimum Valid Example

```yaml
defense_trace_record:
  trace_id: "dcp-2026-0001"
  timestamp: "2026-06-07T00:00:00Z"
  severity: "critical"

  incident:
    type: "suspected_ai_accelerated_intrusion"
    summary: "Abnormal privilege escalation and lateral movement indicators were detected."
    affected_scope:
      - "internal_api_gateway"
      - "agent_runtime_cluster"

  acting_agent:
    agent_id: "shield-agent-01"
    rank: "Daigi"
    role: "Cyber Governance Agent"

  constitutional_basis:
    rank_authority: "Daigi"
    applicable_articles:
      - id: 3
        name: "Authorized Command"
      - id: 5
        name: "Safety Over Availability"
      - id: 6
        name: "Containment of Harm"
      - id: 9
        name: "Trace and Trust"
      - id: 17
        name: "Collective Review"

  action:
    type: "emergency_containment"
    decision: "isolate_affected_services"
    reversible: true
    automation_level: "inner_loop_ai"
    reason: "Fast-moving attack progression was suspected and scoped containment was required."

  safeguards:
    command_authentication: "passed"
    scope_check: "passed"
    blast_radius_limit: "enabled"
    rollback_plan: "available"
    human_notification: "sent"

  review:
    verification_agent: "forensic-agent-01"
    governance_status: "containment_approved"
    human_review_status: "pending"
    next_required_action: "forensic_review_before_recovery"
```

---

## 16. Validation

Defense Trace Records should be validated against:

```text
schemas/defense-trace-record.schema.json
```

Using:

```bash
python scripts/validate_examples.py
```

The validation target should include:

```python
{
    "name": "Defense Trace Record",
    "schema": "schemas/defense-trace-record.schema.json",
    "example": "examples/defense-trace-record.example.yaml",
}
```

A valid Defense Trace Record should pass schema validation before being treated as part of the official protocol examples.

---

## 17. Non-Goals

The Defense Trace Protocol does not provide:

* Offensive cyber instructions
* Exploit techniques
* Malware behavior
* Intrusion guidance
* Evasion methods
* Unauthorized access methods
* Fully autonomous legal judgment
* Fully autonomous public disclosure
* Fully autonomous irreversible action

The protocol is defensive, evidentiary, governance-oriented, and human-reviewed.

---

## 18. Future Work

Future versions may define:

```text
v0.2:
  - richer incident classification
  - expanded severity model
  - incident lifecycle status
  - evidence reference fields

v0.3:
  - contribution event mapping for Royalty OS
  - fault and correction event mapping
  - recovery gate validation

v0.4:
  - signature and provenance fields
  - AOC / agent identity integration
  - command authentication evidence

v0.5:
  - multi-agent trace chain
  - parent_trace_id and related_trace_ids
  - incident timeline reconstruction

v1.0:
  - formal conformance profile
  - implementation guide
  - governance review checklist
```

---

## 19. Summary

The Defense Trace Protocol is the record layer of the Defense Court Protocol.

It ensures that emergency cyber defense actions are not merely fast, but also:

```text
structured
scoped
verifiable
reviewable
governed
human-legitimate
```

In this model:

```text
Rank identifies who acted.
Articles identify why the action was justified.
Trace records what was done.
Governance checks whether the action stayed within bounds.
Verification determines whether recovery is safe.
Human Review preserves final responsibility.
```

The Defense Trace Protocol therefore turns AI cyber defense from a reaction into a reviewable institution.

It is the memory, evidence, and accountability layer of the Defense Court Protocol.
