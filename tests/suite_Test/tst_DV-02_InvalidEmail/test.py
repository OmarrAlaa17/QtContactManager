# -*- coding: utf-8 -*-

import names


def main():
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    emailField = waitForObjectExists(names.mainWindow_emailTxt_QPlainTextEdit)
     
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "o")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Incorrect Email Address")
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar Alaa")
        type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937775")
        type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "o")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Single Character Email")
        clickButton(waitForObject(names.error_OK_QPushButton))
    
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "@")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Incorrect Email Address")
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar Adel")
        type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937779")
        type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "o@")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Email wrong format")
        clickButton(waitForObject(names.error_OK_QPushButton))
    
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "g")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Incorrect Email Address")
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar Madbouly")
        type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937782")
        type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "o@g")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Email wrong format")
        clickButton(waitForObject(names.error_OK_QPushButton))
    

    emailField.setProperty("plainText", "")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "12Omar@gmail.com")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Incorrect Email Address")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Email wrong format")
        clickButton(waitForObject(names.error_OK_QPushButton))
