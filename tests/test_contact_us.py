import allure

@allure.feature("Contact Us")
class TestContactUs:

    @allure.testcase(url='', name="Send Message to Customer Care")
    def test_send_cc_message(self, contact_us_page, cc_message):
        with allure.step("Open Contact Us Page"):
            assert contact_us_page.open()
        with allure.step("Validate Mandatory Components on Contact Us page"):
            assert contact_us_page.validate_mandatory_components()
        with allure.step("Submit Customer Care Feedback Form"):
            assert contact_us_page.submit_customer_care_form(cc_message)
        with allure.step("Verify success message"):
            assert contact_us_page.validate_success_message(cc_message)
