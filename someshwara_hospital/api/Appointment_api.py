from healthcare.healthcare.doctype.patient_appointment.patient_appointment import (
    PatientAppointment
)

import frappe, json

# ✅ Get all Medical Departments
@frappe.whitelist(allow_guest=True)
def get_departments():
    try:
        departments = frappe.get_all(
            "Medical Department",
            fields=["name", "department"]
        )
        return {"status": "success", "data": departments}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_departments API Error")
        return {"status": "error", "message": str(e)}

# ✅ Get Practitioners by Department
@frappe.whitelist(allow_guest=True)
def get_practitioners(department):
    try:
        doctors = frappe.get_all(
            "Healthcare Practitioner",
            filters={
                "custom_online_visibility": "Yes"
            },
            fields=[
                "name",
                "first_name",
                "last_name",
                "designation",
                "custom_online_visibility",
                "custom_order_by"   # ✅ Added field
            ],
            order_by="custom_order_by asc"   # ✅ Sort ascending
        )

        return {
            "status": "success",
            "data": doctors
        }

    except Exception as e:
        frappe.log_error(
            frappe.get_traceback(),
            "get_practitioners API Error"
        )

        return {
            "status": "error",
            "message": str(e)
        }


# ✅ Get Appointment Types by Department (and hide specific type for a doctor)
@frappe.whitelist(allow_guest=True)
def get_appointment_types(department=None, practitioner=None):
    try:
        filters = {}

        if department:
            filters["department"] = department

        appointment_types = frappe.get_all(
            "Appointment Type",
            filters=filters,
            fields=["name", "appointment_type"]
        )

        # ✅ Hide ONLY "1st Appointment" for this doctor
        if practitioner == "HLC-PRAC-2026-00001":
            appointment_types = [
                a for a in appointment_types
                if a.get("appointment_type") != "1st Appointment"
            ]

        return {
            "status": "success",
            "data": appointment_types
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "get_appointment_types API Error")
        return {
            "status": "error",
            "message": str(e)
        }

#✅ Get Doctor Schedule
import frappe

# @frappe.whitelist(allow_guest=True)
# def get_doctor_schedule(practitioner):
#     """Return day and time slots for a given practitioner"""
#     try:
#         practitioner_doc = frappe.get_doc("Healthcare Practitioner", practitioner)
#         schedule_list = []

#         for row in practitioner_doc.practitioner_schedules:
#             schedule_doc = frappe.get_doc("Practitioner Schedule", row.schedule)
#             for s in schedule_doc.time_slots:
#                 schedule_list.append({
#                     "day": s.day,
#                     "from_time": s.from_time,
#                     "to_time": s.to_time,
#                     "custom_token_no": s.custom_token_no
#                 })

#         return schedule_list

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "get_doctor_schedule_error")
#         return {"status": "error", "message": str(e)}
import frappe
from frappe.utils import getdate

@frappe.whitelist(allow_guest=True)
def get_doctor_schedule(practitioner, appointment_date=None):
    """Return all slots without booking restrictions"""

    try:
        if not practitioner:
            return []

        if appointment_date:
            appointment_date = getdate(appointment_date)

        practitioner_doc = frappe.get_doc(
            "Healthcare Practitioner",
            practitioner
        )

        schedule_list = []

        for row in practitioner_doc.practitioner_schedules:
            schedule_doc = frappe.get_doc(
                "Practitioner Schedule",
                row.schedule
            )

            for s in schedule_doc.time_slots:
                schedule_list.append({
                    "appointment_date": appointment_date,
                    "day": s.day,
                    "from_time": s.from_time,
                    "to_time": s.to_time,
                    "custom_token_no": s.custom_token_no,
                    "booked": False
                })

        return schedule_list

    except Exception:
        frappe.log_error(
            frappe.get_traceback(),
            "get_doctor_schedule_error"
        )
        return []



# ✅ Create Patient Appointment (Guest Booking Supported)

import frappe
import json
from datetime import datetime


def get_or_create_patient(name, phone, custom_email, gender, age):
    """
    Create Patient if not exists (based on phone)
    Handles mandatory `first_name` field
    """

    # Check existing patient by phone
    patient = frappe.db.get_value(
        "Patient",
        {"mobile": phone},
        "name"
    )

    if patient:
        return patient

    # Create new Patient
    patient_doc = frappe.get_doc({
        "doctype": "Patient",

        # ✅ REQUIRED FIELD IN YOUR SYSTEM
        "first_name": name,

        # Optional but safe (some setups still use it)
        "patient_name": name,

        "mobile": phone,
        "custom_email": custom_email,
        "sex": gender,
        "age": age
    })

    patient_doc.insert(ignore_permissions=True)
    frappe.db.commit()

    return patient_doc.name


import frappe
import json
from datetime import datetime


@frappe.whitelist(allow_guest=True)
def create_appointment():
    """Create Patient Appointment from Website (Guest Allowed)"""

    try:
        # ---------------------------------------------------
        # 1️⃣ Read Incoming Data
        # ---------------------------------------------------
        data = frappe.local.form_dict
        if isinstance(data, str):
            data = json.loads(data)

        patient_name = data.get("name1")
        custom_email = data.get("custom_email")
        gender = data.get("gender")
        phone = data.get("phone")
        age = data.get("age")

        practitioner = data.get("practitioner")
        department = data.get("department")
        appointment_type = data.get("appointment_type")
        appointment_date = data.get("appointment_date")
        appointment_time = data.get("appointment_time")
        notes = data.get("notes", "")
        custom_token_no = data.get("custom_token_no")
        custom_location = data.get("custom_location")

        # ✅ NEW FIELDS
        custom_alternative_phone_number = data.get("custom_alternative_phone_number")
        custom_whatsapp_number = 1 if str(data.get("custom_whatsapp_number")).lower() in ["1", "true", "yes"] else 0


        # ---------------------------------------------------
        # 2️⃣ Required Field Validation
        # ---------------------------------------------------
        if not all([
            patient_name,
            phone,
            practitioner,
            appointment_date,
            appointment_time,
            appointment_type
        ]):
            frappe.throw("Missing required appointment details")

        # ---------------------------------------------------
        # 3️⃣ Parse Appointment Time Safely
        # ---------------------------------------------------
        if "-" in appointment_time:
            appointment_time = appointment_time.split("-")[0].strip()

        try:
            start_time = datetime.strptime(
                appointment_time, "%H:%M:%S"
            ).time()
        except ValueError:
            start_time = datetime.strptime(
                appointment_time, "%H:%M"
            ).time()

        # ---------------------------------------------------
        # 4️⃣ Check Existing Patient by Phone
        # ---------------------------------------------------
        existing_patient = frappe.db.get_value(
            "Patient",
            {"mobile": phone},
            ["name", "patient_name"],
            as_dict=True
        )

        patient = None

        if existing_patient:
            if (
                existing_patient.patient_name.strip().lower()
                == patient_name.strip().lower()
            ):
                patient = existing_patient.name


        # ---------------------------------------------------
        # 7️⃣ Create Patient If Not Exists
        # ---------------------------------------------------
        if not patient:
            patient_doc = frappe.get_doc({
                "doctype": "Patient",
                "first_name": patient_name,
                "patient_name": patient_name,
                "mobile": phone,
                "custom_email": custom_email,
                "sex": gender,
                "age": age,
            })
            patient_doc.insert(ignore_permissions=True)
            patient = patient_doc.name

        # ---------------------------------------------------
        # 8️⃣ Create Appointment
        # ---------------------------------------------------
        appointment = frappe.get_doc({
            "doctype": "Patient Appointment",
            "appointment_for": "Practitioner",
            "patient": patient,
            "appointment_type": appointment_type,
            "appointment_date": appointment_date,
            "appointment_time": start_time,
            "practitioner": practitioner,
            "department": department,
            "notes": notes,
            "custom_token_no": custom_token_no,
            "custom_location": custom_location,
            "phone_number": phone,
            "custom_alternative_phone_number": custom_alternative_phone_number,
            "custom_whatsapp_number": custom_whatsapp_number,
            "custom_booking_type": "Online"
        })

        from healthcare.healthcare.doctype.patient_appointment.patient_appointment import (
            PatientAppointment
        )

        original_validate_overlaps = PatientAppointment.validate_overlaps

        try:
            PatientAppointment.validate_overlaps = lambda self: None

            appointment.insert(ignore_permissions=True)
            frappe.db.commit()

        finally:
            PatientAppointment.validate_overlaps = original_validate_overlaps

        return {
            "status": "success",
            "appointment_id": appointment.name,
            "appointment_date": appointment.appointment_date,
            "appointment_time": str(appointment.appointment_time),
            "patient": patient,
            "custom_token_no": appointment.custom_token_no,
            "practitioner": practitioner,
            "custom_alternative_phone_number": custom_alternative_phone_number,
            "custom_whatsapp_number": custom_whatsapp_number
        }

    except Exception as e:
        frappe.log_error(
            frappe.get_traceback(),
            "Create Appointment API Error"
        )
        return {
            "status": "error",
            "message": str(e)
        }
