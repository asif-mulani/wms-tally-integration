# hooks.py for wms_tally_integration

from . import __version__ as app_version

app_name = "wms_tally_integration"
app_title = "WMS Tally Integration"
app_publisher = "Asif Mulani"
app_description = "A Frappe app for integrating Tally with WMS"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "example@example.com"
app_license = "MIT"

# Scheduled tasks
scheduler_events = {
    "all": [
        "wms_tally_integration.tasks.all"
    ],
    "daily": [
        "wms_tally_integration.tasks.daily"
    ],
    "hourly": [
        "wms_tally_integration.tasks.hourly"
    ],
    "weekly": [
        "wms_tally_integration.tasks.weekly"
    ],
    "monthly": [
        "wms_tally_integration.tasks.monthly"
    ]
}

# Document events
doc_events = {
    "*": {
        "on_update": "wms_tally_integration.events.on_update",
        "on_cancel": "wms_tally_integration.events.on_cancel",
        "on_trash": "wms_tally_integration.events.on_trash"
    }
}