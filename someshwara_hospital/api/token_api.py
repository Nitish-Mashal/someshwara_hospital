import frappe
from frappe.utils import getdate, get_time

@frappe.whitelist(allow_guest=True)
def get_token_for_appointment(practitioner, appointment_date, appointment_time):
    """
    Returns token number for given practitioner + date + time
    """

    if not (practitioner and appointment_date and appointment_time):
        return None

    
    day = getdate(appointment_date).strftime("%A")

    
    appt_time = get_time(appointment_time)
    appt_minutes = appt_time.hour * 60 + appt_time.minute

    practitioner_doc = frappe.get_doc("Healthcare Practitioner", practitioner)

    for row in practitioner_doc.practitioner_schedules:
        schedule_doc = frappe.get_doc("Practitioner Schedule", row.schedule)

        for slot in schedule_doc.time_slots:
            if slot.day != day:
                continue

            from_minutes = int(slot.from_time.total_seconds() / 60)
            to_minutes = int(slot.to_time.total_seconds() / 60)

            if from_minutes <= appt_minutes < to_minutes:
                return slot.custom_token_no

    return None