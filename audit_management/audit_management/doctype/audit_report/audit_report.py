import frappe
from frappe.model.document import Document

class AuditReport(Document):
    def on_submit(self):
        self.db_set("status", "Final")
    
    def validate(self):
        self.set_report_summary()

    def set_report_summary(self):
        findings = self.findings or []

        self.total_findings = len(findings)
        self.high_severity_findings = 0
        self.medium_severity_findings = 0
        self.low_severity_findings = 0

        for row in findings:
            severity = (row.severity or "").strip().lower()
            if severity == "high":
                self.high_severity_findings += 1
            elif severity == "medium":
                self.medium_severity_findings += 1
            elif severity == "low":
                self.low_severity_findings += 1

        self.open_capas = 0
        self.overdue_capas = 0

        engagements = [row.engagement for row in (self.engagements or []) if row.engagement]
        if not engagements:
            return

        self.open_capas = frappe.db.count(
            "CAPA",
            {
                "audit_engagement": ["in", engagements],
                "status": ["!=", "Closed"]
            }
        )

        self.overdue_capas = frappe.db.count(
            "CAPA",
            {
                "audit_engagement": ["in", engagements],
                "status": ["!=", "Closed"],
                "is_overdue": 1
            }
        )