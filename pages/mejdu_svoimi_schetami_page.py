from generator.generator import generated_person
from locators.elements_locator import AllLocators
from pages.base_page import BasePage


class BetweenCardsPayments(BasePage):
    locators = AllLocators

    def login_page(self):
        client_info = next(generated_person())
        number_login = client_info.loginnumber
        password = client_info.password
        for _ in range(2):
            self.element_is_clickable(self.locators.ENTER_OK).click()
        self.element_is_clickable(self.locators.NUMBER).send_keys(number_login)
        self.element_is_clickable(self.locators.PASSWORD).send_keys(password)
        self.element_is_visible(self.locators.LOGIN).click()
        cancel = self.element_is_visible(self.locators.CANCEL)
        set_pin = self.element_is_visible(self.locators.SET_PIN)
        choose_sender = self.element_is_visible(self.locators.CHOOSE_SEND)
        if cancel is not None and set_pin is not None:
            cancel.click()
        else:
            choose_sender.click()
        choose_sender.click()

    def choose_sender(self, choose_sender):
        sender_cards = {
            'uzcard_salary': {'choose': self.locators.UZCARD_SALARY},
            'uzcard_kapital': {'choose': self.locators.UZCARD_OTHER},
            'uzcard_cobage': {'choose': self.locators.UZCARD_COBAGE},
            'uzcard_ofb': {'choose': self.locators.UZCARD_OFB},
            'humo_salary': {'choose': self.locators.HUMO_SALARY},
            'humo_other': {'choose': self.locators.HUMO_SALARY},
            'humo_anor': {'choose': self.locators.HUMO_ANOR},
            'wallet': {'choose': self.locators.WALLET}
        }
        if choose_sender in ['uzcard_salary', 'uzcard_kapital', 'uzcard_cobage', 'uzcard_ofb']:
            card_element = self.element_is_visible(sender_cards[choose_sender]['choose'])
            card_element.click()
        elif choose_sender in ['humo_salary']:
            self.scroll_down()
            card_element = self.element_is_visible(sender_cards[choose_sender]['choose'])
            card_element.click()
        elif choose_sender in ['humo_other', 'humo_anor', 'wallet']:
            self.touch_action_scroll_down(self.element_is_visible(self.locators.UZCARD_COBAGE))
            card_element = self.element_is_visible(sender_cards[choose_sender]['choose'])
            card_element.click()
        else:
            print('card not found')

    def taker_cards(self, cards_choose):
        client_info = next(generated_person())
        summa = client_info.summa
        self.element_is_visible(self.locators.CHOOSE_TAKE).click()
        taker_cards = {
            'uzcard_salary': {'choose': self.locators.UZCARD_SALARY},
            'uzcard_kapital': {'choose': self.locators.UZCARD_OTHER},
            'uzcard_cobage': {'choose': self.locators.UZCARD_COBAGE},
            'uzcard_ofb': {'choose': self.locators.UZCARD_OFB},
            'humo_salary': {'choose': self.locators.HUMO_SALARY},
            'humo_other': {'choose': self.locators.HUMO_SALARY},
            'humo_anor': {'choose': self.locators.HUMO_ANOR},
            'wallet': {'choose': self.locators.WALLET}
        }
        if cards_choose in ['uzcard_salary', 'uzcard_kapital']:
            card_element = self.element_is_visible(taker_cards[cards_choose]['choose'])
            card_element.click()
        elif cards_choose in ['uzcard_cobage', 'uzcard_ofb', 'humo_salary', 'humo_other']:
            self.scroll_down()
            card_element = self.element_is_visible(taker_cards[cards_choose]['choose'])
            card_element.click()
        elif cards_choose in ['humo_anor', 'wallet']:
            self.touch_action_scroll_down(self.element_is_visible(self.locators.UZCARD_COBAGE))
            card_element = self.element_is_visible(taker_cards[cards_choose]['choose'])
            card_element.click()
        else:
            print('card not found')
        self.element_is_visible(self.locators.SUMMA).send_keys(summa)
        self.element_is_visible(self.locators.NEXT_BUTTON).click()
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_CLOSE).click()
        self.element_is_clickable(self.locators.TAB_BAR_ISTORIYA).click()