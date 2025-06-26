import frappe
import unittest

class TestAuditProcedureTemplateItem(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Procedure Template Item",
            "audit_procedure": "TEST001"
        })
        doc.insert()
        self.assertTrue(doc.name)
