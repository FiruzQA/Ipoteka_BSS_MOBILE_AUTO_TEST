import time
from pages.login_page import LoginPage


class TestElements:
    class TestPage:
        def test_between_uzcard_salary_to_uzcard_other(self, mobile_driver):
            test_transfer = LoginPage(mobile_driver)
            test_transfer.login_page()
            test_transfer.choose_sender('uzcard_salary')
            test_transfer.taker_cards('uzcard_kapital')
            time.sleep(10)

        def test_between_uzcard_salary_uzcard_cobage(self, mobile_driver):
            test_transfer = LoginPage(mobile_driver)
            test_transfer.login_page()
            test_transfer.choose_sender('uzcard_salary')
            test_transfer.taker_cards('uzcard_cobage')
            time.sleep(10)

        def test_between_uzcard_salary_humo_salary(self, mobile_driver):
            test_transfer = LoginPage(mobile_driver)
            test_transfer.login_page()
            test_transfer.choose_sender('uzcard_salary')
            test_transfer.taker_cards('humo_salary')
            time.sleep(10)

        def test_between_uzcard_salary_humo_anor(self, mobile_driver):
            test_transfer = LoginPage(mobile_driver)
            test_transfer.login_page()
            test_transfer.choose_sender('humo_salary')
            test_transfer.taker_cards('humo_anor')
            time.sleep(10)