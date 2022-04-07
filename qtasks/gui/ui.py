# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSplitter,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(241, 491)
        self.actionAddTask = QAction(MainWindow)
        self.actionAddTask.setObjectName(u"actionAddTask")
        self.actionAddList = QAction(MainWindow)
        self.actionAddList.setObjectName(u"actionAddList")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_Qt = QAction(MainWindow)
        self.actionAbout_Qt.setObjectName(u"actionAbout_Qt")
        self.actionRemoveTask = QAction(MainWindow)
        self.actionRemoveTask.setObjectName(u"actionRemoveTask")
        self.actionRemoveList = QAction(MainWindow)
        self.actionRemoveList.setObjectName(u"actionRemoveList")
        self.actionAddAccount = QAction(MainWindow)
        self.actionAddAccount.setObjectName(u"actionAddAccount")
        self.actionViewCompletedTasks = QAction(MainWindow)
        self.actionViewCompletedTasks.setObjectName(u"actionViewCompletedTasks")
        self.actionViewCompletedTasks.setCheckable(True)
        self.actionViewCompletedTasks.setChecked(False)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.comboBox = QComboBox(self.splitter)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.splitter.addWidget(self.comboBox)

        self.verticalLayout.addWidget(self.splitter)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 241, 19))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAdd = QMenu(self.menuFile)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuRemove = QMenu(self.menuFile)
        self.menuRemove.setObjectName(u"menuRemove")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuVIew = QMenu(self.menubar)
        self.menuVIew.setObjectName(u"menuVIew")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuVIew.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuAdd.menuAction())
        self.menuFile.addAction(self.menuRemove.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAddAccount)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPreferences)
        self.menuFile.addAction(self.actionClose)
        self.menuAdd.addAction(self.actionAddTask)
        self.menuAdd.addAction(self.actionAddList)
        self.menuRemove.addAction(self.actionRemoveTask)
        self.menuRemove.addAction(self.actionRemoveList)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuVIew.addAction(self.actionViewCompletedTasks)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAddTask.setText(QCoreApplication.translate("MainWindow", u"&Task", None))
#if QT_CONFIG(shortcut)
        self.actionAddTask.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionAddList.setText(QCoreApplication.translate("MainWindow", u"&List", None))
#if QT_CONFIG(shortcut)
        self.actionAddList.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"&About", None))
        self.actionAbout_Qt.setText(QCoreApplication.translate("MainWindow", u"About &Qt", None))
        self.actionRemoveTask.setText(QCoreApplication.translate("MainWindow", u"Task", None))
#if QT_CONFIG(shortcut)
        self.actionRemoveTask.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionRemoveList.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.actionAddAccount.setText(QCoreApplication.translate("MainWindow", u"Add Account", None))
        self.actionViewCompletedTasks.setText(QCoreApplication.translate("MainWindow", u"&Completed tasks", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"&Close", None))
#if QT_CONFIG(shortcut)
        self.actionClose.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"&Preferences", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Lists", None))

        self.lineEdit.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"&Add", None))
        self.menuRemove.setTitle(QCoreApplication.translate("MainWindow", u"&Remove", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menuVIew.setTitle(QCoreApplication.translate("MainWindow", u"&VIew", None))
    # retranslateUi

