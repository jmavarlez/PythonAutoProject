import pytest
from PythonSeleniumPytest.util import jsonData
from PythonSeleniumPytest.pages.SauceDemo.Login_Page import LoginPage
from PythonSeleniumPytest.pages.SauceDemo.BuyItem_Page import BuyItemPage
import os


class TestSauceDemoBuyItem:

    dataloc = 'PythonSeleniumPytest/data/SauceDemo/BuyItemTestData.json'

    @pytest.fixture(autouse=True)
    def SetUp(self, SetupAndTeardown):
        self.LoginPage = LoginPage(self.driver, self.log)
        self.BuyItemPage = BuyItemPage(self.driver, self.log)
        self.driver.get("https://www.saucedemo.com/")
        self.log.info(os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0])


    def test_BuyItem_TC01_BuySingleItem(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'],testdata['password'])
        result = self.BuyItemPage.click_button_add_to_cart(testdata['item'])
        assert result == True
        result = self.BuyItemPage.verify_shopping_cart_number_of_items(testdata['item'])
        assert result == True
        self.BuyItemPage.click_button_shopping_cart()
        result = self.BuyItemPage.verify_shopping_cart_item_list(testdata['item'])
        assert result == True
        self.BuyItemPage.click_button_checkout()
        self.BuyItemPage.input_buyer_details(testdata['firstname'],testdata['lastname'],testdata['postalcode'])
        self.BuyItemPage.click_button_continue()
        result = self.BuyItemPage.verify_checkout_details(testdata['payment_information'], testdata['shipping_information'], testdata['item_total'], testdata['tax'], testdata['total'])
        assert result == True
        self.BuyItemPage.click_button_finish()
        result = self.BuyItemPage.verify_checkout_message()
        assert result == True


    def test_BuyItem_TC02_BuyMultipleItem(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'],testdata['password'])
        result = self.BuyItemPage.click_button_add_to_cart(testdata['item'])
        assert result == True
        result = self.BuyItemPage.verify_shopping_cart_number_of_items(testdata['item'])
        assert result == True
        self.BuyItemPage.click_button_shopping_cart()
        result = self.BuyItemPage.verify_shopping_cart_item_list(testdata['item'])
        assert result == True
        self.BuyItemPage.click_button_checkout()
        self.BuyItemPage.input_buyer_details(testdata['firstname'],testdata['lastname'],testdata['postalcode'])
        self.BuyItemPage.click_button_continue()
        result = self.BuyItemPage.verify_checkout_details(testdata['payment_information'], testdata['shipping_information'], testdata['item_total'], testdata['tax'], testdata['total'])
        assert result == True
        self.BuyItemPage.click_button_finish()
        result = self.BuyItemPage.verify_checkout_message()
        assert result == True

    def test_BuyItem_TC03_BuyerDetailsMandatory(self):
        testdata = jsonData.jsonData.loaddata(self.dataloc)
        self.LoginPage.SauceDemoLogin(testdata['username'],testdata['password'])
        result = self.BuyItemPage.click_button_add_to_cart(testdata['item'])
        assert result == True
        result = self.BuyItemPage.verify_shopping_cart_number_of_items(testdata['item'])
        assert result == True
        self.BuyItemPage.click_button_shopping_cart()
        result = self.BuyItemPage.verify_shopping_cart_item_list(testdata['item'])
        assert result == True
        self.BuyItemPage.click_button_checkout()
        self.BuyItemPage.input_buyer_firstname(testdata['firstname'])
        self.BuyItemPage.input_buyer_lastname(testdata['lastname'])
        self.BuyItemPage.click_button_continue()
        result = self.BuyItemPage.verify_buyerdetails_error(testdata['postalcodeerr'])
        assert result == True
        self.BuyItemPage.click_button_cancel()
        self.BuyItemPage.click_button_checkout()
        self.BuyItemPage.input_buyer_lastname(testdata['lastname'])
        self.BuyItemPage.input_buyer_postalcode(testdata['postalcode'])
        self.BuyItemPage.click_button_continue()
        result = self.BuyItemPage.verify_buyerdetails_error(testdata['firstnameerr'])
        assert result == True
        self.BuyItemPage.click_button_cancel()
        self.BuyItemPage.click_button_checkout()
        self.BuyItemPage.input_buyer_firstname(testdata['firstname'])
        self.BuyItemPage.input_buyer_postalcode(testdata['postalcode'])
        self.BuyItemPage.click_button_continue()
        result = self.BuyItemPage.verify_buyerdetails_error(testdata['lastnameerr'])
        assert result == True


    def xtest_BuyItem_TC01_BuySingleItem(self):
        pass






