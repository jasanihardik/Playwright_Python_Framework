#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Checkboxes and Radio Buttons Page Object for WebDriverUniversity.
"""

import logging
from typing import Dict, List, Optional

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utilities.screenshot_utils import ScreenshotUtils

logger = logging.getLogger("PlaywrightFramework")


class CheckboxesRadioPage(BasePage):
    """
    Page Object for the Checkboxes and Radio Buttons page.

    URL:
        https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html
    """

    # Page URL
    _URL = "https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html"

    # Page text
    _PAGE_TITLE = "Dropdown Menu(s), Checkboxe(s) & Radio Button(s)"
    _CHECKBOX_HEADER = "Checkboxe(s)"
    _RADIO_BUTTON_HEADER = "Radio Button(s)"
    _SELECTED_DISABLED_HEADER = "Selected & Disabled"
    _FRUIT_DROPDOWN_HEADER = "Dropdown Menu(s)"

    # Checkbox indexes
    _CHECKBOX_1 = 0
    _CHECKBOX_2 = 1
    _CHECKBOX_3 = 2
    _CHECKBOX_4 = 3

    # Color radio indexes
    _RADIO_GREEN = 0
    _RADIO_BLUE = 1
    _RADIO_YELLOW = 2
    _RADIO_ORANGE = 3
    _RADIO_PURPLE = 4

    # Vegetable radio indexes
    _RADIO_LETTUCE = 5
    _RADIO_CABBAGE = 6
    _RADIO_PUMPKIN = 7

    # Fruit dropdown index
    _FRUIT_DROPDOWN = 3

    def __init__(self, page: Page) -> None:
        """
        Initialize the Checkboxes and Radio Buttons page object.

        Args:
            page: Playwright page object.
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
            str: The page title text.
        """
        logger.info("Getting page title")

        title = self.page.get_by_role(
            "heading",
            name=self._PAGE_TITLE,
            exact=True,
        )

        text = title.text_content()
        return text.strip() if text else ""

    def get_checkbox_header(self) -> str:
        """
        Get the checkbox section header text.

        Returns:
            str: The checkbox section header text.
        """
        logger.info("Getting checkbox header text")

        header = self.page.get_by_role(
            "heading",
            name=self._CHECKBOX_HEADER,
            exact=True,
        )

        text = header.text_content()
        return text.strip() if text else ""

    def is_checkbox_checked(self, checkbox_number: int) -> bool:
        """
        Check if a checkbox is checked.

        Args:
            checkbox_number: The checkbox number from 1 to 4.

        Returns:
            bool: True if the checkbox is checked, False otherwise.
        """
        checkbox_index = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Checking if checkbox {checkbox_number} is checked")

        return self.page.get_by_role("checkbox").nth(checkbox_index).is_checked()

    def check_checkbox(self, checkbox_number: int) -> None:
        """
        Check a checkbox if it is not already checked.

        Args:
            checkbox_number: The checkbox number from 1 to 4.
        """
        checkbox_index = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Checking checkbox {checkbox_number}")

        checkbox = self.page.get_by_role("checkbox").nth(checkbox_index)

        if not checkbox.is_checked():
            checkbox.check()

    def uncheck_checkbox(self, checkbox_number: int) -> None:
        """
        Uncheck a checkbox if it is checked.

        Args:
            checkbox_number: The checkbox number from 1 to 4.
        """
        checkbox_index = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Unchecking checkbox {checkbox_number}")

        checkbox = self.page.get_by_role("checkbox").nth(checkbox_index)

        if checkbox.is_checked():
            checkbox.uncheck()

    def toggle_checkbox(self, checkbox_number: int) -> None:
        """
        Toggle a checkbox state.

        Args:
            checkbox_number: The checkbox number from 1 to 4.
        """
        checkbox_index = getattr(self, f"_CHECKBOX_{checkbox_number}")
        logger.info(f"Toggling checkbox {checkbox_number}")

        checkbox = self.page.get_by_role("checkbox").nth(checkbox_index)

        if checkbox.is_checked():
            checkbox.uncheck()
        else:
            checkbox.check()

    def get_all_checkboxes_state(self) -> Dict[str, bool]:
        """
        Get the state of all checkboxes.

        Returns:
            Dict[str, bool]: Dictionary with checkbox numbers as keys and their checked state as values.
        """
        logger.info("Getting state of all checkboxes")

        states = {}

        for checkbox_number in range(1, 5):
            states[f"checkbox_{checkbox_number}"] = self.is_checkbox_checked(
                checkbox_number,
            )

        return states

    def get_radio_button_header(self) -> str:
        """
        Get the radio button section header text.

        Returns:
            str: The radio button section header text.
        """
        logger.info("Getting radio button header text")

        header = self.page.get_by_role(
            "heading",
            name=self._RADIO_BUTTON_HEADER,
            exact=True,
        )

        text = header.text_content()
        return text.strip() if text else ""

    def select_radio_button(self, color: str) -> None:
        """
        Select a radio button by color.

        Args:
            color: The color to select. Supported values are green, blue, yellow, orange, and purple.
        """
        radio_index = getattr(self, f"_RADIO_{color.upper()}")
        logger.info(f"Selecting radio button: {color}")

        self.page.get_by_role("radio").nth(radio_index).check()

    def get_selected_radio_button(self) -> str:
        """
        Get the selected radio button color.

        Returns:
            str: The selected radio button color or empty string if none is selected.
        """
        logger.info("Getting selected radio button")

        colors = ["green", "blue", "yellow", "orange", "purple"]

        for color in colors:
            radio_index = getattr(self, f"_RADIO_{color.upper()}")

            if self.page.get_by_role("radio").nth(radio_index).is_checked():
                return color

        return ""

    def get_selected_disabled_header(self) -> str:
        """
        Get the selected and disabled section header text.

        Returns:
            str: The selected and disabled section header text.
        """
        logger.info("Getting selected and disabled header text")

        header = self.page.get_by_role(
            "heading",
            name=self._SELECTED_DISABLED_HEADER,
            exact=True,
        )

        text = header.text_content()
        return text.strip() if text else ""

    def is_radio_disabled(self, vegetable: str) -> bool:
        """
        Check if a vegetable radio button is disabled.

        Args:
            vegetable: The vegetable to check. Supported values are lettuce, cabbage, and pumpkin.

        Returns:
            bool: True if the radio button is disabled, False otherwise.
        """
        radio_index = getattr(self, f"_RADIO_{vegetable.upper()}")
        logger.info(f"Checking if radio button {vegetable} is disabled")

        return self.page.get_by_role("radio").nth(radio_index).is_disabled()

    def select_vegetable_radio(self, vegetable: str) -> None:
        """
        Select a vegetable radio button.

        Args:
            vegetable: The vegetable to select. Supported values are lettuce, cabbage, and pumpkin.
        """
        radio_index = getattr(self, f"_RADIO_{vegetable.upper()}")
        logger.info(f"Selecting vegetable radio button: {vegetable}")

        radio_button = self.page.get_by_role("radio").nth(radio_index)

        if not radio_button.is_disabled():
            radio_button.check()
        else:
            logger.warning(
                f"Radio button {vegetable} is disabled and cannot be selected"
            )

    def get_selected_vegetable_radio(self) -> str:
        """
        Get the selected vegetable radio button.

        Returns:
            str: The selected vegetable radio button or empty string if none is selected.
        """
        logger.info("Getting selected vegetable radio button")

        vegetables = ["lettuce", "cabbage", "pumpkin"]

        for vegetable in vegetables:
            radio_index = getattr(self, f"_RADIO_{vegetable.upper()}")

            if self.page.get_by_role("radio").nth(radio_index).is_checked():
                return vegetable

        return ""

    def get_fruit_dropdown_header(self) -> str:
        """
        Get the fruit dropdown section header text.

        Returns:
            str: The fruit dropdown section header text.
        """
        logger.info("Getting fruit dropdown header text")

        header = self.page.get_by_role(
            "heading",
            name=self._FRUIT_DROPDOWN_HEADER,
            exact=True,
        )

        text = header.text_content()
        return text.strip() if text else ""

    def select_fruit(self, fruit: str) -> None:
        """
        Select a fruit from the dropdown.

        Args:
            fruit: The fruit to select.
        """
        logger.info(f"Selecting fruit: {fruit}")

        self.page.get_by_role("combobox").nth(self._FRUIT_DROPDOWN).select_option(
            value=fruit,
        )

    def get_selected_fruit(self) -> str:
        """
        Get the selected fruit.

        Returns:
            str: The selected fruit.
        """
        logger.info("Getting selected fruit")

        return self.page.get_by_role("combobox").nth(
            self._FRUIT_DROPDOWN,
        ).input_value()

    def get_available_fruits(self) -> List[str]:
        """
        Get all available fruits in the dropdown.

        Returns:
            List[str]: List of available fruits.
        """
        logger.info("Getting available fruits")

        fruit_dropdown = self.page.get_by_role("combobox").nth(self._FRUIT_DROPDOWN)
        options = fruit_dropdown.get_by_role("option").all()

        fruits = []

        for option in options:
            value = option.get_attribute("value")
            if value:
                fruits.append(value)

        logger.info(f"Available fruits: {fruits}")

        return fruits

    def take_screenshot(self, test_name: str, screenshot_name: str) -> str:
        """
        Take a screenshot of the current page state.

        Args:
            test_name: The name of the test.
            screenshot_name: The name for the screenshot.

        Returns:
            str: The path to the saved screenshot.
        """
        return ScreenshotUtils.take_screenshot(
            self.page,
            f"{test_name}_{screenshot_name}",
        )

    def is_disabled(self, selector: str, timeout: Optional[int] = None) -> bool:
        """
        Check if an element is disabled.

        Args:
            selector: Selector for the element.
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
            selector: Selector for the dropdown.
            timeout: Optional timeout in milliseconds.

        Returns:
            List[str]: List of option values.
        """
        logger.info(f"Getting option values from dropdown: {selector}")

        try:
            dropdown = self.wait_for_selector(selector, timeout=timeout)
            options = dropdown.query_selector_all("option")

            values = []

            for option in options:
                value = option.get_attribute("value")
                if value:
                    values.append(value)

            logger.info(f"Found options: {values}")

            return values
        except Exception as e:
            logger.error(f"Error getting option values: {str(e)}")
            return []

    def get_selected_value(self, selector: str, timeout: Optional[int] = None) -> str:
        """
        Get the selected value from a dropdown.

        Args:
            selector: Selector for the dropdown.
            timeout: Optional timeout in milliseconds.

        Returns:
            str: The selected option value.
        """
        logger.info(f"Getting selected value from dropdown: {selector}")

        try:
            dropdown = self.wait_for_selector(selector, timeout=timeout)
            value = dropdown.input_value()

            logger.info(f"Selected value: {value}")

            return value
        except Exception as e:
            logger.error(f"Error getting selected value: {str(e)}")
            return ""