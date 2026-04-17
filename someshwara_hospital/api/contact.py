import frappe
import json

@frappe.whitelist(allow_guest=True)
def submit_contact():
    try:
        # Parse incoming JSON
        data = frappe.local.form_dict or {}
        if isinstance(data, str):
            data = json.loads(data)

    except Exception:
        return {
            "status": "error",
            "message": "Invalid JSON data"
        }

    # Map fields
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    source = data.get("source")
    comments = data.get("comments")

    # Validation
    if not name or not email:
        return {
            "status": "error",
            "message": "Name and Email are required"
        }

    try:
        doc = frappe.get_doc({
            "doctype": "Contact Enquiry",
            "name1": name,
            "email": email,
            "phone_number": phone,
            "how_did_you_find_us": source,
            "comments": comments,
            "status": "Open"   # default status
        })

        doc.insert(ignore_permissions=True)
        frappe.db.commit()

    except Exception:
        frappe.log_error(frappe.get_traceback(), "Contact Enquiry API Error")
        return {
            "status": "error",
            "message": "Failed to save enquiry"
        }

    return {
        "status": "success",
        "message": "Thank you for contacting Someshwara Hospital. Our team will connect with you shortly."
    }