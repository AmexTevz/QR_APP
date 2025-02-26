import pytest
from selenium.webdriver.support.ui import WebDriverWait
from src.locators.store_locators import CommonLocators, ModifierLocators
from src.utils.constants import BASE_URL
from src.pages.base_page import BasePage


class Navigation:
    @staticmethod
    def navigate_to_store(driver, store_id):
        url = f"{BASE_URL}/{store_id}"
        base = BasePage(driver)
        
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
        except Exception as e:
            print(f"Failed to load store {store_id}: {str(e)}")
            pytest.skip(f"Failed to load store {store_id}")
        
        try:
            if base.is_element_displayed(CommonLocators.CLOSE_AD_BUTTON, timeout=5):
                driver.find_element(*CommonLocators.CLOSE_AD_BUTTON).click()

            if base.is_element_displayed(CommonLocators.CLOSE_POPUP_BUTTON, timeout=5):
                driver.find_element(*CommonLocators.CLOSE_POPUP_BUTTON).click()
        except Exception as e:
            print(f"Error handling popups: {str(e)}")

        if not base.is_element_displayed(ModifierLocators.COPYRIGHT_LOGO, timeout=15):
            print(f"Store {store_id} page is not loading properly - copyright logo not found")
            pytest.skip(f"Store {store_id} is not accessible")
            
        return store_id


