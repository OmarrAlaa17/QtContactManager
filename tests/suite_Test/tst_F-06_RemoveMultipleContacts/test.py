# -*- coding: utf-8 -*-

import names


def main():
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Omar")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01096937772")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    type(waitForObject(names.mainWindow_nameTxt_QPlainTextEdit), "Alaa")
    type(waitForObject(names.mainWindow_phoneTxt_QPlainTextEdit), "01008175442")
    clickButton(waitForObject(names.mainWindow_addBtn_QPushButton))
    
    
    contactsTable = waitForObjectExists(names.mainWindow_phoneBookTable_QTableWidget)
    test.compare(2, contactsTable.rowCount, "Two contacts added successfully")
    
    # Temporarily set MultiSelection (if needed)
    currentSelectionMode = contactsTable.property("selectionMode")
    if currentSelectionMode != "MultiSelection":
        contactsTable.setProperty("selectionMode", "MultiSelection")
        
    mouseClick(waitForObject(names.o1_HeaderViewItem), 3, 7, Qt.NoModifier, Qt.LeftButton)
    mouseClick(waitForObject(names.o2_HeaderViewItem), 10, 9, Qt.ShiftModifier, Qt.LeftButton)
    clickButton(waitForObject(names.mainWindow_removeBtn_QPushButton))
    
    test.compare(0, contactsTable.rowCount, "Two Contacts Removed successfully")
    
    # Revert Selection Mode
    if currentSelectionMode != "MultiSelection":
        contactsTable.setProperty("selectionMode", currentSelectionMode)
