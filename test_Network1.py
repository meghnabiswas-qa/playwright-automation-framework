import pytest
from playwright.sync_api import Page

fakePayLoadOrederResponse = {"data": [], "message": "No Orders"}

def intercept_response(route):
    route.fulfill(
        json= fakePayLoadOrederResponse
    )


@pytest.mark.smoke
def test_network_1(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("meghna20was@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Meghna@123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    orders_text = page.locator((".mt-4")).text_content()
    print(orders_text)