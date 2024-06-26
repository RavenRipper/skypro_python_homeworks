from selenium.webdriver.common.by import By
import allure


class FormFill:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Заполнить все поля и нажать на кнопку отправить")
    def fill_all_fields(self, dict: dict) -> None:
        """
        Метод заполняет поля формы и нажимает на кнопку submit
        """
        for name, value in dict.items():
            self._driver.find_element(By.NAME, name).send_keys(value)

        self._driver.find_element(
            By.CSS_SELECTOR, "button.btn-outline-primary").click()

    @allure.step("Получить свойства элемента - {property}")
    def get_property_element(self, element: str, property: str, value: str) -> bool:
        """
        Метод получает значение css свойства элемента
        """
        check_property = self._driver.find_element(
            By.ID, element).value_of_css_property(property)
        if (check_property != value):
            print(f'Error {id} property = {check_property} not {value}')
            return False
        return True

    @allure.step("Получить свойства элементов - {property}")
    def get_property_elements(self, list: list, property: str, value: str) -> bool:
        """
        Метод получает значение css свойства элементов
        """
        for id in list:
            id_check = self._driver.find_element(
                By.ID, id).value_of_css_property(property)
            if (id_check != value):
                print(f'Error {id} property = {id_check} not {value}')
                return False
        return True