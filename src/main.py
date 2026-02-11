from base_page import *
from selenium import webdriver
from selenium.webdriver.common.by import By
# CONSTANTS
LOGIN_PAGE = "https://www.saucedemo.com/"
PASSWORD = "secret_sauce"
# should add correct usernames as csv?
USERNAME = "standard_user"

driver = webdriver.Chrome()

class MainMagic:
    def __init__(self):
        #self.options = None
        self.driver = webdriver.Chrome(options=None)
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless=new")
        self.options.add_argument("--disable-search-engine-choice-screen")
        self.options.add_argument("disable-infobars")


        # todo: do that with all page objects
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def start(self):
        self.driver.get(LOGIN_PAGE)

    def empty_login(self):
        self.driver.find_element(By.NAME, "login-button").click()

    def locator_check(self):
        self.driver.find_element(self.inventory_page.locator.BIKE_LIGHT_LINK).click()

    def correct_login(self):
        self.login_page.login(USERNAME, PASSWORD)

    def current_url(self):
        expected_url = self.driver.current_url
        return expected_url


x = MainMagic()
x.start()
x.login_page.login(USERNAME, PASSWORD)

'''x.inventory_page.add_to_cart()
x.inventory_page.go_to_cart()
x.cart_page.get_cart_item_count()'''

print(x.current_url())








