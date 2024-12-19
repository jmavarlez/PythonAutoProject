import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class ChromeActions:

    def __init__(self):
        os.environ['WDM_SSL_VERIFY'] = '0'
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--no-sandbox')
        #self.option.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.option)
        self.driver.implicitly_wait(10)

    def loaddata(self, data):
        with open(data, 'r') as read:
            return dict(json.load(read))

    def openURL(self, url):
        self.driver.get(url)

    def clickelement(self, element):
        self.driver.find_element(By.XPATH, element).click()

    def inputtext(self, element, text):
        self.driver.find_element(By.XPATH, element).send_keys(text)

    def iframeaccess(self, iframename, element, action):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, iframename))
        self.driver.implicitly_wait(5)
        self.clickelement(element)
        self.driver.switch_to.default_content()

    def selectdropdownoption(self, dropdown, value):
        self.driver.find_element(By.XPATH,dropdown).click()
        option = self.driver.Select(dropdown)


        #self.driver.find_element(text)


    def ActionDoesNotExistError(Exception):
        pass