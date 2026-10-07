from .OrderDetails import OrderDetailsPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def selectorders(self, orderID):
        row = self.page.locator("tr").filter(has_text=orderID)
        row.get_by_role("button", name="View").click()
        orderdetailspage = OrderDetailsPage(self.page)
        return orderdetailspage

