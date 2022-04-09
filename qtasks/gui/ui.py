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
    QHBoxLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(241, 510)
        MainWindow.setMinimumSize(QSize(128, 0))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
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
        self.centralwidget.setMinimumSize(QSize(128, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(64, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: none;\n"
"	background-color: \"white\";\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.lineEdit)

        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFont(font1)
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"	border: none;\n"
"	background-color: \"white\";\n"
"    color: black;\n"
"}\n"
"\n"
"\n"
"QAbstractItemView {\n"
"    padding: 0 0.4em;\n"
"}\n"
"\n"
"QAbstractItemView::item {\n"
"    padding: 0.4em 0 0.2em;\n"
"}\n"
"\n"
"QListView::item:selected:!active {\n"
"    background: none;\n"
"}")
        self.listWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setProperty("isWrapping", True)
        self.listWidget.setWordWrap(True)

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Roboto Medium"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.comboBox.setFont(font2)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border: none;\n"
"    color: rgb(	95, 99, 104);\n"
"    background: white;\n"
"	font: 500 12pt \"Roboto Medium\";\n"
"    selection-background-color: rgb(207, 207, 207);\n"
"    border-radius: 10%;\n"
"\n"
"}\n"
"\n"
"QComboBox:on {\n"
"    border: none;\n"
"    color: rgb(	95, 99, 104);\n"
"	background: white;\n"
"    selection-background-color: rgb(207, 207, 207);\n"
"	font: 10pt \"Roboto\";\n"
"    border-radius: 10%;\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border-radius: 10%;\n"
"    selection-background-color: rgb(207, 207, 207);\n"
"	background: white;\n"
"}\n"
"\n"
"QComboBox::drop-down, QComboBox::drop-down:on {\n"
"    border: none;\n"
"    selection-background-color: rgb(207, 207, 207);\n"
"	background: white;\n"
"}\n"
"\n"
"QComboBox::down-arrow, QComboBox::down-arrow:on {\n"
"    image: url(:/assets/triangle.svg);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: center right;\n"
"    padding-right: 10px;"
                        "\n"
"}")
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout.addWidget(self.comboBox, 0, Qt.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add a task...", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Item1", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Item2", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Item3", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All Lists", None))

        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"&File", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"&Add", None))
        self.menuRemove.setTitle(QCoreApplication.translate("MainWindow", u"&Remove", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"&Help", None))
        self.menuVIew.setTitle(QCoreApplication.translate("MainWindow", u"&VIew", None))
    # retranslateUi

