frappe.ui.form.on('Audit Plan', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button('Start Engagement', () => {
        frappe.new_doc('Audit Engagement', {
          audit_plan: frm.doc.name,
        });
      }, 'Actions');
    }
  }
});
