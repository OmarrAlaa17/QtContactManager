# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "<Tab>")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(waitForObjectExists(names.phoneBookTable_0_1_QModelIndex).displayText, "Omar")
    test.compare(waitForObjectExists(names.phoneBookTable_0_2_QModelIndex).displayText, "01096937772")
    test.compare(waitForObjectExists(names.phoneBookTable_0_3_QModelIndex).displayText, "")
