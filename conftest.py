import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    print('\nStart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=2880,1800')
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
    else:
        driver = webdriver.Chrome(service=Service())
        driver.maximize_window()
    yield driver
    print('\nQuit browser...')
    driver.quit()
