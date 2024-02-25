from pages.base_page import BasePage
from locators.add_customer_locators import AddCustomerLocators as Locator


class AddCustomerPage(BasePage):

    def fill_first_name(self, first_name) -> None:
        self.send_keys_in_input(Locator.FIRST_NAME, first_name)

    def fill_last_name(self, last_name) -> None:
        self.send_keys_in_input(Locator.LAST_NAME, last_name)

    def fill_post_code(self, post_code) -> None:
        self.send_keys_in_input(Locator.POST_CODE, post_code)

    def click_add_customer_button(self) -> None:
        self.click_button(Locator.ADD_CUSTOMER_BUTTON)
