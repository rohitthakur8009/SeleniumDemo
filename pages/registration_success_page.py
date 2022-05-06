from pages import (
    BasePage,
    ElementLocator,
)
from .sub_pages import (
    SectionHeader,
    SectionLogin,

)
from selenium.webdriver.common.by import By


class RegistrationSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url_path = "parabank/register.htm"
        self.section_header = SectionHeader(driver)
        self.section_login = SectionLogin(driver)

        # Section Services:
        self.label_welcome_user = ElementLocator("Welcome user label", "//h1[@class='title']")

        registration_success_text = "Your account was created successfully. You are now logged in."
        self.label_registration_success_info = \
            ElementLocator("Registration success text",
                           "//div[@id='rightPanel']/p[contains(text(), 'Your account was created')]",
                           displayed_text=registration_success_text
                           )

        self._mandatory_components = [
            self.label_welcome_user,
            self.label_registration_success_info,
            *self.section_header.mandatory_components,
            *self.section_login.mandatory_components,
        ]

    def validate_username(self, username):
        welcome_element = self.driver.find_element(*self.label_welcome_user.get_locator())
        return username == welcome_element.text.split(' ')[1]
