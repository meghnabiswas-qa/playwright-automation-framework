import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightbasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com")


# chromium launch we can also do using "page" fixture, but it always runs in headless mode

def test_playwrightshortcut(page: Page):
    page.goto("https://www.google.com")

# page:Page playwright will automatically run in Chrome browser
def test_corelocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check() # we can use CSS locator --- #Id, .class_name
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    time.sleep(5)

#for assertion error if the password is wrong, and it takes time to load
def test_corelocatorsassertion(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check() # we can use CSS locator --- #Id, .class_name
    page.get_by_role("link", name = "terms and conditions").click()
    page.get_by_role("button", name = "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

# for firefox browser
def test_firefoxbrowser(playwright:Playwright):
    firefoxbrowser = playwright.firefox.launch(headless = False)
    page = firefoxbrowser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()  # we can use CSS locator --- #Id, .class_name
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()




