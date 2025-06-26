import frappe
import unittest

class TestCAPA(unittest.TestCase):
    def test_create_capa(self):
        doc = frappe.get_doc({
            "doctype": "CAPA",
            "reference_finding": "TEST-FINDING",
            "description": "Corrective action to address issue",
            "status": "Open"
        })
        self.assertEqual(doc.status, "Open")
