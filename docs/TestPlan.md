# Contact Manager Application Test Plan

## 1. Introduction

This document outlines the test plan for the Contact Manager application. The plan was  developed through analyzing the business and functionality of the application, outlining potential user stories, deriving detailed test scenarios, and conducting multiple rounds of testing to validate various aspects of the application's performance and usability.

This test plan will focus on four main aspects:

* **UI Testing:** Evaluate the visual presentation and user experience of the application.
* **Functionality Testing:** Verify the correct behavior of all core features.
* **Data Validation Testing:** Ensure the accuracy and integrity of data within the application.
* **Usability Testing:** Evaluate the user-friendliness and intuitiveness of the system's structure and interactions.

## 2. Test Cases

### 2.1 UI Testing

| Test Case ID | Test Case Name | Description | Expected Result | Priority | 
|---|---|---|---|---|
| UI-01 | Layout Check | Check all elements are visible and correctly positioned | All elements are positioned correctly and consistently. | High |
| UI-02 | Horizontal Window Resize | Check boundary conditions by dragging window horizontally | Elements should expand with widow responsively and some limits can't be exceeded | High |
| UI-03 | Vertical Window Resize | Check boundary conditions dragging the window vertically | Elements should resize with window and limit's can't be exceeded | High |
| UI-04 | Scrollable Contacts table size | Check the behavior when are added and information exceeds table size | No shifts should occur and table should be scrollable | Medium
| UI-05 | Draggable Columns |Table columns can be manually adjusted | Table should be draggable to adjust column width | Low


### 2.2 Functionality Testing

| Test Case ID | Test Case Name | Description | Expected Result | Priority |
|---|---|---|---|---|
| F-01 | Add Contact - Valid Data | Add all contact information name, phone number and email | Contact is added into contacts table and input fields should be cleared | High |
| F-02 | Add Contact - Empty Required Fields | Trying to add contact while name or phone number is empty | Error message is displayed. Contact is not added. | High |
| F-03 | Add Contact - Existing Info | Trying to add a contact with existing information | Warning should occur that contact already exists. Contact is not added | High
| F-04 | Add Contact - With Empty Email | Adding a contact with only the required data name and phone number | Contact should be added and input fields should be cleared | High | 
| F-05 | Remove Contact - Single | Try selecting a row and removing the contact | Contact is successfully deleted from the table. | High |
| F-06 | Remove Contact - Multiple | Try selecting multiple rows and then delete | Contacts are successfully deleted from the table. | Medium |
| F-07 | Remove All | Try clicking on remove all button to clear contacts table | Contacts table should be cleared after confirming | Medium

### 2.3 Data Validation Testing

| Test Case ID | Test Case Name | Description | Expected Result | Priority |
|---|---|---|---|---|
| DV-01 | Add Contact - Invalid Phone | Trying to add a contact with an invalid phone number containing letters or not starting with correct values (010 ex) | Error message is displayed. Contact is not added. (Assuming only Egyptian numbers) | High | 
| DV-02 | Add Contact - Invalid Email |Trying to add a contact with invalid email | Error Message is displayed. Contact is not added | High | 
| DV-03 | Input Fields - Exceeding limit | Make sure that input fields does't exceed a certain number of characters | Error message is displayed. Contact is nor added. | Medium | 


### 2.4 Usability Testing

| Test Case ID | Test Case Name | Description | Expected Result | Priority |
|---|---|---|---|---|
| US-01 | Intuitive Interface | Make sure that all buttons, tables and fields are clear and visible | The interface is easy to understand and navigate | Medium |
| US-02 | Checking error messages | Making sure that error messages are explaining clearly the issue | Well describing error messages | Medium |
| US-03 | Removing with no row selection | Try clicking on remove with no rows selected | Warning message should occur | Low |
| US-04 | Removing empty table | Try clicking on remove with no empty contacts table | Warning message should occur | Low |
| US-05 | Confirming Before Remove All | Make sure that the user confirms removing all contacts | Clicking remove all should open a modal to confirm removing | Low |

## 3. Test Environment

* **Operating System:** Windows 10
* **Software:** Qt 6.8.1 MinGW 64-bit ,Python 3.10, Squish 

## 4. Conclusion
In conclusion, the outlined test plan not only ensures thorough validation of the application's functionality but also serves as an ongoing verification process. By integrating GitHub Actions, the test cases are automatically executed upon every commit pushed to the remote repository. This continuous testing approach helps maintain the application's reliability and ensures that new changes do not compromise existing functionality.
