import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate

class CAPA(Document):
    
    def on_update(self):
        if self.reference_finding:
            frappe.get_doc("Audit Finding", self.reference_finding).update_status_from_linked_capa()

    
    def validate(self):
        self.set_overdue_flag()
        self.validate_closure_fields()

    def set_overdue_flag(self):
        self.is_overdue = 0

        if self.target_date and self.status != "Closed":
            if getdate(self.target_date) < getdate(today()):
                self.is_overdue = 1

    def validate_closure_fields(self):
        if self.status == "Closed":
            if not self.evidence_of_closure:
                frappe.throw("Please provide Evidence of Closure before closing the CAPA.")

            if not self.closure_validated_by:
                frappe.throw("Please set Closure Validated By before closing the CAPA.")

            if not self.closure_validated_on:
                frappe.throw("Please set Closure Validated On before closing the CAPA.")