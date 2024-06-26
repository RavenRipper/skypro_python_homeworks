from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By 
from configuration import *
from time import sleep


def test_data_types_form(firefox_browser):
    firefox_browser.get(URL_1)
    form_data = {
        'first-name': First_name, 
        'last-name': Last_name, 
        'address': Address, 
        'e-mail': Email, 
        'phone': Phone_number, 
        'zip-code': Zip_code, 
        'city': City, 
        'country': Country, 
        'job-position': Job_position, 
        'company': Company
    }

    for field_name, value in form_data.items():
        firefox_browser.find_element(By.NAME, field_name).send_keys(value) 

    WebDriverWait(firefox_browser, 40, 0.1).until(
        ec.element_to_be_clickable((By.TAG_NAME, "button"))).click() 

    sleep(2)

    field_classes = {
        'first-name': "success",
        'last-name': "success",
        'address': "success", 
        'e-mail': "success",
        'phone': "success",
        'zip-code': "danger",
        'city': "success",
        'country': "success",
        'job-position': "success",
        'company': "success"
    }

    for field_id, class_name in field_classes.items():
        assert class_name in firefox_browser.find_element(
            By.ID, field_id).get_attribute("class") 
    
