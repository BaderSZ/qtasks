"""Basic dict types."""

raw_type = {"kind": "tasks#unknown", "title": "Default Name", "updated": "datetime.datetime", "id": "randomid"}
raw_task = {
    "status": "needsAction",
    "kind": "tasks#task",
    "updated": "A String",
    "title": "Default Title",
    "notes": "Added with gtasks",
    "id": "randomid"
}
raw_list = {"kind": "tasks#taskList", "title": "A String", "updated": "A String", "id": "randomid"}

## copy-pasta'd from Google docs

# raw_task = {
#     "status": "needsAction",  # Status: "needsAction" or "completed".
#     "kind": "tasks#task",  # Type of the resource. This is always "tasks#task".
#     "updated": "A String",  # Last modified RFC 3339 Zulu time
#     # "parent": "", # Parent task identifier. Read-only, omitted when top-level. Use `move()`
#     # "links": [  # Collection of links. This collection is read-only.
#     #    {
#     #        "type": "",  # Type of the link, e.g. "email".
#     #        "link": "",  # The URL.
#     #        "description": "", # In HTML (<a>)
#     #    },
#     # ],
#     "title": "Default Title",  # Title of the task.
#     # "deleted": False, # Is task deleted? default: False.
#     # "completed": "", # Completed RFC 3339 Zulu time
#     # "due": "A String", # Due: RFC 3339 Zulu time. Optional. Unreadable via API
#     # "etag": "A String",  # ETag of the resource.
#     "notes": "Added with gtasks",  # Notes describing the task. Optional. Takes HTML <a>
#     # "position": "000000007", # Position: Read-only. use `move`
#     # "hidden": False, # True if completed. Read-only.
#     # "id": "A String",  # Task identifier.
#     # "selfLink": "A String", # Web URL. Used to retrieve update, delete.
# }
# raw_list = {
#     # Type of the resource. This is always "tasks#taskList".
#     "kind": "tasks#taskList",
#     "title": "A String",  # Title of the task list.
#     "updated": "A String",  # Last modified RFC 3339 Zulu time
#     # "etag": "A String",  # ETag of the resource.
#     # "id": "A String",  # Task list identifier.
#     # "selfLink": "A String",  # Web URL. Used to retrieve update, delete.
# }
