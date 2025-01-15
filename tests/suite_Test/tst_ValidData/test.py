# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "omar@gmail.com")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(waitForObjectExists(names.phoneBookTable_0_1_QModelIndex).text, "Omar")
    test.compare(waitForObjectExists(names.phoneBookTable_0_2_QModelIndex).text, "01096937772")
    test.compare(waitForObjectExists(names.phoneBookTable_0_3_QModelIndex).text, "omar@gmail.com")
