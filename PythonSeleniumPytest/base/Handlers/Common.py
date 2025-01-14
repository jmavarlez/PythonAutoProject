from selenium.webdriver.support import expected_conditions as EX
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

class CommonMethods:

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
        element = CommonMethods.wait_element(self, locator)
        if element:
            return element.text
        elif element == None:
            self.log.error(f'{locator} does not exist!')


    def get_text_element(self, element):
        try:
            return element.text
        except:
            self.log.error(f'{locator} does not exist!')


    def find_elements(self,locator):
        return self.driver.find_elements(By.XPATH, locator)


    def get_attribute(self, element, attribute):
        try:
            if isinstance(element, list) == True:
                attributevalues = [ele.get_attribute(attribute) for ele in element]
                return attributevalues
            else:
                attributevalue = element.get_attribute(attribute)
                return attributevalue
        except NoSuchElementException:
            self.log.error(f'{locator} does not exist!')

    def find_elements_with_specific_text(self, text):
        return self.driver.find_elements(By.XPATH, "//*[text()='"+text+"']")