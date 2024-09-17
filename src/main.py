from selenium import webdriver
import unittest
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com/")


#CONSTANTS
PASSWORD = "secret_sauce"
USERNAME = "standard_user"
# should add correct usernames as csv?

