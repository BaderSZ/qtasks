#!/bin/env python

"""Main function: start gui."""


import logging

from qtasks.gui.mainwindow import start_gui


# levels: Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


if __name__ == "__main__":
    start_gui()
