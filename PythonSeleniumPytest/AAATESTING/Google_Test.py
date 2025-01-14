import os
import pytest
from selenium.webdriver.common.by import By
from PythonSeleniumPytest.AAATESTING.Setup import LibActions
from Elements import GoogleElements


class TestSauceDemo:

    def __init__(self):
        self.doact = LibActions.ChromeActions()
        self.driver = self.doact.driver
        self.elements = GoogleElements.GoogleElement()


    def TC01_1_ValidSignIn(self):
        #Verify that user can sign-in google with valid credentials
        self.doact.openURL("http://www.google.com")
        #datalist = self.doact.loaddata('Data/GoogleTC01.json')
        datalist = self.doact.loaddata('PythonSeleniumPytest/AAATESTING/Data/GoogleTC01.json')
        self.doact.clickelement(self.elements.button_googleapps)
        self.doact.iframeaccess(self.elements.iframe_googlehome)
        self.doact.clickelement(self.elements.button_googleapps_gmail)
        self.doact.mainframeaccess()
        self.doact.clickelement(self.elements.button_workspace_signin)


    def Reserve(self):
        self.doact.openURL("https://www.letskodeit.com/practice")
        elelist = list(self.driver.find_elements(By.XPATH,"//table[@id='product']//tr"))
        eledict = {'RowToVerify':['Author ','Course ','Price ']}
        elerow = ''
        for x, ele in enumerate(eledict['RowToVerify']):
            elerow = elerow + eledict['RowToVerify'][x]
        for ele in elelist:
            print (f"{ele.text} vs. {elerow}")
            if ele.text == elerow[:-1]:
                print ("Found It")
                break
        else:
            print ("Not Found")

    def Reserve2(self):
        self.doact.openURL("http://www.google.com")
        elewait = self.doact.waitforelement(self.elements.button_googleapps_gmail)
        #elewait.click()
        self.doact.clickelement(elewait)

    @classmethod
    def StatTest(self):
        print(os.getlogin())

    def Test(self):
        datalist = self.doact.loaddata('Data/GoogleTC01.json')
        print (datalist)



x = TestSauceDemo()
x.Test()
