# Copyright (c) 2026, Paavan Infotech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AuditProcedureRisk(Document):
    def validate(self):
        self.validate_unique_procedure_risk()

    def validate_unique_procedure_risk(self):
        if not self.audit_procedure or not self.audit_risk:
            return

        exists = frappe.db.exists(
            "Audit Procedure Risk",
            {
                "audit_procedure": self.audit_procedure,
                "audit_risk": self.audit_risk,
            }
        )

        if exists:
            frappe.throw(
                frappe._(
                    "Audit Risk '{0}' is already linked to Audit Procedure '{1}'."
                ).format(self.audit_risk, self.audit_procedure),
                title=frappe._("Duplicate Mapping"),
            )
