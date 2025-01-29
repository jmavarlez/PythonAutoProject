from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import logging

class SetupAndTeardown:
    #DRIVER_INSTANCE = ""

    #def __init__(self):
        #pass

    def Setup(self, url):
        try:
            self.option = webdriver.ChromeOptions()
            self.option.add_argument('--no-sandbox')
            self.option.add_experimental_option('detach', True)
            self.option.add_experimental_option('excludeSwitches', ['enable-logging'])
            '''
            global DRIVER_INSTANCE
            DRIVER_INSTANCE = webdriver.Chrome(service=ChromeService(),options=self.option)
            DRIVER_INSTANCE.maximize_window()
            DRIVER_INSTANCE.implicitly_wait(5)
            '''
            self.driver = webdriver.Chrome(service=ChromeService(), options=self.option)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.get(url)

        except:
            logging.error('Exception Occurred')


    #def openURL(self, url):
        #DRIVER_INSTANCE.get(url)