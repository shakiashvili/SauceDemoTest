import pytest
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def driver():
    options = Options()

    if os.getenv("CI"):  # Running in GitHub Actions
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    else:  # Local run
        options.add_argument("--guest")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def driver():
   
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