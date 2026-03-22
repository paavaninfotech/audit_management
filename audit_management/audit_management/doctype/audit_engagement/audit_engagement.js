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

    frm.add_custom_button(__("View Audit Programs"), () => {
			frappe.set_route("List", "Audit Program", {
				audit_engagement: frm.doc.name
			});
		}, __("View"));

		frm.add_custom_button(__("View Findings"), () => {
			frappe.set_route("List", "Audit Finding", {
				audit_engagement: frm.doc.name
			});
		}, __("View"));

		frm.add_custom_button(__("View CAPAs"), () => {
			frappe.set_route("List", "CAPA", {
				audit_engagement: frm.doc.name
			});
		}, __("View"));

		frm.add_custom_button(__("View Overdue CAPAs"), () => {
			frappe.set_route("List", "CAPA", {
				audit_engagement: frm.doc.name,
				is_overdue: 1
			});
		}, __("View"));
  }
});
