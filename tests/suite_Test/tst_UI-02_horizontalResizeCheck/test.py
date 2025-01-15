# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QResizeEvent", waitForObject(names.mainWindow_MainWindow), 689, 628, 3358, 508)
    test.compare(waitForObjectExists(names.phoneBookTable_qt_scrollarea_vcontainer_QWidget).enabled, True)
    test.compare(waitForObjectExists(names.phoneBookTable_qt_scrollarea_vcontainer_QWidget).geometry.width, 100)
    test.compare(waitForObjectExists(names.mainWindow_addBtn_QPushButton).frameSize.width, 671)
    sendEvent("QResizeEvent", waitForObject(names.mainWindow_MainWindow), 165, 628, 2836, 627)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.width, 300)