import allure
import pytest

from data.data import DataAddCustomer
from data.data_urls import DataUrls
from pages.add_customer_page import AddCustomerPage
from pages.customers_page import CustomersPage
from pages.manager_page import ManagerPage
from pages.open_account_page import OpenAccountPage


class TestManagerPage:

    @allure.title("Проверка сообщения об успешном добавлении клиента")
    @allure.description("""
    Цель: Добавить клипента и проверить сообщение об успешном добавлении клиента
        
    Предусловие:
    - Открыть браузер
            
    Шаги:
    1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 
    2. Нажать кнопку Add Customer
    3. Дождаться появление формы Add Customer
    4. Заполнить поле Post Code
    5. Заполнить поле First Name
    6. Заполнить поле Last Name
    7. Нажать кнопку Add Customer
    8. Проверить сообщение об успешном добавлении клиента, сообщение должно содержать текст "Customer added 
    successfully with customer id" и нажать кнопку ОК
     
    Постусловие:
    - Удалить созданного клиента
            
    Ожидаемый результат:
    - Новый клиент успешно добавлен в систему
    - Появилось сообщение об успешном добавлении клиента, сообщение содержит текст 'Customer added 
    successfully with customer id'""")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("TC_01.01")
    @allure.label("owner", "Липатникова А.В.")
    @pytest.mark.ui
    def test_verify_alert_message_after_customer_add(self, driver):

        with allure.step("Открытие страницы globalsqa.com/angularJs-protractor/BankingProject/#/manager"):
            manager_page = ManagerPage(driver, DataUrls.MANAGER_URL)
            manager_page.open()

        with allure.step("Нажать кнопку Add Customer"):
            manager_page.click_button_add_customer()
            add_customer_page = AddCustomerPage(driver, manager_page.get_current_url())

        with allure.step("Заполнить поле Post Code"):
            post_code = add_customer_page.fill_post_code()

        with allure.step("Заполнить поле First Name"):
            first_name = add_customer_page.fill_first_name(post_code)

        with allure.step("Заполнить поле Last Name"):
            add_customer_page.fill_last_name()

        with allure.step("Нажать кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("Проверить сообщение об успешном добавлении клиента"):
            assert DataAddCustomer.MSG_SUCCESS in add_customer_page.get_alert_text(), \
                "The expected message about the successful addition of the Customer is not displayed correctly"

        with allure.step("Удалить созданного клиента"):
            manager_page.click_button_customers()
            customers_page = CustomersPage(driver, add_customer_page.get_current_url())
            customers_page.open()
            customers_page.delete_create_customer(first_name)

    @allure.title("Проверка данных созданного клиента с данными в таблице Customers")
    @allure.description("""
    Цель: Проверить данные созданного клиента (Add Customer) с данными в таблице Customers

    Предусловие:
    - Открыть браузер

    Шаги:
    1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 
    2. Нажать кнопку Add Customer
    3. Дождаться появление формы Add Customer
    4. Заполнить поле Post Code
    5. Заполнить поле First Name
    6. Заполнить поле Last Name
    7. Нажать кнопку Add Customer
    8. В сообщении об успешном добавлении клиента нажать кнопку ОК
    9. Перейти в Customers (нажать кнопку Customers)
    10. Из таблицы Customers получить список клиентов
    11. Проверить, что клиент с First_name, Last_name, Post_code введенными при добавлении клиента,  
    отображается в таблице Customers
        
    Постусловие:
    - Удалить созданного клиента (удалить тестовые данные)

    Ожидаемый результат:
    - Новый клиент успешно добавлен в систему
    - В таблице Customers появилась строка (запись клиента) с First_name, Last_name, Post_code 
    соответствующим введенным при создании клиента""")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("TC_01.02")
    @allure.label("owner", "Липатникова А.В.")
    @pytest.mark.ui
    def test_add_customer_and_verify_customer_in_table_customers(self, driver):
        with allure.step("Открытие страницы globalsqa.com/angularJs-protractor/BankingProject/#/manager"):
            manager_page = ManagerPage(driver, DataUrls.MANAGER_URL)
            manager_page.open()

        with allure.step("Нажать кнопку Add Customer"):
            manager_page.click_button_add_customer()

        with allure.step("Дождаться появление формы Add Customer"):
            add_customer_page = AddCustomerPage(driver, manager_page.get_current_url())

        with allure.step("Заполнить поле Post Code"):
            post_code = add_customer_page.fill_post_code()

        with allure.step("Заполнить поле First Name"):
            first_name = add_customer_page.fill_first_name(post_code)

        with allure.step("Заполнить поле Last Name"):
            last_name = add_customer_page.fill_last_name()
            expected_list = [f'{first_name} {last_name} {post_code}']

        with allure.step("Нажать кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("В сообщении об успешном добавлении клиента нажать кнопку ОК"):
            add_customer_page.get_alert_text()

        with allure.step("Нажать кнопку Customers"):
            manager_page.click_button_customers()

        with allure.step("Перейти в Customers"):
            customers_page = CustomersPage(driver, add_customer_page.get_current_url())
            customers_page.open()

        with allure.step("Из таблицы Customers получить список клипентов"):
            customers_list = customers_page.get_rows_customers()
            customers_list = customers_page.format_result(customers_list)

        with allure.step("Проверить, что клиент с First_name, Last_name, Post_code "
                         "введенными при добавлении клиента,  отображается в таблице Customers"):
            assert customers_page.verify_new_customer_in_list_customers(expected_list, customers_list)

        with allure.step("Удалить созданного клиента"):
            customers_page.delete_create_customer(first_name)

    @allure.title("Проверка данных созданного клиента с данными в dropdown меню в Open Account")
    @allure.description("""
    Цель: Проверить данные созданного клиента (Add Customer) с данными в dropdown меню в Open Account

    Предусловие:
    - Открыть браузер

    Шаги:
    1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager 
    2. Нажать кнопку Add Customer
    3. Дождаться появление формы Add Customer
    4. Заполнить поле Post Code
    5. Заполнить поле First Name
    6. Заполнить поле Last Name
    7. Нажать кнопку Add Customer
    8. В сообщении об успешном добавлении клиента нажать кнопку ОК
    9. Нажать кнопку Open Account
    10. Проверить, что в dropdown меню есть клиент с First_name, Last_name введенными при добавлении клиента

    Постусловие:
    - Удалить созданного клиента

    Ожидаемый результат:
    - Новый клиент успешно добавлен в систему
    - В dropdown меню есть клиент с First_name, Last_name введенными при добавлении клиента""")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase("TC_01.03")
    @allure.label("owner", "Липатникова А.В.")
    @pytest.mark.ui
    def test_add_customer_and_verify_customer_in_dropdown_menu_in_open_account(self, driver):
        with allure.step("Открытие страницы globalsqa.com/angularJs-protractor/BankingProject/#/manager"):
            manager_page = ManagerPage(driver, DataUrls.MANAGER_URL)
            manager_page.open()

        with allure.step("Нажать кнопку Add Customer"):
            manager_page.click_button_add_customer()

        with allure.step("Дождаться появление формы Add Customer"):
            add_customer_page = AddCustomerPage(driver, manager_page.get_current_url())

        with allure.step("Заполнить поле Post Code"):
            post_code = add_customer_page.fill_post_code()

        with allure.step("Заполнить поле First Name"):
            first_name = add_customer_page.fill_first_name(post_code)

        with allure.step("Заполнить поле Last Name"):
            last_name = add_customer_page.fill_last_name()
            expected_name = f'{first_name} {last_name}'

        with allure.step("Нажать кнопку Add Customer"):
            add_customer_page.click_add_customer_button()

        with allure.step("В сообщении об успешном добавлении клиента нажать кнопку ОК"):
            add_customer_page.get_alert_text()

        with allure.step("Нажать кнопку Open Account"):
            manager_page.click_button_open_account()
            open_account_page = OpenAccountPage(driver, manager_page.get_current_url())

        with allure.step("Проверить, что в dropdown меню есть клиент с First_name, Last_name "
                         "введенными при добавлении клиента"):
            assert open_account_page.find_name_in_dropdown(expected_name), \
                "The expected name was not found in the dropdown menu"

        with allure.step("Удалить созданного клиента"):
            manager_page.click_button_customers()
            customers_page = CustomersPage(driver, add_customer_page.get_current_url())
            customers_page.open()
            customers_page.delete_create_customer(first_name)
