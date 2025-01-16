# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    clickButton(waitForObject(names.mainWindow_removeBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.info_QMessageBox).text), "Please select a row to be removed!")
    clickButton(waitForObject(names.info_OK_QPushButton))
