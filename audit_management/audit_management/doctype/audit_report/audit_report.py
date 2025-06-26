import frappe
from frappe.model.document import Document

class AuditReport(Document):
    def on_submit(self):
        self.db_set("status", "Final")