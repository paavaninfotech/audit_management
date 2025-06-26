frappe.ui.form.on('Audit Finding', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button('Create CAPA', () => {
        frappe.new_doc('CAPA', {
          reference_finding: frm.doc.name,
        });
      }, 'Actions');
    }
  }
});
