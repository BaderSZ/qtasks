#!/bin/env python
#!/bin/env python

"""Main function of the program part."""

# TODO

import sys
import logging

from qtasks.manager.servicemanager import ServiceManager

from qtasks.gtypes.services import TaskListService, TaskService

# from qtasks.gtypes.task import Task
# from qtasks.gtypes.tasklist import TaskList

from qtasks.keys import keys


# levels: Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

if __name__ == "__main__":
    servicemanager = ServiceManager()
    servicemanager.create(keys.TOKENFILE)
    taskservice = TaskService(servicemanager=servicemanager)
    tasklistservice = TaskListService(servicemanager=servicemanager)
    sys.exit()
