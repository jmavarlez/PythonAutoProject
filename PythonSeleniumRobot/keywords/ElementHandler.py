from selenium import webdriver
from selenium.webdriver.common.by import By
import SetupAndTeardown
import logging

class ElementHandler:
    def input_text(self, locator, text):
        logging.info (SetupAndTeardown.DRIVER_INSTANCE)
        try:
            SetupAndTeardown.DRIVER_INSTANCE.find_element(By.XPATH, locator).send_keys(text)
            logging.info(f"Element: {locator} is populated with text {text}.")
        except:
            logging.error(f"Exception occurred!")
            raise