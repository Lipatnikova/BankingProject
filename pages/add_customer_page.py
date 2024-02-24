from generator.generator import get_customer, generate_post_code

from pages.base_page import BasePage
from locators.add_customer_locators import AddCustomerLocators as Locator


class AddCustomerPage(BasePage):

    @staticmethod
    def generate_first_name(post_code: str):
        # Разбиваем число на двузначные цифры
        digits = [int(post_code[i:i + 2]) for i in range(0, 10, 2)]
        # Преобразуем каждую цифру в соответствующую букву алфавита
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        letters = [alphabet[digit % 26] for digit in digits]
        # Объединяем буквы в одну строку
        result = ''.join(letters)
        return result

    def fill_first_name(self, post_code: str) -> str:
        first_name = self.generate_first_name(post_code)
        self.send_keys_in_input(Locator.FIRST_NAME, first_name)
        print(first_name)
        return first_name

    def fill_last_name(self) -> str:
        info = next(get_customer())
        last_name = info.last_name
        self.send_keys_in_input(Locator.LAST_NAME, last_name)
        print(last_name)
        return last_name

    def fill_post_code(self) -> str:
        post_code = generate_post_code()
        self.send_keys_in_input(Locator.POST_CODE, post_code)
        print(post_code)
        return post_code

    def click_add_customer_button(self) -> None:
        self.click_button(Locator.ADD_CUSTOMER_BUTTON)
