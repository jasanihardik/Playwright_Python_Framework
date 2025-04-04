#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Checkboxes and Radio Buttons Page Object for WebdriverUniversity
"""

import logging
from typing import List, Optional, Union, Dict, Any

from playwright.sync_api import Page

from pages.base_page import BasePage
from utilities.screenshot_utils import ScreenshotUtils

logger = logging.getLogger("PlaywrightFramework")


class CheckboxesRadioPage(BasePage):
    """
    Page Object for the Checkboxes and Radio Buttons page.
    URL: https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html
    """

    # Page URL
    _URL = "https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html"

    # Page selectors
    _PAGE_TITLE = "h1"
    _CHECKBOX_HEADER = "h2"
    _RADIO_BUTTON_HEADER = "h2"
    _SELECTED_DISABLED_HEADER = "h2"
    _FRUIT_DROPDOWN_HEADER = "h2"
    
    # Checkboxes selectors
    _CHECKBOXES = "input[type='checkbox']"
    _CHECKBOX_1 = "input[value='option-1']"
    _CHECKBOX_2 = "input[value='option-2']"
    _CHECKBOX_3 = "input[value='option-3']"
    _CHECKBOX_4 = "input[value='option-4']"
    
    # Radio buttons selectors
    _RADIO_BUTTONS = "input[type='radio'][name='color']"
    _RADIO_GREEN = "input[value='green']"
    _RADIO_BLUE = "input[value='blue']"
    _RADIO_YELLOW = "input[value='yellow']"
    _RADIO_ORANGE = "input[value='orange']"
    _RADIO_PURPLE = "input[value='purple']"
    
    # Selected & Disabled selectors
    _SELECTED_DISABLED_RADIOS = "input[type='radio'][name='vegetable']"
    _RADIO_LETTUCE = "input[value='lettuce']"
    _RADIO_CABBAGE = "input[value='cabbage']"
    _RADIO_PUMPKIN = "input[value='pumpkin']"
    
    # Fruit dropdown selectors
    _FRUIT_DROPDOWN = "#fruit-selects"
    _FRUIT_OPTIONS = "#fruit-selects option"

    def __init__(self, page: Page) -> None:
        """
        Initialize the Checkboxes and Radio Buttons page object.

        Args:
            page: Playwright page object
        """
        super().__init__(page)

    def navigate(self) -> None:
        """
        Navigate to the Checkboxes and Radio Buttons page.
        """
        logger.info(f"Navigating to Checkboxes and Radio Buttons page: {self._URL}")
        super().navigate_to(self._URL)
        
    def get_page_title(self) -> str:
        """
        Get the page title text.

        Returns:
            str: The page title text
        """
        logger.info("Getting page title")
        return self.get_text(self._PAGE_TITLE)

    # Checkbox methods
    def get_checkbox_header(self) -> str:
        """
        Get the checkbox section header text.

        Returns:
            str: The checkbox section header text
        """
        logger.info("Getting checkbox header text")
        # Find all h2 elements and get the one with "Checkboxe(s)" text
        h2_elements = self.page.query_selector_all(self._CHECKBOX_HEADER)
        for element in h2_elements:
            text = element.inner_text()
            if "Checkboxe(s)" in text:
                return text
        return ""

    def is_checkbox_checked(self, checkbox_number: int) -> bool:
        """
        Check if a checkbox is checked.

        Args:
            checkbox_number: The checkbox number (1-4)

        Returns:
            bool: True if the checkbox is checked, False otherwise
        """
        checkbox_selector = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Checking if checkbox {checkbox_number} is checked")
        return self.is_checked(checkbox_selector)

    def check_checkbox(self, checkbox_number: int) -> None:
        """
        Check a checkbox if it's not already checked.

        Args:
            checkbox_number: The checkbox number (1-4)
        """
        checkbox_selector = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Checking checkbox {checkbox_number}")
        if not self.is_checked(checkbox_selector):
            self.check(checkbox_selector)

    def uncheck_checkbox(self, checkbox_number: int) -> None:
        """
        Uncheck a checkbox if it's checked.

        Args:
            checkbox_number: The checkbox number (1-4)
        """
        checkbox_selector = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Unchecking checkbox {checkbox_number}")
        if self.is_checked(checkbox_selector):
            self.uncheck(checkbox_selector)

    def toggle_checkbox(self, checkbox_number: int) -> None:
        """
        Toggle a checkbox state.

        Args:
            checkbox_number: The checkbox number (1-4)
        """
        checkbox_selector = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Toggling checkbox {checkbox_number}")
        if self.is_checked(checkbox_selector):
            self.uncheck(checkbox_selector)
        else:
            self.check(checkbox_selector)

    def get_all_checkboxes_state(self) -> Dict[str, bool]:
        """
        Get the state of all checkboxes.

        Returns:
            Dict[str, bool]: Dictionary with checkbox numbers as keys and their checked state as values
        """
        logger.info("Getting state of all checkboxes")
        states = {}
        for i in range(1, 5):
            checkbox_selector = getattr(self, f"_CHECKBOX_{i}")
            states[f"checkbox_{i}"] = self.is_checked(checkbox_selector)
        return states

    # Radio button methods
    def get_radio_button_header(self) -> str:
        """
        Get the radio button section header text.

        Returns:
            str: The radio button section header text
        """
        logger.info("Getting radio button header text")
        # Find all h2 elements and get the one with "Radio Button(s)" text
        h2_elements = self.page.query_selector_all(self._RADIO_BUTTON_HEADER)
        for element in h2_elements:
            text = element.inner_text()
            if "Radio Button(s)" in text:
                return text
        return ""

    def select_radio_button(self, color: str) -> None:
        """
        Select a radio button by color.

        Args:
            color: The color to select (green, blue, yellow, orange, purple)
        """
        radio_selector = getattr(self, f"_RADIO_{color.upper()}")
        logger.info(f"Selecting radio button: {color}")
        self.click(radio_selector)

    def get_selected_radio_button(self) -> str:
        """
        Get the selected radio button color.

        Returns:
            str: The selected radio button color or empty string if none selected
        """
        logger.info("Getting selected radio button")
        colors = ["green", "blue", "yellow", "orange", "purple"]
        for color in colors:
            radio_selector = getattr(self, f"_RADIO_{color.upper()}")
            if self.is_checked(radio_selector):
                return color
        return ""

    # Selected & Disabled methods
    def get_selected_disabled_header(self) -> str:
        """
        Get the selected & disabled section header text.

        Returns:
            str: The selected & disabled section header text
        """
        logger.info("Getting selected & disabled header text")
        # Find all h2 elements and get the one with "Selected & Disabled" text
        h2_elements = self.page.query_selector_all(self._SELECTED_DISABLED_HEADER)
        for element in h2_elements:
            text = element.inner_text()
            if "Selected & Disabled" in text:
                return text
        return ""

    def is_radio_disabled(self, vegetable: str) -> bool:
        """
        Check if a vegetable radio button is disabled.

        Args:
            vegetable: The vegetable to check (lettuce, cabbage, pumpkin)

        Returns:
            bool: True if the radio button is disabled, False otherwise
        """
        radio_selector = getattr(self, f"_RADIO_{vegetable.upper()}")
        logger.info(f"Checking if radio button {vegetable} is disabled")
        return self.is_disabled(radio_selector)

    def select_vegetable_radio(self, vegetable: str) -> None:
        """
        Select a vegetable radio button.

        Args:
            vegetable: The vegetable to select (lettuce, cabbage, pumpkin)
        """
        radio_selector = getattr(self, f"_RADIO_{vegetable.upper()}")
        logger.info(f"Selecting vegetable radio button: {vegetable}")
        if not self.is_disabled(radio_selector):
            self.click(radio_selector)
        else:
            logger.warning(f"Radio button {vegetable} is disabled and cannot be selected")

    def get_selected_vegetable_radio(self) -> str:
        """
        Get the selected vegetable radio button.

        Returns:
            str: The selected vegetable radio button or empty string if none selected
        """
        logger.info("Getting selected vegetable radio button")
        vegetables = ["lettuce", "cabbage", "pumpkin"]
        for vegetable in vegetables:
            radio_selector = getattr(self, f"_RADIO_{vegetable.upper()}")
            if self.is_checked(radio_selector):
                return vegetable
        return ""

    # Fruit dropdown methods
    def get_fruit_dropdown_header(self) -> str:
        """
        Get the fruit dropdown section header text.

        Returns:
            str: The fruit dropdown section header text
        """
        logger.info("Getting fruit dropdown header text")
        # Find all h2 elements and get the one with "Dropdown Menu(s)" text
        h2_elements = self.page.query_selector_all(self._FRUIT_DROPDOWN_HEADER)
        for element in h2_elements:
            text = element.inner_text()
            if "Dropdown Menu(s)" in text:
                return text
        return ""

    def select_fruit(self, fruit: str) -> None:
        """
        Select a fruit from the dropdown.

        Args:
            fruit: The fruit to select
        """
        logger.info(f"Selecting fruit: {fruit}")
        self.select_option(self._FRUIT_DROPDOWN, value=fruit)

    def get_selected_fruit(self) -> str:
        """
        Get the selected fruit.

        Returns:
            str: The selected fruit
        """
        logger.info("Getting selected fruit")
        return self.get_selected_value(self._FRUIT_DROPDOWN)

    def get_available_fruits(self) -> List[str]:
        """
        Get all available fruits in the dropdown.

        Returns:
            List[str]: List of available fruits
        """
        logger.info("Getting available fruits")
        return self.get_option_values(self._FRUIT_DROPDOWN)

    def take_screenshot(self, test_name: str, screenshot_name: str) -> str:
        """
        Take a screenshot of the current page state.

        Args:
            test_name: The name of the test
            screenshot_name: The name for the screenshot

        Returns:
            str: The path to the saved screenshot
        """
        return ScreenshotUtils.take_screenshot(self.page, f"{test_name}_{screenshot_name}")

    def is_disabled(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Check if an element is disabled.

        Args:
            selector: CSS selector for the element.
            timeout: Optional timeout in milliseconds.

        Returns:
            bool: True if the element is disabled, False otherwise.
        """
        try:
            element = self.wait_for_selector(selector, timeout=timeout)
            return element.is_disabled()
        except Exception as e:
            logger.error(f"Error checking if element is disabled: {str(e)}")
            return False

    def get_option_values(self, selector: str, timeout: Optional[int] = None) -> List[str]:
        """
        Get all option values from a dropdown.

        Args:
            selector: CSS selector for the dropdown.
            timeout: Optional timeout in milliseconds.

        Returns:
            List[str]: List of option values.
        """
        logger.info(f"Getting option values from dropdown: {selector}")
        try:
            dropdown = self.wait_for_selector(selector, timeout=timeout)
            options = self.page.evaluate("""(selector) => {
                const options = Array.from(document.querySelector(selector).options);
                return options.map(option => option.value);
            }""", selector)
            logger.info(f"Found options: {options}")
            return options
        except Exception as e:
            logger.error(f"Error getting option values: {str(e)}")
            return []

    def get_selected_value(self, selector: str, timeout: Optional[int] = None) -> str:
        """
        Get the selected value from a dropdown.

        Args:
            selector: CSS selector for the dropdown.
            timeout: Optional timeout in milliseconds.

        Returns:
            str: The selected option value.
        """
        logger.info(f"Getting selected value from dropdown: {selector}")
        try:
            dropdown = self.wait_for_selector(selector, timeout=timeout)
            value = self.page.evaluate("""(selector) => {
                const select = document.querySelector(selector);
                return select.options[select.selectedIndex].value;
            }""", selector)
            logger.info(f"Selected value: {value}")
            return value
        except Exception as e:
            logger.error(f"Error getting selected value: {str(e)}")
            return "" 