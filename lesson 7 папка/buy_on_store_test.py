from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.BuyOnStorePage import BuyOnStorePage


def test_buy_on_store():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    buy = BuyOnStorePage(browser)
    buy.authorization_username('standard_user')
    buy.authorization_password('secret_sauce')
    buy.add_to_cart()
    buy.shopping_cart()
    buy.checkout()
    buy.input_first_name('Ilia')
    buy.input_last_name('Klimov')
    buy.input_postal_code('2403CW')
    buy.button_continue()
    total = buy.summary_total()

    assert total == 'Total: $58.29'

    browser.quit()