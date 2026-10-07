import pytest


@pytest.fixture(scope="module")
def prework():
    print("I setup browser instance")
    return "Pass"


@pytest.fixture(scope="function")
def secondwork():
    print("I setup second instance")
    yield
    print("I teardown browser instance")

@pytest.mark.smoke
def test_firstCheck(prework, secondwork):  # using test word make sure it is a test
    print("This is first check")
    assert prework == "Pass"

@pytest.mark.skip
def test_secondCheck(preSetUpwork, secondwork):
    print("This is second check")
