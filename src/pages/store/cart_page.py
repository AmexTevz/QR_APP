import random
import logging
import time
from src.pages.base_page import BasePage
from src.locators.store_locators import ModifierLocators,CalculationLocators
import math
from selenium.webdriver.common.by import By


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
        self.click(ModifierLocators.EXPAND_BUTTON)

    # def expand_cart_items(self):
    #     self.click(ModifierLocators.EXPAND_BUTTON)

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


    def cart_calculations(self):
        cart_items = []
        main_items = self.driver.find_elements(*CalculationLocators.MAIN_ITEMS)
        for item in main_items:
            if "modifier" in item.get_attribute("class") and not "has-modifiers" in item.get_attribute("class"):
                continue

            try:
                item_name = item.find_element(By.CSS_SELECTOR, "h3.cart-title").text
            except:
                try:
                    item_name = item.find_element(By.CSS_SELECTOR, "h3.typography-text-p3.cart-title").text
                except:
                    item_name = "Unknown Item"

            try:
                price_element = item.find_element(By.CSS_SELECTOR, "div.table-col-cart-4 p")
                price = price_element.text
            except:
                try:
                    price_element = item.find_element(By.CSS_SELECTOR, "div.table-col-cart-4.item-price")
                    price = price_element.text
                except:
                    price = "Price not found"

            item_data = {
                "name": item_name,
                "price": price,
                "modifiers": []
            }

            if "has-modifiers" in item.get_attribute("class"):
                next_element = item.find_element(By.XPATH, "following-sibling::li[1]")
                while next_element and "modifier" in next_element.get_attribute(
                        "class") and not "has-modifiers" in next_element.get_attribute("class"):
                    try:
                        modifier_name = next_element.find_element(By.CSS_SELECTOR, "div.table-col-cart-10").text
                    except:
                        modifier_name = "Unknown Modifier"

                    try:
                        modifier_price = next_element.find_element(By.CSS_SELECTOR, "p.price.modifier-price").text
                    except:
                        try:
                            modifier_price = next_element.find_element(By.CSS_SELECTOR, "div.table-col-cart-4").text
                        except:
                            modifier_price = "Price not found"

                    item_data["modifiers"].append({
                        "name": modifier_name,
                        "price": modifier_price
                    })

                    try:
                        next_element = next_element.find_element(By.XPATH, "following-sibling::li[1]")
                    except:
                        break

            cart_items.append(item_data)

        script_subtotal = 0
        for item in cart_items:
            total_item_price = 0
            print(f"\nItem: {item['name']}")
            print(f"Price: {item['price']}")
            item_price_float = float(item['price'].split('$')[1])
            total_item_price += item_price_float

            if item['modifiers']:
                print("Modifiers:")
                for modifier in item['modifiers']:
                    mod_price = modifier['price'] if modifier['price'] else 'No additional cost'
                    print(f"  - {modifier['name']}: {mod_price}")
                    if '$' in mod_price:
                        modifier_price_float = float(modifier['price'].split('$')[1])
                        total_item_price += modifier_price_float
                        print(f"Total Price for the item - ${total_item_price}")
            else:
                print("No modifiers")
                print(f"Total Price for the item - ${total_item_price}")
            print("-" * 40)
            script_subtotal += total_item_price
            script_subtotal = math.ceil(script_subtotal * 100) / 100
        print(f"Script calculated total: ${script_subtotal}")
        app_subtotal = self.driver.find_element(*CalculationLocators.SUBTOTAL).text
        print(f"App provided total: ${app_subtotal}")

        return script_subtotal, float(app_subtotal.replace('$', ''))