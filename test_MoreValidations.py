import time

from playwright.sync_api import Page, expect


def test_uichecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name = "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Alert boxes
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name = "Confirm").click()

    #MouseHover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name = "Reload").click()

    # FrameHandling
    pageframe = page.frame_locator("#courses-iframe")
    pageframe.get_by_role("link", name = "All Access Plan").click()
    expect(pageframe.locator("body")).to_contain_text("Happy Subscibers")

    # dynamic elements in a table
def test_dynamicelements(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            pricecolvalue = index
            print(f"Price of rice is {pricecolvalue}")
            break

    ricerow = page.locator("tr").filter(has_text= "Rice")
    expect(ricerow.locator("td").nth(pricecolvalue)).to_have_text("37")


