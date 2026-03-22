frappe.ui.form.on('Audit Finding', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      frm.add_custom_button('Create CAPA', () => {
        frappe.new_doc('CAPA', {
          reference_finding: frm.doc.name,
        });
      }, 'Actions');
    }

    frm.set_query("procedure_id", function() {
			if (!frm.doc.audit_program) {
				return {};
			}

			return {
				query: "audit_management.audit_management.doctype.audit_finding.audit_finding.get_program_procedures",
				filters: {
					audit_program: frm.doc.audit_program
				}
			};
		});

    frm.add_custom_button(__("Fetch Risks & Controls"), () => {
			if (!frm.doc.procedure_id) {
				frappe.msgprint(__("Please select an Audit Procedure first."));
				return;
			}

			frappe.call({
				method: "audit_management.audit_management.doctype.audit_finding.audit_finding.get_related_risks_and_controls",
				args: {
					audit_procedure: frm.doc.procedure_id
				},
				callback: function(r) {
					const data = r.message || {};

					frm.clear_table("related_risks");
					frm.clear_table("related_controls");

					(data.risks || []).forEach(row => {
						frm.add_child("related_risks", {
							audit_risk: row.audit_risk || ""
						});
					});

					(data.controls || []).forEach(row => {
						frm.add_child("related_controls", {
							audit_control: row.audit_control || ""
						});
					});

					frm.refresh_field("related_risks");
					frm.refresh_field("related_controls");

					frappe.show_alert({
						message: __("Related risks and controls fetched successfully."),
						indicator: "green"
					});
				}
			});
		}, __("Actions"));
	},

	procedure_id(frm) {
		if (!frm.doc.audit_procedure) {
			return;
		}

		if ((frm.doc.related_risks || []).length || (frm.doc.related_controls || []).length) {
			return;
		}

		frappe.call({
			method: "audit_management.audit_management.doctype.audit_finding.audit_finding.get_related_risks_and_controls",
			args: {
				audit_procedure: frm.doc.audit_procedure
			},
			callback: function(r) {
				const data = r.message || {};

				(data.risks || []).forEach(row => {
					frm.add_child("related_risks", {
						audit_risk: row.audit_risk || ""
					});
				});

				(data.controls || []).forEach(row => {
					frm.add_child("related_controls", {
						audit_control: row.audit_control || ""
					});
				});

				frm.refresh_field("related_risks");
				frm.refresh_field("related_controls");
			}
		});
  }
});
