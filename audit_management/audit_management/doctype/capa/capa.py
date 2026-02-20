import frappe
from frappe.model.document import Document
from frappe.utils import today

class CAPA(Document):
    def validate(self):
        if self.status != "Closed" and self.target_date and self.target_date < today():
            self.status = "Overdue"

    def on_update(self):
        if self.reference_finding:
            frappe.get_doc("Audit Finding", self.reference_finding).update_status_from_linked_capa()