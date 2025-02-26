import random
import logging
import time
from src.pages.base_page import BasePage
from src.locators.store_locators import ModifierLocators


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    def add_to_cart(self):
        required_groups = self.get_elements(ModifierLocators.REQUIRED_MODIFIER_GROUP)
        for group in required_groups:
            radio_options = group.find_elements(*ModifierLocators.RADIO_OPTIONS)
            if radio_options:
                selected_option = random.choice(radio_options)
                self.click(selected_option)
        optional_groups = self.get_elements(ModifierLocators.OPTIONAL_MODIFIER_GROUP)

        for group in optional_groups:
            group_title = group.text.lower()
            if 'additional instructions' in group_title or 'remove' in group_title:
                continue
            checkbox_options = group.find_elements(*ModifierLocators.CHECKBOX_OPTIONS)
            if checkbox_options and random.choice([True, False]):
                num_to_select = random.randint(1, min(2, len(checkbox_options)))
                selected_options = random.sample(checkbox_options, num_to_select)
                for option in selected_options:
                    self.click(option)
        self.click(ModifierLocators.ADD_TO_CART)
        time.sleep(1)


    def go_to_cart(self):
        time.sleep(0.5)
        self.click(ModifierLocators.CART_BUTTON)

    def add_charity(self):
        self.click(ModifierLocators.CHARITY_BUTTON)

    def manage_tips(self, amount=None):
        try:
            if amount == 0:
                self.click(ModifierLocators.NO_TIP)
            elif amount is None:
                self.click(random.choice([ModifierLocators.TIP_22, ModifierLocators.TIP_20, ModifierLocators.TIP_18]))
            else:
                self.click(ModifierLocators.CUSTOM_TIP)
                custom_tip_input = self.find_element(ModifierLocators.CUSTOM_TIP_INPUT)
                custom_tip_input.clear()
                custom_tip_input.send_keys(str(amount))
        except:
            pass

    def click_pay_now_button(self):
        self.click(ModifierLocators.PAY_NOW_BUTTON)