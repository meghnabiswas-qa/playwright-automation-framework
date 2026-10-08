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
├── pytest/               # [describe what this folder holds]
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

- `test_UIvalidations_1.py`, `test_MoreValidations.py`: [UI validations]
- `test_Network1.py`, `test_Network2.py`: [network interception / mocking]
- `test_Web_API.py`, `test_framework_Web_API.py`: [API and combined UI + API flows]
- `test_pytest-bddTest.py`: BDD scenarios with pytest-bdd
- `test_playwrightBasics.py`: Playwright basics