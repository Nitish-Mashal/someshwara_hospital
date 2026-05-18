import frappe

@frappe.whitelist(allow_guest=True)
def get_treatments():
    """
    Guest API to fetch all active Treatments
    Ordered by order_by_sequence (ascending)
    """

    try:
        treatments = frappe.get_all(
            "Treatments",
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
            "count": len(treatments),
            "data": treatments
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Treatments API Error")

        return {
            "status": "error",
            "message": str(e)
        }