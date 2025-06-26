frappe.ui.form.on('Audit Engagement', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button('Add Audit Program', () => {
        frappe.new_doc('Audit Program', {
          audit_engagement: frm.doc.name,
        });
      }, 'Actions');
      frm.add_custom_button('Generate Report', () => {
        frappe.new_doc('Audit Report', {
          audit_engagement: frm.doc.name,
        });
      }, 'Actions');
    }
  }
});
