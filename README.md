# **BecomeQAEngineerCourse**
***
This is module-based testing framework designed in order to perform tests for github using UI and API approaches.

## **Framework structure**
src and tests directories are created to keep framework source code separated from tests logic.

### **Applications module**
Applications module contains folder for every tested application.\
This module stores elements required to support different types of tests like API or UI tests for some specific application.\
For now this framework is focused on github tests, that is why applications contains only github folder.

**How to add application under test:**
1. create a folder in *applications/* module with *application_name*
2. create a folder inside *applications/application_name/* with type of test (e.g. api, ui)
3. create a file *application_name_test_type* inside *applications/application_name/test_type/*
###### example: *src/applications/github/api/github_api.py*

### **Config module**
Config module contains configuration settings for whole framework in config.py which stores Config class.

The purpose of config module is to:
* keep test configurations seperate from test logic
* allow tests be executed without changing test code
* keep settings in one place
* make configuration settings easy to change when needed

**How to add config values:**
1. add configurations such as flags, settings, paths, every parameter that can be configured in multiple ways in *src/config/config.py*

### **Helpers module**
Helper module contains helper functions in helper.py file.

The purpose of helper functions is to:
* perform specific task
* be reused in multiple places which allows to avoid code repetition
* help write tests without introducing additional logic inside specific test

**How to add helper function:**
1. add helper function in *src/helpers/helper.py*

### **Tests module**
This module contains API and UI tests written for some specific application.\
Tests cases contained in this module should be strictly focused on test logic of the application.\
For now this framework is focused on github tests, that is why tests contains only github folder.

**How to add test for application:**
1. create a folder in *tests/* module with *application_name*
2. create a folder inside *tests/application_name/* with type of test (e.g api, ui)
3. create specific test file *test_test_type* inside *tests/application_name/test_type/*
###### example: *tests/github/api/test_api.py*
