import time
import pytest
from pages.mejdu_svoimi_schetami_page import BetweenCardsPayments


class TestElements:
    class TestPageBetweenCards:
        @pytest.mark.parametrize("sender, taker", [
            ('uzcard_salary', 'uzcard_kapital'),
            ('uzcard_salary', 'uzcard_cobage'),
            ('uzcard_salary', 'humo_salary'),
            ('uzcard_salary', 'humo_anor'),
            ('uzcard_salary', 'wallet'),
            ('uzcard_kapital', 'uzcard_salary'),
            ('uzcard_kapital', 'uzcard_cobage'),
            ('uzcard_kapital', 'uzcard_ofb'),
            ('uzcard_kapital', 'humo_salary'),
            ('uzcard_kapital', 'humo_anor'),
            ('uzcard_kapital', 'wallet'),
            ('uzcard_cobage', 'uzcard_salary'),
            ('uzcard_kapital', 'uzcard_kapital'),
            ('uzcard_cobage', 'humo_salary'),
            ('uzcard_cobage', 'humo_anor'),
            ('uzcard_cobage', 'wallet'),
            ('humo_salary', 'uzcard_salary'),
            ('humo_salary', 'uzcard_kapital'),
            ('humo_salary', 'uzcard_cobage'),
            ('humo_salary', 'humo_anor'),
            ('humo_salary', 'wallet'),
            ('humo_anor', 'uzcard_salary'),
            ('humo_anor', 'uzcard_kapital'),
            ('humo_anor', 'uzcard_cobage'),
            ('humo_anor', 'humo_salary'),
            ('humo_anor', 'humo_other'),
            ('humo_anor', 'wallet'),
            ('wallet', 'uzcard_salary'),
            ('wallet', 'uzcard_kapital'),
            ('wallet', 'uzcard_cobage'),
            ('wallet', 'humo_salary'),
            ('wallet', 'humo_anor'),
        ])
        def test_transfer_between_senders_and_takers(self, mobile_driver, sender, taker):
            test_transfer = BetweenCardsPayments(mobile_driver)
            test_transfer.login_page()
            test_transfer.choose_sender(sender)
            test_transfer.taker_cards(taker)
            time.sleep(5)