"""
Base page class for the Playwright Automation Framework.
Provides common functionality for all page objects.
"""
from typing import Optional, Dict, Any, List, Union

from playwright.sync_api import Page, Locator, ElementHandle, expect, TimeoutError

from config.config import TIMEOUT_SETTINGS
from utilities.logger import logger
from utilities.screenshot_utils import ScreenshotUtils


class BasePage:
    """Base page class for all page objects in the framework."""
    
    def __init__(self, page: Page):
        """
        Initialize the base page.
        
        Args:
            page: Playwright page object.
        """
        self.page = page
        self.screenshot_utils = ScreenshotUtils()

    def navigate_to(self, url: str) -> None:
        """
        Navigate to the specified URL.
        
        Args:
            url: URL to navigate to.
        """
        logger.info(f"Navigating to URL: {url}")
        self.page.goto(url)

    def get_title(self) -> str:
        """
        Get the page title.
        
        Returns:
            str: The page title.
        """
        title = self.page.title()
        logger.info(f"Page title: {title}")
        return title

    def get_url(self) -> str:
        """
        Get the current URL.
        
        Returns:
            str: The current URL.
        """
        url = self.page.url
        logger.info(f"Current URL: {url}")
        return url

    def wait_for_url(self, url: str, timeout: Optional[int] = None) -> None:
        """
        Wait for URL to be a specific value.
        
        Args:
            url: URL to wait for.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["navigation_timeout"]
        logger.info(f"Waiting for URL to be: {url}")
        self.page.wait_for_url(url, timeout=wait_timeout)

    def wait_for_selector(self, selector: str, timeout: Optional[int] = None, state: str = "visible") -> Locator:
        """
        Wait for an element matching the selector.
        
        Args:
            selector: CSS selector.
            timeout: Optional timeout in milliseconds.
            state: State to wait for: 'attached', 'detached', 'visible', or 'hidden'.
            
        Returns:
            Locator: The element locator.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Waiting for selector: {selector}")
        self.page.wait_for_selector(selector, timeout=wait_timeout, state=state)
        return self.page.locator(selector)

    def fill_text(self, selector: str, text: str, timeout: Optional[int] = None) -> None:
        """
        Fill text into an input field.
        
        Args:
            selector: CSS selector for the input field.
            text: Text to fill.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Filling text into {selector}: {text}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        element.fill(text)

    def click(self, selector: str, timeout: Optional[int] = None, force: bool = False) -> None:
        """
        Click on an element.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
            force: Whether to force the click.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Clicking on element: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        element.click(force=force)

    def double_click(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Double-click on an element.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Double-clicking on element: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        element.dblclick()

    def hover(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Hover over an element.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Hovering over element: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        element.hover()

    def get_text(self, selector: str, timeout: Optional[int] = None) -> str:
        """
        Get text content of an element.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
            
        Returns:
            str: Text content of the element.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Getting text from element: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        text = element.text_content()
        logger.info(f"Element text: {text}")
        return text or ""

    def get_attribute(self, selector: str, attribute: str, timeout: Optional[int] = None) -> Optional[str]:
        """
        Get attribute value of an element.
        
        Args:
            selector: CSS selector for the element.
            attribute: Attribute name.
            timeout: Optional timeout in milliseconds.
            
        Returns:
            Optional[str]: Attribute value or None if not found.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Getting attribute '{attribute}' from element: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        value = element.get_attribute(attribute)
        logger.info(f"Attribute value: {value}")
        return value

    def select_option(self, selector: str, value: Optional[str] = None, label: Optional[str] = None, 
                     index: Optional[int] = None, timeout: Optional[int] = None) -> List[str]:
        """
        Select an option from a dropdown.
        
        Args:
            selector: CSS selector for the dropdown.
            value: Option value to select.
            label: Option label to select.
            index: Option index to select.
            timeout: Optional timeout in milliseconds.
            
        Returns:
            List[str]: List of selected values.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Selecting option from dropdown: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        
        if value:
            logger.info(f"Selecting by value: {value}")
            return element.select_option(value=value)
        elif label:
            logger.info(f"Selecting by label: {label}")
            return element.select_option(label=label)
        elif index is not None:
            logger.info(f"Selecting by index: {index}")
            return element.select_option(index=index)
        else:
            logger.warning("No selection criteria provided (value, label, or index)")
            return []

    def check(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Check a checkbox.
        
        Args:
            selector: CSS selector for the checkbox.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Checking checkbox: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        element.check()

    def uncheck(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Uncheck a checkbox.
        
        Args:
            selector: CSS selector for the checkbox.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Unchecking checkbox: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        element.uncheck()

    def is_checked(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Check if a checkbox is checked.
        
        Args:
            selector: CSS selector for the checkbox.
            timeout: Optional timeout in milliseconds.
            
        Returns:
            bool: True if checked, False otherwise.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Checking if checkbox is checked: {selector}")
        element = self.wait_for_selector(selector, timeout=wait_timeout)
        is_checked = element.is_checked()
        logger.info(f"Checkbox is checked: {is_checked}")
        return is_checked

    def is_visible(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Check if an element is visible.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
            
        Returns:
            bool: True if visible, False otherwise.
        """
        try:
            wait_timeout = timeout or TIMEOUT_SETTINGS["expect_timeout"]
            logger.info(f"Checking if element is visible: {selector}")
            element = self.page.locator(selector)
            expect(element).to_be_visible(timeout=wait_timeout)
            logger.info(f"Element is visible: {selector}")
            return True
        except TimeoutError:
            logger.info(f"Element is not visible: {selector}")
            return False

    def is_enabled(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Check if an element is enabled.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
            
        Returns:
            bool: True if enabled, False otherwise.
        """
        try:
            wait_timeout = timeout or TIMEOUT_SETTINGS["expect_timeout"]
            logger.info(f"Checking if element is enabled: {selector}")
            element = self.page.locator(selector)
            expect(element).to_be_enabled(timeout=wait_timeout)
            logger.info(f"Element is enabled: {selector}")
            return True
        except TimeoutError:
            logger.info(f"Element is not enabled: {selector}")
            return False

    def accept_alert(self, text: Optional[str] = None) -> None:
        """
        Accept an alert dialog.
        
        Args:
            text: Optional text to enter in prompt dialogs.
        """
        logger.info("Accepting alert dialog")
        self.page.on("dialog", lambda dialog: dialog.accept(text))

    def dismiss_alert(self) -> None:
        """Dismiss an alert dialog."""
        logger.info("Dismissing alert dialog")
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    def take_screenshot(self, test_name: str, description: Optional[str] = None) -> str:
        """
        Take a screenshot of the current page.
        
        Args:
            test_name: Name of the test.
            description: Optional description of the screenshot.
            
        Returns:
            str: Path to the saved screenshot.
        """
        return self.screenshot_utils.take_screenshot(self.page, test_name, description)

    def take_element_screenshot(self, selector: str, test_name: str, description: Optional[str] = None) -> str:
        """
        Take a screenshot of a specific element.
        
        Args:
            selector: CSS selector for the element.
            test_name: Name of the test.
            description: Optional description of the screenshot.
            
        Returns:
            str: Path to the saved screenshot.
        """
        return self.screenshot_utils.take_element_screenshot(self.page, selector, test_name, description)

    def wait_for_invisibility(self, selector: str, timeout: Optional[int] = None) -> None:
        """
        Wait for an element to become invisible.
        
        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.
        """
        wait_timeout = timeout or TIMEOUT_SETTINGS["default_timeout"]
        logger.info(f"Waiting for element to become invisible: {selector}")
        self.wait_for_selector(selector, timeout=wait_timeout, state="hidden") 