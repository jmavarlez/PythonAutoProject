import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from PythonSeleniumPytest.util.CustomExceptions import *

class SeleniumWebDriverInit:

    def DriverSetup(self, browser):
        try:
            if browser == 'chrome':
                self.option = webdriver.ChromeOptions()
                self.option.add_argument('--no-sandbox')
                #self.option.add_experimental_option('detach', True)
                self.option.add_experimental_option('excludeSwitches', ['enable-logging'])
                self.driver = webdriver.Chrome(service=ChromeService(),options=self.option)
                self.driver.maximize_window()
                self.driver.implicitly_wait(5)

            else:
                raise NotAValidBrowser
            return self.driver

        except NotAValidBrowser:
            print('Not a valid browser')
            raise

