from . import __version__ as app_version

app_name = "cleartax_integration"
app_title = "Cleartax Integration"
app_publisher = "8848 Digital LLP"
app_description = "v-13 Compatibility for cleartax app"
app_email = "contact@8848digital.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cleartax_integration/css/cleartax_integration.css"
# app_include_js = "/assets/cleartax_integration/js/cleartax_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/cleartax_integration/css/cleartax_integration.css"
# web_include_js = "/assets/cleartax_integration/js/cleartax_integration.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cleartax_integration/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Delivery Note": "public/js/delivery_note_doctype.js",
    "Sales Invoice": "public/js/sales_invoice_doctype.js",
    "Purchase Invoice" : "public/js/purchase_invoice_doctype.js"
    }

doctype_list_js = {
    "Sales Invoice": "public/js/sales_invoice_list.js",
    "Purchase Invoice": "public/js/purchase_invoice_list.js",
    "Delivery Note": "public/js/delivery_note_list.js"
}

doc_events = {
    "Delivery Note": {
        "before_submit": "cleartax_integration.public.py.delivery_note_doctype.delivery_note_submit",
        "before_save": "cleartax_integration.public.py.delivery_note_doctype.delivery_note_save",
        "before_cancel": "cleartax_integration.public.py.delivery_note_doctype.delivery_note_cancel"
    },
     "Purchase Invoice": {
        "before_submit": "cleartax_integration.public.py.purchase_invoice_doctype.purchase_invoice_submit",
        "before_cancel": "cleartax_integration.public.py.purchase_invoice_doctype.purchase_invoice_cancel",
        "before_save": "cleartax_integration.public.py.purchase_invoice_doctype.purchase_invoice_save"
    },
    "Sales Invoice": {
        "before_submit":"cleartax_integration.public.py.sales_invoice_doctype.sales_invoice_submit",
        "before_cancel": "cleartax_integration.public.py.sales_invoice_doctype.sales_invoice_cancel",
        "before_save": "cleartax_integration.public.py.sales_invoice_doctype.sales_invoice_save"
    }
}


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "cleartax_integration.utils.jinja_methods",
#	"filters": "cleartax_integration.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "cleartax_integration.install.before_install"
# after_install = "cleartax_integration.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cleartax_integration.uninstall.before_uninstall"
# after_uninstall = "cleartax_integration.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cleartax_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"cleartax_integration.tasks.all"
#	],
#	"daily": [
#		"cleartax_integration.tasks.daily"
#	],
#	"hourly": [
#		"cleartax_integration.tasks.hourly"
#	],
#	"weekly": [
#		"cleartax_integration.tasks.weekly"
#	],
#	"monthly": [
#		"cleartax_integration.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "cleartax_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "cleartax_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "cleartax_integration.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"cleartax_integration.auth.validate"
# ]
