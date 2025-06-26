import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label":"Title","fieldname":"title","fieldtype":"Data","width":200},
        {"label":"Engagement","fieldname":"audit_engagement","fieldtype":"Link","options":"Audit Engagement","width":150},
        {"label":"Category","fieldname":"category","fieldtype":"Data","width":120},
        {"label":"Severity","fieldname":"severity","fieldtype":"Select","width":100},
        {"label":"Risk Impact","fieldname":"risk_impact","fieldtype":"Data","width":200},
        {"label":"Status","fieldname":"status","fieldtype":"Select","width":100},
        {"label":"Finding Date","fieldname":"finding_date","fieldtype":"Date","width":100}
    ]

    data = frappe.get_all("Audit Finding", fields=[
        "name as title", "audit_engagement", "category", "severity", "risk_impact", "status", "finding_date"
    ])

    return columns, data
