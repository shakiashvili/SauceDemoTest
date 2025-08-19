from pages.loginpage import LoginPage


def test_login_page_invalid_user(test_data, driver):
    """Testing locked user login and an error message"""
    login_page = LoginPage(driver)
    login_page.login(test_data['login']['invalid_user']['username'], test_data['login']['valid_user']['password'])
    error_message = login_page.get_login_error()
    assert error_message == test_data['error_message']