# 🧾 Audit Management Module – End User Guide

This guide walks you through the full usage of the Audit Management System, from start to follow-up. It includes field explanations and best practices for each Doctype.

---

## 1️⃣ Auditable Entity

Used to register the subject of an audit, such as a company department or an external customer.

**Key Fields:**
- **Entity Type**: Select from Department, Business Unit, Process, or Legal Entity.
- **Audit Type**: Choose `Internal` (linked to Company) or `External` (linked to Customer).
- **Company**: Required for Internal audits.
- **Customer**: Required for External audits.
- **Risk Category**: Low / Medium / High — useful for prioritization.

**Steps:**
1. Navigate to Auditable Entity → New
2. Fill in the entity details.
3. Save and proceed to Audit Plan.

---

## 2️⃣ Audit Plan

Defines what will be audited, by whom, and within what timeframe.

**Key Fields:**
- **Auditable Entity**: Link to a previously created entity.
- **Audit Objective**: Short description of audit goals.
- **Start Date / End Date**: Audit timeline.
- **Audit Lead**: User responsible for leading the audit.

**Steps:**
1. Create an Audit Plan linked to an Auditable Entity.
2. Define scope, objective, and team.
3. Save and initiate Audit Engagement.

---

## 3️⃣ Audit Engagement

Captures the execution phase of the audit and tracks progress.

**Key Fields:**
- **Audit Plan**: Link to the audit plan.
- **Engagement Owner**: Manager responsible for execution.
- **Start / End Date**: Engagement duration.
- **Status**: Draft, In Progress, Completed.

**Steps:**
1. Create an Engagement and assign responsible personnel.
2. Use this to track progress and milestones.
3. Proceed to Audit Program.

---

## 4️⃣ Audit Program

Represents the detailed checklist and tests to be performed.

**Key Fields:**
- **Audit Engagement**: Link to parent engagement.
- **Procedure Title**: What is being tested.
- **Expected Outcome**: What success looks like.
- **Test Steps**: Optional notes for execution.

**Steps:**
1. Create multiple Audit Programs for an engagement.
2. Use them as a structured execution guide.

---

## 5️⃣ Audit Finding

Used to record issues found during audit execution.

**Key Fields:**
- **Audit Program**: Link to source procedure.
- **Description**: What was observed.
- **Severity**: Critical / Major / Minor.
- **Recommendation**: Suggested fix.
- **Status**: Open, Closed, Mitigated.

**Steps:**
1. Log a Finding for each deviation or issue.
2. Set severity and recommendation.
3. Move to CAPA creation.

---

## 6️⃣ CAPA (Corrective and Preventive Action)

Manages responses to findings.

**Key Fields:**
- **Reference Finding**: Finding being addressed.
- **Description**: What action will be taken.
- **Action Owner**: Person responsible.
- **Target Completion Date**: Deadline.
- **Status**: Open, In Progress, Closed.

**Steps:**
1. Link a CAPA to each relevant finding.
2. Track progress and responsibility.
3. Mark complete when verified.

---

## 7️⃣ Audit Report

Summarizes all findings and outcomes of the audit.

**Key Fields:**
- **Audit Engagement**: Link to source engagement.
- **Summary**: Executive overview.
- **Status**: Draft / Final.
- **Attachments**: Upload signed report.

**Steps:**
1. Prepare and submit the final report.
2. Use it for management review or compliance.

---

## 8️⃣ Follow-Up Audit

Verifies effectiveness of CAPA.

**Key Fields:**
- **Previous Audit**: The engagement being followed up.
- **Follow-up Date**: Scheduled recheck.
- **Status**: Scheduled / Completed.

**Steps:**
1. Schedule a follow-up after CAPA completion.
2. Verify implementation success.

---

## 9️⃣ Communication Log Entry

Tracks all audit-related communication.

**Key Fields:**
- **Reference Type / Name**: Link to CAPA, Finding, etc.
- **Communication Type**: Email, Call, Meeting.
- **Subject / Content**: Details of communication.

**Steps:**
1. Log emails or discussions for traceability.
2. Keep record against audit items.

---

## 📊 Dashboards & Reports

Dashboards and script reports give you:
- **CAPA Tracker** – status of corrective actions
- **Findings by Severity** – critical risk items
- **Audit Volume by Type** – internal vs external coverage

Access these via:
```
Audit Management → Dashboard / Reports
```

---

## ✅ Recommended Usage Flow

1. Create **Auditable Entity**
2. Define an **Audit Plan**
3. Launch an **Audit Engagement**
4. Build **Audit Programs**
5. Record **Findings**
6. Issue **CAPA** tasks
7. Finalize **Audit Report**
8. Conduct **Follow-Up Audit**

---

## 🔐 Role Access (Suggested)

| Role               | Permissions               |
|--------------------|---------------------------|
| Auditor            | Read/Write Audit Programs |
| Audit Manager      | Full on Plans & Reports   |
| Compliance Officer | View Reports & CAPAs      |

---

For questions, contact your administrator or project lead.
