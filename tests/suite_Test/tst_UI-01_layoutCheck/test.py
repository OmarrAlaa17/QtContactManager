# -*- coding: utf-8 -*-

import names


def main():
    test.compare(str(waitForObjectExists(names.mainWindow_nameLabel_QLabel).text), "Name")
    test.compare(str(waitForObjectExists(names.mainWindow_phoneLabel_QLabel).text), "Phone Number")
    test.compare(str(waitForObjectExists(names.mainWindow_emailLabel_QLabel).text), "Email (Optional)")
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.x, 100)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.y, 16)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.width, 315)
    test.compare(waitForObjectExists(names.mainWindow_nameTxt_QPlainTextEdit).geometry.height, 35)
    test.compare(waitForObjectExists(names.mainWindow_phoneTxt_QPlainTextEdit).geometry.x, 100)
    test.compare(waitForObjectExists(names.mainWindow_phoneTxt_QPlainTextEdit).geometry.y, 57)
    test.compare(waitForObjectExists(names.mainWindow_phoneTxt_QPlainTextEdit).geometry.width, 315)
    test.compare(waitForObjectExists(names.mainWindow_phoneTxt_QPlainTextEdit).geometry.height, 35)
    test.compare(waitForObjectExists(names.mainWindow_emailTxt_QPlainTextEdit).geometry.x, 100)
    test.compare(waitForObjectExists(names.mainWindow_emailTxt_QPlainTextEdit).geometry.y, 98)
    test.compare(waitForObjectExists(names.mainWindow_emailTxt_QPlainTextEdit).geometry.width, 315)
    test.compare(waitForObjectExists(names.mainWindow_emailTxt_QPlainTextEdit).geometry.height, 35)
    test.compare(waitForObjectExists(names.mainWindow_addBtn_QPushButton).visible, True)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.x, 9)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.y, 224)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.width, 406)
    test.compare(waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget).geometry.height, 320)
    test.compare(str(waitForObjectExists(names.mainWindow_removeBtn_QPushButton).objectName), "removeBtn")
    test.compare(str(waitForObjectExists(names.mainWindow_removeAllBtn_QPushButton).objectName), "removeAllBtn")
