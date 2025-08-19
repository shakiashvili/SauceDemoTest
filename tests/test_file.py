# Test the names of choosen elements 
# and the methods click, write, sort
import pytest
from selenium.webdriver.common.alert import Alert

from pages.loginpage import LoginPage
from pages.productpage import ProductPage
from pages.checkoutpage import CheckoutPage


def test_login_page(test_data, driver):
    login_page = LoginPage(driver)
    login_page.login(test_data['login']['valid_user']['username'], test_data['login']['valid_user']['password'])
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed, URL did not change to inventory page"


def test_sorting_products_by_name(driver):
    """Testing sorting by price A To Z"""

    product_page = ProductPage(driver)
    name_list = product_page.get_product_names()
    product_page.sort_products("Name (A to Z)")
    sorted_names = product_page.get_product_names()
    assert sorted(name_list) == sorted_names, "Products are not sorted by name correctly"

def test_sorting_products_by_name_reversed(driver):
    """Testing sorting by price Z to A"""
    product_page = ProductPage(driver)
    name_list = product_page.get_product_names()
    product_page.sort_products("Name (Z to A)")
    sorted_names = product_page.get_product_names()
    assert sorted(name_list, reverse=True) == sorted_names, "Products are not sorted by name correctly"

def test_sorting_products_by_price_low_to_high(driver):
    """Testing sorting by price low to high"""
    product_page = ProductPage(driver)
    price_list = product_page.get_product_prices()
    product_page.sort_products("Price (low to high)")
    sorted_prices = product_page.get_product_prices()
    assert sorted(price_list) == sorted_prices, "Products are not sorted by price correctly"

def test_sorting_products_by_price_high_to_low(driver):
    """Testing sorting by price high to low"""
    product_page = ProductPage(driver)
    price_list = product_page.get_product_prices()
    product_page.sort_products("Price (high to low)")
    sorted_prices = product_page.get_product_prices()
    assert sorted(price_list, reverse=True) == sorted_prices, "Products are not sorted by price correctly"


def test_checkout_process(test_data, driver):
    """Testing whole checkout process and assert price is included in text e.g('total $15.29')"""
    checkout_page = CheckoutPage(driver)
    price  = checkout_page.checkout(test_data['checkout_user']['shipping_info']['first_name'],
                           test_data['checkout_user']['shipping_info']['last_name'],
                           test_data['checkout_user']['shipping_info']['postal_code'])
    assert '32.39' in price, "Total price does not match with expected one"
    completion_message = checkout_page.get_completion_message()
    assert completion_message == test_data['completion_message'], 'Completion message is not correct'
