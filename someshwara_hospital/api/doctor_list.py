import frappe

@frappe.whitelist(allow_guest=True)
def get_doctors():
    """
    Returns a list of all Healthcare Practitioners with basic info.
    """

    doctors = frappe.get_all(
        "Healthcare Practitioner",
        #  filters={
        #     "custom_online_visibility": "Yes"
        # },
        fields=[
            "name",
            "first_name",
            "department",
            "image",
            "hospital",
            "custom_order_by",
            "custom_experience",
            "custom_qualification",
            "custom_online_visibility"
            # "custom_linkedin",
            # "custom_facebook",
            # "custom_twitter",
        ],
        order_by="custom_order_by asc"
    )

    return doctors


@frappe.whitelist(allow_guest=True)
def get_doctor(id):
    """
    Returns detailed info for a single doctor by name (ID).
    """
    doctor = frappe.get_all(
        "Healthcare Practitioner",
        filters={"name": id,"custom_online_visibility": "Yes"},
        fields=[
            "name",
            "first_name",
            "last_name",
            "department",
            "image",
            "hospital",
            "custom_experience",
            "custom_qualification",
            "custom_online_visibility"
            # "custom_linkedin",
            # "custom_facebook",
            # "custom_twitter",
            # "custom_working_at",
            # "custom_joining_date",
            # "op_consulting_charge",
            # "hospital",
            # "custom_degree",
        ],
    )

    if not doctor:
        frappe.throw("Doctor not found", frappe.DoesNotExistError)

    return doctor[0]