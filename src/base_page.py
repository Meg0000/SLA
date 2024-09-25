import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
import loctrs


class BasePage:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-search-engine-choice-screen")
        self.options.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(options=self.options)


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.locator = loctrs.LoginLoc

    def login(self, password, username):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        time.sleep(3)


class InventoryPage(BasePage):
    def __init__(self):
        super().__init__()
        self.locator = loctrs.InventoryLoc

# todo: 20222F bg + iceberg
# todo: customer path: login>add to cart> checkout

'''
t1 = LoginPage()
t1.login("secret_sauce", "standard_user")
'''
