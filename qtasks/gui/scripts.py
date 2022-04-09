"""Generate resource scripts and files. Using PySide6's build in tools."""
# flake8: NOQA 

import os
from pathlib import Path

from PySide6.scripts.pyside_tool import uic, rcc, qt_tool_wrapper


path = Path().resolve()

resource_arg = [os.fspath(path / "qtasks/gui/resources.qrc"), "--output", os.fspath(path / "qtasks/gui/assets/resources.py")]

ui_arg = [os.fspath(path / "qtasks/gui/form.ui") , "--output" ,os.fspath(path / "qtasks/gui/ui.py")]


def generate_rcc():
    qt_tool_wrapper("rcc", ['-g', 'python'] + resource_arg, True)


def generate_uic():
    qt_tool_wrapper("uic", ['-g', 'python'] + ui_arg , True)

def generate():
    generate_rcc()
    generate_uic()
