import json
#pytest Playwright --browser_name chrome -n 3 --tracing on --html=report.html --> cmd
import pytest
from playwright.sync_api import Playwright

from PageObject.Login import LoginPage

from utils.API_BaseFramework import APIutils

#jsonfile --> utils --> access to the test
with open("Playwright/Data/credentials.json") as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data["user_credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_web_api(playwright:Playwright, browserinstance,  user_credentials):
    userEmail = user_credentials["userEmail"]
    password = user_credentials["userPassword"]


    #create order --> Order ID
    api_utils = APIutils()
    orderID = api_utils.createorder(playwright, user_credentials)


    # Login
    loginpage = LoginPage(browserinstance)   # object for LoginPage class
    loginpage.navigate()
    dashboard = loginpage.login(userEmail, password)

    # dashboard page where we click on Orders
    orderhistorypage = dashboard.ordersnav()
    orderdetailspage = orderhistorypage.selectorders(orderID)
    orderdetailspage.verifyordermessage()



