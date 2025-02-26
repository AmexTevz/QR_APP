from src.pages.base_page import BasePage
from src.locators.store_locators import (
    PriceLocators,
    MenuCategories,
    ModifierLocators
)
from src.utils.navigation import Navigation
import random

PRICE_CHECK_VALUE = "9.69"

class MenuPage(BasePage):
    def navigate_to_store(self, store_id):
        self.store_id = Navigation.navigate_to_store(self.driver, store_id)

    def check_all_prices(self):
        invalid_items = []
        price_to_check = PRICE_CHECK_VALUE
        processed_categories = set()

        initial_categories = [
            cat.text for cat in self.get_elements(MenuCategories.VISIBLE_SUBCATEGORIES)
            if cat.is_displayed()
        ]
        self.logger.info(f"Found {len(initial_categories)} main categories")

        def check_items_in_current_view(category_path=""):
            new_items = self.get_elements(PriceLocators.ITEM_NAME)
            if not new_items:
                return False

            self.logger.info(f"Found {len(new_items)} items in {category_path}")
            for i in new_items:
                new_item_name = None
                try:
                    new_item_name = i.text
                    self.click(i)
                    item_price = self.get_text(PriceLocators.INDIVIDUAL_PRICE)
                    self.logger.info(f"Checking {category_path} > {new_item_name}: {item_price}")

                    if item_price == price_to_check:
                        self.take_screenshot(self.store_id, new_item_name, sub_folder="invalid_price")
                        
                        invalid_items.append({
                            'category': category_path,
                            'name': new_item_name,
                            'price': item_price
                        })
                    self.driver.back()
                except Exception as e:
                    error_item = new_item_name if new_item_name else "unknown item"
                    self.logger.error(f"Error checking {error_item}: {str(e)}")
            return True

        def explore_category(main_category_name, depth=0, new_path=""):
            if main_category_name in processed_categories:
                self.logger.info(f"Already checked {main_category_name}, skipping...")
                return

            current_path = f"{new_path} > {main_category_name}" if new_path else main_category_name
            self.logger.info(f"\nExploring depth {depth}: {current_path}")

            try:
                category_locator = MenuCategories.CATEGORY_BY_NAME(main_category_name)
                self.click(category_locator)
                processed_categories.add(main_category_name)

                if check_items_in_current_view(current_path):
                    self.driver.back()
                    return

                subcategories = [
                    i.text for i in self.get_elements(MenuCategories.VISIBLE_SUBCATEGORIES)
                    if i.is_displayed() and i.text not in processed_categories
                ]

                if subcategories:
                    self.logger.info(f"Found subcategories in {current_path}: {subcategories}")
                    for i in subcategories:
                        explore_category(i, depth + 1, current_path)
                self.driver.back()
            except Exception as e:
                self.logger.error(f"Error exploring {current_path}: {str(e)}")
                for _ in range(depth + 1):
                    try:
                        self.driver.back()
                    except:
                        pass

        for category_name in initial_categories:
            explore_category(category_name)

        return invalid_items

    def select_random_item(self):
        main_categories = self.get_elements(MenuCategories.ALL_CATEGORIES)
        if not main_categories:
            print("No categories found, retrying...")
            self.driver.refresh()
            main_categories = self.get_elements(MenuCategories.ALL_CATEGORIES)
            if not main_categories:
                raise Exception("No menu categories found after retry")
            
        random_category = random.choice(main_categories)
        self.click(random_category)
        while True:
            try:
                clickable_elements = self.get_elements(
                    MenuCategories.ALL_SUB_CATEGORIES,
                    MenuCategories.ALTERNATIVE_CATEGORIES
                )
                if not clickable_elements:
                    clickable_elements = self.get_elements(ModifierLocators.MENU_ITEMS)

                if clickable_elements:
                    random_element = random.choice(clickable_elements)
                    self.click(random_element)
                else:
                    self.driver.back()
                if self.is_element_displayed(ModifierLocators.ADD_TO_CART):
                    return True
            except Exception as e:
                self.logger.error(f"Error during navigation: {str(e)}")
                self.driver.back()
                continue