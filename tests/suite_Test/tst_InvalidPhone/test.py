# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    phoneField = waitForObjectExists(names.mainWindow_phoneTxt_QPlainTextEdit)
    phoneField.setProperty("plainText", "") 
    #Adding string to phone number
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "word")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "String in phone number")
    clickButton(waitForObject(names.error_OK_QPushButton))
    
    #Number Containing String
    phoneField.setProperty("plainText", "") 
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01072327AAA")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "String in phone number")
    clickButton(waitForObject(names.error_OK_QPushButton))
    
    #More than 11 digit number
    phoneField.setProperty("plainText", "") 
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "010723271001")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "Phone number exceeding 11 digits")
    clickButton(waitForObject(names.error_OK_QPushButton))
    
    #Less than 11 digit number
    phoneField.setProperty("plainText", "")  
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "0107232710")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "Phone number less than 11 digits")
    clickButton(waitForObject(names.error_OK_QPushButton))

    #Not an Egypt number should start with (010|011|012)
    phoneField.setProperty("plainText", "") 
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "02182611924")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect phone number", "Phone number starting with wrong digits")
    clickButton(waitForObject(names.error_OK_QPushButton))
