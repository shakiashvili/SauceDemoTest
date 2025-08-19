from selenium.webdriver.common.by import By
from .basepage import BasePage


class CheckoutPage(BasePage):
    """This class represent checkout page, locators and methods for checkouting products"""
    add_cart_locator = (By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']")
    cart_icon_locator = (By.XPATH, "//*[@class='shopping_cart_link']")
    checkout_button_locator = (By.ID, "checkout")
    first_name_locator = (By.ID, "first-name")
    last_name_locator = (By.ID, "last-name")
    postal_code_locator = (By.ID, "postal-code")
    continue_button_locator = (By.ID, "continue")
    finish_button_locator = (By.ID, "finish")
    complete_header_locator = (By.XPATH, "//*[@class='complete-header']")
    summary_total_label = (By.XPATH, "//*[@class='summary_total_label']")

    def __init__(self, driver):
        super().__init__(driver)


    def checkout(self, first_name: str, last_name:str, postal_code: str):

        """It adds product to cart, navigates to it, then fills out all fields, get the total price and finishes the checkout process"""
        self.click(self.add_cart_locator)
        self.click(self.cart_icon_locator)
        self.click(self.checkout_button_locator)
        self.write(self.first_name_locator, first_name)
        self.write(self.last_name_locator, last_name)
        self.write(self.postal_code_locator, postal_code)
        self.click(self.continue_button_locator)
        total_price = self.find_element(self.summary_total_label).text
        self.click(self.finish_button_locator)
        return total_price


    def get_completion_message(self):
        try:
            completion_element = self.find_element(self.complete_header_locator)
            return completion_element.text
        except Exception as e:
            return e

