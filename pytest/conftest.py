import pytest


@pytest.fixture(scope="session")
def preSetUpwork():
    print("I setup new browser instance")