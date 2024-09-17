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


