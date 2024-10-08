from selenium.webdriver.common.by import By


class LoginLoc:

    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "login-button")
    LOGIN_CONFIRMATION_MSG = None
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")


class InventoryLoc:

    SAUCE_LABS_BACKPACK_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHOPPING_CART_ITEM_COUNT = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')


