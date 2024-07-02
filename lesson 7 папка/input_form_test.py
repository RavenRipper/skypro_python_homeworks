from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.InputFormPage import InputFormPage


def test_unput_form():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    input_form = InputFormPage(browser)
    input_form.first_name('Иван')
    input_form.last_name('Петров')
    input_form.address('Ленина, 55-3')
    input_form.e_mail('test@skypro.com')
    input_form.phone('+7985899998787')
    input_form.zip_code('')
    input_form.city('Москва')
    input_form.country('Россия')
    input_form.job_position('QA')
    input_form.company('SkyPro')
    input_form.submit()

    alert_danger = input_form.alert_danger()

    assert alert_danger == "rgba(248, 215, 218, 1)"

    alert_succes = input_form.alert_success()

    assert alert_succes == "rgba(209, 231, 221, 1)"

    browser.quit()