from selenium.webdriver.common.by import By


class InputFormPage():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    def last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    def address(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    def zip_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]').send_keys(term)

    def city(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    def country(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    def e_mail(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    def phone(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    def job_position(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    def company(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(term)

    def submit(self):
        self._driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def alert_danger(self):
        alert_danger = self._driver.find_element(By.CSS_SELECTOR, 'div.alert.py-2.alert-danger').value_of_css_property("background-color")
        return alert_danger

    def alert_success(self):
        allert_success = self._driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
        for form in allert_success:
            return form.value_of_css_property("background-color")