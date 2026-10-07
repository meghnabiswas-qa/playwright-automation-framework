from playwright.sync_api import Playwright, expect

from utils.API_Base import APIutils


def test_e2e_web_api(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order --> Order ID
    api_utils = APIutils()
    orderID = api_utils.createorder(playwright)


    # Login
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_placeholder("email@example.com").fill("meghna20was@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Meghna@123")
    page.get_by_role("button", name = "Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #Order History Page --> Order is present
    row = page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button", name = "View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()

