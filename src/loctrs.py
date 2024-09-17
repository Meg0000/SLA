from selenium.webdriver.common.by import By


class LoginLoc:

    USERNAME = (By.NAME, "user-name")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "login-button")
    LOGIN_CONFIRMATION = None

