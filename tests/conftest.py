import pytest

from data.data_urls import DataUrls
from pages.customers_page import CustomersPage


@pytest.fixture
def delete_customer(driver):
    def delete_customer(first_name):
        customers_page = CustomersPage(driver, DataUrls.CUSTOMERS_URL)
        customers_page.open()
        customers_page.delete_create_customer(first_name)
        customers_page.verify_delete_customer(first_name)

    yield delete_customer
