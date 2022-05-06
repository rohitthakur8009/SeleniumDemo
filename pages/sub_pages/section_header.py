from pages import (
    BasePage,
    ElementLocator,
)
from selenium.webdriver.common.by import By


class SectionHeader(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.image_logo = ElementLocator('Parabank Logo Image', '//img[@title="ParaBank"]',
                                         attributes={'src': '/parabank/images/logo.gif'})
        self.label_caption = ElementLocator('Caption Text on Header', '//p[@class="caption"]',
                                            displayed_text="Experience the difference")

        self._mandatory_components = [
            self.image_logo,
            self.label_caption,
        ]
