"""QMainWindow object for QTasks."""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QEvent
from PySide6.QtCore import QFile, QDir, QStandardPaths, QFileInfo
from PySide6.QtGui import QPalette, QColor

from qtasks.gui.assets import resources # NOQA

from qtasks import __appname__

from qtasks.gtypes.task import Task
from qtasks.gtypes.tasklist import TaskList

from qtasks.gui.worker import ProcessManager
from qtasks.gui.ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """Qt Window object. Inherits QMainWindow."""

    def __init__(self) -> None:
        """Initialize GUI, Stylesheets and start processes."""
        super().__init__()
        self.setWindowTitle(__appname__)
        self.setWindowModality(Qt.WindowModal)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget.clear()
        self.ui.statusbar.showMessage("Ready")
        self.current_list_data = None

        # configs
        configdir = QDir(QStandardPaths.writableLocation(
            QStandardPaths.AppConfigLocation))

        if not configdir.exists():
            configdir.mkpath(configdir.absolutePath())

        tokenfile = QFile(configdir.absolutePath() + "/token.json")

        self.tokenfilepath = QFileInfo(tokenfile).absoluteFilePath()

        # element styles
        self.ui.comboBox.view().setStyleSheet("background: white;")
        self.ui.comboBox.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint)

        # actions and slots
        self.ui.listWidget.keyPressEvent = self.key_pressed_event
        self.ui.lineEdit.returnPressed.connect(self.return_pressed)
        self.ui.actionAbout_Qt.triggered.connect(QApplication.aboutQt)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionPreferences.triggered.connect(
            self.show_preferences_dialog)
        self.ui.comboBox.currentIndexChanged.connect(self.set_list_widget)

        # start the fun part
        # TODO: create a thread for this bottleneck
        self.processmanager = ProcessManager(self.tokenfilepath)

        # grab data and set gui elements
        self.refresh_list(0)
        self.set_combo_box()
        self.set_list_widget(0)

    # Slots Functions
    def key_pressed_event(self, event: QEvent) -> None:
        """Delete or deselect a task if event is pressed."""
        if event.key() == Qt.Key_Delete:
            try:
                self.delete_task()
            except Exception as exp:
                self.alert("Cannot delete\n" + exp)
        elif event.key() == Qt.Key_Escape:
            self.ui.listWidget.clearSelection()

    def set_combo_box(self) -> None:
        """Clear and set comboBox options."""
        somelist = [d['title'] for d in self.processmanager.get_tasklist_items()]
        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(somelist)

    def refresh_list(self, list_number: int) -> None:
        """Update the currently displayed tasklist."""
        self.processmanager.fetch_lists()
        self.current_list_data = self.processmanager.get_tasklist_items()[list_number]
        self.set_list_widget(list_number)

    def set_list_widget(self, list_number: int) -> None:
        """Slot: Get tasklist data and its tasks and add to listWidget."""
        tasklist = TaskList.from_request_data(self.processmanager.get_tasklist_items()[list_number])
        self.processmanager.taskservice.get(tasklist=tasklist)

        somelist = [d['title'] for d in self.processmanager.get_task_items()]
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(somelist)

    def return_pressed(self) -> None:
        """Slot: Add the task from lineEdit to the selected/visible list."""
        title = self.ui.lineEdit.text()
        if not title:
            pass
        self.add_task(title)

    def add_task(self, title: str) -> None:
        """Create a task object and call add to the list."""
        self.ui.statusbar.showMessage("Adding task...")
        self.processmanager.add_task(Task(title=title))

        self.ui.lineEdit.clear()
        list_index = self.ui.comboBox.currentIndex()

        # Have to refresh the list, otherwise future delete() requests are ignored
        self.refresh_list(list_index)
        self.ui.statusbar.showMessage("Task added!")

    def delete_task(self) -> None:
        """Delete task selected in listWidget."""
        item_index = self.ui.listWidget.currentRow()
        list_index = self.ui.comboBox.currentIndex()

        if self.ui.listWidget.item(item_index).isSelected():
            self.ui.statusbar.showMessage("Deleting task...")
            task = Task.from_request_data(self.processmanager.get_task_items()[item_index])
            tasklist = TaskList.from_request_data(self.processmanager.get_tasklist_items()[list_index])
            self.processmanager.delete_task(task, tasklist)

            self.ui.listWidget.takeItem(item_index)
            self.refresh_list(list_index)
            self.ui.statusbar.showMessage("Task deleted!")

    def alert(self, message: str) -> None:
        """Show a QMessageBox alert."""
        msgbox = QMessageBox(QMessageBox.Information, "QTasks Error", message, QMessageBox.Ok, self)
        msgbox.exec()
        if msgbox.clickedButton() == QMessageBox.Ok:
            msgbox.close()

    def about(self) -> None:
        """TODO."""
        self.alert("Unimplemented!")

    def show_preferences_dialog(self) -> None:
        """TODO."""
        self.alert("Unimplemented!")


def start_gui() -> None:
    """Start the GUI, set palette."""
    app = QApplication(sys.argv)
    app.setApplicationName(__appname__)

    # Set lineedit placeholdertext to blue. Can't do that in QDesigner
    pal = QPalette()
    pal.setColor(QPalette.PlaceholderText, QColor("#1a73e8"))
    app.setPalette(pal)

    widget = MainWindow()
    widget.show()

    sys.exit(app.exec())
