from pages import (
    BasePage,
    ElementLocator,
)
from .sub_pages import (
    SectionHeader,
    SectionLogin,

)
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url_path = "parabank/index.htm"
        self.section_header = SectionHeader(driver)
        self.section_login = SectionLogin(driver)

        # Section Services:
        self.label_atm_services = ElementLocator("Atm Services label", "//li[@class='captionone']",
                                                 displayed_text='ATM Services')

        self._mandatory_components = [
            self.label_atm_services,
            *self.section_header.mandatory_components,
            *self.section_login.mandatory_components,
        ]
