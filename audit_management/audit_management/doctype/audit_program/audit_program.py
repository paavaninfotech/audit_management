import frappe
from frappe.model.document import Document

class AuditProgram(Document):
    def on_update(self):
        if self.audit_engagement:
            frappe.get_doc("Audit Engagement", self.audit_engagement).update_status_based_on_programs()