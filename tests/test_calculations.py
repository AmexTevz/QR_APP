import time
import pytest
from selenium.webdriver.common.by import By
import math
from conftest import driver
from src.pages.store.menu_page import MenuPage
from src.pages.store.cart_page import CartPage
from src.pages.store.payment_page import CheckoutPage
from src.utils.config_reader import read_store_data
from src.locators.store_locators import CalculationLocators
import os


def get_all_store_ids():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, '..', 'src', 'data', 'stores.csv')
    stores = read_store_data(file_path)
    return stores


@pytest.mark.edge
@pytest.mark.calculations
@pytest.mark.parametrize('store_id', get_all_store_ids())
def test_price_calculation(driver, store_id):
    cart_items = []
    menu_page = MenuPage(driver)
    cart_page = CartPage(driver)
    payment_page = CheckoutPage(driver)
    payment_page.store_id = store_id

    menu_page.navigate_to_store(store_id)
    for _ in range(3):
        menu_page.select_random_item()
        cart_page.add_to_cart()
    cart_page.go_to_cart()
    # script_calculated_subtotal, app_calculated_subtotal = cart_page.cart_calculations()

    # assert script_calculated_subtotal == app_calculated_subtotal
    main_items = driver.find_elements(By.CSS_SELECTOR, "li.table-row")
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
    app_subtotal = driver.find_element(*CalculationLocators.SUBTOTAL).text
    print(f"App provided total - ${app_subtotal}")
    assert script_subtotal == float(app_subtotal)



    time.sleep(5)























