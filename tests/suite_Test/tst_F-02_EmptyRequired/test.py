# -*- coding: utf-8 -*-

import names


def main():
    # Check Empty Name
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    if(contactsTable.rowCount == 1):
        test.fail("Code doesn't check on empty name field")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Name cannot be empty.")
        clickButton(waitForObject(names.error_OK_QPushButton))
        
    # Check Empty Phone Number
    prevRowCount = contactsTable.rowCount
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevRowCount):
        test.fail("Code doesn't check on empty phone number field")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Phone number cannot be empty.")
        clickButton(waitForObject(names.error_OK_QPushButton))
