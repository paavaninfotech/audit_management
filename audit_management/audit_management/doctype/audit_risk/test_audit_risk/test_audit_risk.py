import frappe
import unittest

class TestAuditRisk(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Risk",
            "risk_id": "TEST001"
        })
        doc.insert()
        self.assertTrue(doc.name)
