# Audit Management Module

The **Audit Management** module is designed for audit firms and internal compliance teams to plan, execute, and monitor audits across multiple companies and clients.

---

## 🏢 Key Stakeholders

- Internal Audit Teams
- External Audit Firms
- Compliance Officers
- Management

---

## 📦 Core Features

### 1. **Auditable Entity**
Defines the unit, department, process, or client being audited.

- Fields: Entity Type, Risk Category, Audit Type (Internal/External), Customer/Company Link

### 2. **Audit Plan**
Captures the scope, objectives, audit period, and responsible audit team.

- Includes audit planning milestones and deadlines.

### 3. **Audit Engagement**
Links the plan with execution phases and resource allocation.

- Tracks status of engagement and resource assignments.

### 4. **Audit Program**
Details the procedures, checklist, and control tests to be performed.

- Supports child tables for repeatable procedures.

### 5. **Audit Finding**
Captures observations during the audit, severity, impact, and recommendations.

- Classifies findings into critical, major, and minor.

### 6. **CAPA (Corrective and Preventive Action)**
Linked to findings to track resolution actions, owners, deadlines, and status.

- Status: Open, In Progress, Closed, Overdue

### 7. **Audit Report**
Summarizes engagement, key findings, management responses, and sign-off.

- Attaches final documents and approvals.

### 8. **Follow-Up Audit**
Conducts post-audit verification of CAPA effectiveness and closure.

---

## 🧾 Communication & Logs

### - **Communication Log Entry**
Used to record any formal communication or notes exchanged during an audit.

---

## 📊 Dashboards & Reports

- **Dashboards:**
  - Findings by Severity
  - CAPA Status Overview
  - Audit Volume by Type

- **Script Reports:**
  - Open Audit Findings
  - CAPA Tracker

---

## 🧪 Testing

All core doctypes include unit test coverage using `frappe.get_doc()` creation tests.

---

## ⚙️ Setup Instructions

1. Install the app:
   ```bash
   bench get-app audit_management
   bench --site your-site-name install-app audit_management
   ```

2. Reload all custom doctypes:
   ```bash
   bench --site your-site-name migrate
   ```

---

## 🔐 Permissions & Roles

Define role-based access to:
- View/Manage Audit Records
- Submit Reports
- Track CAPA Tasks

You can customize via **Role Permission Manager**.

---

## 📄 Terms & Privacy

Refer to:
- [Terms of Service](terms_of_service.md)
- [Privacy Policy](privacy_policy.md)

---

## 🧠 Future Enhancements

- Workflow-based approvals for CAPA and Audit Reports
- Email Notifications and Reminders
- Integration with DMS for audit evidence
- Risk Heatmaps and scoring models

---

For questions or contributions, visit the GitHub repository.
