from selenium.webdriver.common.by import By


class CustomersLocators:
    SEARCH = (By.XPATH, "//*[@ng-model='searchCustomer']")
    SORT_FIRST_NAME = (By.XPATH, "//table/thead/tr/td[1]/a")
    CUSTOMER = (By.XPATH, "//tr[@class='ng-scope']")
    FIRST_NAMES = (By.XPATH, "//table/tbody/tr/td[1]")
    DELETE_BUTTON = (By.XPATH, "//*[@ng-click='deleteCust(cust)']")
