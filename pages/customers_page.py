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

    def delete_create_customer(self, first_name) -> None:
        """This method deletes the created customer"""
        self.send_key_in_search(first_name)
        self.click_button_delete()

    def verify_delete_customer(self, first_name):
        """This method sends the First Name value to the Search field and checks
        if the client with such a First Name has been deleted"""
        self.fill_in_input(Locator.SEARCH, first_name)
        assert self.is_present_element(Locator.CUSTOMER) is False, \
            "The customer has not been deleted"

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

    def find_all_first_names(self) -> List[WebElement]:
        return self.elements_are_visible(Locator.FIRST_NAMES)

    def get_first_names_customers(self) -> List:
        customers = self.find_all_first_names()
        data = []
        for i in customers:
            data.append(i.text.splitlines())
        return data

    @staticmethod
    def find_closest_name_length(names: [List[str]]) -> int:
        """
        Метод находит длину имени клиента, ближней к среднему арифметическому длин всех имен в списке.
        :param names: Список имен.
        :return: int: Длина имени клиента, ближней к среднему арифметическому длин всех имен в списке.
        """

        lengths = [len(name[0]) for name in names]
        average_length = sum(lengths) / len(lengths)

        min_difference = float('inf')
        closest_length = None

        for length in lengths:
            difference = abs(length - average_length)
            if difference < min_difference:
                closest_length = length
                min_difference = difference

        return closest_length

    @staticmethod
    def find_indices_by_name_length(names, num):
        """
        Метод находит индексы элементов в списке, ближайших к среднему арифметическому длин всех имен в списке.
        :param names: Список имен, num: Среднеарифтемическая длина имен из списка.
        :return: список индексов.
        """
        indices = []
        for i, name in enumerate(names):
            if len(name[0]) == num:
                indices.append(i)
        return indices

    def click_delete_by_indices(self, indices) -> int:
        """
        Нажимает кнопку Delete у элементов по индексу кнопки
        :param indices: массив индексов элементов, которые необходимо удалить
        :return: количество нажатий на кнопку Delete
        """
        count_click = 0
        for num_del in reversed(indices):
            self.driver.find_element("xpath", f"//table/tbody/tr[{num_del+1}]/td[5]/button").click()
            count_click += 1
        return count_click
