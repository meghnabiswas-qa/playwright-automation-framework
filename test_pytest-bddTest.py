import pytest
from pytest_bdd import given, when, then, parsers, scenario, scenarios

from PageObject.Login import LoginPage
from utils.API_BaseFramework import APIutils

scenarios('Feature/OrderTransaction.feature')


@pytest.fixture
def shared_data():
    return {}


@given(parsers.parse('place the order with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {}
    user_credentials["userEmail"] = username
    user_credentials["userPassword"] = password
    api_utils = APIutils()
    orderID = api_utils.createorder(playwright, user_credentials)
    shared_data["order_id"] = orderID

@given('the user is on landing page')
def user_login_page(browserinstance, shared_data):
    loginpage = LoginPage(browserinstance)  # object for LoginPage class
    loginpage.navigate()
    shared_data["login_page"] = loginpage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    loginpage = shared_data["login_page"]
    dashboard = loginpage.login(username, password)
    shared_data["dashboard_page"] = dashboard

@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard = shared_data["dashboard_page"]
    orderhistorypage = dashboard.ordersnav()
    shared_data["orders_page"] = orderhistorypage


@when('select the orderId')
def select_order_id(shared_data):
    orderhistorypage = shared_data["orders_page"]
    orderID = shared_data["order_id"]
    orderdetailspage = orderhistorypage.selectorders(orderID)
    shared_data["order_details_page"] = orderdetailspage



@then('order message is successfully displayed')
def order_message(shared_data):
    orderdetailspage = shared_data["order_details_page"]
    orderdetailspage.verifyordermessage()