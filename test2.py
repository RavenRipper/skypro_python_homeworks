from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from configuration import *
from time import sleep

def test_calculator_form(firefox_browser):
    firefox_browser.get(URL_2)
    delay_input = firefox_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    firefox_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    firefox_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    firefox_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    firefox_browser.find_element(By.XPATH, "//span[text() = '=']").click()
    WebDriverWait(firefox_browser, 46).until(ec.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = firefox_browser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"
