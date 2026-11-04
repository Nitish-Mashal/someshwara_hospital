import json

import frappe
from frappe.utils import safe_decode

DOCTYPE = "Module Def"
CACHE_KEY = "_user_settings"


def execute():
    """Reset the saved Desk list-view filters of the Module Def list.

    The list view stores the filters a user applied in the `__UserSettings`
    table and the `_user_settings` Redis hash, and restores them with top
    priority on every visit (see frappe/public/js/frappe/list/list_view.js).
    A leftover filter - for example one saved before the labratory module was
    renamed, or a search that was applied once - keeps Module Def records
    hidden from the Desk list forever, even though the records exist in the
    database.

    This clears the saved filters for the Module Def list only, so every
    Module Def record is listed again. Sort order and all other view settings
    are left untouched, and no Module Def records are created or modified.
    Safe to run any number of times.
    """
    users = _collect_users()

    for user in sorted(users):
        cached = frappe.cache.hget(CACHE_KEY, f"{DOCTYPE}::{user}")
        stored = frappe.db.sql(
            """select data from `__UserSettings`
            where user = %s and doctype = %s""",
            (user, DOCTYPE),
        )
        stored = stored and stored[0][0]

        cleaned = _without_filters(cached)
        if cleaned:
            frappe.cache.hset(CACHE_KEY, f"{DOCTYPE}::{user}", cleaned)

        cleaned = _without_filters(stored)
        if cleaned:
            frappe.db.sql(
                """update `__UserSettings` set data = %s
                where user = %s and doctype = %s""",
                (cleaned, user, DOCTYPE),
            )


def _collect_users() -> set:
    """Users that have Module Def list settings in Redis or in the database."""
    users = set()

    for key in frappe.cache.hgetall(CACHE_KEY) or {}:
        key = safe_decode(key)
        if key.startswith(f"{DOCTYPE}::"):
            users.add(key.split("::", 1)[1])

    users.update(
        row[0]
        for row in frappe.db.sql(
            """select distinct user from `__UserSettings`
            where doctype = %s""",
            (DOCTYPE,),
        )
    )

    return users


def _without_filters(raw) -> str | None:
    """Return the settings JSON with view filters cleared, or None to keep it."""
    if not raw:
        return None

    try:
        data = json.loads(raw)
    except (TypeError, ValueError):
        return None

    if not isinstance(data, dict):
        return None

    changed = False
    for view_settings in data.values():
        if isinstance(view_settings, dict) and view_settings.get("filters"):
            view_settings["filters"] = []
            changed = True

    return json.dumps(data) if changed else None
