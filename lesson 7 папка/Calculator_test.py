from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage


def test_calculator():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    calculator = CalculatorPage(browser)
    calculator.delay('45')

    calculator.click()

    screen = calculator.screen()

    assert screen == '15'

    browser.quit()