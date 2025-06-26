import frappe
import unittest

class TestAuditReportFinding(unittest.TestCase):
    def test_basic_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Report Finding"
        })
        doc.insert()
        self.assertTrue(doc.name)
