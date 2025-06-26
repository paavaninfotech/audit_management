frappe.ui.form.on('CAPA', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button('Log Communication', () => {
        frappe.new_doc('Communication Log Entry', {
          reference_type: 'CAPA',
          reference_name: frm.doc.name,
        });
      }, 'Actions');
      frm.add_custom_button('Schedule Follow-up', () => {
        frappe.new_doc('Follow-Up Audit', {
          previous_audit: frm.doc.name,
        });
      }, 'Actions');

    }
  }
});
