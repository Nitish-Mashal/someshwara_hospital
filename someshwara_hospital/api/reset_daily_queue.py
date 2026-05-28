import frappe


def reset_daily_queue():

    masters = frappe.get_all(
        "Practitioner Queue Master",
        fields=["name", "queue_start_number"]
    )

    for master in masters:

        doc = frappe.get_doc(
            "Practitioner Queue Master",
            master.name
        )

        doc.current_queue_number = 0

        doc.save(ignore_permissions=True)

    frappe.db.commit()