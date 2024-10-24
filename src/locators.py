from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "login-button")
    LOGIN_CONFIRMATION_MSG = None
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")


class InventoryLocators:
    SAUCE_LABS_BACKPACK_TO_CART = (By.NAME, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_ITEM_COUNT = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    # todo: get all items names locators>append to list


class CartLocators:
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPP_BUTTON = (By.ID, "continue-shopping")
    GO_TO_ITEM = None
    # todo: how to use data-test id

