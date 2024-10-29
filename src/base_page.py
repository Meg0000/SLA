import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Initializes the driver


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.LoginLocators

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.locator.USERNAME_LOCATOR)
        )

        self.driver.find_element(*self.locator.USERNAME_LOCATOR).send_keys(username)
        self.driver.find_element(*self.locator.PASSWORD_LOCATOR).send_keys(password)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        time.sleep(3)


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.InventoryLocators

    def add_to_cart_inv_page(self):
        self.driver.find_element(*self.locator.BACKPACK_TO_CART).click()

        element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.locator.SHOPPING_CART_ITEM_COUNT)
        )
        cart_count = element.text
        print("items in cart:", cart_count)


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.CartLocators


class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.CheckoutLocators




# todo: cookies for easier login

