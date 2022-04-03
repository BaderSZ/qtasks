"""Run a few tests on the build in types and methods."""

from qtasks.gtypes.task import Task
from qtasks.gtasks.tasklist import TaskList

# from qtasks import __version__


def test_pytest():
    """Make sure pytest isn't broken."""
    assert 2 == 2   


def test_task_basic_init():
    """Check title assignment in init function."""
    task = Task("My fancy title")
    assert task.data['title'] == "My fancy title"


def test_task_request_data():
    """Check functions that read data."""
    randomdata = {'kind': 'tasks#task',
                  'id': 'MYRANDOMID',
                  'etag': '"ETAGDATA"',
                  'title': 'A Task',
                  'updated': '2022-04-03T19:37:16.927Z',
                  'selfLink': 'https://www.googleapis.com/tasks/v1/users/@me/lists/MYRANDOMID'
                  }

    task = Task.from_request_data(randomdata)

    assert task.get_last_updated() == randomdata['updated']
    assert task.get_id() == randomdata['id']
    assert task.data == randomdata


def test_task_time_management():
    """Make sure time conversion works."""
    from datetime import datetime

    dt_time = datetime(2022, 2, 2, 22, 11, 33, 111111)
    iso_time = '2022-02-02T22:11:33.111111'
    zulu_time = iso_time + "Z"

    task = Task(title="Test", updated=dt_time)

    assert task.data['updated'] == zulu_time

    assert Task.format_time(dt_time) == zulu_time


def test_tasklist_default_id():
    """Check the name of the default list."""
    assert TaskList.default_list_id == "@default"