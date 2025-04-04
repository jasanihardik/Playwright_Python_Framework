"""
Browser factory module for the Playwright Automation Framework.
Provides browser initialization functionality for the framework.
"""
from typing import Dict, Any, Optional

from playwright.sync_api import sync_playwright, Browser, Page

from config.config import BROWSER_SETTINGS, TIMEOUT_SETTINGS
from utilities.logger import logger


class BrowserFactory:
    """Browser factory class for the Playwright Automation Framework."""

    @staticmethod
    def get_browser(browser_name: Optional[str] = None, headless: Optional[bool] = None) -> Browser:
        """
        Initialize and return a browser instance based on the configuration.
        
        Args:
            browser_name: Optional browser name to override the configuration.
            headless: Optional headless mode to override the configuration.
            
        Returns:
            Browser: A Playwright browser instance.
        """
        # Use parameters or fallback to config
        browser_type = browser_name or BROWSER_SETTINGS["browser_name"]
        is_headless = headless if headless is not None else BROWSER_SETTINGS["headless"]
        
        logger.info(f"Initializing {browser_type} browser (headless: {is_headless})")
        
        playwright = sync_playwright().start()
        
        # Get the appropriate browser type
        if browser_type.lower() == "chromium":
            browser_instance = playwright.chromium
        elif browser_type.lower() == "firefox":
            browser_instance = playwright.firefox
        elif browser_type.lower() == "webkit":
            browser_instance = playwright.webkit
        else:
            logger.warning(f"Unknown browser type: {browser_type}. Defaulting to chromium.")
            browser_instance = playwright.chromium
        
        # Launch the browser with appropriate options
        browser = browser_instance.launch(
            headless=is_headless,
            slow_mo=BROWSER_SETTINGS["slow_mo"]
        )
        
        logger.info(f"Browser initialized successfully: {browser_type}")
        return browser

    @staticmethod
    def get_page(browser: Browser) -> Page:
        """
        Create and return a new page with appropriate configurations.
        
        Args:
            browser: Playwright browser instance.
            
        Returns:
            Page: A configured Playwright page.
        """
        logger.info("Creating new page with configuration")
        
        # Create a new page
        page = browser.new_page(
            viewport=BROWSER_SETTINGS["viewport"],
            ignore_https_errors=BROWSER_SETTINGS["ignore_https_errors"],
        )
        
        # Set timeouts
        page.set_default_navigation_timeout(TIMEOUT_SETTINGS["navigation_timeout"])
        page.set_default_timeout(TIMEOUT_SETTINGS["default_timeout"])
        
        logger.info("Page created successfully with configured timeouts and viewport")
        return page 