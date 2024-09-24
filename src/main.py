from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from base_page import LoginPage

#CONSTANTS
LOGIN_PAGE = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
# should add correct usernames as csv?
USERNAME = "standard_user"


class MainMagic:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--disable-search-engine-choice-screen")
        self.options.add_argument("disable-infobars")
        self.driver = webdriver.Chrome(options=self.options)

    def start(self):
        self.driver.get(LOGIN_PAGE)

    def wrong_login(self):
        MainMagic.start()
        self.driver.find_element(By.NAME, "login-button").click()

    def correct_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.login(PASSWORD, USERNAME)

    def current_url(self):
        expected_url = self.driver.current_url
        return expected_url


class LoginTest(unittest.TestCase):
    def test_if_login_correct(self):
        x = MainMagic()
        x.start()
        x.correct_login()
        expected_url = "https://www.saucedemo.com/inventory.html"
        current_url = x.current_url()
        self.assertEqual(current_url, expected_url)
        

x = LoginTest()
x.test_if_login_correct()

if __name__ == '__main__':
    unittest.main()

# todo: review last test-where it is stored, how to add messages etc.
# todo: LoginTest - optimise, change 'x' value to sth more readable
# todo: correct login,wrong login etc - reorganise to be more readable, add tests

'''class EmptyLoginCredentials(unittest.TestCase):
    def empty_creds_error(self):
        self.assertEqual()'''
