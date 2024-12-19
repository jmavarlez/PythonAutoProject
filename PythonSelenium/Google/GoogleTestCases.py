from selenium.webdriver.common.by import By
from PythonSelenium.Setup import LibActions
from Elements import GoogleElements

class GoogleTest:
    def __init__(self):
        self.doact = LibActions.ChromeActions()
        self.driver = self.doact.driver
        self.driver.maximize_window()
        self.elements = GoogleElements.GoogleElement()


    def TC01_1_SignIn(self):
        #Verify that user can sign-in google with valid credentials
        self.doact.openURL("http://www.google.com")
        datalist = self.doact.loaddata('Data/GoogleTC01.json')
        self.doact.clickelement(self.elements.button_googleapps)
        self.doact.iframeaccess(self.elements.iframe_googlehome, self.elements.button_googleapps_gmail,'click')
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


run = GoogleTest()
#run.TC01_1_SignIn()
run.Test()


