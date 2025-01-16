# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).rowCount, 1, "Row Added")
    mouseClick(waitForObject(names.o1_HeaderViewItem), 3, 11, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_removeBtn_QPushButton))
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).rowCount, 0, "Row Removed")
