# **BecomeQAEngineerCourse**
***
This is module-based test automation framework designed in order to perform tests for github using UI and API approaches.

## **Prerequisites**
Make sure you have Docker installed on your machine.

## **Installation**

1. Navigate to the project directory:
    ```bash
    cd path/to/project
    ```

2. Clone this repository:
    ```bash
    git clone https://github.com/KatarzynaJuszczak/BecomeQAEngineerCourse.git
    ```

3. Navigate to the `BecomeQAEngineerCourse` directory:
    ```bash
    cd path/to/project/BecomeQAEngineerCourse
    ```

4. Build the Docker Image:
    ```bash
    docker build -t your-image-name .
    ```
   
5. Run the Docker Container:
    ```bash
    docker run -t your-image-name
    ```

## **Framework structure**
src and tests directories are created to keep framework source code separated from tests logic.

### **Applications module**
Applications module contains folder for every tested application.
This module stores elements required to support different types of tests like API or UI tests for some specific application.
For now this framework is focused on github tests, that is why applications contains only `github` folder.
Every tested application contains also `test_data` folder with test data JSON file. Update the JSON file with your test data.

**How to add application under test:**
1. create a folder in `applications/` module with `application_name`
2. create a folder inside `applications/application_name/` with type of test e.g. `api, ui`
3. create a file `application_name_test_type` inside `applications/application_name/test_type/`

``
 example: src/applications/github/api/github_api.py
``

### **Config module**
Config module contains configuration settings for whole framework in `config.py`. 
Adjust the configuration settings to match your test environment and requirements. Configuration settings can be stored in JSON file and in environmental variables.

The purpose of config module is to:
* keep test configurations seperate from test logic
* allow tests be executed without changing test code
* keep settings in one place
* make configuration settings easy to change when needed

**How to add and modify config values:**
1. register configurations such as flags, settings, paths, every parameter that can be configured in multiple ways in `src/config/config.py`
2. modify configurations in environmental variables or in `src/config/envs/<config_file_name>.json`

### **Helpers module**
Helper module contains helper functions in `helper.py` file.

The purpose of helper functions is to:
* perform specific task
* be reused in multiple places which allows to avoid code repetition
* help write tests without introducing additional logic inside specific test

**How to add helper function:**
1. add helper function in `src/helpers/helper.py`

### **Logger module**
The framework based on built-in Python `logging` module for logging.\
Logs are stored in the `BecomeQAEngineerCourse/tests/logs/` directory. 

### **Providers module**
Providers module contains providers which read configuration data from files and environment variables and provide them for other modules.
* `json_provider.py`
* `os_provider.py`

This module also contains provider which returns the initialized driver for desired browser:
* `browser_provider.py`


### **Tests module**
This module contains API and UI tests written for some specific application.
Tests cases contained in this module should be strictly focused on test logic of the application.
For now this framework is focused on github tests, that is why tests contains only github folder.

**How to add test for application:**
1. create a folder in `tests/` module with `application_name`
2. create a folder inside `tests/application_name/` with type of test e.g `api, ui`
3. create specific test file `test_test_type` inside `tests/application_name/test_type/`

``
example: tests/github/api/test_api.py
``

## **Running Tests**

Framework uses `pytest` to run tests.
`pytest` will run all files of the form `test_*.py` or `*_test.py` in the current directory and its subdirectories.
All the command-line flags can be obtained by running `pytest --help`

Frequently used pytest flags:

`pytest -k EXPRESSION` only run tests which match the given substring expression\
`pytest -v` increase the verbosity level\
`pytest -x` exit instantly on first error or failed test