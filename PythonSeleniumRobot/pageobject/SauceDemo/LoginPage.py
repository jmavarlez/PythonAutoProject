from PythonSeleniumRobot.keywords.ElementHandler import ElementHandler
from robot.libraries.BuiltIn import BuiltIn

class LoginPage(ElementHandler):

    def __init__(self):
        self.driver = BuiltIn().get_library_instance('SeleniumLibrary').driver
        super().__init__(self.driver)

