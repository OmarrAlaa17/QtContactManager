# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Alaa")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01008175442")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar Alaa")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01008179142")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    
    
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    test.compare(3, contactsTable.rowCount, "Contacts added successfully")
    
    clickButton(waitForObject(names.mainWindow_removeAllBtn_QPushButton))
    clickButton(waitForObject(names.confirm_Remove_All_Yes_QPushButton))
    
    test.compare(0, contactsTable.rowCount, "All Contacts are removed"
)
