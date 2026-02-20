# Copyright (c) 2026, Paavan Infotech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AuditProcedureControl(Document):
    def validate(self):
        self.validate_unique_procedure_control()

    def validate_unique_procedure_control(self):
        if not self.audit_procedure or not self.audit_control:
            return

        exists = frappe.db.exists(
            "Audit Procedure Control",
            {
                "audit_procedure": self.audit_procedure,
                "audit_control": self.audit_control,
            }
        )

        if exists:
            frappe.throw(
                frappe._(
                    "Audit Control '{0}' is already linked to Audit Procedure '{1}'."
                ).format(self.audit_control, self.audit_procedure),
                title=frappe._("Duplicate Mapping"),
            )
