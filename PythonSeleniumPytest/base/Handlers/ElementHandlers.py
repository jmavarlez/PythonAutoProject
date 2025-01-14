from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from PythonSeleniumPytest.base.Handlers.Common import CommonMethods

class ElementHandler:


    def click(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator).click()
            self.log.info(f"Element: {locator} is clicked.")
        except:
            self.log.error(f"Exception occurred!")


    def input_text(self, locator, text):
        try:
            self.driver.find_element(By.XPATH, locator).send_keys(text)
            self.log.info(f"Element: {locator} is populated with text {text}.")
        except:
            self.log.error(f"Exception occurred!")



    def clear_text(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator).clear()
            self.log.info(f"Element: {locator} is cleared.")
        except:
            self.log.error(f"Exception occurred!")




