import frappe
import unittest

class TestAuditReportEngagementReference(unittest.TestCase):
    def test_basic_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Report Engagement Reference"
        })
        doc.insert()
        self.assertTrue(doc.name)
