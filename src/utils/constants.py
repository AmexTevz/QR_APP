from pathlib import Path

# Screenshot directories
SCREENSHOTS_DIR = Path("screenshots")
SCREENSHOTS_DIR.mkdir(exist_ok=True)

# Base URL
BASE_URL = "https://qaquickpay.hmshost.com/Menu"

# Browser configurations
BROWSER_OPTIONS = {
    'chrome': {
        'default': [
            "--start-maximized",
            "--disable-notifications",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-infobars",
            "--disable-browser-side-navigation",
            "--disable-site-isolation-trials",
            "--page-load-strategy=normal",
            "--disable-extensions",
            "--dns-prefetch-disable",
            "--disable-web-security",
            "--ignore-certificate-errors"
        ]
    },
    'firefox': {
        'preferences': {
            "browser.startup.homepage": "about:blank",
            "startup.homepage_welcome_url": "about:blank",
            "browser.download.folderList": 2,
            "browser.download.manager.showWhenStarting": False
        }
    },
    'edge': {
        'default': [
            "--start-maximized",
            "--disable-notifications",
            # "--headless=new",
            "--disable-gpu",
            "--no-sandbox"
        ]
    }
}

# Timeouts
TIMEOUTS = {
    'implicit': 0,
    'explicit': 10,
    'page_load': 30,
    'payment': 60
}


