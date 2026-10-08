# Playwright Automation Framework

A test automation framework built with Python, Pytest and Playwright for UI and API testing. It uses the Page Object Model (POM) for maintainability and reuse.

## Features

- UI automation with Playwright
- API testing with Python and Pytest
- Page Object Model architecture
- Pytest fixtures for setup and teardown (`conftest.py`)
- Data-driven testing
- BDD-style tests with pytest-bdd
- HTML reports with pytest-html
- Reusable utility functions

## Tech stack

Python, Pytest, Playwright, pytest-bdd, pytest-html

## Project structure

```
.
├── Data/                 # test data
├── Feature/              # BDD feature files
├── PageObject/           # page object classes
├── utils/                # reusable helpers
├── assets/
├── pytest/               # pytest basics: fixture scopes (session, module, function), markers (smoke, skip)
├── conftest.py           # shared fixtures
├── test_UIvalidations_1.py
├── test_MoreValidations.py
├── test_Network1.py
├── test_Network2.py
├── test_Web_API.py
├── test_framework_Web_API.py
├── test_playwrightBasics.py
└── test_pytest-bddTest.py
```

## Setup

```bash
pip install -r requirements.txt
playwright install
```

## Run the tests

```bash
pytest                                   # run everything
pytest test_Web_API.py                   # run one file
pytest --headed                          # watch the browser
pytest --html=report.html --self-contained-html
```

## What each test file covers

- `test_UIvalidations_1.py`: UI flows on a practice site: login, dropdown, checkbox, adding products to the cart, checkout, and child window (popup) handling
- `test_MoreValidations.py`: element visibility, alert dialogs, mouse hover, iframe handling, and reading a dynamic table
- `test_Network1.py`: network interception, mocking the orders API response with a fake "No Orders" payload
- `test_Network2.py`: request interception on the order details call, plus injecting an API-generated token into local storage to skip the UI login
- `test_Web_API.py`: end-to-end flow: create an order through the API, log in through the UI, and verify the order in the order history
- `test_framework_Web_API.py`: the same end-to-end flow built with the framework: page objects, API utilities, and data-driven runs from `Data/credentials.json`
- `test_pytest-bddTest.py`: BDD scenarios with pytest-bdd
- `test_playwrightBasics.py`: Playwright basics