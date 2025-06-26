// Copyright (c) 2025, Paavan Infotech and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Auditable Entity", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Auditable Entity', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button('Create Audit Plan', () => {
        frappe.new_doc('Audit Plan', {
          auditable_entity: frm.doc.name,
        });
      }, 'Actions');
    }
  }
});
