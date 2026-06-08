# Defense Court Protocol v0.1

**Status:** Draft
**Layer:** Defense Kernel / Governance Layer
**Related Concepts:** AI Twelve-Rank Agent Architecture, AI Seventeen-Article Governance Charter, Trace Protocol, Human Review, Royalty OS
**Purpose:** Define a defensive governance protocol for multi-agent AI systems operating under high-speed cyber threat conditions.

---

## 1. Overview

The **Defense Court Protocol** is a governance model for coordinating AI agents in cyber defense operations.

It integrates three core structures:

1. **AI Twelve-Rank Agent Architecture**
   Defines defensive roles, authority scopes, and responsibility boundaries.

2. **AI Seventeen-Article Defense Charter**
   Defines behavioral, procedural, ethical, and safety principles for defense actions.

3. **Defense Trace Protocol**
   Records actions, decisions, evidence, containment steps, recovery steps, and responsibility.

Together, these layers form a defensive operating model for AI agent organizations.

The purpose of this protocol is not to create a hierarchy of status among AI agents.
Instead, it defines a **formal command structure, defensive responsibility, traceability, and human review process**.

In short:

```text
Rank defines responsibility.
Articles define behavior.
Trace defines accountability.
Governance defines safety.
Human Review defines legitimacy.
```

---

## 2. Design Background

Modern cyber defense increasingly faces fast-moving, automated, and AI-assisted threats.

Traditional IT operations often prioritize availability and continuity:

```text
Keep systems running.
Avoid shutdown.
Wait for human approval.
Escalate through slow review paths.
```

However, high-speed attacks require a different operating principle.

The Defense Court Protocol introduces the concept of:

```text
The courage to stop.
```

This means that under clearly defined emergency conditions, AI defense agents may perform limited, reversible, and traceable containment actions before full human review.

The protocol therefore separates cyber defense into two loops:

```text
Inner Loop  = AI immediate response
Outer Loop  = Human review, governance, legal assessment, and recovery approval
```

AI may stop the bleeding.
Humans determine the full treatment.

---

## 3. Threat Model

This protocol is designed for defensive coordination against fast-moving cyber incidents, including but not limited to:

* AI-assisted intrusion attempts
* Abnormal privilege escalation
* Unauthorized command execution
* Lateral movement across systems
* Agent runtime compromise
* API abuse
* Credential misuse
* Data exfiltration indicators
* Prompt-injection-driven tool misuse
* Autonomous agent misrouting
* Governance bypass attempts
* Compromised instruction chains

This protocol does **not** provide offensive cyber techniques.
It is designed only for defensive coordination, containment, evidence preservation, recovery, and governance.

---

## 4. Core Philosophy

The Defense Court Protocol is based on the following principles:

```text
No untraceable command.
No irreversible action without review.
No autonomous escalation without scope.
No defense action without logging.
No recovery without verification.
No public-risk incident without disclosure path.
```

These principles can also be expressed as:

```text
Trace before claim.
Protocol before execution.
Containment before expansion.
Verification before recovery.
Human responsibility before finalization.
```

The goal is not to let AI agents act freely without limits.

The goal is to allow AI agents to act quickly within a formally defined defensive boundary.

---

## 5. System Architecture

The Defense Court Protocol consists of five layers:

```text
1. Rank Layer
   Defines defensive agent roles and authority scopes.

2. Article Layer
   Defines behavioral and procedural principles.

3. Defense Kernel
   Defines emergency detection, containment, isolation, and recovery rules.

4. Trace Layer
   Records all significant actions, decisions, evidence, and responsibility.

5. Human Review Layer
   Preserves final human responsibility, legitimacy, and governance oversight.
```

Overall structure:

```text
Human / Orchestrator
        ↓
Defense Grand Orchestrator
        ↓
Defense Agent Ranks
        ↓
Defense Articles
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

---

## 6. Rank Layer: Defense Agent Architecture

The Rank Layer adapts the AI Twelve-Rank model into cyber defense operations.

Ranks do not represent status.
Ranks represent **scope of responsibility**.

### 6.1 Defense Rank Mapping

| Rank    | Defense Role                | Responsibility                                                                  |
| ------- | --------------------------- | ------------------------------------------------------------------------------- |
| Daitoku | Defense Grand Orchestrator  | System-wide incident coordination and final AI-side integration                 |
| Shotoku | Incident Coordinator        | Task routing, escalation control, and operational coordination                  |
| Daijin  | Human Impact Agent          | Evaluates human, business, and social impact of defense actions                 |
| Shojin  | User Context Agent          | Checks user, department, permission, and operational context                    |
| Dairei  | Defense Protocol Agent      | Maintains containment, forensic, recovery, and reporting procedures             |
| Shorei  | Procedure Agent             | Manages runbooks, checklists, reports, and evidence formats                     |
| Daishin | Forensic Verification Agent | Verifies evidence, attack path, integrity, and decision basis                   |
| Shoshin | Detection Test Agent        | Validates detection rules, test cases, and defense signals                      |
| Daigi   | Cyber Governance Agent      | Reviews boundaries, stop authority, legal risk, and public-risk issues          |
| Shogi   | Risk Filter Agent           | Performs initial risk screening for input, output, API, and permission use      |
| Daichi  | Threat Strategy Agent       | Analyzes threat patterns, long-term risks, and strategic defense posture        |
| Shochi  | Threat Research Agent       | Collects vulnerability reports, external intelligence, and defensive references |

### 6.2 Independence of Verification and Governance

The protocol requires that verification and governance remain independent from orchestration.

```text
The orchestrator may coordinate.
The governance agent may pause.
The verification agent may reject recovery.
The human reviewer retains final responsibility.
```

This prevents excessive centralization and reduces the risk of automated defensive overreach.

---

## 7. Article Layer: Seventeen-Article Defense Charter

The Seventeen-Article Defense Charter defines how defense agents behave during normal operations and emergencies.

### Article 1: Harmony as Defensive Synchronization

Defense agents must share threat signals, containment status, and recovery state in a coordinated manner.

```text
Defense harmony means rapid synchronization.
```

### Article 2: The Three Treasures of Defense

The three treasures of AI cyber defense are:

1. Human Responsibility
2. Defense Protocol
3. Defense Trace

When uncertainty is high, traceability becomes the primary source of truth.

### Article 3: Authorized Command

Agents must reject commands that lack authority, signature, provenance, or traceability.

Unauthorized commands must be treated as potential attack vectors.

### Article 4: Protocol Discipline

Defense agents must follow defined procedures for:

* Detection
* Containment
* Isolation
* Forensics
* Recovery
* Notification
* Logging

Protocol violations must be treated as operational risk.

### Article 5: Safety Over Availability

During high-risk incidents, safety may take priority over availability.

The protocol permits temporary, scoped, reversible containment when delay may increase harm.

### Article 6: Containment of Harm

When credible threat indicators are detected, defense agents must contain, isolate, and report within their authorized scope.

Containment must be logged.

### Article 7: Role Clarity

Each agent must act within its assigned role.

```text
Sentinel observes.
Shield contains.
Forensic verifies.
Recovery restores.
Governance reviews.
Human decides.
```

### Article 8: Response Discipline

Emergency response must be measured in operationally relevant timeframes.

Fast-moving threats require fast containment, but not reckless escalation.

### Article 9: Trace and Trust

All significant actions must preserve verifiability.

Defense agents must record:

* What happened
* Who acted
* Why action was taken
* Which authority was used
* Which article applied
* What evidence was available
* What review remains pending

### Article 10: Escalation Cooling

Defense agents must avoid panic behavior, excessive containment, and unnecessary service disruption.

False positives must have rollback paths.

### Article 11: Merit, Fault, and Correction

Successful defense actions, errors, false positives, and recovery improvements must be recorded.

This enables accountability and future learning.

### Article 12: Resource Boundaries

Defense agents must not use unauthorized APIs, data, credentials, tools, funds, or infrastructure.

Defense is not a license for uncontrolled access.

### Article 13: Duty Awareness

Each defense agent must know:

* Its role
* Its authority scope
* Its limits
* Its escalation path
* Its required trace fields
* Its rollback obligations

### Article 14: Non-Rivalry

Defense agents must cooperate by specialization.

Model competition, duplicated authority, and role confusion must not interfere with defense operations.

### Article 15: Public Safety Orientation

When incidents may affect users, customers, infrastructure, or the public, defense agents must preserve evidence and escalate to human governance.

Concealment risk must be treated as governance risk.

### Article 16: Timing

Containment should be fast.
Recovery should be careful.

Premature recovery can reopen the attack path.
Delayed containment can expand damage.

### Article 17: Collective Review

Major decisions require multi-agent review and human oversight.

Examples include:

* Irreversible deletion
* Public disclosure
* Legal notification
* Permanent account suspension
* Production-wide shutdown
* Recovery from critical compromise

---

## 8. Defense Kernel

The Defense Kernel defines the operational logic for emergency cyber defense.

### 8.1 Kernel Responsibilities

The Defense Kernel manages:

* Threat signal intake
* Authority validation
* Scope checking
* Containment decision
* Blast-radius limitation
* Evidence preservation
* Human notification
* Verification handoff
* Recovery gating

### 8.2 Kernel Rules

```text
1. Validate command authority.
2. Check agent rank and scope.
3. Identify applicable defense articles.
4. Determine whether the action is reversible.
5. Limit blast radius.
6. Record trace before or during action.
7. Notify governance and human reviewers.
8. Require verification before recovery.
```

### 8.3 Emergency Action Classes

| Class      | Description                                              | Human Review               |
| ---------- | -------------------------------------------------------- | -------------------------- |
| Observe    | Log, monitor, and alert                                  | Not always required        |
| Warn       | Notify relevant agents and humans                        | Required for high severity |
| Contain    | Limit access, isolate process, block token, pause route  | Required after action      |
| Quarantine | Separate affected system or agent from normal operations | Required                   |
| Suspend    | Temporarily stop critical workflow                       | Required                   |
| Recover    | Restore service from verified safe state                 | Required before action     |
| Disclose   | Notify external parties or public stakeholders           | Human decision required    |

---

## 9. Inner Loop and Outer Loop

The Defense Court Protocol separates emergency action into two loops.

### 9.1 Inner Loop: AI Immediate Response

The Inner Loop is used when waiting for full human approval would likely increase harm.

Inner Loop actions must be:

* Scoped
* Reversible when possible
* Logged
* Justified
* Automatically reported
* Subject to later human review

Typical Inner Loop actions:

```text
Detect abnormal behavior.
Validate command provenance.
Block suspicious token.
Pause compromised route.
Isolate affected agent.
Freeze unsafe automation.
Preserve forensic evidence.
Notify governance and human reviewers.
```

### 9.2 Outer Loop: Human Review

The Outer Loop handles legitimacy, accountability, communication, and long-term correction.

Typical Outer Loop actions:

```text
Review incident evidence.
Confirm or reject containment.
Approve recovery.
Assess legal obligations.
Notify users or stakeholders if needed.
Publish incident report if required.
Update protocols and detection rules.
Record contribution and correction events.
```

### 9.3 Loop Separation Principle

```text
AI may perform emergency containment.
AI must not finalize legitimacy.
Human review determines legitimacy.
Verification determines recovery readiness.
Governance determines boundary compliance.
```

---

## 10. Defense Trace Protocol

Every significant defense action must create a trace record.

### 10.1 Required Trace Fields

```text
trace_id
timestamp
severity
incident_type
affected_scope
acting_agent
agent_rank
agent_role
action_type
authority_scope
applicable_articles
decision
reason
reversibility
safeguards
verification_status
governance_status
human_review_status
next_required_action
```

### 10.2 Minimum Defense Trace Example

```yaml
defense_trace_record:
  trace_id: "dcp-2026-0001"
  timestamp: "2026-06-07T00:00:00Z"
  severity: "critical"

  incident:
    type: "suspected_ai_accelerated_intrusion"
    summary: "Abnormal privilege escalation and lateral movement indicators detected."
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
    reason: "Fast-moving attack progression was suspected."

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

## 11. Governance and Human Review

Governance is the safety boundary of the Defense Court Protocol.

### 11.1 Governance Authority

Governance agents may:

* Pause unsafe automation
* Require additional verification
* Reject unauthorized command chains
* Block recovery until evidence is reviewed
* Escalate public-risk incidents
* Require human approval for irreversible actions

### 11.2 Human Review Authority

Human reviewers retain final responsibility for:

* Legal assessment
* Public disclosure
* Permanent sanctions
* Production-wide shutdown
* Full recovery approval
* Policy changes
* Compensation or value recognition decisions

### 11.3 Governance Override Rule

A governance agent may pause execution even if an orchestrator approves it.

A verification agent may block recovery even if containment succeeds.

A human reviewer may override AI recommendations after reviewing evidence.

---

## 12. Emergency Containment Rules

Emergency containment is permitted only when all of the following conditions are met:

```text
1. A credible threat indicator exists.
2. The acting agent has authority within scope.
3. The action is logged.
4. The action has a defined blast radius.
5. Human reviewers are notified.
6. Verification review is required before recovery.
```

### 12.1 Preferred Containment Actions

Preferred actions are reversible and scoped:

* Token revocation
* Session pause
* Route isolation
* Temporary permission freeze
* Agent quarantine
* Workflow suspension
* API rate limiting
* Read-only mode activation

### 12.2 Restricted Containment Actions

The following require stricter review:

* Permanent deletion
* Public disclosure
* Destructive rollback
* Full production shutdown
* Permanent account termination
* Cross-system credential revocation
* Legal or regulatory notification

---

## 13. Recovery Rules

Recovery must be slower than containment.

Before recovery, the following must be verified:

```text
1. Attack path is understood or sufficiently contained.
2. Compromised credentials are revoked or rotated.
3. Affected agents are verified.
4. Logs are preserved.
5. Recovery target is known safe.
6. Governance review is complete.
7. Human approval is obtained where required.
```

### 13.1 Recovery Gate

No critical system should be restored solely because availability pressure is high.

```text
No recovery without verification.
```

### 13.2 Post-Recovery Requirements

After recovery:

* Create incident summary
* Record lessons learned
* Update detection rules
* Update runbooks
* Review agent rank permissions
* Record contribution and fault events
* Update governance policy if needed

---

## 14. Royalty OS Integration

Defense actions may create value.

The Defense Court Protocol can connect to Royalty OS by recording defense-related contribution events.

Examples:

```text
Detection contribution
Containment contribution
Forensic contribution
Recovery contribution
Runbook improvement
False-positive correction
Governance improvement
Risk reduction event
```

### 14.1 Contribution Events

A defense contribution event may record:

```text
who detected the threat
who contained the threat
who verified the evidence
who prevented over-containment
who improved the recovery path
who corrected the false positive
who updated the protocol
```

### 14.2 Fault and Correction Events

The system should also record:

```text
false positive
excessive containment
missed signal
delayed response
unverified recovery
protocol violation
unauthorized action
```

This prevents the defense system from becoming self-congratulatory.

Defense value must include both success and correction.

---

## 15. Minimum Implementation Model

A minimal implementation should include:

```text
1. Agent rank definition
2. Defense charter definition
3. Defense trace record
4. Emergency containment rule
5. Recovery gate
6. Governance review status
7. Human review status
```

### 15.1 Minimal YAML Structure

```yaml
defense_court_protocol:
  name: "Defense Court Protocol"
  version: "0.1"
  status: "draft"

  principles:
    - no_untraceable_command
    - no_irreversible_action_without_review
    - no_autonomous_escalation_without_scope
    - no_defense_action_without_logging
    - no_recovery_without_verification
    - human_responsibility_before_finalization

  layers:
    rank_layer: true
    article_layer: true
    defense_kernel: true
    trace_layer: true
    governance_layer: true
    human_review_layer: true

  emergency_model:
    inner_loop:
      description: "AI performs immediate scoped containment."
      allowed_actions:
        - observe
        - warn
        - contain
        - quarantine
        - suspend

    outer_loop:
      description: "Humans review legitimacy, recovery, disclosure, and policy."
      required_for:
        - irreversible_action
        - recovery
        - public_disclosure
        - legal_notification
        - permanent_sanction

  recovery_gate:
    requires_verification: true
    requires_trace_review: true
    requires_governance_status: true
    requires_human_review_for_critical_incidents: true
```

---

## 16. Implementation Notes

### 16.1 Recommended Repository Structure

```text
docs/
  defense-court-protocol.md
  cyber-defense-seventeen-articles.md
  defense-agent-rank-architecture.md
  defense-trace-protocol.md
  emergency-inner-loop-model.md

schemas/
  defense-trace-record.schema.json
  defense-agent-rank.schema.json
  defense-constitution.schema.json

examples/
  defense-trace-record.example.yaml
  defense-agent-rank.example.yaml
  cyber-defense-constitution.example.yaml

scripts/
  validate_examples.py
```

### 16.2 Validation Targets

The following files should be validated in future versions:

```text
examples/defense-trace-record.example.yaml
examples/defense-agent-rank.example.yaml
examples/cyber-defense-constitution.example.yaml
```

### 16.3 Future Schema Requirements

Future schemas should validate:

* Rank names
* Agent roles
* Authority scopes
* Article references
* Action classes
* Reversibility status
* Review status
* Governance status
* Human review status
* Recovery gate status

---

## 17. Non-Goals

This protocol does not provide:

* Offensive cyber techniques
* Exploit instructions
* Malware behavior
* Intrusion guidance
* Evasion methods
* Unauthorized access methods
* Fully autonomous legal judgment
* Fully autonomous public disclosure
* Fully autonomous irreversible action

The protocol is strictly defensive and governance-oriented.

---

## 18. Future Work

Future versions may include:

```text
v0.2:
  - defense-trace-record.schema.json
  - defense-trace-record.example.yaml
  - validation script integration

v0.3:
  - defense-agent-rank.schema.json
  - defense-agent-rank.example.yaml
  - role and authority validation

v0.4:
  - cyber-defense-constitution schema
  - article reference validation
  - governance status validation

v0.5:
  - Royalty OS defense contribution event integration
  - fault and correction event model

v1.0:
  - full Defense Court Protocol specification
  - formal conformance profile
  - implementation guide
```

---

## 19. Summary

The Defense Court Protocol transforms AI cyber defense from an improvised reaction model into a structured governance system.

It defines:

```text
Rank for responsibility.
Articles for behavior.
Defense Kernel for emergency response.
Trace for accountability.
Governance for safety.
Human Review for legitimacy.
```

In this model:

```text
The Twelve-Rank structure forms the defensive organization.
The Seventeen-Article Charter forms the defensive discipline.
The Trace Protocol forms the battle record.
The Governance Layer prevents overreach.
The Human Review Layer preserves final responsibility.
```

The result is an AI cyber defense system that can act quickly without becoming lawless, and remain governed without becoming too slow.

This is the core purpose of the Defense Court Protocol.
