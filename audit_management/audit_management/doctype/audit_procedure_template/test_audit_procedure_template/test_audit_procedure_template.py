import frappe
import unittest

class TestAuditProcedureTemplate(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Procedure Template",
            "template_name": "TEST001"
        })
        doc.insert()
        self.assertTrue(doc.name)
