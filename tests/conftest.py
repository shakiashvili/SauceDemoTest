import pytest
import json
import os
from selenium import webdriver

from selenium.webdriver.chrome.options import Options




@pytest.fixture(scope="session")
def driver():
    #  Add this while running tests in locally
    # options = Options()
    # options.add_argument("--guest")
    driver = webdriver.Chrome()
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