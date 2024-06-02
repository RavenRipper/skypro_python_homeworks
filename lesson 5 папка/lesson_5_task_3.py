from selenium import webdriver
from time import sleep

Cdriver = webdriver.Chrome
Fdriver = webdriver.Firefox

try:
    Cdriver.get("http://uitestinplayground.com/classattr")
    Fdriver.get("http://uitestinplayground.com/classattr")
    for _ in range(3):
        blue_button = Cdriver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary')]")
        blue_button = Fdriver.find_element(
            "xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary')]")
        blue_button.click()
        sleep(2)
        Cdriver.switch_to.alert.accept()
        Fdriver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:
    Cdriver.quit()
    Fdriver.quit()
