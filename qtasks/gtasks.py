#!/bin/env python

"""Startup function for the program."""

import logging

from servicemanager import ServiceManager

# from gtypes.services import TaskListService, TaskService

# from gtypes.task import Task
# from gtypes.tasklist import TaskList

from keys import keys


# levels: Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


def run() -> None:
    """Run main function."""
    servicemanager = ServiceManager()
    servicemanager.create(keys.TOKENFILE)
    # taskservice = TaskService(servicemanager=servicemanager)
    # tasklistservice = TaskListService(servicemanager=servicemanager)
