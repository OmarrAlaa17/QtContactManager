# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Name cannot be empty.")
    test.compare(waitForObjectExists(names.error_QMessageBox).visible, True)
    clickButton(waitForObject(names.error_OK_QPushButton))
    mouseClick(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), 42, 29, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    mouseClick(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), 32, 16, Qt.NoModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(waitForObjectExists(names.error_QMessageBox).visible, True)
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Phone number cannot be empty.")
    clickButton(waitForObject(names.error_OK_QPushButton))
