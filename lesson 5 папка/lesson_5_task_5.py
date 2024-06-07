from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

Cdriver = webdriver.Chrome
Fdriver = webdriver.Firefox

try:
    Cdriver.get("http://the-internet.herokuapp.com/inputs")
    Fdriver.get("http://the-internet.herokuapp.com/inputs")
    input_field = Cdriver.find_element(By.TAG_NAME, "input")
    input_field = Fdriver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")
    sleep(2)
    input_field.clear()
    sleep(1)
    input_field.send_keys("999")
    sleep(2)

except Exception as ex:
    print(ex)
finally:
    Cdriver.quit()
    Fdriver.quit()