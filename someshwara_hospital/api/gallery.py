import frappe

@frappe.whitelist(allow_guest=True)
def get_gallery_images():

    records = frappe.get_all(
        "Gallery Image",
        filters={"is_active": 1},
        fields=["name", "upload_image", "date"],
        order_by="date desc"
    )

    response = {}
    all_tags = set()

    for row in records:

        # ✅ Correct way to fetch tags
        tags = frappe.get_all(
            "Tag Link",
            filters={
                "document_type": "Gallery Image",
                "document_name": row.name
            },
            pluck="tag"
        )

        # If no tags → fallback
        if not tags:
            tags = ["All"]

        for tag in tags:
            all_tags.add(tag)

            if tag not in response:
                response[tag] = []

            if row.upload_image:
                response[tag].append(row.upload_image)

    return {
        "status": "success",
        "tags": sorted(list(all_tags)),
        "images_by_tag": response
    }