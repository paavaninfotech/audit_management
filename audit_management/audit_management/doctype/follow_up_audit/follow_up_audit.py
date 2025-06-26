import frappe
from frappe.model.document import Document

class FollowUpAudit(Document):
    def validate(self):
        findings = frappe.get_all("Audit Findings", filters={"follow_up_audit": self.name}, fields=["status"])
        capa_status = frappe.get_all("CAPA", filters={"follow_up_audit": self.name}, fields=["status"])

        if all(f["status"] == "Closed" for f in findings) and all(c["status"] == "Closed" for c in capa_status):
            self.status = "Resolved"
        elif any(c["status"] in ("Open", "Overdue") for c in capa_status):
            self.status = "Unresolved"
        else:
            self.status = "In Progress"