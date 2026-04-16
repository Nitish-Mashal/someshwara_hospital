import frappe

@frappe.whitelist(allow_guest=True)
def get_our_services():
    """
    Guest API to fetch all active Our Services
    Ordered by order_by_sequence (ascending)
    """

    try:
        services = frappe.get_all(
            "Our Services",
            filters={
                "is_active": 1
            },
            fields=[
                "name1",
                "description",
                "url",
                "created_date",
                "meta_title",
                "meta_keyword",
                "meta_description",
                "thumnail_image",
                "order_by_sequence"
            ],
            order_by="order_by_sequence asc"
        )

        return {
            "status": "success",
            "count": len(services),
            "data": services
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Our Services API Error")

        return {
            "status": "error",
            "message": str(e)
        }