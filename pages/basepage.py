
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)
        """Intantiation of the BasePage class, with WebDriver instance, optional URL and WebDriver explicit wait"""


    def find_element(self,locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))
    
    
    def find_elements(self, locator: tuple) -> List[WebElement]:
         return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def click(self, locator: tuple):
        element = self.find_element(locator)
        element.click()

    def write(self, locator: tuple, text: str):
        element = self.find_element(locator)
        element.send_keys(text)