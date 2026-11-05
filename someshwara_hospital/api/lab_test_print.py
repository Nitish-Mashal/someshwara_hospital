import frappe
from frappe import _


@frappe.whitelist()
def set_print_templates(name, templates=None):
    """Persist the print template selection for a Lab Test.

    Uses frappe.db.set_value (raw update) so no ORM/validation side effects
    run (CustomLabTest.validate, modified timestamp, etc.).
    """
    if not name:
        frappe.throw(_("Lab Test is required"))

    if not (
        frappe.has_permission("Lab Test", "write", doc=name)
        or frappe.has_permission("Lab Test", "print", doc=name)
    ):
        frappe.throw(_("Not permitted to update print selection"), frappe.PermissionError)

    if isinstance(templates, (list, tuple)):
        parts = [str(t).strip() for t in templates]
    else:
        parts = [t.strip() for t in (templates or "").split(",")]

    value = ",".join(t for t in parts if t)
    frappe.db.set_value(
        "Lab Test", name, "custom_selected_print_templates", value, update_modified=False
    )
    return value


def filter_selected_templates(doc, method=None, print_settings=None):
    """doc_events hook: Lab Test.before_print.

    Filters result rows in memory (no save) so every print format - preview
    and PDF - only renders the selected templates. Empty selection = print all.
    """
    selected_raw = doc.get("custom_selected_print_templates") or ""
    selected = {t.strip() for t in selected_raw.split(",") if t.strip()}
    if not selected:
        return

    filtered = {}
    any_rows = False
    any_match = False
    for fieldname in ("normal_test_items", "descriptive_test_items"):
        rows = doc.get(fieldname) or []
        if not rows:
            continue
        any_rows = True
        if any(row.get("template") in selected for row in rows):
            any_match = True
        filtered[fieldname] = [
            row for row in rows if not row.get("template") or row.get("template") in selected
        ]

    # a stale selection that matches nothing must not blank the report
    if not any_rows or not any_match:
        return

    for fieldname, kept in filtered.items():
        doc.set(fieldname, kept)
