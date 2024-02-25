from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from typing import List

from data.config import WAIT_TIMEOUT


class BasePage:
    def __init__(self, driver, url):
        """This method initializes the BasePage object"""
        self.driver = driver
        self.url = url

    def open(self) -> None:
        """This method opens a browser by the provided link"""
        self.driver.get(self.url)

    def get_current_url(self) -> str:
        """This method returns the current URL of the browser"""
        return self.driver.current_url

    def element_is_clickable(self, locator: WebElement or tuple[str, str], timeout: int = WAIT_TIMEOUT) -> WebElement:
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator: WebElement or tuple[str, str], timeout: int = WAIT_TIMEOUT) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def element_is_visible(self, locator: WebElement or tuple[str, str], timeout: int = WAIT_TIMEOUT) -> WebElement:
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_present(
            self, locator: WebElement or tuple[str, str], timeout: int = WAIT_TIMEOUT) -> List[WebElement]:
        """
        This method expects to verify that the elements are present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_are_visible(
            self, locator: WebElement or tuple[str, str], timeout: int = WAIT_TIMEOUT) -> List[WebElement]:
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 10 seconds, but it can be modified if needed.
        """
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def go_to_element(self, element: WebElement or tuple[str, str]) -> None:
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def send_keys_in_input(self, locator: WebElement or tuple[str, str], key: str) -> None:
        """
        This method sends the key in the field.
        """
        self.element_is_visible(locator).send_keys(key)

    def fill_in_input(self, locator: WebElement or tuple[str, str], key: str) -> None:
        """This method fills in a specified field with provided value"""
        input_field = self.element_is_visible(locator)
        input_field.click()
        input_field.clear()
        input_field.send_keys(key)

    def click_button(self, locator: WebElement or tuple[str, str]) -> None:
        """This method expects to verify that the element is visible,
        displayed on the page, and enabled. The element is present in the DOM tree.
        After clicking the element, the page scrolls to the element."""
        self.element_is_clickable(locator).click()

    def click_element(self, locator: WebElement or tuple[str, str]) -> None:
        """This method clicks on the element"""
        self.element_is_visible(locator).click()

    def select_dropdown_option_with_expected_text(self, locator: WebElement or tuple[str, str], option_text: str):
        """This method selects an option from the dropdown"""
        dropdown = self.element_is_clickable(locator)
        for option in dropdown.find_elements("tag name", "option"):
            if option.text == option_text:
                option.click()
                break

    def fetch_and_accept_alert_text(self) -> str:
        """Fetches the text of an alert dialog and accepts the alert.
        :return: str: The text content of the alert dialog."""
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def is_present_element(self, locator: WebElement or tuple[str, str]) -> bool:
        """This method checks the presence of an element on the page"""
        try:
            self.element_is_present(locator)
            return True
        except TimeoutException:
            return False
