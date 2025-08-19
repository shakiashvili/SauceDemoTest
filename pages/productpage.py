from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .basepage import BasePage


class ProductPage(BasePage):
   price_locator = (By.XPATH,"//*[@class='inventory_item_price']")
   product_name_locator = (By.XPATH,"//*[contains(@class, 'inventory_item_name')]")
   sort_locator = (By.XPATH,"//*[contains(@class, 'product_sort_container')]")
   """This class is representing products page, I have impelemnted sorting method 
   and getting prices and names of products after sorting
   to cover sorting functioniality"""
   def __init__(self, driver):
       super().__init__(driver)

   def get_product_prices(self):
      """I have stripped the $ sign from the price,converted it to float and make a list of them"""
      price_elements = self.find_elements(self.price_locator)
      prices = [float(price.text.strip("$")) for price in price_elements]        
      return prices
   def get_product_names(self):
      """I have made a list of names of products"""

      name_elements = self.find_elements(self.product_name_locator)
      names = [name.text for name in name_elements]
      return names
   def sort_products(self, sort_option: str):
      """This method sorts products by the option"""
      self.click(self.sort_locator)
      sort_dropdown = Select(self.find_element(self.sort_locator))
      sort_dropdown.select_by_visible_text(sort_option)  
       
