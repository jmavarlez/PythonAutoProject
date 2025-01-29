from PythonSeleniumPytest.locators.SauceDemo.LoginPageLoc import *
from PythonSeleniumPytest.base.Handlers.ElementHandlers import ElementHandler


class LoginPage(ElementHandler):

    def __init__(self, driver, log):
        super().__init__(driver, log)


    def m_input_username(self, text):
        self.input_text(loginpage_input_username,text)


    def m_input_password(self, text):
        self.input_text(loginpage_input_password, text)


    def click_button_login(self):
        self.click(loginpage_button_login)


    def verify_text_login_error_displayed(self):
        return self.verifyifelementisdisplayed(loginpage_text_login_error)


    def verify_text_locked_error_displayed(self):
        return self.verifyifelementisdisplayed(loginpage_text_login_locked_error)


    def verify_text_login_error_not_displayed(self):
        return self.verifyifelementisnotdisplayed(loginpage_text_login_error)


    def SauceDemoLogin(self, username, password):
        self.m_input_username(username)
        self.m_input_password(password)
        self.click_button_login()