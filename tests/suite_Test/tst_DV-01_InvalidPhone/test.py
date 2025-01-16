# -*- coding: utf-8 -*-

import names


def main():
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    phoneField = waitForObjectExists(names.mainWindow_phoneTxt_QPlainTextEdit)
    phoneField.setProperty("plainText", "") 
    #Adding string to phone number
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "word")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if phone number is not digits")
        # Add the name again for the following test cases
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar  Alaa")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "String in phone number")
        clickButton(waitForObject(names.error_OK_QPushButton))
    
    #Number Containing String
    phoneField.setProperty("plainText", "") 
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01072327AAA")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if phone number contains not digits")
        # Add the name again for the following test cases
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar Adel")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "String in phone number")
        clickButton(waitForObject(names.error_OK_QPushButton))
    
    #More than 11 digit number
    phoneField.setProperty("plainText", "") 
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "010723271001")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if phone number exceeds 11 digits")
        # Add the name again for the following test cases
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar Madbouly")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "Phone number exceeding 11 digits")
        clickButton(waitForObject(names.error_OK_QPushButton))
    
    #Less than 11 digit number
    phoneField.setProperty("plainText", "")  
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "0107232710")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if phone number is less that 11 digits")
        # Add the name again for the following test cases
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar X")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "Phone number less than 11 digits")
        clickButton(waitForObject(names.error_OK_QPushButton))

    #Not an Egypt number should start with (010|011|012)
    phoneField.setProperty("plainText", "") 
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "02182611924")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if phone number contains not digits")
        # Add the name again for the following test cases
        type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "Phone number starting with wrong digits")
        clickButton(waitForObject(names.error_OK_QPushButton))
