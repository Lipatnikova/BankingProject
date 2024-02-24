from typing import List

from locators.customers_locators import CustomersLocators as Locator
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class CustomersPage(BasePage):

    def send_key_in_search(self, key: str) -> None:
        self.send_keys_in_input(Locator.SEARCH, key)

    def click_button_delete(self) -> None:
        self.click_button(Locator.DELETE_BUTTON)

    def sort_by_first_name_click(self) -> None:
        self.click_element(Locator.SORT_FIRST_NAME)

    def find_all_rows_customers(self) -> List[WebElement]:
        return self.elements_are_visible(Locator.CUSTOMER)

    def get_rows_customers(self) -> List:
        """Retrieve rows of customer data from the page.
            Returns:
                List: A list containing the rows of customer data retrieved from the page"""
        customers = self.find_all_rows_customers()
        data = []
        for i in customers:
            data.append(i.text.splitlines())
        return data

    @staticmethod
    def format_result(data) -> List[List[str]]:
        """This method removes all "Delete" values from the list of lists"""
        cleaned_data = []
        for sublist in data:
            cleaned_sublist = [item.replace(' Delete', '') for item in sublist]
            cleaned_data.append(cleaned_sublist)
        return cleaned_data

    @staticmethod
    def verify_new_customer_in_list_customers(list1, list2) -> bool:
        """This method verifies if all items in list1 are present in the first elements of sublists in list2"""
        for item in list1:
            if item not in [sublist[0] for sublist in list2]:
                return False
        return True

    def delete_create_customer(self, first_name):
        """This method deletes the created customer"""
        self.send_key_in_search(first_name)
        self.click_button_delete()

    @staticmethod
    def check_alphabetical_names(data: List[List[str]]) -> bool:
        """This method checks whether the elements of each sublist are in alphabetical order"""
        names = [item[0].split()[0] for item in data]
        sorted_names = sorted(names)
        return names == sorted_names

    @staticmethod
    def check_reverse_alphabetical_names(data: List[List[str]]) -> bool:
        """This method checks whether the elements of each sublist are in reverse alphabetical order"""
        names = [item[0].split()[0] for item in data]
        sorted_names = sorted(names, reverse=True)
        return names == sorted_names
