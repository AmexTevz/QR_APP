import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from src.utils.constants import (
    BROWSER_OPTIONS,
    TIMEOUTS
)


@pytest.fixture(scope="session")
def driver(request):
    browser = 'chrome'
    driver = None

    try:
        if browser == 'chrome':
            options = ChromeOptions()
            for option in BROWSER_OPTIONS['chrome']['default']:
                options.add_argument(option)
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

        elif browser == 'firefox':
            options = FirefoxOptions()
            for pref, value in BROWSER_OPTIONS['firefox']['preferences'].items():
                options.set_preference(pref, value)
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            driver.maximize_window()

        elif browser == 'edge':
            options = EdgeOptions()
            for option in BROWSER_OPTIONS['edge']['default']:
                options.add_argument(option)
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

        if driver:
            driver.implicitly_wait(TIMEOUTS['implicit'])
            driver.set_page_load_timeout(TIMEOUTS['page_load'])
            driver.set_script_timeout(TIMEOUTS['page_load'])
            yield driver
            driver.quit()

    except Exception:
        if driver:
            driver.quit()
        raise



