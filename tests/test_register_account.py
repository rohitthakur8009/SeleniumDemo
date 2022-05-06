import allure
from selenium.webdriver import Chrome

@allure.feature("Sign Up")
class TestRegisterAccount:

    @allure.testcase(url='', name="Login Successful Check")
    def test_successful_registration(self, home_page, register_page, registration_success_page, new_user):
        with allure.step("Open Home Page"):
            assert home_page.open()
        with allure.step("Verify Home page mandatory components"):
            assert home_page.validate_mandatory_components()
        with allure.step("Click Register Account Link"):
            assert home_page.section_login.click_register_account_link()
        with allure.step("Check User redirected to Register Page"):
            assert register_page.check_page_url()
        with allure.step("Verify Register page mandatory components"):
            assert register_page.validate_mandatory_components()
        with allure.step("Submit registration form with new user data"):
            assert register_page.submit_register_account_form(new_user)
        with allure.step("Verify Register Success page mandatory components"):
            assert registration_success_page.validate_mandatory_components()
            assert registration_success_page.validate_username(new_user.username)

