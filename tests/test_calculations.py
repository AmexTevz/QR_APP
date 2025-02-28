import time
import pytest
from conftest import driver
from src.pages.store.menu_page import MenuPage
from src.pages.store.cart_page import CartPage
from src.pages.store.payment_page import CheckoutPage
from src.utils.config_reader import read_store_data
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
    menu_page = MenuPage(driver)
    cart_page = CartPage(driver)
    payment_page = CheckoutPage(driver)
    payment_page.store_id = store_id

    menu_page.navigate_to_store(store_id)
    for _ in range(3):
        menu_page.select_random_item()
        cart_page.add_to_cart()
    cart_page.go_to_cart()
    
    script_calculated_subtotal, app_calculated_subtotal = cart_page.cart_calculations()
    assert script_calculated_subtotal == app_calculated_subtotal

    time.sleep(5) 