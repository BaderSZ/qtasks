"""Task and TaskList Service Managers. Inherits from skeleton.py:ServiceType."""

from googleapiclient.discovery import Resource

from .task import Task
from .tasklist import TaskList

from . import skeleton


class TaskService(skeleton.ServiceType):
    """TaskService class to manage with Google Service API, based on ServiceType."""

    def __init__(self, service: Resource) -> None:
        """Create a task service, given an existing ServiceManager resource."""
        super().__init__(service)
        self._service = service.tasks()

    def add(self, task: Task):
        """Add task to queue. Run execute() after this."""
        super().add(task)

    def clear(self, tasklist: TaskList) -> None:
        """Clear tasklist and add request to queue."""
        self._queue_request(self._service.clear(tasklist=tasklist.get_id()))

    def delete(self, task: Task, tasklist: TaskList) -> None:
        """Delete Task and add request to queue."""
        self._queue_request(self._service.delete(tasklist=tasklist.get_id(), task=task.get_id()))


class TaskListService(skeleton.ServiceType):
    """TaskListService class to manage with Google Service API, based on ServiceType."""

    def __init__(self, service: Resource) -> None:
        """Create a tasklist service, given an existing ServiceManager resource.."""
        super().__init__(service)
        self._service = service.tasklists()

    def add(self, tasklist: TaskList):
        """Add tasklist to queue. Run execute() after this."""
        super().add(tasklist)

    def delete(self, tasklist: TaskList) -> None:
        """Delete Tasklist and add request to queue."""
        self._queue_request(self._service.delete(tasklist=tasklist.get_id()))
