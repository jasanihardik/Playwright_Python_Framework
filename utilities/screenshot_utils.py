"""
Screenshot utility module for the Playwright Automation Framework.
Provides screenshot functionality for the framework.
"""
import os
from datetime import datetime
from typing import Optional

from playwright.sync_api import Page

from config.config import DIRECTORY_PATHS, SCREENSHOT_SETTINGS
from utilities.logger import logger


class ScreenshotUtils:
    """Screenshot utility class for the Playwright Automation Framework."""

    @staticmethod
    def take_screenshot(page: Page, test_name: str, description: Optional[str] = None) -> str:
        """
        Take a screenshot of the current page state.
        
        Args:
            page: Playwright page object.
            test_name: Name of the test.
            description: Optional description of the screenshot.
            
        Returns:
            str: Path to the saved screenshot.
        """
        # Create screenshots directory if it doesn't exist
        timestamp_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = os.path.join(DIRECTORY_PATHS["screenshots"], timestamp_folder)
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Generate screenshot file name
        timestamp = datetime.now().strftime("%H-%M-%S-%f")
        desc = f"_{description}" if description else ""
        file_name = f"{SCREENSHOT_SETTINGS['screenshot_prefix']}{test_name}{desc}_{timestamp}.{SCREENSHOT_SETTINGS['screenshot_format']}"
        file_path = os.path.join(screenshot_dir, file_name)
        
        # Take screenshot
        logger.info(f"Taking screenshot: {file_name}")
        try:
            page.screenshot(path=file_path, full_page=True)
            logger.info(f"Screenshot saved to: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")
            return ""

    @staticmethod
    def take_element_screenshot(page: Page, selector: str, test_name: str, description: Optional[str] = None) -> str:
        """
        Take a screenshot of a specific element on the page.
        
        Args:
            page: Playwright page object.
            selector: CSS selector for the element.
            test_name: Name of the test.
            description: Optional description of the screenshot.
            
        Returns:
            str: Path to the saved screenshot.
        """
        # Create screenshots directory if it doesn't exist
        timestamp_folder = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_dir = os.path.join(DIRECTORY_PATHS["screenshots"], timestamp_folder)
        os.makedirs(screenshot_dir, exist_ok=True)
        
        # Generate screenshot file name
        timestamp = datetime.now().strftime("%H-%M-%S-%f")
        desc = f"_{description}" if description else ""
        file_name = f"{SCREENSHOT_SETTINGS['screenshot_prefix']}{test_name}_element{desc}_{timestamp}.{SCREENSHOT_SETTINGS['screenshot_format']}"
        file_path = os.path.join(screenshot_dir, file_name)
        
        # Take element screenshot
        logger.info(f"Taking element screenshot: {file_name}")
        try:
            element = page.locator(selector)
            element.screenshot(path=file_path)
            logger.info(f"Element screenshot saved to: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Failed to take element screenshot: {str(e)}")
            return "" 