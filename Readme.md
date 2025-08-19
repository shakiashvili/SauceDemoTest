## This project is about testing SauceDemo website using Selenium and Pytest,while Dockerizing and applying Github Actions.
## I have tested login form with locked and normal user, tested sorting functions and checkout process for normal users
### Have used seperate test data json file for saving login infromation and messages,Then in conftest file
### I have created fixture to return test data
 
### It is highly recommended to have virtual envirnonment,leaving code for activation
`python -m venv venv`
`source venv/bin/activate`
### To install all dependencies use:
`pip install -r requirements.txt`

### To generete Allure Report run:
### `cd tests` go to test folder 
`pip install allure-pytest`
`pytest --alluredir=allure-results .`

`allure serve allure-results`

