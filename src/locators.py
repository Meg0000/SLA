from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME_LOCATOR = (By.NAME, "user-name")
    PASSWORD_LOCATOR = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "login-button")
    LOGIN_CONFIRMATION_MSG = None
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")


class InventoryLocators:
    BACKPACK_TO_CART = (By.NAME, "add-to-cart-sauce-labs-backpack")
    INVENTORY_CART_ITEM_COUNT = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    BIKE_LIGHT_LINK = (By.XPATH, "//div[normalize-space()='Sauce Labs Bike Light']")
    GO_TO_CART = (By.XPATH, "//a[@class=\'shopping_cart_link\']")



class CartLocators:
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOP_BUTTON = (By.ID, "continue-shopping")
    GO_TO_ITEM = None
    CHECKOUT_CART_ITEM_COUNT = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')


class CheckoutLocators:
    CONTINUE_SHOP_BUTTON = (By.ID,"continue-shopping")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    GO_TO_ITEM_PAGE = (By.XPATH, "//div[@class=\'inventory_item_name\']")


