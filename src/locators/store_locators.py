# Locators for simulation 1
from selenium.webdriver.common.by import By

class CommonLocators:
    CLOSE_AD_BUTTON = (By.CSS_SELECTOR, 'i.icons-close-ad')
    CLOSE_POPUP_BUTTON = (By.CSS_SELECTOR, 'button#CookiePrefencesModalButton')

class MenuCategories:
    BREAKFAST = (By.XPATH, "//h1[contains(.,'Breakfast')]")
    NON_ALCOHOLIC = (By.XPATH, "//h1[contains(.,'Non-Alcoholic Beverages')]")
    APPETIZERS = (By.XPATH, "//h1[contains(.,'Appetizers')]")
    HANDHELDS = (By.XPATH, "//h1[contains(.,'Handhelds')]")
    FAJITAS = (By.XPATH, "//h1[contains(.,'Fajitas')]")
    KIDS = (By.XPATH, "//h1[contains(.,'For The Kids')]")
    SIDES = (By.XPATH, "//h1[contains(.,'Sides')]")
    ALCOHOLIC = (By.XPATH, "//h1[contains(.,'Alcoholic Beverages')]")
    ALL_CATEGORIES = (By.CSS_SELECTOR, "h1.typography-text-h4")
    ALL_SUB_CATEGORIES = (By.CSS_SELECTOR, "h3.typography-text-h4")
    ALTERNATIVE_CATEGORIES = (By.CSS_SELECTOR, "h1.landing-cat-title")
    CATEGORY_BY_NAME = lambda name: (
    By.XPATH, f"//h1[contains(@class,'category-title') or contains(@class,'title')][normalize-space(text())='{name}']")
    VISIBLE_SUBCATEGORIES = (By.XPATH, "//h1[contains(@class,'category-title') or contains(@class,'title')]")

class AppetizerItems:
    BONELESS_BUFFALO_WINGS = (By.XPATH, "//h3[contains(.,'Boneless Buffalo Wings')]")
    BONELESS_HONEY_CHIPOTLE = (By.XPATH, "//h3[contains(.,'Boneless Honey Chipotle Wings')]")
    CHIPS_AND_SALSA = (By.XPATH, "//h3[contains(.,'Chips & Salsa')]")
    CHIPS_AND_QUESO = (By.XPATH, "//h3[contains(.,'Chips & Salsa with Chili's® Queso')]")
    SOUTHWESTERN_EGGROLLS = (By.XPATH, "//h3[contains(.,'Southwestern Eggrolls™')]")
    TRIPLE_DIPPER = (By.XPATH, "//h3[contains(.,'Triple Dipper™')]")

class PriceLocators:
    ITEM_PRICE_BY_NAME = (By.XPATH, "//h3[contains(text(),'{}')]/..//p[contains(@class,'palette-neutral100-color typography-text-p2')]")
    ITEM_CONTAINER = (By.XPATH, "//div[contains(@class,'menu-item')]")
    ITEM_NAME = (By.XPATH, ".//h3")
    ITEM_PRICE = (By.XPATH, ".//p[contains(@class,'palette-neutral100-color typography-text-p2')]")
    CATEGORY_CONTAINER = (By.XPATH, "//div[contains(@class,'category-section')]")
    INDIVIDUAL_PRICE = (By.CSS_SELECTOR, "p#itemPrice")
    
class CustomizationLocators:
    DIPPING_SAUCE_DROPDOWN = (By.XPATH, "//div[contains(text(),'Choose Dipping Sauce')]")
    ADD_TOPPINGS_DROPDOWN = (By.XPATH, "//div[text()='Add Toppings']")
    REMOVE_TOPPINGS_DROPDOWN = (By.XPATH, "//div[text()='Remove Toppings']")
    ADDITIONAL_INSTRUCTIONS = (By.XPATH, "//input[@placeholder='e.g. allergies, etc']")
    
    # Sauce options with checkboxes
    BLEU_CHEESE_CHECKBOX = (By.CSS_SELECTOR, "i.icons-radio-empty[for='811900705-1']")
    HOUSE_MADE_RANCH_CHECKBOX = (By.CSS_SELECTOR, "i.icons-radio-empty[for='811902602-1']")
    
    # Selected state (when checked)
    BLEU_CHEESE_CHECKED = (By.CSS_SELECTOR, "i.icons-radio-filled[for='811900705-1']")
    HOUSE_MADE_RANCH_CHECKED = (By.CSS_SELECTOR, "i.icons-radio-filled[for='811902602-1']")

class OrderControlsLocators:
    DECREASE_QUANTITY = (By.XPATH, "//button[contains(@class,'decrease')]")
    INCREASE_QUANTITY = (By.XPATH, "//button[contains(@class,'increase')]")
    QUANTITY_INPUT = (By.XPATH, "//input[@type='number']")
    TOTAL_PRICE = (By.XPATH, "//div[contains(text(),'Total:')]//span")



class ModifierLocators:
    MODIFIER_HEADER = (By.CSS_SELECTOR, "div.modifier-header")
    MODIFIER_TEXT = (By.CSS_SELECTOR, "label.typography-text-p3")
    REQUIRED_SECTION = (By.XPATH, "//span[contains(@class, 'text-danger') and contains(text(), '(Required)')]")
    RADIO_OPTIONS = (By.CSS_SELECTOR, "i.icons-radio-empty")
    RADIO_OPTIONS_CHECKED = (By.CSS_SELECTOR, "i.icons-radio-filled")
    CHECKBOX_OPTIONS = (By.CSS_SELECTOR, "i.icons-checkbox-empty")
    CHECKBOX_OPTIONS_CHECKED = (By.CSS_SELECTOR, "i.icons-checkbox-filled ")
    CATEGORY_HEADERS = (By.XPATH, "//h1[contains(@class,'category-title') or contains(@class,'title')]")
    MENU_ITEMS = (By.XPATH, "//h3[contains(@class, 'typography-text-h4')]")
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-primary, button#AddItem')
    CART_BUTTON = (By.CSS_SELECTOR, "i.icons-cart")
    PAY_NOW_BUTTON = (By.CSS_SELECTOR, "button#PayNow")
    COPYRIGHT_LOGO = (By.CSS_SELECTOR, "p.copyright")
    MODIFIER_REQUIRED = (By.CSS_SELECTOR, "li.item-modifier-required")
    MODIFIER_OPTIONAL = (By.CSS_SELECTOR, "li.item-modifier-optional")
    UNIVERSAL = (By.CSS_SELECTOR, "label.typography-text-p3")
    REQUIRED_MODIFIER_GROUP = (By.CSS_SELECTOR, "ul.required-modifier-group")
    OPTIONAL_MODIFIER_GROUP = (By.CSS_SELECTOR, "ul.optional-modifier-group")
    CHARITY_BUTTON = (By.CSS_SELECTOR, "input#roundUpTrigger")
    NO_TIP = (By.CSS_SELECTOR, "button#cashTipTrigger")
    TIP_22 = (By.CSS_SELECTOR, "button[id='22TipTrigger']")
    TIP_20 = (By.CSS_SELECTOR, "button[id='20TipTrigger']")
    TIP_18 = (By.CSS_SELECTOR, "button[id='18TipTrigger']")
    CUSTOM_TIP = (By.CSS_SELECTOR, "button#customTipTrigger")
    CUSTOM_TIP_INPUT = (By.CSS_SELECTOR, "input#Tip")
    EXPAND_BUTTON = (By.CSS_SELECTOR, "p.show-toggle-cart")

class PaymentPageLocators:
    NAME_ON_CARD = (By.CSS_SELECTOR, "input#inputNameOnCard")
    CARD_NUMBER = (By.CSS_SELECTOR, "input#CardNumber")
    EXPIRATION_DATE = (By.CSS_SELECTOR, "input#ExpirationDate")
    SECURITY_CODE = (By.CSS_SELECTOR, "input#SecurityCode")
    POSTAL_CODE = (By.CSS_SELECTOR, "input#PostalCode")
    PAY_BUTTON = (By.CSS_SELECTOR, "button#btnPay")
    FRAME = (By.ID, "hpc--card-frame")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "p.p")
    PROCESSING_MESSAGE = (By.XPATH, "//div[contains(text(), 'Processing')]")


class CalculationLocators:
    MAIN_ITEMS = (By.CSS_SELECTOR, "li.table-row")
    ITEM_NAME_1 =(By.CSS_SELECTOR, "h3.cart-title")
    ITEM_NAME_2 = (By.CSS_SELECTOR, "h3.typography-text-p3.cart-title")
    ITEM_PRICE_1 = (By.CSS_SELECTOR, "div.table-col-cart-4 p")
    ITEM_PRICE_2 = (By.CSS_SELECTOR, "div.table-col-cart-4.item-price")
    NEXT_ITEM = (By.XPATH, "following-sibling::li[1]")
    MODIFIER_NAME = (By.CSS_SELECTOR, "div.table-col-cart-10")
    MODIFIER_PRICE_1 = (By.CSS_SELECTOR, "p.price.modifier-price")
    MODIFIER_PRICE_2 = (By.CSS_SELECTOR, "div.table-col-cart-4")
    SUBTOTAL = (By.CSS_SELECTOR, ".table-row:first-of-type .price span")
    TAX = (By.CSS_SELECTOR, ".table-row:nth-of-type(2) .price span")
    AUTO_SERVICE_CHARGE = (By.CSS_SELECTOR, ".table-row:nth-of-type(4) .price span")
    TIP = (By.CSS_SELECTOR, "span#lblTip")
    DONATION = (By.CSS_SELECTOR, "span#lblDonation")
    TOTAL = (By.CSS_SELECTOR, "span#lblTotal")
