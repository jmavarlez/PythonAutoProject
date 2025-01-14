from PythonSeleniumPytest.locators.SauceDemo.LoginPageLoc import *
from PythonSeleniumPytest.base.Handlers import *


class LoginPage:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log

    #ElementInteraction
    def m_input_username(self, text):
        ElementHandlers.ElementHandler.input_text(self,loginpage_input_username,text)

    def m_input_password(self, text):
        ElementHandlers.ElementHandler.input_text(self, loginpage_input_password, text)

    def click_button_login(self):
        ElementHandlers.ElementHandler.click(self,loginpage_button_login)

    def verify_text_login_error_displayed(self):
        return VerifyHandlers.VerifyHandler.verifyifelementisdisplayed(self, loginpage_text_login_error)

    def verify_text_locked_error_displayed(self):
        return VerifyHandlers.VerifyHandler.verifyifelementisdisplayed(self, loginpage_text_login_locked_error)

    def verify_text_login_error_not_displayed(self):
        return VerifyHandlers.VerifyHandler.verifyifelementisnotdisplayed(self, loginpage_text_login_error)


    #CommonActions
    def SauceDemoLogin(self, username, password):
        self.m_input_username(username)
        self.m_input_password(password)
        self.click_button_login()