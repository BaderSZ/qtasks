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

    def add(self, task: Task, tasklist: TaskList = None):
        """Add task to queue. Run execute() after this."""       
        if tasklist is None:
            self._queue_request(self._service.insert(tasklist="@default", body=task.dump()))    
        else:
            self._queue_request(self._service.insert(tasklist=tasklist.get_id(), body=task.dump()))

    def get(self, tasklist: TaskList, show_completed: bool = False):
        """Get list of tasks in a tasklist."""
        super().get(tasklist=tasklist, show_completed=show_completed)

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
        self.default_id = "@default"

    def add(self, tasklist: TaskList) -> None:
        """Add tasklist to queue. Run execute() after this."""
        super().add(tasklist)

    def get(self) -> None:
        """Get list of TaskLists."""
        super().get()

    def delete(self, tasklist: TaskList) -> None:
        """Delete Tasklist and add request to queue."""
        self._queue_request(self._service.delete(tasklist=tasklist.get_id()))
