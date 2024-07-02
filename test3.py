from selenium.webdriver.common.by import By
from configuration import *
from time import sleep

def test_shop_form(firefox_browser):
    firefox_browser.get(URL_3)
    firefox_browser.find_element(By.ID, "user-name").send_keys("standart_user")
    firefox_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    sleep(2)
    firefox_browser.find_element(By.ID, "login-button").click()
    sleep(2)
    firefox_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    sleep(2)
    firefox_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    sleep(2)
    firefox_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    sleep(2)
    firefox_browser.find_element(By.ID, "shopping_cart_container").click()
    sleep(2)
    firefox_browser.find_element(By.ID, "checkout").click()
    sleep(2)
    firefox_browser.find_element(By.ID, "first-name").send_keys("Vovan")
    firefox_browser.find_element(By.ID, "last-name").send_keys("Ivanov")
    firefox_browser.find_element(By.ID, "postal-code").send_keys("500500")
    sleep(2)
    firefox_browser.find_element(By.ID, "continue").click()
    sleep(2)
    total_price = firefox_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", '')
                                             
    expected_total = "58.29"
    assert total == expected_total 
    print(f"Итоговая сумма равна ${total}")
