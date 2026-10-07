from playwright.sync_api import Page, expect


# to add items in the cart
def test_uivalidationdynamicscript(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()  # we can use CSS locator --- #Id, .class_name
    page.get_by_role("button", name="Sign In").click()
    samsungproduct = page.locator("app-card").filter(has_text="Samsung Note 8")
    samsungproduct.get_by_role("button").click()
    blackberryproduct = page.locator("app-card").filter(has_text="Blackberry")
    blackberryproduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childwindowhandle(page:Page):
    with page.expect_popup() as newpage_info:
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        page.locator(".blinkingText").first.click()
        childpage = newpage_info.value
        text = childpage.locator(".red").text_content()
        print(text) # Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words = text.split("at")
        email = words[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"





