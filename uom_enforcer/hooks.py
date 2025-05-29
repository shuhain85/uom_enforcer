app_name = "uom_enforcer"
app_title = "uom enforcer"
app_publisher = "shuhain"
app_description = "uom enfoercer"
app_email = "shuhain@gmail.com"
app_license = "mit"

# Apps
# ------------------
override_doctype_class = {
    "POS Invoice": "uom_enforcer.overrides.pos_invoice.CustomPOSInvoice"
}
override_doctype_class = {
    "Sales Invoice": "uom_enforcer.overrides.sales_invoice.CustomSalesInvoice"
}
# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "uom_enforcer",
# 		"logo": "/assets/uom_enforcer/logo.png",
# 		"title": "uom enforcer",
# 		"route": "/uom_enforcer",
# 		"has_permission": "uom_enforcer.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/uom_enforcer/css/uom_enforcer.css"
# app_include_js = "/assets/uom_enforcer/js/uom_enforcer.js"

# include js, css files in header of web template
# web_include_css = "/assets/uom_enforcer/css/uom_enforcer.css"
# web_include_js = "/assets/uom_enforcer/js/uom_enforcer.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "uom_enforcer/public/scss/website"

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
# app_include_icons = "uom_enforcer/public/icons.svg"

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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "uom_enforcer.utils.jinja_methods",
# 	"filters": "uom_enforcer.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "uom_enforcer.install.before_install"
# after_install = "uom_enforcer.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "uom_enforcer.uninstall.before_uninstall"
# after_uninstall = "uom_enforcer.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "uom_enforcer.utils.before_app_install"
# after_app_install = "uom_enforcer.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "uom_enforcer.utils.before_app_uninstall"
# after_app_uninstall = "uom_enforcer.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "uom_enforcer.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"uom_enforcer.tasks.all"
# 	],
# 	"daily": [
# 		"uom_enforcer.tasks.daily"
# 	],
# 	"hourly": [
# 		"uom_enforcer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"uom_enforcer.tasks.weekly"
# 	],
# 	"monthly": [
# 		"uom_enforcer.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "uom_enforcer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "uom_enforcer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "uom_enforcer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["uom_enforcer.utils.before_request"]
# after_request = ["uom_enforcer.utils.after_request"]

# Job Events
# ----------
# before_job = ["uom_enforcer.utils.before_job"]
# after_job = ["uom_enforcer.utils.after_job"]

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
# 	"uom_enforcer.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

