from PythonSeleniumPytest.base.Handlers.Common import CommonMethods
from PythonSeleniumPytest.locators.SauceDemo.BuyItemPageLoc import *
from PythonSeleniumPytest.util import *
from PythonSeleniumPytest.base.Handlers import *


class BuyItemPage():

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log


    #ElementInteraction
    def click_button_add_to_cart(self, items):
        result=[]
        addtocartbuttons = CommonMethods.find_elements(self, productspage_button_add_to_cart)
        nameofaddtocartbuttons = CommonMethods.get_attribute(self, addtocartbuttons, 'name')
        for item in items:
            itemtext = Utilities.Utilities.replacestring(item, ' ', '-').lower()
            for button in nameofaddtocartbuttons:
                if Utilities.Utilities.findstring(button, itemtext):
                    ElementHandlers.ElementHandler.click(self, f"//button[@name='{button}']")
                    removebutton = Utilities.Utilities.replacestring(button,'add-to-cart','remove')
                    if VerifyHandlers.VerifyHandler.verifyifelementisdisplayed(self,f"//button[@name='{removebutton}']"):
                        result.append(True)
                    else:
                        result.append(False)
                    break
            else:
                result.append(False)
        return all(result)

    def click_button_shopping_cart(self):
        ElementHandlers.ElementHandler.click(self, productspage_button_shopping_cart)

    def click_button_checkout(self):
        ElementHandlers.ElementHandler.click(self,productspage_button_checkout)

    def click_button_continue(self):
        ElementHandlers.ElementHandler.click(self,productspage_button_continue)

    def click_button_finish(self):
        ElementHandlers.ElementHandler.click(self,productspage_button_finish)

    def click_button_cancel(self):
        ElementHandlers.ElementHandler.click(self,productspage_button_cancel)

    def input_buyer_firstname(self, firstname):
        ElementHandlers.ElementHandler.input_text(self, productspage_input_firstname, firstname)

    def input_buyer_lastname(self, lastname):
        ElementHandlers.ElementHandler.input_text(self, productspage_input_lastname, lastname)

    def input_buyer_postalcode(self, postalcode):
        ElementHandlers.ElementHandler.input_text(self, productspage_input_postalcode, postalcode)

    def input_buyer_details(self, firstname, lastname, postalcode):
        self.input_buyer_firstname(firstname)
        self.input_buyer_lastname(lastname)
        self.input_buyer_postalcode(postalcode)

    def clear_buyer_details(self):
        ElementHandlers.ElementHandler.clear_text(self, productspage_input_firstname)
        ElementHandlers.ElementHandler.clear_text(self, productspage_input_lastname)
        ElementHandlers.ElementHandler.clear_text(self, productspage_input_postalcode)

    def verify_buyerdetails_error(self, errmessage):
        errormessage = Utilities.Utilities.replacestring(productspage_error_buyerdetails,'errmesg',errmessage)
        return VerifyHandlers.VerifyHandler.verifyifelementisdisplayed(self, errormessage)


    def verify_checkout_details(self, payment, shipping, itemtotal, tax, total):
        result = []
        if VerifyHandlers.VerifyHandler.verifytextelement(self, productspage_label_payment_information, payment):
            result.append(True)
        else:
            result.append(False)
        if VerifyHandlers.VerifyHandler.verifytextelement(self, productspage_label_shipping_information, shipping):
            result.append(True)
        else:
            result.append(False)
        if VerifyHandlers.VerifyHandler.verifytextelement(self, productspage_label_item_total, itemtotal):
            result.append(True)
        else:
            result.append(False)
        if VerifyHandlers.VerifyHandler.verifytextelement(self, productspage_label_tax, tax):
            result.append(True)
        else:
            result.append(False)
        if VerifyHandlers.VerifyHandler.verifytextelement(self, productspage_label_total, total):
            result.append(True)
        else:
            result.append(False)
        return all(result)

    def verify_shopping_cart_number_of_items(self, items):
        count = str(len(items))
        return VerifyHandlers.VerifyHandler.verifytextelement(self, productspage_button_shopping_cart, count)

    def verify_shopping_cart_item_list(self, items):
        result = []
        itemlist = CommonMethods.find_elements(self, productspage_list_shopping_cart)
        for item in items:
            for cartitem in itemlist:
                if item == CommonMethods.get_text_element(self,cartitem):
                    result.append(True)
                    break
            else:
                result.append(False)
        return all(result)

    def verify_checkout_message(self):
        return VerifyHandlers.VerifyHandler.verifyspecifictextexists(self, 'Thank you for your order!')


