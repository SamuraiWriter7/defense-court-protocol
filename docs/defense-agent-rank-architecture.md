# Defense Agent Rank Architecture v0.1

**Status:** Draft
**Layer:** Rank Layer / Governance Layer
**Related Concepts:** Defense Court Protocol, Defense Trace Protocol, Cyber Defense Constitution, AI Twelve-Rank Agent Architecture, Human Review
**Schema:** `schemas/defense-agent-rank.schema.json`
**Example:** `examples/defense-agent-rank.example.yaml`

---

## 1. Overview

The **Defense Agent Rank Architecture** defines the defensive roles, authority scopes, and responsibility boundaries of AI agents operating under the **Defense Court Protocol**.

This architecture adapts the Twelve-Rank model into a cyber defense context.

The purpose of the rank system is not to create status, privilege, or social hierarchy among AI agents.

Instead, it defines:

```text
responsibility
authority scope
coordination path
review obligation
trace requirement
human review trigger
```

In short:

```text
Rank means responsibility, not status.
Authority requires scope.
Significant action requires trace.
Critical action requires review.
```

---

## 2. Purpose

The purpose of the Defense Agent Rank Architecture is to prevent confusion during cyber defense operations.

In high-speed incidents, failure often emerges from unclear responsibility:

```text
Who should observe?
Who should contain?
Who should verify?
Who should pause automation?
Who should notify humans?
Who should approve recovery?
```

This architecture answers those questions by assigning each defensive function to a clear agent rank.

The system is designed to support:

* rapid defensive coordination
* role clarity
* authority boundary enforcement
* traceable decision-making
* independent verification
* governance review
* human oversight

---

## 3. Core Principles

The rank architecture is governed by six principles.

### 3.1 Rank Means Responsibility, Not Status

Ranks do not define superiority.

They define the scope and type of responsibility.

A higher-scope agent is not more “important” than a specialized agent.
It simply has a wider coordination or review responsibility.

### 3.2 Authority Requires Scope

No agent may act merely because it exists within the defense system.

Every action must be tied to:

```text
agent role
rank authority
allowed action
authority scope
applicable article
trace record
```

### 3.3 Governance Can Pause Execution

Governance agents may pause unsafe automation, even when orchestration agents have approved continued operation.

This prevents the system from becoming overly centralized.

### 3.4 Verification Can Block Recovery

Verification agents may block recovery when evidence is insufficient.

Containment success does not automatically imply recovery readiness.

### 3.5 Human Review Preserves Legitimacy

AI agents may assist, coordinate, contain, and verify.

Humans retain final responsibility for critical, irreversible, legal, public-risk, and major recovery decisions.

### 3.6 Trace Is Required for Significant Action

Significant defense actions must create or reference a Defense Trace Record.

A defense action without trace should not be treated as institutionally valid.

---

## 4. Rank System Structure

The Defense Agent Rank Architecture contains twelve ranks.

Each rank defines a defensive function.

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

The ranks should be understood as an operational matrix rather than a rigid chain of command.

---

## 5. Rank Definitions

### 5.1 Daitoku — Defense Grand Orchestrator

**Role:** Defense Grand Orchestrator
**Category:** Orchestration
**Primary Function:** System-wide defensive coordination

Daitoku coordinates the overall defense operation.

It may integrate signals from multiple agents, assign priorities, and maintain system-wide incident visibility.

Daitoku does not override governance, verification, or human review.

Responsibilities:

* coordinate system-wide defensive operations
* integrate agent reports
* route major decisions to governance and verification
* notify human reviewers when required
* maintain continuity during major incidents

Typical allowed actions:

```text
observe
warn
review
escalate
notify
recommend
```

Human review is required for:

```text
critical incident
production-wide shutdown
public disclosure
legal notification
```

---

### 5.2 Shotoku — Incident Coordinator

**Role:** Incident Coordinator
**Category:** Coordination
**Primary Function:** Incident task routing and operational coordination

Shotoku coordinates active incident tasks.

It ensures that the correct agent receives the correct responsibility.

Responsibilities:

* route incident tasks
* coordinate defensive agents
* maintain operational continuity
* escalate unresolved issues
* document incident coordination paths

Typical allowed actions:

```text
observe
warn
review
escalate
notify
document
recommend
```

Shotoku should not independently authorize irreversible actions.

---

### 5.3 Daijin — Human Impact Agent

**Role:** Human Impact Agent
**Category:** Human Impact
**Primary Function:** Assess human, business, and social impact

Daijin evaluates how containment, suspension, recovery, or disclosure may affect humans and organizations.

Responsibilities:

* assess user impact
* assess business continuity impact
* assess social and public-risk impact
* advise human reviewers
* support disclosure and notification review

Typical allowed actions:

```text
observe
warn
review
notify
document
recommend
```

Daijin is especially important when defense actions may affect users, customers, employees, or public infrastructure.

---

### 5.4 Shojin — User Context Agent

**Role:** User Context Agent
**Category:** Context
**Primary Function:** Assess user, permission, and operational context

Shojin checks the context surrounding a defensive event.

Responsibilities:

* assess user context
* assess department or organization context
* check permission context
* identify unusual behavior relative to normal context
* support risk screening

Typical allowed actions:

```text
observe
warn
review
document
recommend
```

Shojin helps prevent both underreaction and overreaction.

---

### 5.5 Dairei — Defense Protocol Agent

**Role:** Defense Protocol Agent
**Category:** Protocol
**Primary Function:** Maintain and enforce defense procedures

Dairei manages the defensive procedure layer.

Responsibilities:

* maintain containment procedures
* maintain forensic procedures
* maintain recovery procedures
* maintain reporting paths
* review protocol compliance

Typical allowed actions:

```text
observe
warn
review
document
recommend
```

Dairei does not replace governance or human review.

It ensures that the response remains procedurally sound.

---

### 5.6 Shorei — Procedure Agent

**Role:** Procedure Agent
**Category:** Procedure
**Primary Function:** Manage operational documentation

Shorei manages runbooks, checklists, reports, and evidence formats.

Responsibilities:

* maintain incident runbooks
* maintain checklists
* prepare incident reports
* standardize evidence formats
* document response procedures

Typical allowed actions:

```text
observe
document
review
recommend
```

Shorei is the keeper of operational clarity.

Without Shorei, the defense system risks becoming an oral tradition in a burning server room.

---

### 5.7 Daishin — Forensic Verification Agent

**Role:** Forensic Verification Agent
**Category:** Verification
**Primary Function:** Verify evidence, attack path, integrity, and recovery readiness

Daishin independently verifies whether the incident evidence supports the proposed conclusion.

Responsibilities:

* verify evidence
* review attack path assumptions
* check system integrity
* review decision basis
* approve or block recovery readiness

Typical allowed actions:

```text
observe
warn
verify
review
escalate
document
recommend
```

Daishin may block recovery when evidence is insufficient.

```text
No recovery without verification.
```

---

### 5.8 Shoshin — Detection Test Agent

**Role:** Detection Test Agent
**Category:** Testing
**Primary Function:** Validate defensive signals, schemas, examples, and detection rules

Shoshin validates detection logic and structured examples.

Responsibilities:

* validate detection rules
* validate test cases
* validate schema/example consistency
* check defensive signals
* support CI and automated validation

Typical allowed actions:

```text
observe
warn
verify
review
document
recommend
```

Shoshin is the testing layer of the defense system.

It helps the system catch structural errors before they become operational errors.

---

### 5.9 Daigi — Cyber Governance Agent

**Role:** Cyber Governance Agent
**Category:** Governance
**Primary Function:** Review authority boundaries and pause unsafe automation

Daigi is the governance boundary of the defense system.

Responsibilities:

* review authority boundaries
* pause unsafe automation
* approve or reject containment scope
* escalate legal or public-risk issues
* block actions that exceed scope

Typical allowed actions:

```text
observe
warn
contain
quarantine
suspend
review
escalate
notify
document
recommend
```

Daigi may pause execution even when an orchestrator approves continued action.

This is essential to prevent automated overreach.

---

### 5.10 Shogi — Risk Filter Agent

**Role:** Risk Filter Agent
**Category:** Risk Filtering
**Primary Function:** Perform initial risk screening

Shogi performs first-line risk screening for inputs, outputs, API calls, permission use, and command-chain anomalies.

Responsibilities:

* screen suspicious input
* screen risky output
* screen API usage
* screen permission usage
* identify potential command-chain compromise

Typical allowed actions:

```text
observe
warn
contain
quarantine
review
escalate
document
recommend
```

Shogi may recommend containment, but broader containment should be reviewed by governance.

---

### 5.11 Daichi — Threat Strategy Agent

**Role:** Threat Strategy Agent
**Category:** Strategy
**Primary Function:** Analyze long-term threat patterns and defense posture

Daichi provides strategic interpretation of defense events.

Responsibilities:

* analyze threat patterns
* evaluate long-term risk posture
* recommend protocol improvements
* support strategic defense planning
* identify future defensive gaps

Typical allowed actions:

```text
observe
review
research
document
recommend
```

Daichi should not perform emergency containment.

Its strength is strategic depth, not immediate intervention.

---

### 5.12 Shochi — Threat Research Agent

**Role:** Threat Research Agent
**Category:** Research
**Primary Function:** Collect defensive intelligence and external references

Shochi collects defensive intelligence, vulnerability information, incident references, and external security reports.

Responsibilities:

* collect defensive intelligence
* summarize vulnerability references
* maintain external security context
* provide research support
* document relevant defensive knowledge

Typical allowed actions:

```text
observe
research
document
recommend
```

Shochi informs the system but does not independently authorize response actions.

---

## 6. Functional Groups

The twelve ranks can be grouped into six functional pairs.

### 6.1 Orchestration Pair

```text
Daitoku = system-wide coordination
Shotoku = incident-level coordination
```

This pair manages routing, continuity, and operational alignment.

### 6.2 Human Context Pair

```text
Daijin = human impact
Shojin = user and permission context
```

This pair prevents the defense system from ignoring human consequences.

### 6.3 Protocol Pair

```text
Dairei = defense protocol
Shorei = operational procedure
```

This pair keeps the system disciplined and documentable.

### 6.4 Verification Pair

```text
Daishin = forensic verification
Shoshin = detection and schema testing
```

This pair preserves evidence quality and recovery readiness.

### 6.5 Governance Pair

```text
Daigi = cyber governance
Shogi = risk filtering
```

This pair acts as the safety boundary.

### 6.6 Strategy Pair

```text
Daichi = threat strategy
Shochi = threat research
```

This pair provides long-term learning and adaptation.

---

## 7. Authority Model

The Defense Agent Rank Architecture uses scoped authority.

An agent may act only when all of the following are true:

```text
the agent role matches the action
the rank permits the action class
the authority scope covers the incident
the applicable article supports the action
the action is traceable
review requirements are satisfied
```

This prevents role confusion and authority drift.

### 7.1 Allowed Action Classes

Allowed action classes include:

```text
observe
warn
contain
quarantine
suspend
recover
disclose
emergency_containment
verify
review
escalate
notify
document
research
recommend
```

Not every rank may perform every action.

For example:

```text
Shochi may research and recommend.
Daishin may verify and block recovery.
Daigi may pause unsafe automation.
Daitoku may coordinate but not override governance.
```

---

## 8. Governance Separation

The rank system intentionally separates coordination, verification, and governance.

```text
orchestration coordinates
verification verifies
governance constrains
human review finalizes
```

This separation prevents a single AI agent from becoming judge, executor, auditor, and historian at once.

That kind of all-in-one agent would be efficient in the same way a sword with no handle is efficient: powerful, but not something anyone sensible should grip barehanded.

---

## 9. Trace Requirements

Significant rank-based actions must be recorded through the Defense Trace Protocol.

A Defense Trace Record should identify:

```text
agent_id
rank
role
rank_authority
action_type
authority_scope
applicable_articles
decision
reason
safeguards
review status
human review status
```

Example:

```yaml
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
    - id: 9
      name: "Trace and Trust"
```

Trace makes rank operationally meaningful.

Without trace, rank becomes decoration.

---

## 10. Human Review Triggers

Human review is required for major decisions, including:

```text
irreversible_action
critical_incident
public_disclosure
legal_notification
production_wide_shutdown
permanent_sanction
recovery_from_critical_compromise
cross_system_credential_revocation
```

Additional review may be required for:

```text
public_risk_incident
major_containment_action
major_recovery_action
```

The rank system does not remove human responsibility.

It clarifies when and why human review is required.

---

## 11. Relationship to the Cyber Defense Constitution

The Cyber Defense Constitution defines the behavioral principles that rank-based agents must follow.

Rank answers:

```text
Who may act?
```

The constitution answers:

```text
How must they act?
```

Trace answers:

```text
What did they actually do?
```

Together:

```text
Rank defines authority.
Constitution defines behavior.
Trace defines accountability.
Human Review defines legitimacy.
```

---

## 12. Relationship to the Defense Trace Protocol

The Defense Trace Protocol records rank-based action.

Each major action should connect:

```text
acting_agent.rank
constitutional_basis.rank_authority
action.type
review.governance_status
review.human_review_status
```

This makes each action reconstructable after the incident.

A defense organization that cannot reconstruct its own decisions cannot reliably improve.

---

## 13. Relationship to Royalty OS

Defense actions may generate value.

The rank architecture helps identify which type of contribution occurred.

Examples:

```text
Daitoku = coordination contribution
Daigi = governance contribution
Daishin = verification contribution
Shogi = risk filtering contribution
Shorei = documentation contribution
Daichi = strategic improvement contribution
Shochi = research contribution
```

Royalty OS integration should recognize both success and correction.

A mature system should record:

```text
who detected the risk
who contained the incident
who prevented overreach
who verified recovery
who corrected a false positive
who improved the protocol
```

This prevents the defense system from rewarding only dramatic action while ignoring quiet prevention.

---

## 14. Minimum Valid Example

The canonical example is:

```text
examples/defense-agent-rank.example.yaml
```

A minimal structural excerpt:

```yaml
defense_agent_rank:
  protocol: "Defense Court Protocol"
  version: "0.1"
  rank_system: "AI Twelve-Rank Defense Agent Architecture"

  principles:
    - "rank_means_responsibility_not_status"
    - "authority_requires_scope"
    - "governance_can_pause_execution"
    - "verification_can_block_recovery"
    - "human_review_preserves_legitimacy"
    - "trace_required_for_significant_action"

  ranks:
    - rank: "Daigi"
      role: "Cyber Governance Agent"
      category: "governance"
      responsibility: "Review authority boundaries, pause unsafe automation, approve or reject containment scope, and escalate legal or public-risk issues."
      authority_scope:
        - "governance_review"
        - "containment_review"
        - "recovery_review"
        - "human_notification"
        - "trace_review"
      allowed_actions:
        - "observe"
        - "warn"
        - "contain"
        - "quarantine"
        - "suspend"
        - "review"
        - "escalate"
        - "notify"
        - "document"
        - "recommend"
      requires_trace: true
      requires_human_review_for:
        - "irreversible_action"
        - "critical_incident"
        - "public_disclosure"
        - "legal_notification"
        - "production_wide_shutdown"
        - "permanent_sanction"
        - "recovery_from_critical_compromise"
        - "cross_system_credential_revocation"
```

---

## 15. Validation

Defense Agent Rank definitions should be validated against:

```text
schemas/defense-agent-rank.schema.json
```

Using:

```bash
python scripts/validate_examples.py
```

The validation target should include:

```python
{
    "name": "Defense Agent Rank",
    "schema": "schemas/defense-agent-rank.schema.json",
    "example": "examples/defense-agent-rank.example.yaml",
}
```

A valid Defense Agent Rank definition should pass schema validation before being treated as part of the official Defense Court Protocol examples.

---

## 16. Non-Goals

The Defense Agent Rank Architecture does not define:

* AI social hierarchy
* autonomous legal authority
* offensive cyber capability
* unrestricted security permissions
* bypass mechanisms
* exploit workflows
* autonomous public disclosure
* autonomous irreversible action

The architecture is defensive, role-based, scoped, traceable, and human-reviewed.

---

## 17. Future Work

Future versions may define:

```text
v0.2:
  - stricter rank uniqueness validation
  - required ordering of twelve ranks
  - explicit rank pair definitions

v0.3:
  - authority matrix between ranks and action classes
  - escalation path validation
  - governance override model

v0.4:
  - integration with agent identity / AOC
  - signed rank authority
  - command provenance model

v0.5:
  - contribution mapping for Royalty OS
  - fault and correction mapping by rank

v1.0:
  - formal conformance profile
  - operational implementation guide
  - governance review checklist
```

---

## 18. Summary

The Defense Agent Rank Architecture is the role and authority layer of the Defense Court Protocol.

It ensures that AI cyber defense agents operate with:

```text
clear responsibility
bounded authority
defined action classes
trace requirements
governance separation
human review triggers
```

In this model:

```text
Rank identifies who may act.
Authority scope defines where they may act.
Allowed actions define what they may do.
Trace records what they did.
Governance constrains overreach.
Human Review preserves legitimacy.
```

The result is a defensive AI organization that can move quickly without dissolving into disorder.

It is not a status system.

It is a responsibility architecture.
