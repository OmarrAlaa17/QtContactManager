# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "<Tab>")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    sendEvent("QResizeEvent", waitForObject(names.mainWindow_MainWindow), 318, 583, 2990, 705)
    scrollTo(waitForObject(names.phoneBookTable_QScrollBar), 0)
    scrollTo(waitForObject(names.phoneBookTable_QScrollBar), 2)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).autoScroll, False)
    
    # Make sure that table size is draggable
    mouseClick(waitForObject(names.email_HeaderViewItem), 0, 17, Qt.NoModifier, Qt.LeftButton)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).dragEnabled, True)
