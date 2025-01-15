# -*- coding: utf-8 -*-

import names

def resetFields():
    waitForObject(names.mainWindow_nameTxt_QPlainTextEdit).setProperty("plainText", "")
    waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit).setProperty("plainText", "")
    waitForObject(names.mainWindow_emailTxt_QPlainTextEdit).setProperty("plainText", "")

def main():
    # Check Name Field Character LImit
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaar")
    mouseClick(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), 105, 18, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    if(contactsTable.rowCount == 1):
        test.fail("Code doesn't check on character limit in name field")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error", "Error detected")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Name field exceeds limit of 30 characters.", "Name Field Exceeds 30 Characters")
        clickButton(waitForObjectExists(names.error_OK_QPushButton))
    
    #Check Email Field Character Limit 
    resetFields()   
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "omarAlaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa@gmail.com")
    prevRowCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    
    if(prevRowCount<contactsTable.rowCount):
        test.fail("Code doesn't check on character limit in email field")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error", "Error detected")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Email exceeds 50 characters limit", "Email Field Exceeds 50 Characters")
        clickButton(waitForObject(names.error_OK_QPushButton))
