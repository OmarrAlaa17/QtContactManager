# -*- coding: utf-8 -*-

import names


def main():
    clickButton(waitForObject(names.mainWindow_removeBtn_QPushButton))
    test.compare(str(waitForObjectExists(names.info_QMessageBox).text), "Table is empty!")
    clickButton(waitForObject(names.info_OK_QPushButton))
