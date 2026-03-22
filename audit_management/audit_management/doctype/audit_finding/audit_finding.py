import frappe
from frappe.model.document import Document

class AuditFinding(Document):
    def update_status_from_linked_capa(self):
        linked_capas = frappe.get_all("CAPA", filters={"reference_finding": self.name}, fields=["status"])
        if linked_capas:
            if all(capa["status"] == "Closed" for capa in linked_capas):
                self.db_set("status", "Closed")
            else:
                self.db_set("status", "Under Review")
        else:
            self.db_set("status", "Open")
    
    def validate(self):
        self.validate_target_closure_date()

    def validate_target_closure_date(self):
        if self.target_closure_date and self.finding_date:
            if self.target_closure_date < self.finding_date:
                frappe.throw("Target Closure Date cannot be before the Audit Date.")

@frappe.whitelist()
def get_related_risks_and_controls(audit_procedure):
    if not audit_procedure:
        return {
            "risks": [],
            "controls": []
        }

    procedure_risks = frappe.get_all(
        "Audit Procedure Risk",
        filters={
            "audit_procedure": audit_procedure
        },
        fields=[
            "audit_risk"
        ],
        order_by="creation asc"
    )

    procedure_controls = frappe.get_all(
        "Audit Procedure Control",
        filters={
            "audit_procedure": audit_procedure
        },
        fields=[
            "audit_control"
        ],
        order_by="creation asc"
    )

    return {
        "risks": procedure_risks,
        "controls": procedure_controls
    }

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_program_procedures(doctype, txt, searchfield, start, page_len, filters):
    audit_program = filters.get("audit_program")
    if not audit_program:
        return []

    procedure_names = frappe.get_all(
        "Audit Procedure",
        filters={"parent": audit_program},
        pluck="procedure_id"
    )

    procedure_names = [p for p in procedure_names if p]
    if not procedure_names:
        return []

    # Return rows as tuples/lists, not dicts
    return frappe.db.sql(
        f"""
        SELECT
            apc.name,
            apc.procedure_title
        FROM `tabAudit Procedure Catalog` apc
        WHERE apc.name IN %(procedure_names)s
          AND (
                apc.name LIKE %(txt)s
                OR apc.procedure_title LIKE %(txt)s
              )
        ORDER BY apc.procedure_title ASC
        LIMIT %(start)s, %(page_len)s
        """,
        {
            "procedure_names": tuple(procedure_names),
            "txt": f"%{txt}%",
            "start": start,
            "page_len": page_len,
        },
        as_list=True,
    )