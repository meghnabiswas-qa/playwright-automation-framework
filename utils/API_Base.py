from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}


class APIutils:

    #Token
    def get_token(self, playwright: Playwright):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/auth/login",
            data={"userEmail":"meghna20was@gmail.com","userPassword":"Meghna@123"})

        assert response.ok
        print(response.json())
        responsebody = response.json()
        return responsebody["token"]


    def createorder(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(
            "/api/ecom/order/create-order",
            data=ordersPayload,
            headers={
                "Authorization": token,
                "Content-Type": "application/json"
            }
        )
        print(response.json())
        response_body = response.json()
        orderID = response_body["orders"][0]
        return orderID

