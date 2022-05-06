import allure
from config import logger
from functools import reduce
from selenium import (
    webdriver,
)
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ElementLocator:
    def __init__(self, name: str, locator: str, locator_type = By.XPATH, displayed_text='', attributes = {}):
        self.name = name
        self.value = locator
        self.locator_type = locator_type
        self.displayed_text = displayed_text
        self.attritutes = attributes

    def __iter__(self):
        yield self.locator_type, self.value

    def __repr__(self):
        return f'Name: {self.name} | Locator: By.{self.locator_type}, {self.value}'

    def get_locator(self):
        return self.locator_type, self.value


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self._url_path = ''
        self._mandatory_components = []

    BASE_PATH = 'parabank.parasoft.com'
    PROTOCOL = 'https'

    @property
    def url(self):
        return f'{self.PROTOCOL}://{self.BASE_PATH}/{self._url_path}'

    @property
    def mandatory_components(self):
        return self._mandatory_components

    def check_page_url(self):
        if self.url in self.driver.current_url:
            return True
        raise AssertionError(f'Expected : {self.url} ; Actual : {self.driver.current_url}')

    def click_and_type_text(self, elem: ElementLocator, input):
        input_element = self.driver.find_element(*elem.get_locator())
        if not input_element.is_enabled():
            input_element.click()
        input_element.send_keys(str(input))
        return True

    def click(self, elem: ElementLocator):
        element = self.driver.find_element(*elem.get_locator())
        if element.is_displayed():
            element.click()
            return True
        return False

    def open(self):
        try:
            self.driver.get(url=self.url)
            return True
        except Exception:
            raise

    def validate(self, elem: ElementLocator):
        def logical_and(a, b):
            return a and b

        result = False
        try:
            element = self.driver.find_element(*elem.get_locator())
            result = True
        except NoSuchElementException:
            return False
        if elem.displayed_text:
            result = result and elem.displayed_text == element.text
        if elem.attritutes:
            result = result and \
                     reduce(logical_and, [bool(value in element.get_attribute(name)) for name, value in elem.attritutes.items()])
        logger.info(f"{elem.name} : {result}")
        return result

    def validate_mandatory_components(self, with_wait=False):

        if len(self._mandatory_components) == 0:
            raise NotImplementedError("Mandatory Components not defined for Page {self.__class__}")
        # missing_elements = filter(lambda elem: not(self.validate(elem)), self._mandatory_components)
        missing_elements = [elem for elem in self._mandatory_components if not(self.validate(elem))]
        all_mandatory_component_exists = not bool(missing_elements)

        return all_mandatory_component_exists, missing_elements



