import frappe
from frappe.model.document import Document

class AuditPlan(Document):
    def update_status_based_on_engagements(self):
        engagements = frappe.get_all("Audit Engagement", filters={"audit_plan": self.name}, fields=["status"])
        if not engagements:
            self.db_set("status", "Planned")
        elif all(e.status == "Completed" for e in engagements):
            self.db_set("status", "Completed")
        else:
            self.db_set("status", "In Progress")