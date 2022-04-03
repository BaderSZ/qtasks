"""Tasklist module."""

from datetime import datetime


from . import raw_types, skeleton


class TaskList(skeleton.TaskType):
    """Tasklist object. Inherited from TaskType."""

    def __init__(self,  title: str, updated: datetime = None) -> None:
        """Create TaskList object (inherited from TaskType)."""
        self.data = raw_types.raw_list
        super().__init__(title=title, updated=updated)
