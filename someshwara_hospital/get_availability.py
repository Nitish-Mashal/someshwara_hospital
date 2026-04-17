import frappe
import json


@frappe.whitelist()
def get_availability_data(practitioner, date, appointment=None):
    """
    Clean override to bypass annotation bug + fix dict issue
    """

    # ✅ Step 1: Convert string → dict
    if isinstance(appointment, str):
        try:
            appointment = json.loads(appointment)
        except Exception:
            appointment = None

    # ✅ Step 2: Convert dict → Frappe Doc (CRITICAL FIX)
    if isinstance(appointment, dict):
        appointment = frappe.get_doc(appointment)

    # ✅ Step 3: Call original logic (bypass validation)
    from healthcare.healthcare.doctype.patient_appointment import patient_appointment

    return patient_appointment.get_availability_data.__wrapped__(
        practitioner=practitioner,
        date=date,
        appointment=appointment
    )