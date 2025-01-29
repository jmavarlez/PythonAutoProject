from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class ElementHandler:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log


    def click(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator).click()
            self.log.info(f"Element: {locator} is clicked.")
        except:
            self.log.error(f"Exception occurred!")


    def input_text(self, locator, text):
        try:
            self.driver.find_element(By.XPATH, locator).send_keys(text)
            self.log.info(f"Element: {locator} is populated with text {text}.")
        except:
            self.log.error(f"Exception occurred!")



    def clear_text(self, locator):
        try:
            self.driver.find_element(By.XPATH, locator).clear()
            self.log.info(f"Element: {locator} is cleared.")
        except:
            self.log.error(f"Exception occurred!")


    def verifyifelementisdisplayed(self, locator):
        element = self.wait_element(locator)
        if element:
            self.log.info(f"Element: {locator}, is displayed.")
            return True
        elif element is None:
            self.log.error(f"Element: {locator}, is NOT displayed.")
            return False


    def verifyifelementisnotdisplayed(self, locator):
        element = self.wait_element(locator)
        if element:
            self.log.error(f"Element: {locator}, is displayed.")
            return False
        elif element is None:
            self.log.info(f"Element: {locator}, is NOT displayed.")
            return True


    def verifytextelement(self, locator, text):
        elementtext = self.get_text_element_using_locator(locator)
        if elementtext == text:
            self.log.info(f"Element: {locator}, Actual and Expected text: '{text}'.")
            return True
        else:
            self.log.error(f"Element: {locator}, Actual: {elementtext}, Expected text: '{text}'.")
            return False


    def verifyspecifictextexists(self, text):
        elements = self.find_elements_with_specific_text(text)
        if len(elements) > 0:
            self.log.info(f"Number of elements with text '{text}': {len(elements)}")
            return True
        else:
            self.log.error(f"There are no elements with text: {text}")
            return False


    def wait_element(self, locator, tout=10, pollfreq=1):
        element = None
        self.driver.implicitly_wait(0)
        try:
            wait = WebDriverWait(self.driver, tout, pollfreq)
            element = wait.until(EX.visibility_of_element_located((By.XPATH, locator)))
        except NoSuchElementException:
            self.log.error(f'{locator} does not exist!')
        except ElementNotVisibleException:
            self.log.error(f'{locator} is not visible!')
        except ElementNotSelectableException:
            self.log.error(f'{locator} is not selectable!')
        except TimeoutException:
            self.log.error(f'{locator} does not exist!')
        self.driver.implicitly_wait(5)
        return element


    def get_element(self, locator):
        return self.driver.find_element(By.XPATH, locator)


    def get_text_element_using_locator(self, locator):
        element = self.wait_element(locator)
        if element:
            self.log.info(f'{locator} has text as {element.text}')
            return element.text
        elif element == None:
            self.log.error(f'{locator} does not exist!')


    def get_text_element(self, element):
        try:
            self.log.info(f'Has text as {element.text}')
            return element.text
        except:
            self.log.error(f'{element} does not exist!')


    def find_elements(self,locator):
        return self.driver.find_elements(By.XPATH, locator)


    def get_element_attribute(self, element, attribute):
        try:
            if isinstance(element, list) == True:
                attributevalues = [ele.get_attribute(attribute) for ele in element]
                self.log.info(f'Attributes {attribute} are {attributevalues}')
                return attributevalues
            else:
                attributevalue = element.get_attribute(attribute)
                self.log.info(f'{element} attribute {attribute} is {attributevalue}')
                return attributevalue
        except NoSuchElementException:
            self.log.error(f'{element} does not exist!')


    def find_elements_with_specific_text(self, text):
        return self.driver.find_elements(By.XPATH, "//*[text()='"+text+"']")


    def iframeaccess(self, iframename):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, iframename))


    def mainframeaccess(self):
        self.driver.switch_to.default_content()