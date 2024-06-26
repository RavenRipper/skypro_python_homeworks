import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalculatorPage import Calculator

spinner_time = 5


@allure.epic("hw7")
@allure.feature("калькулятор")
class TestCal:

    @pytest.mark.parametrize('num1, num2, result', [
        (7, 8, 15), (5, 6, 11)])
    @allure.story("сумма целых чисел")
    @allure.title("проверка вычисления суммы целых чисел")
    @allure.description("только целые числа")
    
    @allure.severity("blocker")
    def test_sum(self, num1, num2, result):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))

        calculator_page = Calculator(driver)
        calculator_page.set_timer(spinner_time)
        calculator_page.set_num(num1)
        calculator_page.set_operant('+')
        calculator_page.set_num(num2)
        calculator_page.set_operant('=')
        to_be = result
        as_is = calculator_page.get_calculated_value(
            spinner_time, result)

        with allure.step("проверить, что результат вычисления верный"):
            assert to_be == as_is