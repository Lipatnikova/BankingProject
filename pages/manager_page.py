from locators.manager_page_locators import ManagerPageLocators
from pages.base_page import BasePage


class ManagerPage(BasePage):
    def click_button_add_customer(self) -> None:
        self.click_button(ManagerPageLocators.ADD_CUSTOMER_BUTTON)

    def click_button_open_account(self) -> None:
        self.click_button(ManagerPageLocators.OPEN_ACCOUNT)

    def click_button_customers(self) -> None:
        self.click_button(ManagerPageLocators.CUSTOMERS_BUTTON)
