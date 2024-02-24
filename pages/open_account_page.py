from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.open_account_locators import OpenAccountLocators as Locator


class OpenAccountPage(BasePage):
    def find_name_in_dropdown(self, name) -> bool:
        """Find the specified name in the dropdown menu.
          Args:
              name (str): The name to search for in the dropdown menu.
          Returns:
              bool: True if the specified name is found in the dropdown menu, otherwise False.
          """
        try:
            self.select_dropdown_option_with_expected_text(Locator.DROPDOWN, name)
            return True
        except TimeoutException:
            return False
