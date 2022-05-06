import allure
from selenium.webdriver import Chrome

@allure.feature("Login")
class TestLogin:
    @allure.testcase(url='',name="Login Successful Check")
    def test_successful_login(self, home_page, account_overview_page,  normal_user):
        with allure.step("Open Home Page"):
            assert home_page.open()
        with allure.step("Verify Home page mandatory components"):
            assert home_page.validate_mandatory_components()
        with allure.step("Submit username and password to login"):
            assert home_page.section_login.perform_ui_login(normal_user.username, 'Incorrect_Password')
        with allure.step("Check user landed on Account Overview Page"):
            assert account_overview_page.check_page_url()
        with allure.step("Verify Account overview page mandatory components"):
            assert account_overview_page.validate_mandatory_components()
