import pytest
from selenium import webdriver

pytest.fixture()
def firefox_browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()