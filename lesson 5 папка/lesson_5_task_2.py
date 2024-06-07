from selenium import webdriver
from time import sleep

Cdriver = webdriver.Chrome()
Fdriver = webdriver.Firefox()


try:
    count = 0
    Cdriver.get("http://uitestingplayground.com/dynamicid")
    Fdriver.get("http://uitestingplayground.com/dynamicid")
    blue_button = Cdriver.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button = Fdriver.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    for _ in range(3):
        blue_button = Cdriver.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        blue_button = Fdriver.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]').click()
        count = count + 1
        sleep(2)
        print(count)
except Exception as ex:
    print(ex)
finally:
    Cdriver.quit()
    Fdriver.quit()