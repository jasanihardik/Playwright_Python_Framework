"""
Configuration file for the Playwright Automation Framework.
Contains all settings and configurations for the framework.
"""
import os
from pathlib import Path

# Root path of the project
ROOT_PATH = Path(__file__).parent.parent

# Base URL for the application under test
BASE_URL = "https://webdriveruniversity.com"

# Browser settings
BROWSER_SETTINGS = {
    "browser_name": "chromium",  # "chromium", "firefox", "webkit"
    "headless": False,
    "slow_mo": 0,  # Slow down Playwright operations by the specified milliseconds
    "viewport": {"width": 1920, "height": 1080},
    "ignore_https_errors": True,
    "screenshot": "only-on-failure",  # "off", "on", "only-on-failure"
}

# Timeout settings (in milliseconds)
TIMEOUT_SETTINGS = {
    "navigation_timeout": 30000,
    "default_timeout": 30000,
    "expect_timeout": 5000,
}

# Directory paths
DIRECTORY_PATHS = {
    "reports": os.path.join(ROOT_PATH, "reports"),
    "logs": os.path.join(ROOT_PATH, "logs"),
    "screenshots": os.path.join(ROOT_PATH, "screenshots"),
}

# Reporting settings
REPORTING_SETTINGS = {
    "max_reports_to_keep": 5,
    "report_prefix": "playwright_report_",
}

# Screenshot settings
SCREENSHOT_SETTINGS = {
    "max_screenshots_to_keep": 5,
    "screenshot_prefix": "screenshot_",
    "screenshot_format": "png",
}

# URLs for different pages
PAGE_URLS = {
    "home": BASE_URL,
    "contact_us": f"{BASE_URL}/Contact-Us/contactus.html",
    "login": f"{BASE_URL}/Login-Portal/index.html",
    "button_clicks": f"{BASE_URL}/Click-Buttons/index.html",
    "to_do_list": f"{BASE_URL}/To-Do-List/index.html",
    "dropdown": f"{BASE_URL}/Dropdown-Checkboxes-RadioButtons/index.html",
    "popup_alerts": f"{BASE_URL}/Popup-Alerts/index.html",
}

# Logging settings
LOGGING_SETTINGS = {
    "log_level": "INFO",  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    "log_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "log_file": os.path.join(DIRECTORY_PATHS["logs"], "test_execution.log"),
} 