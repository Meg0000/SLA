import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Initializes the driver

    def wait_for_element(self, locator):

       element = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(locator)
            )
       return element


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.LoginLocators

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")

        self.wait_for_element(self.locator.USERNAME_LOCATOR)

        self.driver.find_element(*self.locator.USERNAME_LOCATOR).send_keys(username)
        self.driver.find_element(*self.locator.PASSWORD_LOCATOR).send_keys(password)
        self.driver.find_element(*self.locator.LOGIN_BUTTON).click()
        time.sleep(3)


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.InventoryLocators

    def add_to_cart(self):
        self.driver.find_element(*self.locator.BACKPACK_TO_CART).click()

        element = self.wait_for_element(self.locator.INVENTORY_CART_ITEM_COUNT)

        cart_count = element.text
        print("items in cart:", cart_count)

    def go_to_cart(self):
        self.driver.find_element(*self.locator.GO_TO_CART).click()

"""def inventory_items_lst(self):"""
    




class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.CartLocators

    def remove_from_cart(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.locator.REMOVE_BUTTON)
        ).click()

    def get_cart_item_count(self):
        # if element is visible>there are items in cart>print number of items
        # if element not visible>no items in cart> print "0"
        try:
            element = self.driver.find_element(*self.locator.CHECKOUT_CART_ITEM_COUNT)
        except:
            print("element not present: items in cart = 0 ")
        else:
            cart_count = element.text
            print("items in cart:", cart_count)

    def go_to_checkout(self):
        self.wait_for_element(self.locator.CHECKOUT_BUTTON).click()

    def continue_shopping(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.locator.CONTINUE_SHOP_BUTTON)
        ).click()




class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = locators.CheckoutLocators




# todo: cookies for easier login

