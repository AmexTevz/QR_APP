from src.pages.base_page import BasePage
from src.utils.credit_card import TEST_CARD
from src.locators.store_locators import PaymentPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from src.utils.constants import TIMEOUTS

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.store_id = None



    def place_the_order(self):
        try:
            card_data = TEST_CARD
            self.send_keys(PaymentPageLocators.NAME_ON_CARD,card_data['fullname'])
            try:
                self.switch_to_frame(PaymentPageLocators.FRAME)
                self.send_keys(PaymentPageLocators.CARD_NUMBER, card_data['number'])
                self.send_keys(PaymentPageLocators.EXPIRATION_DATE, card_data['exp'])
                self.send_keys(PaymentPageLocators.SECURITY_CODE, card_data['cvv'])
                self.send_keys(PaymentPageLocators.POSTAL_CODE, card_data['zip'])
            except:
                pass
            self.switch_to_default_content()
            self.click(PaymentPageLocators.PAY_BUTTON)
            
            print("\nWaiting for receipt page...")

            WebDriverWait(self.driver, TIMEOUTS['payment']).until(
                lambda driver: "Order/Receipt" in driver.current_url
            )
            
            print("Receipt page loaded, getting confirmation...")
            element = self.wait_for_element_visible(PaymentPageLocators.SUCCESS_MESSAGE, timeout=TIMEOUTS['explicit'])
            print(f"Found confirmation element: {element.text}")
            
            confirmation = self.get_text(PaymentPageLocators.SUCCESS_MESSAGE)
            # print(f"Confirmation text: {confirmation}")
            #
            # if not "Thanks" in confirmation:
            #     if not self.store_id and 'store_id' in self.driver.current_url:
            #         self.store_id = self.driver.current_url.split('/')[-1]
            #
            #     self.take_screenshot(
            #         store_id=self.store_id or "unknown",
            #         item_name="payment_failed",
            #         sub_folder="payment_fail"
            #     )
            return confirmation
            
        except Exception:
            if not self.store_id and 'store_id' in self.driver.current_url:
                self.store_id = self.driver.current_url.split('/')[-1]
                
            self.take_screenshot(
                store_id=self.store_id or "unknown",
                item_name="payment_error",
                sub_folder="payment_fail"
            )
            raise
