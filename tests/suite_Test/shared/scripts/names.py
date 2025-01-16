# encoding: UTF-8

from objectmaphelper import *

mainWindow_MainWindow = {"name": "MainWindow", "type": "MainWindow", "visible": 1}
mainWindow_nameTxt_QPlainTextEdit = {"name": "nameTxt", "type": "QPlainTextEdit", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_phoneTxt_QPlainTextEdit = {"name": "phoneTxt", "type": "QPlainTextEdit", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_addBtn_QPushButton = {"name": "addBtn", "type": "QPushButton", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_phoneBookTable_QTableWidget = {"name": "phoneBookTable", "type": "QTableWidget", "visible": 1, "window": mainWindow_MainWindow}
phoneBookTable_QHeaderView = {"container": mainWindow_phoneBookTable_QTableWidget, "orientation": 2, "type": "QHeaderView", "unnamed": 1, "visible": 1}
o1_HeaderViewItem = {"container": phoneBookTable_QHeaderView, "text": 1, "type": "HeaderViewItem", "visible": True}
phoneBookTable_0_1_QModelIndex = {"column": 1, "container": mainWindow_phoneBookTable_QTableWidget, "row": 0, "type": "QModelIndex"}
phoneBookTable_0_3_QModelIndex = {"column": 3, "container": mainWindow_phoneBookTable_QTableWidget, "row": 0, "type": "QModelIndex"}
phoneBookTable_0_2_QModelIndex = {"column": 2, "container": mainWindow_phoneBookTable_QTableWidget, "row": 0, "type": "QModelIndex"}
error_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Error"}
error_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": error_QMessageBox}
error_qt_msgbox_label_QLabel = {"name": "qt_msgbox_label", "type": "QLabel", "visible": 1, "window": error_QMessageBox}
mainWindow_emailTxt_QPlainTextEdit = {"name": "emailTxt", "type": "QPlainTextEdit", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_phoneLabel_QLabel = {"name": "phoneLabel", "type": "QLabel", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_nameLabel_QLabel = {"name": "nameLabel", "type": "QLabel", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_emailLabel_QLabel = {"name": "emailLabel", "type": "QLabel", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_removeBtn_QPushButton = {"name": "removeBtn", "type": "QPushButton", "visible": 1, "window": mainWindow_MainWindow}
phoneBookTable_qt_scrollarea_vcontainer_QWidget = {"container": mainWindow_phoneBookTable_QTableWidget, "name": "qt_scrollarea_vcontainer", "type": "QWidget", "visible": 0}
phoneBookTable_QScrollBar = {"container": mainWindow_phoneBookTable_QTableWidget, "type": "QScrollBar", "unnamed": 1, "visible": 1}
phoneBookTable_QHeaderView_2 = {"container": mainWindow_phoneBookTable_QTableWidget, "orientation": 1, "type": "QHeaderView", "unnamed": 1, "visible": 1}
email_HeaderViewItem = {"container": phoneBookTable_QHeaderView_2, "text": "Email", "type": "HeaderViewItem", "visible": True}
o2_HeaderViewItem = {"container": phoneBookTable_QHeaderView, "text": 2, "type": "HeaderViewItem", "visible": True}
mainWindow_centralwidget_QWidget = {"name": "centralwidget", "type": "QWidget", "visible": 1, "window": mainWindow_MainWindow}
mainWindow_removeAllBtn_QPushButton = {"name": "removeAllBtn", "type": "QPushButton", "visible": 1, "window": mainWindow_MainWindow}
info_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Info"}
info_OK_QPushButton = {"text": "OK", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": info_QMessageBox}
confirm_Remove_All_QMessageBox = {"type": "QMessageBox", "unnamed": 1, "visible": 1, "windowTitle": "Confirm Remove All"}
confirm_Remove_All_Yes_QPushButton = {"text": "Yes", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": confirm_Remove_All_QMessageBox}
confirm_Remove_All_No_QPushButton = {"text": "No", "type": "QPushButton", "unnamed": 1, "visible": 1, "window": confirm_Remove_All_QMessageBox}
