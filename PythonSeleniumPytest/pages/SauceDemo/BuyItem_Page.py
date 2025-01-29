from PythonSeleniumPytest.locators.SauceDemo.BuyItemPageLoc import *
from PythonSeleniumPytest.util.Utilities import Utilities
from PythonSeleniumPytest.base.Handlers.ElementHandlers import ElementHandler


class BuyItemPage(ElementHandler):

    def __init__(self, driver, log):
        super().__init__(driver, log)


    def click_button_add_to_cart(self, items):
        result=[]
        addtocartbuttons = self.find_elements(productspage_button_add_to_cart)
        nameofaddtocartbuttons = self.get_element_attribute(addtocartbuttons, 'name')
        for item in items:
            itemtext = Utilities.replacestring(item, ' ', '-').lower()
            for button in nameofaddtocartbuttons:
                if Utilities.findstring(button, itemtext):
                    self.click(f"//button[@name='{button}']")
                    removebutton = Utilities.replacestring(button,'add-to-cart','remove')
                    if self.verifyifelementisdisplayed(f"//button[@name='{removebutton}']"):
                        result.append(True)
                    else:
                        result.append(False)
                    break
            else:
                result.append(False)
        return all(result)

    def click_button_shopping_cart(self):
        self.click(productspage_button_shopping_cart)

    def click_button_checkout(self):
        self.click(productspage_button_checkout)

    def click_button_continue(self):
        self.click(productspage_button_continue)

    def click_button_finish(self):
        self.click(productspage_button_finish)

    def click_button_cancel(self):
        self.click(productspage_button_cancel)

    def input_buyer_firstname(self, firstname):
        self.input_text(productspage_input_firstname, firstname)

    def input_buyer_lastname(self, lastname):
        self.input_text(productspage_input_lastname, lastname)

    def input_buyer_postalcode(self, postalcode):
        self.input_text(productspage_input_postalcode, postalcode)

    def input_buyer_details(self, firstname, lastname, postalcode):
        self.input_buyer_firstname(firstname)
        self.input_buyer_lastname(lastname)
        self.input_buyer_postalcode(postalcode)

    def clear_buyer_details(self):
        self.clear_text(productspage_input_firstname)
        self.clear_text(productspage_input_lastname)
        self.clear_text(productspage_input_postalcode)

    def verify_buyerdetails_error(self, errmessage):
        errormessage = Utilities.replacestring(productspage_error_buyerdetails,'errmesg',errmessage)
        return self.verifyifelementisdisplayed(errormessage)


    def verify_checkout_details(self, payment, shipping, itemtotal, tax, total):
        result = []
        if self.verifytextelement(productspage_label_payment_information, payment):
            result.append(True)
        else:
            result.append(False)
        if self.verifytextelement(productspage_label_shipping_information, shipping):
            result.append(True)
        else:
            result.append(False)
        if self.verifytextelement(productspage_label_item_total, itemtotal):
            result.append(True)
        else:
            result.append(False)
        if self.verifytextelement(productspage_label_tax, tax):
            result.append(True)
        else:
            result.append(False)
        if self.verifytextelement(productspage_label_total, total):
            result.append(True)
        else:
            result.append(False)
        return all(result)

    def verify_shopping_cart_number_of_items(self, items):
        count = str(len(items))
        return self.verifytextelement(productspage_button_shopping_cart, count)

    def verify_shopping_cart_item_list(self, items):
        result = []
        itemlist = self.find_elements(productspage_list_shopping_cart)
        for item in items:
            for cartitem in itemlist:
                if item == self.get_text_element(cartitem):
                    result.append(True)
                    break
            else:
                result.append(False)
        return all(result)

    def verify_checkout_message(self):
        return self.verifyspecifictextexists('Thank you for your order!')


