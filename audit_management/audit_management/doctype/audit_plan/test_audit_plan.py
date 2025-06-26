# Copyright (c) 2025, Your Company and contributors
# See license.txt

import frappe
import unittest
from frappe.test_runner import make_test_records

class TestAuditPlan(unittest.TestCase):
    def setUp(self):
        frappe.set_user("Administrator")

    def test_create_audit_plan(self):
        audit_plan = frappe.get_doc({
            "doctype": "Audit Plan",
            "audit_title": "Test Audit FY25",
            "audit_type": "Internal",
            "company": frappe.defaults.get_user_default("Company"),
            "start_date": "2025-04-01",
            "end_date": "2025-04-30",
            "objective": "Test internal controls",
            "scope": "Finance and Inventory",
            "status": "Planned",
            "audit_team": [
                {
                    "team_member": frappe.session.user,
                    "role": "Lead Auditor"
                }
            ]
        })
        audit_plan.insert()
        self.assertTrue(audit_plan.name)
        self.assertEqual(audit_plan.status, "Planned")
