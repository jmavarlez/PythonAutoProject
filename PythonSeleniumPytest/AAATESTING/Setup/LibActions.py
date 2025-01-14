import os
import json
import time
from selenium import webdriver
#from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class ChromeActions:

    def __init__(self):
        os.environ['WDM_SSL_VERIFY'] = '0'
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--no-sandbox')
        #self.option.add_experimental_option('detach', True)
        self.option.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(service=ChromeService(),options=self.option)
        #self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.parentwindow = self.driver.current_window_handle
        self.windowindex = 0
        self.action = ActionChains(self.driver)


    def loaddata(self, data):
        with open(data, 'r') as read:
            return dict(json.load(read))


    def openURL(self, url):
        self.driver.get(url)


    def clickelement(self, element):
        self.driver.find_element(By.XPATH, element).click()


    def inputtext(self, element, text):
        self.driver.find_element(By.XPATH, element).send_keys(text)


    def iframeaccess(self, iframename):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, iframename))


    def mainframeaccess(self):
        self.driver.switch_to.default_content()


    def selectdropdownoption(self, dropdown, value):
        self.driver.find_element(By.XPATH,dropdown).click()
        option = self.driver.Select(dropdown)


    def takescreenshot(self, savename=str(round(time.time()*1000)), dest = "C:/Users/"+os.getlogin()+"/Desktop/Screenshots/"):
        filename = dest+savename+'.png'
        self.driver.save_screenshot(filename)


    def waitforelement(self, element, tout=20, pollfreq=1, igexcept=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException]):
        wait = WebDriverWait(self.driver,tout,pollfreq,igexcept)
        ele = wait.until(EX.visibility_of_element_located((By.XPATH,element)))
        return ele


    def switchtonewwindow(self):
        allwindows = self.driver.window_handles
        self.windowindex += 1
        try:
            self.driver.switch_to.window(allwindows[self.windowindex])
        except IndexError:
            print(str(self.windowindex+1)+"  is not the number of windows opened.")

    def switchtpreviouswwindow(self):
        self.driver.close()
        allwindows = self.driver.window_handles
        self.windowindex -= 1
        try:
            self.driver.switch_to.window(allwindows[self.windowindex])
        except IndexError:
            print(str(self.windowindex+1)+"  is not the number of windows opened.")

    def switchtoparentwindow(self):
        allwindows = self.driver.window_handles
        while self.windowindex != 0:
            self.driver.switch_to.window(allwindows[self.windowindex])
            self.driver.close()
            self.windowindex -= 1


    def jspopup(self, command='accept'):
        try:
            if command.lower() == 'accept':
                self.driver.switch_to.alert.accept()
            elif command.lower() == 'dismiss':
                self.driver.switch_to.alert.dismiss()
            else:
                raise self.ArgumentDoesNotExistError()
        except self.ArgumentDoesNotExistError():
            print (f"{command} is not a valid. Use 'accept' or 'dismiss' only")


    def mousehover(self, element):
        elem = self.driver.find_element(By.XPATH,element)
        self.action.move_to_element(elem).perform()


    def draganddrop(self, fromelement, toelement):
        felem = self.driver.find_element(By.XPATH,fromelement)
        telem = self.driver.find_element(By.XPATH, toelement)
        self.action.drag_and_drop(felem,telem).perform()
        #self.action.click_and_hold(felem).move_to_element(telem).release().perform() same as line above


    def dragslider(self, element, x, y):
        elem = self.driver.find_element(By.XPATH, element)
        self.action.drag_and_drop_by_offset(elem, x, y).perform()


    def ArgumentDoesNotExistError(Exception):
        pass



