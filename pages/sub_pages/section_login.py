from pages import (
    BasePage,
    ElementLocator,
)
from selenium.webdriver.common.by import By


class SectionLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.section_title = ElementLocator('Customer Login Label', '//h2[normalize-space()="Customer Login"]', By.XPATH)
        self.label_username = ElementLocator('Username Label', '//form[@name="login"]//b[normalize-space()="Username"]', By.XPATH)
        self.input_username = ElementLocator('Username Text Box', '//form[@name="login"]//input[@name="username"]', By.XPATH)
        self.label_password = ElementLocator('Password Label', '//form[@name="login"]//b[normalize-space()="Password"]', By.XPATH)
        self.input_password = ElementLocator('Password Text Box', '//form[@name="login"]//input[@name="password"]', By.XPATH)
        self.button_login = ElementLocator('Login Button', '//form[@name="login"]//input[@type="submit"]', By.XPATH)
        self.link_register = ElementLocator('Register Link', '//a[normalize-space()="Register"]')

        self._mandatory_components = [
            self.section_title,
            self.label_username,
            self.button_login,
        ]

    def enter_username(self, username):
        return self.click_and_type_text(self.input_username, username)

    def enter_password(self, password):
        return self.click_and_type_text(self.input_password, password)

    def click_login(self):
        return self.click(self.button_login)

    def click_register_account_link(self):
        return self.validate(self.link_register) and self.click(self.link_register)

    def perform_ui_login(self, username, password):
        return (
            self.enter_username(username) and
            self.enter_password(password) and
            self.click_login()
        )
