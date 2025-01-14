import pytest
from PythonSeleniumPytest.util import *
from PythonSeleniumPytest.pages.SauceDemo import Login_Page


pytest.mark.usefixtures("SetupAndTeardown")
class TestSauceDemoLogin:

    dataloc = 'PythonSeleniumPytest/data/SauceDemo/LoginTestData.json'

    @pytest.fixture(autouse=True)
    def SetUp(self, SetupAndTeardown):
        self.LoginPage = Login_Page.LoginPage(self.driver,self.log)
        self.driver.get("https://www.saucedemo.com/")
        self.log.info(os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])


    def test_Login_TC01_Valid(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'],testdata['password'])
        result = self.LoginPage.verify_text_login_error_not_displayed()
        assert result == True


    def test_Login_TC02_InvalidPassword(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'], testdata['password'])
        result = self.LoginPage.verify_text_login_error_displayed()
        assert result == True


    def test_Login_TC03_InvalidUsername(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'], testdata['password'])
        result = self.LoginPage.verify_text_login_error_displayed()
        assert result == True


    def test_Login_TC04_LockedUser(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'], testdata['password'])
        result = self.LoginPage.verify_text_locked_error_displayed()
        assert result == True


    def xtest(self):
        print(self.dataloc)








