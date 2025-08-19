from selenium.webdriver.common.by import By 
from .basepage import BasePage


class LoginPage(BasePage):
    """This class is representing login page, locators and methods for signing in"""
    username_locator = (By.ID, "user-name")
    password_locator = (By.ID, "password")
    login_button_locator =(By.ID, "login-button")
    login_error_locator = (By.XPATH, "//*[@data-test='error']")


    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"
        self.driver.get(self.url)

    def login(self, username: str, password: str):
        """It fills the login form with username and passowrd, then it clicks login button"""
        self.write(self.username_locator, username)
        self.write(self.password_locator, password)
        self.click(self.login_button_locator)
    
    def get_login_error(self):
        try:
            error_element = self.find_element(self.login_error_locator)
            return error_element.text
        except Exception as e:
            return None