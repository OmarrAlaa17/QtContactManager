# Qt ContactManager Application

This README file provides instructions for setting up the development environment, building the application, and running tests for the Qt PhoneBook application.

## Project Structure

This project follows a well-organized structure for clarity and maintainability:

- **/src** (Source Code): Contains all the source code files for my Qt application.
- **/bin** (Binaries): Stores the compiled executable file (e.g., `qtPhooneBook.exe`) after building the project with all the required files for running.
- **/docs** (Documentation): Houses any documentation related to the project, App Specifications and Test plan documents are written using mark down to be adjusted and structured easily.
- **/tests** (Test Cases): Holds all the Squish test suite folders including all test case files.

# Easy Application Execution

If you simply want to run the application without delving into development details, follow these steps:

1. **Navigate to the Bin Folder:** Open the folder named "bin" within the project directory. 
```bash
   cd bin  
```
2. **Run the Executable:** Double-click the file named "qtPhoneBook.exe" This will launch the application directly.
```bash
    qtPhooneBook.exe
```


# Setup and Running for Development Purposes
## Installation and Setup

**Prerequisites:**

- **Qt IDE:** Download and install Qt Creator from [https://www.qt.io/download-dev](https://www.qt.io/download-dev). Choose the **Qt 6.8.1 version with MinGW 64-bit**.
- **Squish for Qt:** Download Squish for Qt (Binary for Windows 64 Bit, Qt 6.8.x, MinGW, gvv 13.1, SEH, exception handling, posix threading) from [https://account.qt.io/s/qa-software](https://account.qt.io/s/qa-software).


## Building and Running the Application for Development
**Steps to build and launch app:**
-   Navigate to **/src** and run build commands
    ```bash
        cd src
        qmake qtPhooneBook.pro
        mingw32-make
    ```

-   Navigate to **/src/release** and run the application
    ```bash
        cd release
       qtPhooneBook.exe
    ```

**Steps to run tests autonomously:**
-   First of all start the squish server, navigate to the **<path/to/squish/bin>** and run the command
    ```bash
        # <path/to/squish/bin> can fe found in the installation folder for squish
        cd <path/to/squish/bin> 
        squishserver.exe
    ``` 

-   Run the squish test suite command
    ```bash
        cd ../tests
        <path/to/squish/bin/squishrunner.exe> --testsuite suite_Test  --reportgen xml,./results.xml
        #Results will be stored in tests/results
    ```



## Additional Notes
### Building and launching app using the IDE
**1. Open Qt Creator:** Launch Qt Creator after installation.

**2. Import Project:**
   - Click **File** > **Open Project** (or **Import Project**).
   - Navigate to the root directory of your project (where this README file is located).
   - Select the project file (usually named `qtPhooneBook.pro`).

**3. Build and Run:**
   - Click the **Run** button (the play icon) in the toolbar, or press **Ctrl+R**.
   - This builds the project and launches the executable in the **/bin** directory (e.g., `qtPhooneBook.exe`).

### Running Test Cases using squish IDE

1. **Open Squish IDE:** Launch the Squish IDE application.
2. **Open Test Suite:**
   - Click **File** > **Open Test Suite**.
   - Navigate to the **/tests** directory and select the test suite file (e.g., `suite_Test.sui`).
3. **Run Tests:** Click the **Run** button (the play icon) in the toolbar, or press **Ctrl+R**. This executes the automated test cases defined in the suite.

### Testing Summary
After each workflow run results file is uploaded to github artifacts and can be accessed by navigating to the workflow run on github. This summary contains detailed report for the application testing.

## Troubleshooting

- **App cannot start error:** 
    Some dependencies can be missing to fix this
    ```bash
        # Run this command in the directory of the .exe file
        # This is a feature downloaded with the qt setup
        windeployqt .
        
        qtPhooneBook.exe
    ```