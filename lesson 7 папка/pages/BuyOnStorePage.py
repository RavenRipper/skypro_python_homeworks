from selenium.webdriver.common.by import By


class BuyOnStorePage():
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')

    def authorization_username(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)

    def authorization_password(self, term):   
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

    def shopping_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def input_first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(term)

    def input_last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(term)

    def input_postal_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(term)

    def button_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def summary_total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total