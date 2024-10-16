import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import loctrs


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = loctrs.LoginLoc

    def login(self, password, username):
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        time.sleep(3)


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = loctrs.InventoryLoc

    def add_to_cart_inv_page(self):
        self.driver.find_element(*self.locator.SAUCE_LABS_BACKPACK_TO_CART).click()
        element = WebDriverWait(EC.visibility_of_element_located(self.locator.SHOPPING_CART_ITEM_COUNT))
        cart_count = element.txt
        print(cart_count)

# todo: customer path: login>add to cart> checkout
# todo: cookies for easier login
