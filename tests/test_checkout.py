import time
import pytest
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
@pytest.mark.checkout
@pytest.mark.parametrize('store_id', get_all_store_ids())
def test_random_item_checkout(driver, store_id):
    menu_page = MenuPage(driver)
    cart_page = CartPage(driver)
    payment_page = CheckoutPage(driver)
    payment_page.store_id = store_id
    
    menu_page.navigate_to_store(store_id)
    for _ in range(3):
        menu_page.select_random_item()
        cart_page.add_to_cart()
    cart_page.go_to_cart()
    cart_page.manage_tips(8.5)
    cart_page.add_charity()
    cart_page.click_pay_now_button()
    order = payment_page.place_the_order()
    assert "Thanks" in order
    time.sleep(10)







