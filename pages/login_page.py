from selenium.webdriver.common.by import By
from utils.base_action import BaseAction


class LoginPage(BaseAction):

    # Locators
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.XPATH, "//button[@type='submit']")
    DASHBOARD_TEXT = (By.XPATH, "//h6[text()='Dashboard']")

    def login(self, username, password):
        self.type_text(self.USERNAME, username)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_dashboard_visible(self):
        return self.get_text(self.DASHBOARD_TEXT) == "Dashboard"