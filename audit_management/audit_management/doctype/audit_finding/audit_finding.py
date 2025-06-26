import frappe
from frappe.model.document import Document

class AuditFinding(Document):
    def update_status_from_linked_capa(self):
        linked_capas = frappe.get_all("CAPA", filters={"audit_finding": self.name}, fields=["status"])
        if linked_capas:
            if all(capa["status"] == "Closed" for capa in linked_capas):
                self.db_set("status", "Closed")
            else:
                self.db_set("status", "Under Review")
        else:
            self.db_set("status", "Open")