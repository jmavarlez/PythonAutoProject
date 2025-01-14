from selenium.common import NoSuchElementException
from PythonSeleniumPytest.base.Handlers import *


class MainHandler:

    def __init__(self, driver):
        self.driver = driver


    def clickbutton(self, locator):
        EH = ElementHandlers.ElementHandler(self.driver)
        EH.click(locator)


    def inputtext(self, locator, text):
        EH = ElementHandlers.ElementHandler(self.driver)
        EH.input_text(locator, text)


    def waitelement(self, locator):
        EH = ElementHandlers.ElementHandler(self.driver)
        element = EH.wait_element(locator)
        if element:
            return element
        elif element is None:
            raise NoSuchElementException


    def findelements(self, locator):
        EH = ElementHandlers.ElementHandler(self.driver)
        elelist = EH.find_elements(locator)
        return elelist


    def getelementinlistofelements(self, locator, key, attribute):
        listofelements = self.findelements(locator)
        key = Utilities.Utilities.removechar(key, ' ').lower()
        for element in listofelements:
            nameofelement = self.getattribute(element, attribute)
            nameofelement = Utilities.Utilities.removechar(nameofelement, '-').lower()
            key = Utilities.Utilities.findstring(nameofelement, key)
            if key == True:
                self.clickbutton(f"//button[@name='{nameofelement}']")
                break
            else:
                pass
        else:
            print("Item is not found!")


    def getattribute(self, element, attribute):
        EH = ElementHandlers.ElementHandler(self.driver)
        return EH.get_attribute(element,attribute)


    def verifyifelementisdisplayed(self, locator):
        EH = ElementHandlers.ElementHandler(self.driver)
        element = EH.wait_element(locator)
        if element:
            return True
        elif element is None:
            return False


    def verifyifelementisnotdisplayed(self, locator):
        EH = ElementHandlers.ElementHandler(self.driver)
        element = EH.wait_element(locator)
        if element:
            return False
        elif element is None:
            return True


    def test(self):
        strings = 'test'
        ElementHandlers.ElementHandler.testinside(strings)