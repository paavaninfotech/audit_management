frappe.ui.form.on('Audit Program', {
  refresh: function(frm) {
    if (!frm.is_new()) {
      // Button: Log Finding
      frm.add_custom_button('Log Finding', () => {
        frappe.new_doc('Audit Finding', {
          audit_program: frm.doc.name,
        });
      }, 'Actions');

      // Button: Import Procedures from Template
      frm.add_custom_button('Import Procedures from Template', () => {
        frappe.prompt([
          {
            fieldtype: 'Link',
            label: 'Audit Procedure Template',
            fieldname: 'template',
            options: 'Audit Procedure Template',
            reqd: 1
          }
        ], (values) => {
          frappe.call({
            method: 'audit_management.api.import_procedures_from_template',
            args: {
              template: values.template,
              program: frm.doc.name
            },
            callback: () => {
              frappe.msgprint('Procedures imported successfully.');
              frm.reload_doc();
            }
          });
        }, 'Select Template');
      });
    }
  },

  audit_engagement(frm) {
    // Dynamic filter for Engagement Milestone linked to selected Audit Engagement
    frm.set_query("engagement_milestone", () => {
      return {
        filters: {
          parent: frm.doc.audit_engagement
        }
      };
    });
  }
});