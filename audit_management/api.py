import frappe
from frappe import _
from frappe.model.mapper import get_mapped_doc


@frappe.whitelist()
def get_engagements_for_plan(audit_plan):
    return frappe.get_all("Audit Engagement", filters={"audit_plan": audit_plan}, fields=["name", "engagement_title"])

@frappe.whitelist()
def get_findings_for_engagements(engagement_names):
    if isinstance(engagement_names, str):
        import json
        engagement_names = json.loads(engagement_names)

    findings = []
    for engagement in engagement_names:
        rows = frappe.get_all(
            "Audit Finding",
            filters={"audit_engagement": engagement},
            fields=[
                "name as finding",
                "title",
                "observation",
                "severity",
                "root_cause",
                "risk_impact",
                "recommendation",
                "management_owner",
                "target_closure_date",
                "related_process",
                "audit_engagement",
                "status"
            ]
        )
        findings.extend(rows)

    return findings

@frappe.whitelist()
def get_findings_for_engagement(audit_engagement):
    return frappe.get_all(
        "Audit Finding",
        filters={"audit_engagement": audit_engagement},
        fields=["name","title", "observation", "severity"]
    )

@frappe.whitelist()
def import_procedures_from_template(template, program):
    template_doc = frappe.get_doc("Audit Procedure Template", template)
    program_doc = frappe.get_doc("Audit Program", program)

    for item in template_doc.procedures:
        catalog = frappe.get_doc("Audit Procedure Catalog", item.audit_procedure)
        program_doc.append("procedures", {
            "procedure_id":item.audit_procedure,
            "procedure_title": catalog.procedure_title,
            "expected_outcome": catalog.expected_outcome,
            "test_steps": catalog.test_steps,
            "status": "Planned"
        })

    program_doc.save()