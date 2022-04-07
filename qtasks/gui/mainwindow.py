# flake8: noqa

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QFile, QDir, QStandardPaths, QIODevice

from qtasks.manager.servicemanager import ServiceManager
from qtasks.gtypes import services, task, tasklist

from qtasks.gui.ui import Ui_MainWindow

# TODO: Timer event to fetch tasks
# TODO: signals and slots for everything.

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowModality(Qt.WindowModal)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # elements
        self.ui.lineEdit.setPlaceholderText("Add a task...")
        self.ui.lineEdit.returnPressed.connect(self._returnPressedSlot)
        self.ui.listWidget.keyPressEvent = self._keyPressedEvent

        # actions
        self.ui.actionAbout_Qt.triggered.connect(self._aboutQt)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionPreferences.triggered.connect(
            self._showPreferencesDialog)

    # Slots Functions
    def _showPreferencesDialog(self):
        # Do nothing for now
        pass

    def _keyPressedEvent(self, event):
        if event.key() == Qt.Key_Delete:
            print("test delete")
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def _returnPressedSlot(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())

    def _aboutQt(self):
        QApplication.aboutQt()


def startGui() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName("QTasks")

    configDir = QDir(QStandardPaths.writableLocation(
        QStandardPaths.AppConfigLocation))

    if not configDir.exists():
        configDir.mkpath(configDir.absolutePath())

    tokenFile = QFile(configDir.absolutePath() + "/token.json")

    if not tokenFile.open(QIODevice.ReadWrite | QIODevice.Text):
        raise Exception("FileNotOpenable")

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
