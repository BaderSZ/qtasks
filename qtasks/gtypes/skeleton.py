"""task class."""

from queue import Queue, Full as FullException
from datetime import datetime
import logging

import json

from googleapiclient.errors import HttpError, InvalidJsonError

from . import raw_types
from .exceptions import ExecutionError, NoServiceAvailable


class TaskType:
    """Skeleton base class for Task and TaskList."""

    def __init__(self, title: str = "Default Title", updated: datetime = None):
        """Initialize Type by setting dict/json data, title  and updated time."""
        self.data = raw_types.raw_type
        if title is not None:
            self.data["title"] = title
        # If no time is given, use the current time
        if updated is not None:
            self.data["updated"] = self.format_time(updated)
        else:
            self._update_time_now()

    @staticmethod
    def format_time(time: datetime) -> str:
        """Convert datetime to Zulu time str."""
        try:
            return str(time.isoformat("T") + "Z")
        except AttributeError as wrongarg:
            # Better off raising exception instead of returning current time
            logging.exception("_format_time given inappropriate argument. %s", wrongarg)
            raise   

    def _update_time_now(self) -> None:
        """Update task time to current time."""
        self.data["updated"] = self.format_time(datetime.utcnow())

    @classmethod
    def from_request_data(cls, request_data: dict):  # TODO: how do I hint a class method `self`?`
        """Set data of Type from request data."""
        # TODO: check data validity
        self = cls.__new__(cls)
        self.data = request_data
        return self

    def to_json(self) -> str:
        """Return TaskType data (dict) as json (str)."""
        return json.dumps(self.data)

    def dump(self) -> dict:
        """Return TaskType data as (dict)."""
        return self.data

    def get_id(self) -> str:
        """Get TaskType id (str)."""
        return self.data["id"]

    def get_last_updated(self) -> str:
        """Return the time the TaskType was last updated (zulu-time format)."""
        return self.data["updated"]


class ServiceType:
    """Create raw service type."""

    def __init__(self, service=None) -> None:
        """Construct a ServicesType. Raises an exception if no service object exists."""
        if service is None:
            raise NoServiceAvailable("No service created.")
        self.queue = Queue(maxsize=16)  # Choosing 16 temporarily for testing
        self._service = None  # Assign this in inheriting objects
        self.last_request = {"updated": None, "items": None}

    def add(self, task_generic: TaskType) -> None:
        """Add tasktype to queue. Run execute() after this."""
        try:
            self.queue.put(self._service.insert(body=task_generic.dump()))
        except FullException:
            logging.exception("Queue is full! Please run execute if possible.")
            raise

    def _queue_request(self, request):
        """Add request to queue."""
        try:
            self.queue.put(request)
        except FullException:
            logging.exception("Queue is full! Please run execute if possible.")

    def get(self, tasklist: TaskType = None, show_completed: bool = False) -> None:
        """Get any modifications from the 'cloud'."""
        try:
            if tasklist is None:
                # no tasklist given -> presume this is a TaskListService, and
                # get list of tasklists. If otherwise, must want a list of tasks in list
                self.last_request["items"] = self._service.list().execute().get("items", [])
            else:
                self.last_request["items"] = self._service.list(tasklist=tasklist.get_id(),
                                                                showCompleted=show_completed).execute().get("items", [])
        except Exception as exp:
            logging.exception("Unknown exception! %s", exp)
            raise
        self.last_request["updated"] = TaskType().format_time(datetime.now())

    def execute(self) -> None:
        """Execute requests queued requests and push task type item to google cloud."""
        result_queue = Queue()
        error_count = 0
        while not self.queue.empty():
            # Raises if more than 3 requests fail.
            if error_count >= 3:
                raise ExecutionError("Too many failed requests!\nNetwork issues?")
            # Attempt to execute the queued requests and add failed request back in the queue.
            try:
                current_request = self.queue.get()
                current_result = current_request.execute()
            except HttpError as request_error:
                error_count += 1
                logging.exception("Could not execute request!\n%s", request_error)
                self.queue.put(current_request)
            except InvalidJsonError as json_error:
                error_count += 1
                logging.exception(
                    "Invalid JSON. Chec your request.\nException %s\nRequest: %s", json_error, current_request
                )
                result_queue.put(current_result)

