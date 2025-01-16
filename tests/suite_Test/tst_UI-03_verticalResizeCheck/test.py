# -*- coding: utf-8 -*-

import names


def main():
    sendEvent("QResizeEvent", waitForObject(names.mainWindow_MainWindow), 424, 767, 2946, 992)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.height, 35)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.width, 315)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.height, 320)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.width, 406)
    sendEvent("QResizeEvent", waitForObject(names.mainWindow_MainWindow), 424, 561, 2907, 782)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.height, 320)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.width, 315)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.height, 35)
