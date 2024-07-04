import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Pages.FormFillPage import FormFill


full_id_list = {
            "first-name": "Иван", "last-name": "Петров",
            "address": "Ленина, 55-3", "zip-code": "",
            "city": "Москва", "country": "Россия",
            "e-mail": "test@skypro.com", "phone": "+7985899998787",
            "job-position": "QA", "company": "SkyPro"
            }
id_list = ["first-name", "last-name", "address", "city", "country",
           "e-mail", "phone", "job-position", "company"]

property = 'background-color'
not_fill_field = 'zip-code'

background_color_alert_danger = 'rgba(248, 215, 218, 1)'
background_color_alert_success = 'rgba(209, 231, 221, 1)'

@allure.epic("hw7")
@allure.feature("форма")
class TestFormFill:

    @allure.title("проверка свойства незаполненных полей")
    @allure.description("свойство и значение передается в методе")
    @allure.story("цвет фона полей")
    @allure.severity("Minor")
    def test_background_color_unfilled_field_in_form(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

        fill_form = FormFill(driver)
        fill_form.fill_all_fields(full_id_list)
        result = fill_form.get_property_element(
            not_fill_field, property, background_color_alert_danger)

        with allure.step("проверить, что цвет фона\
                        незаполненного поля правильный"):
            assert result is True

        driver.quit()

@allure.title("проверка свойства заполненных полей")
@allure.description("свойство и значение передается в методе")
@allure.story("цвет фона полей")
@allure.severity("Minor")
def test_background_color_fill_field_in_form(self):
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            fill_form = FormFill(driver)
            fill_form.fill_all_fields(full_id_list)
            result = fill_form.get_property_elements(
                id_list, property, background_color_alert_success)
            with allure.step("проверить, что значение свойства\
                            соответствует переданному"):
                assert result is True

            driver.quit()