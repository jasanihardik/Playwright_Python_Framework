"""
Pytest configuration for the Playwright Automation Framework.
Contains fixtures and configurations for the test framework.
"""
import os
import time
import pytest
from datetime import datetime
from typing import Dict, Any, Optional, Generator

from playwright.sync_api import Page, Browser
import logging

from config.config import BROWSER_SETTINGS, DIRECTORY_PATHS
from utilities.browser_factory import BrowserFactory
from utilities.logger import logger
from utilities.screenshot_utils import ScreenshotUtils


def pytest_addoption(parser):
    """Add command-line options to pytest."""
    parser.addoption(
        "--browser-name", 
        action="store", 
        default=BROWSER_SETTINGS["browser_name"],
        help="Browser to run tests on: chromium, firefox, webkit"
    )
    parser.addoption(
        "--headless", 
        action="store", 
        default=str(BROWSER_SETTINGS["headless"]).lower(),
        help="Run browser in headless mode: true, false"
    )


@pytest.fixture(scope="session")
def browser_name(request) -> str:
    """
    Get the browser name from command line option.
    
    Returns:
        str: Browser name.
    """
    return request.config.getoption("--browser-name")


@pytest.fixture(scope="session")
def headless(request) -> bool:
    """
    Get the headless mode setting from command line option.
    
    Returns:
        bool: True if browser should run in headless mode, False otherwise.
    """
    return request.config.getoption("--headless").lower() == "true"


@pytest.fixture(scope="session")
def browser(browser_name: str, headless: bool) -> Generator[Browser, None, None]:
    """
    Initialize and yield a browser instance.
    
    Args:
        browser_name: Browser type to use.
        headless: Whether to run in headless mode.
        
    Yields:
        Browser: A Playwright browser instance.
    """
    # Initialize the browser
    browser = BrowserFactory.get_browser(browser_name, headless)
    logger.info(f"Browser initialized: {browser_name} (headless: {headless})")
    
    # Yield the browser to the test
    yield browser
    
    # Close the browser after the test
    logger.info("Closing browser")
    browser.close()


@pytest.fixture
def page(browser: Browser) -> Generator[Page, None, None]:
    """
    Create and yield a new page for each test.
    
    Args:
        browser: Playwright browser instance.
        
    Yields:
        Page: A Playwright page.
    """
    # Create a new page
    page = BrowserFactory.get_page(browser)
    logger.info("Page created")
    
    # Yield the page to the test
    yield page
    
    # Close the page after the test
    logger.info("Closing page")
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to take screenshot when a test fails.
    
    Args:
        item: Test item.
        call: Test call.
    """
    # Execute the hook wrapper
    outcome = yield
    report = outcome.get_result()
    
    # If test failed, take a screenshot
    if report.when == "call" and report.failed:
        try:
            # Try to get the page from the test
            page = item.funcargs.get("page")
            if page:
                # Create screenshot directory if it doesn't exist
                timestamp_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_dir = os.path.join(DIRECTORY_PATHS["screenshots"], timestamp_folder)
                os.makedirs(screenshot_dir, exist_ok=True)
                
                # Take a screenshot
                logger.info(f"Test failed, taking screenshot: {item.name}")
                timestamp = datetime.now().strftime("%H-%M-%S")
                screenshot_path = os.path.join(screenshot_dir, f"failure_{item.name}_{timestamp}.png")
                page.screenshot(path=screenshot_path, full_page=True)
                logger.info(f"Screenshot saved to: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot on test failure: {str(e)}")


@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Set up logging for the test session."""
    # Ensure logs directory exists
    os.makedirs(DIRECTORY_PATHS["logs"], exist_ok=True)
    
    # Log test session start
    logger.info("="*80)
    logger.info(f"Test session started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*80)
    
    yield
    
    # Log test session end
    logger.info("="*80)
    logger.info(f"Test session ended at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("="*80) 