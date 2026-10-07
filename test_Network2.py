import time

from playwright.sync_api import Page, Playwright, expect

from utils.API_Base import APIutils


def interceptresponse(route):
    route.continue_(url = "https://rahulshettyacademy.com/client/#/dashboard/order-details/6aaea24c2be7a4bc2b5b0e3a")




def test_network_2(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", interceptresponse)
    page.get_by_placeholder("email@example.com").fill("meghna20was@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Meghna@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)

def test_session_storage(playwright:Playwright):
    api_utils = APIutils()
    getToken = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless = False)
    context = browser.new_context()
    page = context.new_page()
    #script to inject token in session local storage
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client/")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()

