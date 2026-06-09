import frappe
from frappe.utils import cint


def generate_queue_number(doc, method=None):

    if doc.custom_queue_number:
        return

    if not doc.practitioner:
        return

    master_name = frappe.db.get_value(
        "Practitioner Queue Master",
        {"practitioner": doc.practitioner}
    )

    if not master_name:
        frappe.throw(
            f"Queue Master not found for Practitioner: {doc.practitioner}"
        )

    master = frappe.get_doc(
        "Practitioner Queue Master",
        master_name
    )

    if not master.current_queue_number:
        next_no = 1
    else:
        next_no = cint(master.current_queue_number) + 1

    doc.custom_queue_number = f"SH-{next_no:03d}"

    master.current_queue_number = next_no
    master.save(ignore_permissions=True)