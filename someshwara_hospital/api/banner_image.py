# someshwara_hospital/api/banner_image.py
import frappe

@frappe.whitelist(allow_guest=True)
def get_banner_images():
    cache_key = "someshwara_homepage_banners"

    # 1️⃣ Try cache first
    cached = frappe.cache().get_value(cache_key)
    if cached:
        return cached

    # 2️⃣ Fetch from DB
    banners = frappe.get_all(
        "Banner Image",
        filters={
            "is_active": 1
        },
        fields=[
            "name",
            "name1",
            "date",
            "order_by_sequence",
            "upload_desktop_image",
            "upload_mobile_image",
            "link",
            "external_site"
        ],
        order_by="order_by_sequence asc"
    )

    # Normalize external_site
    for b in banners:
        b["external_site"] = 1 if str(b.get("external_site")).lower() in ["yes", "1"] else 0

    response = {
        "status": "success",
        "count": len(banners),
        "first_banner": banners[0] if banners else None,
        "data": banners
    }

    # 3️⃣ Cache for 10 minutes
    frappe.cache().set_value(cache_key, response, expires_in_sec=600)

    return response