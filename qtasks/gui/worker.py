"""TODO."""

# from PySide6.QtWidgets import *
# from PySide6.QtGui import *

from qtasks.manager.servicemanager import ServiceManager
from qtasks.gtypes.services import TaskListService, TaskService
from qtasks.gtypes.task import Task
from qtasks.gtypes.tasklist import TaskList


class ProcessManager():
    """TODO."""
    def __init__(self, tokenfilepath: str):
        """TODO."""
        self.servicemanager = ServiceManager()
        self.servicemanager.create(tokenfilepath)
        self.taskservice = TaskService(self.servicemanager)
        self.tasklistservice = TaskListService(self.servicemanager)

    def fetch_tasks(self, tasklist: TaskList = None):
        """TODO."""
        self.taskservice.get(tasklist=tasklist)

    def fetch_lists(self):
        """TODO."""
        self.tasklistservice.get()

    def get_task_items(self):
        """TODO."""
        return self.taskservice.get_items()

    def get_tasklist_items(self):
        """TODO."""
        return self.tasklistservice.get_items()

    def add_task(self, task: Task):
        """TODO."""
        self.taskservice.add(task)
        self.taskservice.execute()

    def add_tasklist(self, tasklist: TaskList):
        """TODO."""
        self.tasklistservice.add(tasklist)
        self.taskservice.execute()

    def delete_task(self, task: Task, tasklist: TaskList):
        """TODO."""
        self.taskservice.delete(task, tasklist)
        self.taskservice.execute()

    def delete_tasklist(self, tasklist: TaskList):
        """TODO."""
        self.tasklistservice.delete(tasklist)
        self.tasklistservice.execute()
