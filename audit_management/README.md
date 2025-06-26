# Audit Management System for ERPNext

This is a custom Frappe/ERPNext app designed for **Audit Firms** and **Internal Audit Teams** to plan, execute, track, and report audits effectively.

---

## 🚀 Features

- 📌 **Audit Universe**: Define auditable entities by client or company.
- 📅 **Audit Plan**: Schedule audits with type, team, and timeline.
- 📋 **Audit Engagement**: Field-level execution tracking with milestones.
- ✅ **Audit Program**: Detailed audit procedure checklist.
- 🕵️‍♂️ **Audit Findings**: Capture non-compliances and issues.
- 🔧 **CAPA**: Track corrective and preventive actions.
- 📄 **Audit Report**: Auto-generate executive summaries and recommendations.
- 🔁 **Follow-Up Audit**: Ensure closure of findings and CAPAs.
- 📊 **Communication Logs**: Record all audit-related interactions.

---

## 📁 Doctypes

- Auditable Entity
- Audit Plan
- Audit Engagement
- Audit Program
- Audit Finding
- CAPA (Corrective and Preventive Action)
- Audit Report
- Follow-Up Audit
- Communication Log Entry (Child)
- Audit Team Member (Child)
- Audit Procedure (Child)
- Report Finding (Child)
- Engagement Milestone (Child)

---

## 🛠 Installation

```bash
cd frappe-bench
bench get-app audit_management https://github.com/your-org/audit_management.git
bench --site your-site-name install-app audit_management
```

---

## 📚 License

MIT License

---

## 🙌 Contributors

Developed by [Your Name / Organization]

Feel free to fork and contribute via pull requests!
