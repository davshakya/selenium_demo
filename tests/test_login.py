from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    # Perform Login
    login_page.login("Admin", "admin123")

    # Validate Dashboard
    driver.implicitly_wait(10)
    assert login_page.is_dashboard_visible()