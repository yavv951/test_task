# API and UI tests different web resourses

# How to start
- Use python 3.8 + Create and activate virtual environments

- python3 -m venv env
source env/bin/activate

- Run in terminal

- pip install -r requirements.txt

## or install poetry https://python-poetry.org/, then

- poetry shell
- poetry install

## Run all tests

- pytest

## Run tests with marks

### for UI test
- pytest -v -m ui_test

### for API test

- pytest -v -m api_test 

## Run reports from allure

- allure serve -r allure-results

