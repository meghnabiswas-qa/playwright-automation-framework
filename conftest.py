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



import os
import requests
from pytest_html import extras

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Agentic AI Hook: Captures failure telemetry, DOM state, and injects RCA into pytest-html."""
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # Grab the 'page' fixture from the test if it exists
        page = item.funcargs.get("page") or item.funcargs.get("browserinstance")
        error_trace = str(report.longrepr)
        current_url = page.url if page else "N/A"
        dom_snapshot = ""

        if page:
            try:
                dom_snapshot = page.content()
                screenshot_bytes = page.screenshot(full_page=True)
                extra.append(extras.image(screenshot_bytes, name="Failure Screenshot"))
            except Exception:
                dom_snapshot = "DOM capture unavailable."

        # AI Triage & Local Heuristic Fallback
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            category = "UI Locator Drift / Timing Flake" if "TimeoutError" in error_trace else "Functional Regression"
            ai_rca = (
                f"[Heuristic Triage Mode - Set OPENAI_API_KEY for LLM Agent]\n"
                f"• Category: {category}\n"
                f"• URL State: {current_url}\n"
                f"• Action: Inspect selector determinism or verify test data state."
            )
        else:
            try:
                resp = requests.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
                    json={
                        "model": "gpt-4o-mini",
                        "messages": [{"role": "user", "content": f"Analyze Playwright test failure:\nTrace:\n{error_trace}\nURL:{current_url}"}],
                        "temperature": 0.1
                    },
                    timeout=8
                )
                ai_rca = resp.json()["choices"][0]["message"]["content"]
            except Exception as e:
                ai_rca = f"AI Triage Request Failed: {e}"

        extra.append(extras.text(ai_rca, name="🤖 Agentic AI Root-Cause Triage"))
        report.extra = extra