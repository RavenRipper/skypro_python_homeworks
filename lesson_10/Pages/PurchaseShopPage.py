from selenium.webdriver.common.by import By
import re
import allure


class PurchasePage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("авторизация пользователя")
    def login_shop(self) -> None:
        """
        Метод выполняет авторизацию пользователя
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
        self._driver.find_element(
            By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
        self._driver.find_element(
            By.CSS_SELECTOR, "input#login-button").click()

    @allure.step("добавить товары в корзину")
    def add_items_to_cart(self, list: list) -> None:
        """
        Метод добавляет в корзину товары из списка
        """
        for item in list:
            self._driver.find_element(
                By.CSS_SELECTOR,
                f"button[data-test='add-to-cart-{item}']").click()

        self._driver.find_element(
            By.CSS_SELECTOR, "a[data-test='shopping-cart-link']").click()

    @allure.step("нажать кнопку checkout в корзине")
    def open_cart(self) -> None:
        """
        Метод в корзине нажимает на кнопку checkout
        """
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.find_element(
            By.CSS_SELECTOR, "button[data-test='checkout']").click()

    @allure.step("заполнить поля формы для доставки")
    def fill_info_form(self, first_name: str,
                       last_name: str, postal_code: int) -> None:
        """
        Метод заполняет форму с информацией пользователя для доставки заказа
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "input[data-test='firstName']"
            ).send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "input[data-test='lastName']"
            ).send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "input[data-test='postalCode']"
            ).send_keys(postal_code)

        self._driver.find_element(By.CSS_SELECTOR,
                                  "input[data-test='continue']").click()

    @allure.step("получить итоговую сумму оформленного заказа")
    def get_total_amount_in_cart(self) -> str:
        """
        Метод возвращает итоговую стоимость заказа
        """
        total_amount = self._driver.find_element(
            By.CSS_SELECTOR, "div[data-test='total-label']").text
        result = re.search(r'\$([0-9]+\.[0-9]+)', total_amount)

        return result.group()