import frappe
import unittest

class TestAuditBusinessProcess(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Business Process",
            "process_id": "TEST001"
        })
        doc.insert()
        self.assertTrue(doc.name)
