# Overview
This repository contains test automation project for Urban Jungle application https://github.com/Urban-Jungle-Project/urban_jungle_app.

# Getting Started

## Requirements

* Python
* Allure CommandLine (for local test report generation). 

## Project setup (Windows)

1. Install Python (Version 3.10 or above) from https://www.python.org/downloads/.
2. Add location of the python.exe to the PATH in System variables.
3. Install virtualenv `python -m pip install virtualenv`. 
4. Clone this project.
5. Create virtualenv within project root folder `python -m virtualenv venv`.
6. Activate virtualenv - execute `venv\scripts\activate` in project root folder.
7. Install python libraries `pip install -r requirements.txt`.

## Test configuration

One can configure test execution with help of the next environment variables:

| Environment variable name | Is required | Example | 
| ---  | --- | ---|
| ENVIRONMENT  | yes | dev, qa, staging |

## Test execution

```
python -m pytest --alluredir allure_results
```

## Allure report generation ( Allure Commandline required)

```
allure serve allure_results
```