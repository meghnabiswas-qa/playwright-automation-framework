from .OrdersHistory import OrdersHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def ordersnav(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderhistorypage = OrdersHistoryPage(self.page)
        return orderhistorypage
