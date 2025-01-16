# -*- coding: utf-8 -*-

import names


def main():
    # Add first contact
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "omar@gmail.com")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    
    # Add second contact
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Alaa")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    if(contactsTable.rowCount == 2):
        test.fail("Code doesn't check if the same number exists")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Phone number already exists.")
        clickButton(waitForObject(names.error_OK_QPushButton))
        
    mouseClick(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), 65, 1, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), 77, 8, Qt.NoModifier, Qt.LeftButton)
    mouseDrag(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), 77, 8, -192, -7, 1, Qt.LeftButton)
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "<Backspace>")
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    mouseDrag(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), 77, 13, -54, 0, 1, Qt.LeftButton)
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "<Backspace>")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "08154113")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if the same name exists")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Name already exists.")
        clickButton(waitForObject(names.error_OK_QPushButton))
        
    mouseClick(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), 63, 18, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), " Alaa")
    mouseClick(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), 35, 15, Qt.NoModifier, Qt.LeftButton)
    type(waitForObject(names.mainWindow_emailTxt_QPlainTextEdit), "omar@gmail.com")
    prevCount = contactsTable.rowCount
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    
    if(contactsTable.rowCount > prevCount):
        test.fail("Code doesn't check if the same email exists")
    else:
        test.compare(str(waitForObjectExists(names.error_QMessageBox).windowTitle), "Error")
        test.compare(str(waitForObjectExists(names.error_QMessageBox).text), "Email address already exists.")
        clickButton(waitForObject(names.error_OK_QPushButton))
