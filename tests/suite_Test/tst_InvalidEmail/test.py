# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "o")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Single Character Email")
    clickButton(waitForObject(names.error_OK_QPushButton))
    
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "@")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Email wrong format")
    clickButton(waitForObject(names.error_OK_QPushButton))
    
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "g")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Email wrong format")
    clickButton(waitForObject(names.error_OK_QPushButton))
    
    emailField = waitForObjectExists(names.mainWindow_emailTxt_QPlainTextEdit)
    emailField.setProperty("plainText", "")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "12Omar@gmail.com")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
    test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Incorrect email address", "Email wrong format")
    clickButton(waitForObject(names.error_OK_QPushButton))
