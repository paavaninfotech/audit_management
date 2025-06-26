import frappe
import unittest

class TestAuditReport(unittest.TestCase):
    def test_basic_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Report"
        })
        doc.insert()
        self.assertTrue(doc.name)
