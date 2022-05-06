from pages import (
    BasePage,
    ElementLocator,
)
from .sub_pages import (
    SectionHeader,
    SectionLogin,

)


class AccountOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url_path = "parabank/overview.htm"
        self.section_header = SectionHeader(driver)
        self.section_login = SectionLogin(driver)

        # Section Services:
        self.label_accounts_overview = ElementLocator("Account Overview label", "//h1[@class='title']",
                                                      displayed_text='Accounts Overview')

        self._mandatory_components = [
            self.label_accounts_overview,
            *self.section_header.mandatory_components,
            *self.section_login.mandatory_components,
        ]
