import frappe
import unittest

class TestAuditControl(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Control",
            "control_id": "TEST001"
        })
        doc.insert()
        self.assertTrue(doc.name)
