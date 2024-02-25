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
    Цель: Добавить клиента и проверить сообщение об успешном добавлении клиента
        
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
            customers_page.verify_delete_customer(first_name)

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
            customers_page.verify_delete_customer(first_name)

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
            customers_page.verify_delete_customer(first_name)

    @allure.title("Проверка сортировки строк таблицы Customers в обратном алфавитном порядке по First Name")
    @allure.description("""
    Цель: Проверить, сортировку по колонке First Name в обратном алфавитном порядке таблицы Customers

    Предусловие:
    - Открыть браузер

    Шаги:
    1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list 
    2. Нажать на First Name
    3. Найти имена в таблице Customers
    4. Проверить, что в таблице Customers значения в колонке First Name расположены в обратном алфавитном порядке

    Ожидаемый результат:
    - В таблице Customers значения в колонке First Name расположены в обратном алфавитном порядке""")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("TC_01.04")
    @allure.label("owner", "Липатникова А.В.")
    @pytest.mark.ui
    def test_verify_sorting_of_the_first_names_in_reverse_alphabetical(self, driver):
        with allure.step("Открытие страницы globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"):
            customers_page = CustomersPage(driver, DataUrls.CUSTOMERS_URL)
            customers_page.open()

        with allure.step("Нажать на First Name"):
            customers_page.sort_by_first_name_click()

        with allure.step("Найти имена в таблице Customers"):
            names_list = customers_page.get_rows_customers()

        with allure.step("Проверить, что все значения в колонке First Name в таблице Customer расположены "
                         "в обратном алфавитном порядке"):
            assert customers_page.check_reverse_alphabetical_names(names_list), \
                "Sorting by First name Z-A works incorrect"

    @allure.title("Проверка сортировки строк таблицы Customers в алфавитном порядке")
    @allure.description("""
    Цель: Проверить, сортировку по колонке First Name в алфавитном порядке таблицы Customers
    
    Предусловие:
    - Открыть браузер

    Шаги:
    1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list 
    2. Нажать на First Name
    3. Нажать на First Name
    4. Найти имена в таблице Customers
    5. Проверить, что значения в колонке First Name расположены в алфавитном порядке

    Ожидаемый результат:
    - В таблице Customers значения в колонке First Name расположены в алфавитном порядке""")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("TC_01.05")
    @allure.label("owner", "Липатникова А.В.")
    @pytest.mark.ui
    def test_verify_sorting_of_the_first_names_in_alphabetical(self, driver):
        with allure.step("Открытие страницы globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"):
            customers_page = CustomersPage(driver, DataUrls.CUSTOMERS_URL)
            customers_page.open()

        with allure.step("Нажать на First Name"):
            customers_page.sort_by_first_name_click()

        with allure.step("Нажать на First Name"):
            customers_page.sort_by_first_name_click()

        with allure.step("Найти имена в таблице Customers"):
            names_list = customers_page.get_rows_customers()

        with allure.step("Проверить, что значения в колонке First Name расположены в алфавитном порядке"):
            assert customers_page.check_alphabetical_names(names_list), \
                "Sorting by First name A-Z works incorrect"

    @allure.title("Проверка удаления сustomers с длиной имени ближнему к среднему арифметическому "
                  "длин всех имен в колонке First Name")
    @allure.description("""
    Цель: Проверить, удаление сustomers с First Name длина которого будет ближе к среднему арифметическому

    Предусловие:
    - Открыть браузер

    Шаги:
    1. Открыть страницу https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/list 
    2. Найти список Customers до удаления
    3. Узнать длину каждого имени, затем найти среднее арифметическое получившихся длин
    4. Удалить клиента с тем именем/именами, у которого(ых) длина будет ближе к среднему арифметическому
    5. Найти имена в таблице Customers
    6. Проверить, что количество записей в таблице Customers уменьшилось и соответствует ожидаемому

    Ожидаемый результат:
    - В таблице Customers удалены клиент(ы) с именем/именами, у которого(ых) длина будет ближе к 
    среднему арифметическому.
    - Количество записей в таблице Customers уменьшилось и соответствует ожидаемому""")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase("TC_01.06")
    @allure.label("owner", "Липатникова А.В.")
    @pytest.mark.ui
    def test_delete_customer_by_average_length(self, driver):
        with allure.step("Открыть страницу Открыть страницу "
                         "globalsqa.com/angularJs-protractor/BankingProject/#/manager/list"):
            customers_page = CustomersPage(driver, DataUrls.CUSTOMERS_URL)
            customers_page.open()

        with allure.step("Найти список Customers до удаления"):
            customers_list = customers_page.get_rows_customers()
            len_customers_list_before = len(customers_list)

        with allure.step("Узнать длину каждого имени, затем найти среднее арифметическое получившихся длин"):
            all_names = customers_page.get_first_names_customers()
            closest_length_for_del = customers_page.find_closest_name_length(all_names)

        with allure.step("Узнать длину каждого имени, затем найти среднее арифметическое получившихся длин"):
            indices_for_del = customers_page.find_indices_by_name_length(all_names, closest_length_for_del)

        with allure.step("Удалить клиента(ов) с тем именем/именами, у которого(ых) длина будет ближе к среднему "
                         "арифметическому"):
            count_click_del = customers_page.click_delete_by_indices(indices_for_del)

        with allure.step("Найти имена в таблице Customers"):
            customers_list = customers_page.get_rows_customers()

        with allure.step("Проверить, что количество записей в таблице Customers "
                         "уменьшилось и соответствует ожидаемому"):
            len_customers_list_after = len(customers_list)
            assert len_customers_list_before - count_click_del == len_customers_list_after, \
                "Deleting customer does not work correctly"
