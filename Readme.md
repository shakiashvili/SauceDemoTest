## This project is about testing SauceDemo website using Selenium and Pytest, while Dockerizing and applying Github Actions.
## I have tested the login form with locked and normal user, tested sorting functions and the checkout process for normal users
### Have used a separate test data JSON file for saving login information and messages, then in the conftest file
### I have created a fixture to return test data

### To see allure report - visit: https://shakiashvili.github.io/SauceDemoTest/

## To run it locally, follow the instructions:
### It is highly recommended to have a virtual environment, leaving the code for activation
`python -m venv venv`
`source venv/bin/activate`
### To install all dependencies, use:
`pip install -r requirements.txt`

### To generate Allure Report run:
### `cd tests` go to the test folder 
`pip install allure-pytest`
`pytest --alluredir=allure-results .`
`allure serve allure-results`



