"""task class."""

from datetime import datetime

from . import raw_types, skeleton


class Task(skeleton.TaskType):
    """Task class."""

    def __init__(self, title: str, updated: datetime = None, due: datetime = None,
                 status: str = None, _position: int = None, parent: str = None) -> None:
        """Create Task object inherited from TaskType."""
        self.data = raw_types.raw_task
        if due is not None:
            self.data['due'] = self._format_time(due)
        if status is not None and status in ("needsAction", "completed"):
            self.data['status'] = status
        super().__init__(title=title, updated=updated)

    def set_due_datetime(self, new_time: datetime) -> None:
        """Set due time of a task."""
        self.data['due'] = self._format_time(time=new_time)
