from pages import (
    BasePage,
    ElementLocator,
)
from .sub_pages import (
    SectionHeader,
    SectionLogin,

)
from config import logger
from data.models import CCMessage
from selenium.webdriver.common.by import By


class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._url_path = "parabank/contact.htm"
        self.section_header = SectionHeader(driver)
        self.section_login = SectionLogin(driver)

        self.label_customer_care_heading = ElementLocator("Sign Up Heading label", "//h1[@class='title']",
                                                          displayed_text="Customer Care")
        email_support_text = "Email support is available by filling out the following form."
        self.label_email_support_info = ElementLocator("Sign Up Info text", "//div[@id='rightPanel']//p[1]",
                                                       displayed_text=email_support_text)

        form_section_locator = "//form[@id='contactForm']"
        # Form Elements:

        self.label_name = ElementLocator("Name Label", form_section_locator + "//tbody/tr[1]/td[1]/b",
                                         displayed_text="Name:")
        self.input_name = ElementLocator("Name Input",
                                         form_section_locator + "//input[@id='name']")

        self.label_email = ElementLocator("Email Label", form_section_locator + "//tbody/tr[2]/td[1]/b",
                                          displayed_text="Email:")
        self.input_email = ElementLocator("Email Input",
                                          form_section_locator + "//input[@id='email']")

        self.label_phone_number = ElementLocator("Phone Label", form_section_locator + "//tbody/tr[3]/td[1]/b",
                                                 displayed_text="Phone:")
        self.input_phone_number = ElementLocator("Phone Input",
                                                 form_section_locator + "//input[@id='phone']")

        self.label_message = ElementLocator('Message Label', form_section_locator + "//tbody/tr[4]/td[1]/b",
                                            displayed_text="Message:")
        self.input_message = ElementLocator("Message Input",
                                            form_section_locator + "//textarea[@id='message']")

        self.button_send_to_cc = ElementLocator("Send to CC Button",
                                                form_section_locator + "//input[@value='Send to Customer Care']")

        self.label_thank_you = ElementLocator("Thank you label", "//div[@id='rightPanel']/p[contains(text(), 'Thank you')]")

        cc_info_text = "A Customer Care Representative will be contacting you."
        self.label_cc_info = ElementLocator("CC info text",
                                              f"//div[@id='rightPanel']/p[contains(text(), '{cc_info_text}')]")

        self._mandatory_components = [
            self.label_customer_care_heading,
            self.label_email_support_info,
            self.label_name,
            self.button_send_to_cc,
            *self.section_header.mandatory_components,
            *self.section_login.mandatory_components,
        ]

    def submit_customer_care_form(self, cc_message: CCMessage):
        inputs = [
            (self.input_name, cc_message.name),
            (self.input_email, cc_message.email),
            (self.input_phone_number, cc_message.phone),
            (self.input_message, cc_message.message),
        ]
        for input in inputs:
            try:
                self.click_and_type_text(*input)
            except Exception:
                logger.error(f'Error Inputting {input[0].name}')
                raise

        return self.click(self.button_send_to_cc)

    def validate_success_message(self, cc_message: CCMessage):
        self.label_thank_you.displayed_text = f'Thank you {cc_message.name}'
        return self.validate(self.label_thank_you) and self.validate(self.label_cc_info)

