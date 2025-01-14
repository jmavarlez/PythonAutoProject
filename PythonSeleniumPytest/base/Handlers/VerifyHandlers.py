from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.wait import WebDriverWait
from PythonSeleniumPytest.base.Handlers.Common import CommonMethods


class VerifyHandler:

    def verifyifelementisdisplayed(self, locator):
        element = CommonMethods.wait_element(self, locator)
        if element:
            self.log.info(f"Element: {locator}, is displayed.")
            return True
        elif element is None:
            self.log.error(f"Element: {locator}, is NOT displayed.")
            return False


    def verifyifelementisnotdisplayed(self, locator):
        element = CommonMethods.wait_element(self, locator)
        if element:
            self.log.error(f"Element: {locator}, is displayed.")
            return False
        elif element is None:
            self.log.info(f"Element: {locator}, is NOT displayed.")
            return True


    def verifytextelement(self, locator, text):
        elementtext = CommonMethods.get_text_element_using_locator(self, locator)
        if elementtext == text:
            self.log.info(f"Element: {locator}, Actual and Expected text: '{text}'.")
            return True
        else:
            self.log.error(f"Element: {locator}, Actual: {elementtext}, Expected text: '{text}'.")
            return False

    def verifyspecifictextexists(self, text):
        elements = CommonMethods.find_elements_with_specific_text(self, text)
        if len(elements) > 0:
            self.log.info(f"Number of elements with text '{text}': {len(elements)}")
            return True
        else:
            self.log.error(f"There are no elements with text: {text}")
            return False

    #def verifymultipleelementsaredisplayed(self, elementlist):
        #for element in elementlist:

            #element = CommonMethods.wait_element(self, element)

