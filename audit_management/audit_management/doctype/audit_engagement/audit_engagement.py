import frappe
from frappe.model.document import Document

class AuditEngagement(Document):
    def on_update(self):
        self.update_status_from_milestones()
        if self.audit_plan:
            frappe.get_doc("Audit Plan", self.audit_plan).update_status_based_on_engagements()

    def update_status_from_milestones(self):
        milestones = self.get("milestones") or []
        if not milestones:
            self.db_set("status", "Draft")
            self.db_set("completion_percent", 0)
            return

        completed = len([m for m in milestones if m.status == "Done"])
        in_progress = len([m for m in milestones if m.status == "In Progress"])
        total = len(milestones)

        if completed == total:
            self.db_set("status", "Completed")
        elif in_progress > 0 or completed > 0:
            self.db_set("status", "In Progress")
        else:
            self.db_set("status", "Draft")

        percent_complete = round((completed / total) * 100, 1)
        self.db_set("completion_percent", percent_complete)

    def update_status_based_on_programs(self):
        programs = frappe.get_all("Audit Program", filters={"audit_engagement": self.name}, fields=["status"])
        if not programs:
            self.db_set("status", "Draft")
        elif all(p.status == "Finalized" for p in programs):
            self.db_set("status", "Completed")
        else:
            self.db_set("status", "In Progress")
    
    def validate(self):
        self.set_engagement_summary()

    def set_engagement_summary(self):
        self.total_programs = frappe.db.count(
            "Audit Program",
            {"audit_engagement": self.name}
        )

        self.open_findings = frappe.db.count(
            "Audit Finding",
            {
                "audit_engagement": self.name,
                "status": ["!=", "Closed"]
            }
        )

        self.open_capas = frappe.db.count(
            "CAPA",
            {
                "audit_engagement": self.name,
                "status": ["!=", "Closed"]
            }
        )

        self.overdue_capas = frappe.db.count(
            "CAPA",
            {
                "audit_engagement": self.name,
                "is_overdue": 1,
                "status": ["!=", "Closed"]
            }
        )