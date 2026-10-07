import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client", help="url selection"
    )


@pytest.fixture(scope = "session")
def user_credentials(request):
    return request.param


@pytest.fixture
def browserinstance(playwright, request):
    browsername = request.config.getoption("browser_name")
    urlname = request.config.getoption("url_name")
    if browsername == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browsername == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    #page.goto(urlname)
    yield page
    context.close()
    browser.close()