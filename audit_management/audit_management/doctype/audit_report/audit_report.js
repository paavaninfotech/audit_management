frappe.ui.form.on('Audit Report', {
    refresh(frm) {
        if (!frm.is_new() && frm.doc.audit_plan) {
            frm.add_custom_button('Get Engagements from Plan', () => {
                frappe.call({
                    method: 'audit_management.api.get_engagements_for_plan',
                    args: {
                        audit_plan: frm.doc.audit_plan
                    },
                    callback: function(r) {
                        if (r.message) {
                            frm.clear_table('engagements');
                            r.message.forEach(row => {
                                frm.add_child('engagements', {
                                    audit_engagement: row.name,
                                    title: row.engagement_title
                                });
                            });
                            frm.refresh_field('engagements');
                            frappe.msgprint('Engagements added successfully.');
                        }
                    }
                });
            }, 'Actions');

            frm.add_custom_button('Get Findings from Engagements', () => {
                const engagements = frm.doc.engagements.map(e => e.engagement);
                if (!engagements.length) {
                    frappe.msgprint('No audit engagements found in the table.');
                    return;
                }
                frappe.call({
                    method: 'audit_management.api.get_findings_for_engagements',
                    args: {
                        engagement_names: engagements
                    },
                    callback: function(r) {
                        if (r.message) {
                            frm.clear_table('findings');
                            r.message.forEach(f => {
                                frm.add_child('findings', {
                                    finding: f.finding,
                                    finding_title: f.title,
                                    description: f.observation,
                                    severity: f.severity,
                                    audit_engagement: f.audit_engagement
                                });
                            });
                            frm.refresh_field('findings');
                            frappe.msgprint('Findings added successfully.');
                        }
                    }
                });
            }, 'Actions');
        }
    }
});