import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

Cdriver = webdriver.Chrome
Fdriver = webdriver.Firefox

try:
    Cdriver.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(Cdriver, 10)
    Fdriver.get("http://the-internet.herokuapp.com/entry_ad")
    wait = WebDriverWait(Fdriver, 10)
    modal_window = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal")))
    close_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".modal-footer")))
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    Cdriver.quit()
    Fdriver.quit()
    