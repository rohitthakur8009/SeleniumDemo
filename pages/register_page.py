from pages import (
    BasePage,
    ElementLocator,
)
from .sub_pages import (
    SectionHeader,
    SectionLogin,

)
from config import logger
from data.models import Account
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url_path = "parabank/register.htm"
        self.section_header = SectionHeader(driver)
        self.section_login = SectionLogin(driver)

        self.label_signup_heading = ElementLocator("Sign Up Heading label", "//h1[@class='title']",
                                                   displayed_text="Signing up is easy!")
        sign_up_info_text = "If you have an account with us you can sign-up for free instant online access. " \
                            "You will have to provide some personal information."
        self.label_signup_info_text = ElementLocator("Sign Up Info text", "//div[@id='rightPanel']//p[1]",
                                                     displayed_text=sign_up_info_text)

        form_section_locator = "//form[@id='customerForm']"
        # Form Elements:

        self.label_first_name = ElementLocator("First Name Label", form_section_locator + "//tbody/tr[1]/td[1]/b",
                                               displayed_text="First Name:")
        self.input_first_name = ElementLocator("First Name Input",
                                               form_section_locator + "//input[@id='customer.firstName']")

        self.label_last_name = ElementLocator("Last Name Label", form_section_locator + "//tbody/tr[2]/td[1]/b",
                                              displayed_text="Last Name:")
        self.input_last_name = ElementLocator("Last Name Input",
                                              form_section_locator + "//input[@id='customer.lastName']")

        self.label_address = ElementLocator("Address Label", form_section_locator + "//tbody/tr[3]/td[1]/b",
                                            displayed_text="Address:")
        self.input_address_street = ElementLocator("Address Input",
                                                   form_section_locator + "//input[@id='customer.address.street']")

        self.label_city = ElementLocator("City Label", form_section_locator + "//tbody/tr[4]/td[1]/b",
                                         displayed_text="City:")
        self.input_city = ElementLocator("City Input",
                                         form_section_locator + "//input[@id='customer.address.city']")

        self.label_state = ElementLocator("State Label", form_section_locator + "//tbody/tr[5]/td[1]/b",
                                          displayed_text="State:")
        self.input_state = ElementLocator("State Input",
                                          form_section_locator + "//input[@id='customer.address.state']")

        self.label_zipcode = ElementLocator("State Label", form_section_locator + "//tbody/tr[6]/td[1]/b",
                                            displayed_text="Zip Code:")
        self.input_zipcode = ElementLocator("State Input",
                                            form_section_locator + "//input[@id='customer.address.zipCode']")

        self.label_phone_number = ElementLocator("Phone # Label", form_section_locator + "//tbody/tr[7]/td[1]/b",
                                                 displayed_text="Phone #:")
        self.input_phone_number = ElementLocator("State Input",
                                                 form_section_locator + "//input[@id='customer.phoneNumber']")

        self.label_ssn = ElementLocator("SSN Label", form_section_locator + "//tbody/tr[8]/td[1]/b",
                                                 displayed_text="SSN:")
        self.input_ssn = ElementLocator("SSN Input",
                                                 form_section_locator + "//input[@id='customer.ssn']")

        self.label_username = ElementLocator("Username Label", form_section_locator + "//tbody/tr[10]/td[1]/b",
                                        displayed_text="Username:")
        self.input_username = ElementLocator("Username Input",
                                        form_section_locator + "//input[@id='customer.username']")

        self.label_password = ElementLocator("Password Label", form_section_locator + "//tbody/tr[11]/td[1]/b",
                                        displayed_text="Password:")
        self.input_password = ElementLocator("Password Input",
                                        form_section_locator + "//input[@id='customer.password']")

        self.label_password_confirm = ElementLocator("Password Confirm Label", form_section_locator + "//tbody/tr[11]/td[1]/b",
                                        displayed_text="Confirm:")
        self.input_password_confirm = ElementLocator("Password Confirm Input",
                                        form_section_locator + "//input[@id='repeatedPassword']")

        self.button_register = ElementLocator("Register Button", form_section_locator + "//input[@value='Register']")

        self._mandatory_components = [
            self.label_signup_heading,
            self.input_first_name,
            self.button_register,
            *self.section_header.mandatory_components,
            *self.section_login.mandatory_components,
        ]

    def submit_register_account_form(self, account: Account):
        inputs = [
            (self.input_first_name, account.first_name),
            (self.input_last_name, account.last_name),
            (self.input_address_street, account.address.address_street),
            (self.input_city, account.address.city),
            (self.input_state, account.address.state),
            (self.input_zipcode, account.address.zipcode),
            (self.input_phone_number, account.phone_no),
            (self.input_ssn, account.ssn),
            (self.input_username, account.username),
            (self.input_password, account.password),
            (self.input_password_confirm, account.password)
         ]
        for input in inputs:
            try:
                self.click_and_type_text(*input)
            except Exception:
                logger.error(f'Error Inputting {input[0].name}')
                raise

        return self.click(self.button_register)
