import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--guest")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)

    chrome_options.add_argument("--headless=new")   
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()




@pytest.fixture(scope="session")
def test_data():

    file_path = os.path.join(os.path.dirname(__file__), "..", "data", "testdata.json")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test data file is not found path: {file_path}")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data