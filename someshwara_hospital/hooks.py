app_name = "someshwara_hospital"
app_title = "Someshwara Hospital"
app_publisher = "Nitish Mashal"
app_description = "Our hospital provides comprehensive medical services, ranging from outpatient consultations and emergency care to specialised treatments and advanced regenerative therapies."
app_email = "nitish.m@quantumberg.com"
app_license = "mit"


override_whitelisted_methods = {
    "healthcare.healthcare.doctype.patient_appointment.patient_appointment.get_availability_data":
    "someshwara_hospital.get_availability.get_availability_data"
}

website_route_rules = [

    # ✅ Only map frontend routes explicitly
    {"from_route": "/", "to_route": "index"},
    {"from_route": "/about-us", "to_route": "index"},
    {"from_route": "/dr-virupaksha-n-s", "to_route": "index"},
    {"from_route": "/doctors-list", "to_route": "index"},
    {"from_route": "/thank-you", "to_route": "index"},
    {"from_route": "/gallery", "to_route": "index"},
    {"from_route": "/blog", "to_route": "index"},
    {"from_route": "/contact-us", "to_route": "index"},
    {"from_route": "/appointment-page", "to_route": "index"},

    # ✅ Dynamic frontend routes
    {"from_route": "/services/<path:slug>", "to_route": "index"},
    {"from_route": "/viewProfile/<path:id>", "to_route": "index"},
    {"from_route": "/blogdetails/<path:slug>", "to_route": "index"},
]

fixtures = [
    # Custom Fields
    {
        "doctype": "Custom Field",
        "filters": [
            ["dt", "in", [
                "Patient Appointment",
                "Healthcare Schedule Time Slot",
                "Healthcare Practitioner"
            ]]
        ]
    },

    # Property Setters (if used)
    {
        "doctype": "Property Setter",
        "filters": [
            ["doc_type", "in", [
                "Patient Appointment",
                "Healthcare Schedule Time Slot",
                "Healthcare Practitioner"
            ]]
        ]
    },

    # ✅ Client Scripts
    {
        "doctype": "Client Script",
        "filters": [
            ["dt", "in", [
                "Patient Appointment",
                "Practitioner Schedule"
            ]]
        ]
    }
]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "someshwara_hospital",
# 		"logo": "/assets/someshwara_hospital/logo.png",
# 		"title": "Someshwara Hospital",
# 		"route": "/someshwara_hospital",
# 		"has_permission": "someshwara_hospital.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/someshwara_hospital/css/someshwara_hospital.css"
# app_include_js = "/assets/someshwara_hospital/js/someshwara_hospital.js"

# include js, css files in header of web template
# web_include_css = "/assets/someshwara_hospital/css/someshwara_hospital.css"
# web_include_js = "/assets/someshwara_hospital/js/someshwara_hospital.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "someshwara_hospital/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "someshwara_hospital/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "someshwara_hospital.utils.jinja_methods",
# 	"filters": "someshwara_hospital.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "someshwara_hospital.install.before_install"
# after_install = "someshwara_hospital.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "someshwara_hospital.uninstall.before_uninstall"
# after_uninstall = "someshwara_hospital.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "someshwara_hospital.utils.before_app_install"
# after_app_install = "someshwara_hospital.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "someshwara_hospital.utils.before_app_uninstall"
# after_app_uninstall = "someshwara_hospital.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "someshwara_hospital.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"someshwara_hospital.tasks.all"
# 	],
# 	"daily": [
# 		"someshwara_hospital.tasks.daily"
# 	],
# 	"hourly": [
# 		"someshwara_hospital.tasks.hourly"
# 	],
# 	"weekly": [
# 		"someshwara_hospital.tasks.weekly"
# 	],
# 	"monthly": [
# 		"someshwara_hospital.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "someshwara_hospital.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "someshwara_hospital.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "someshwara_hospital.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "someshwara_hospital.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["someshwara_hospital.utils.before_request"]
# after_request = ["someshwara_hospital.utils.after_request"]

# Job Events
# ----------
# before_job = ["someshwara_hospital.utils.before_job"]
# after_job = ["someshwara_hospital.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"someshwara_hospital.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

