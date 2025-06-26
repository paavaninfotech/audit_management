import frappe
import unittest

class TestAuditProcedureCatalog(unittest.TestCase):
    def test_creation(self):
        doc = frappe.get_doc({
            "doctype": "Audit Procedure Catalog",
            "procedure_title": "TEST001"
        })
        doc.insert()
        self.assertTrue(doc.name)
