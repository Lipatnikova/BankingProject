from selenium.webdriver.common.by import By


class AddCustomerLocators:
    FIRST_NAME = (By.XPATH, "//*[@ng-model='fName']")
    LAST_NAME = (By.XPATH, "//*[@ng-model='lName']")
    POST_CODE = (By.XPATH, "//*[@ng-model='postCd']")
    ADD_CUSTOMER_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default")
