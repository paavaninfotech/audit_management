frappe.ui.form.on("Audit Report", {
	refresh(frm) {
		if (frm.is_new()) return;

		frm.add_custom_button(__("Get Engagements from Plan"), () => {
			if (!frm.doc.audit_plan) {
				frappe.msgprint(__("Please select an Audit Plan first."));
				return;
			}

			frappe.call({
				method: "audit_management.api.get_engagements_for_plan",
				args: {
					audit_plan: frm.doc.audit_plan
				},
				callback: function (r) {
					const rows = r.message || [];

					frm.clear_table("engagements");

					rows.forEach(row => {
						frm.add_child("engagements", {
							engagement: row.name,
							status: ""
						});
					});

					frm.refresh_field("engagements");

					frappe.msgprint(__("{0} engagement(s) added successfully.", [rows.length]));
				}
			});
		}, __("Actions"));

		frm.add_custom_button(__("Get Findings from Engagements"), () => {
			const engagements = (frm.doc.engagements || [])
				.map(d => d.engagement)
				.filter(Boolean);

			if (!engagements.length) {
				frappe.msgprint(__("No audit engagements found in the table."));
				return;
			}

			frappe.call({
				method: "audit_management.api.get_findings_for_engagements",
				args: {
					engagement_names: engagements
				},
				callback: function (r) {
					const findings = r.message || [];

					frm.clear_table("findings");

					findings.forEach(f => {
						frm.add_child("findings", {
							finding: f.finding || "",
							finding_title: f.title || "",
							description: f.observation || "",
							severity: f.severity || "",
							cause: f.root_cause || "",
							impact: f.risk_impact || "",
							recommendation: f.recommendation || "",
							audit_engagement: f.audit_engagement || "",
							management_owner: f.management_owner || "",
							target_resolution_date: f.target_closure_date || "",
							related_process: f.related_process || "",
							finding_status: f.status || ""
						});
					});

					frm.refresh_field("findings");

					frappe.msgprint(__("{0} finding(s) added successfully.", [findings.length]));
				}
			});
		}, __("Actions"));
	}
});