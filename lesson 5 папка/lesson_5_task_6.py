from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

Cdriver = webdriver.Chrome
Fdriver = webdriver.Firefox

try:
    Cdriver.get("http://the-internet.herokuapp.com/login")
    Fdriver.get("http://the-internet.herokuapp.com/login")
    input_name = Cdriver.find_element(By.ID, "username").send_keys("tomsmith")
    input_name = Fdriver.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)
    input_pass = Cdriver.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    input_pass = Fdriver.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)
    button = Cdriver.find_element(By.TAG_NAME, "button").click()
    button = Fdriver.find_element(By.TAG_NAME, "button").click()
    sleep(2)
except Exception as ex:
    print(ex)
finally:
    Cdriver.quit()
    Fdriver.quit()