from selenium import webdriver
from selenium.webdriver.common.by import By
import SetupAndTeardown
import logging
from robot.libraries.BuiltIn import BuiltIn

class ElementHandler:

    def __init__(self, driver):
        self.driver = driver


    def input_text(self, locator, text):
        logging.info (self.driver)
        try:
            self.driver.find_element(By.XPATH, locator).send_keys(text)
            logging.info(f"Element: {locator} is populated with text {text}.")
        except:
            logging.error(f"Exception occurred!")
            raise


    def click(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator).click()
            self.log.info(f"Element: {locator} is clicked.")
        except:
            self.log.error(f"Exception occurred!")
