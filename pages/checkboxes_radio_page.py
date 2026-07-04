#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Checkboxes and Radio Buttons Page Object for WebDriverUniversity.
"""

import logging
from typing import Dict, List

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from utilities.screenshot_utils import ScreenshotUtils

logger = logging.getLogger("PlaywrightFramework")


class CheckboxesRadioPage(BasePage):
    """
    Page Object for the Checkboxes and Radio Buttons page.

    This page object uses Playwright role-based and label-based locators
    instead of raw CSS selectors wherever the demo page exposes usable
    accessibility information.

    URL:
        https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html
    """

    _URL = "https://webdriveruniversity.com/Dropdown-Checkboxes-RadioButtons/index.html"

    _PAGE_TITLE_TEXT = "Dropdown Menu(s), Checkboxe(s) & Radio Button(s)"
    _CHECKBOX_HEADER_TEXT = "Checkboxe(s)"
    _RADIO_BUTTON_HEADER_TEXT = "Radio Button(s)"
    _SELECTED_DISABLED_HEADER_TEXT = "Selected & Disabled"
    _FRUIT_DROPDOWN_HEADER_TEXT = "Dropdown Menu(s)"

    _CHECKBOX_LABELS: Dict[int, str] = {
        1: "Option 1",
        2: "Option 2",
        3: "Option 3",
        4: "Option 4",
    }

    _COLOR_RADIO_INDEXES: Dict[str, int] = {
        "green": 0,
        "blue": 1,
        "yellow": 2,
        "orange": 3,
        "purple": 4,
    }

    _VEGETABLE_RADIO_INDEXES: Dict[str, int] = {
        "lettuce": 5,
        "cabbage": 6,
        "pumpkin": 7,
    }

    def __init__(self, page: Page) -> None:
        """
        Initialize the Checkboxes and Radio Buttons page object.

        Args:
            page: Playwright page instance.
        """
        super().__init__(page)

        self.page_title: Locator = self.page.get_by_role(
            "heading",
            name=self._PAGE_TITLE_TEXT,
            exact=True,
        )

        self.checkbox_header: Locator = self.page.get_by_role(
            "heading",
            name=self._CHECKBOX_HEADER_TEXT,
            exact=True,
        )

        self.radio_button_header: Locator = self.page.get_by_role(
            "heading",
            name=self._RADIO_BUTTON_HEADER_TEXT,
            exact=True,
        )

        self.selected_disabled_header: Locator = self.page.get_by_role(
            "heading",
            name=self._SELECTED_DISABLED_HEADER_TEXT,
            exact=True,
        )

        self.fruit_dropdown_header: Locator = self.page.get_by_role(
            "heading",
            name=self._FRUIT_DROPDOWN_HEADER_TEXT,
            exact=True,
        )

        self.checkboxes: Locator = self.page.get_by_role("checkbox")
        self.radio_buttons: Locator = self.page.get_by_role("radio")
        self.fruit_dropdown: Locator = self.page.get_by_role("combobox").nth(3)

    def navigate(self) -> None:
        """
        Navigate to the Checkboxes and Radio Buttons page.
        """
        logger.info("Navigating to Checkboxes and Radio Buttons page: %s", self._URL)
        super().navigate_to(self._URL)

    def get_page_title(self) -> str:
        """
        Get the main page heading text.

        Returns:
            Main page heading text.
        """
        logger.info("Getting page title")
        return self._get_text_content(self.page_title)

    def get_checkbox_header(self) -> str:
        """
        Get the checkbox section header text.

        Returns:
            Checkbox section header text.
        """
        logger.info("Getting checkbox header text")
        return self._get_text_content(self.checkbox_header)

    def get_radio_button_header(self) -> str:
        """
        Get the radio button section header text.

        Returns:
            Radio button section header text.
        """
        logger.info("Getting radio button header text")
        return self._get_text_content(self.radio_button_header)

    def get_selected_disabled_header(self) -> str:
        """
        Get the selected and disabled section header text.

        Returns:
            Selected and disabled section header text.
        """
        logger.info("Getting selected and disabled header text")
        return self._get_text_content(self.selected_disabled_header)

    def get_fruit_dropdown_header(self) -> str:
        """
        Get the fruit dropdown section header text.

        Returns:
            Fruit dropdown section header text.
        """
        logger.info("Getting fruit dropdown header text")
        return self._get_text_content(self.fruit_dropdown_header)

    def is_checkbox_checked(self, checkbox_number: int) -> bool:
        """
        Check whether a checkbox is selected.

        Args:
            checkbox_number: Checkbox number from 1 to 4.

        Returns:
            True if the checkbox is selected, otherwise False.

        Raises:
            ValueError: If the checkbox number is invalid.
        """
        logger.info("Checking if checkbox %s is checked", checkbox_number)
        return self._get_checkbox(checkbox_number).is_checked()

    def check_checkbox(self, checkbox_number: int) -> None:
        """
        Select a checkbox if it is not already selected.

        Args:
            checkbox_number: Checkbox number from 1 to 4.

        Raises:
            ValueError: If the checkbox number is invalid.
        """
        logger.info("Checking checkbox %s", checkbox_number)

        checkbox = self._get_checkbox(checkbox_number)
        if not checkbox.is_checked():
            checkbox.check()

    def uncheck_checkbox(self, checkbox_number: int) -> None:
        """
        Clear a checkbox if it is currently selected.

        Args:
            checkbox_number: Checkbox number from 1 to 4.

        Raises:
            ValueError: If the checkbox number is invalid.
        """
        logger.info("Unchecking checkbox %s", checkbox_number)

        checkbox = self._get_checkbox(checkbox_number)
        if checkbox.is_checked():
            checkbox.uncheck()

    def toggle_checkbox(self, checkbox_number: int) -> None:
        """
        Toggle a checkbox state.

        Args:
            checkbox_number: Checkbox number from 1 to 4.

        Raises:
            ValueError: If the checkbox number is invalid.
        """
        logger.info("Toggling checkbox %s", checkbox_number)

        checkbox = self._get_checkbox(checkbox_number)
        if checkbox.is_checked():
            checkbox.uncheck()
        else:
            checkbox.check()

    def get_all_checkboxes_state(self) -> Dict[str, bool]:
        """
        Get the selected state of all checkboxes.

        Returns:
            Dictionary containing checkbox names and their selected states.
        """
        logger.info("Getting state of all checkboxes")

        return {
            f"checkbox_{checkbox_number}": self.is_checkbox_checked(checkbox_number)
            for checkbox_number in self._CHECKBOX_LABELS
        }

    def select_radio_button(self, color: str) -> None:
        """
        Select a color radio button.

        Args:
            color: Color radio option to select.
                Supported values: green, blue, yellow, orange, purple.

        Raises:
            ValueError: If the color is invalid.
        """
        normalized_color = color.lower()
        logger.info("Selecting color radio button: %s", normalized_color)

        self._get_color_radio(normalized_color).check()

    def get_selected_radio_button(self) -> str:
        """
        Get the selected color radio button.

        Returns:
            Selected color value, or an empty string if none is selected.
        """
        logger.info("Getting selected color radio button")

        for color in self._COLOR_RADIO_INDEXES:
            if self._get_color_radio(color).is_checked():
                return color

        return ""

    def is_radio_disabled(self, vegetable: str) -> bool:
        """
        Check whether a vegetable radio button is disabled.

        Args:
            vegetable: Vegetable radio option to check.
                Supported values: lettuce, cabbage, pumpkin.

        Returns:
            True if the radio button is disabled, otherwise False.

        Raises:
            ValueError: If the vegetable name is invalid.
        """
        normalized_vegetable = vegetable.lower()
        logger.info(
            "Checking if vegetable radio button is disabled: %s",
            normalized_vegetable,
        )

        return self._get_vegetable_radio(normalized_vegetable).is_disabled()

    def select_vegetable_radio(self, vegetable: str) -> None:
        """
        Select a vegetable radio button when it is enabled.

        Args:
            vegetable: Vegetable radio option to select.
                Supported values: lettuce, cabbage, pumpkin.

        Raises:
            ValueError: If the vegetable name is invalid.
        """
        normalized_vegetable = vegetable.lower()
        logger.info("Selecting vegetable radio button: %s", normalized_vegetable)

        vegetable_radio = self._get_vegetable_radio(normalized_vegetable)

        if vegetable_radio.is_disabled():
            logger.warning(
                "Vegetable radio button '%s' is disabled and cannot be selected",
                normalized_vegetable,
            )
            return

        vegetable_radio.check()

    def get_selected_vegetable_radio(self) -> str:
        """
        Get the selected vegetable radio button.

        Returns:
            Selected vegetable value, or an empty string if none is selected.
        """
        logger.info("Getting selected vegetable radio button")

        for vegetable in self._VEGETABLE_RADIO_INDEXES:
            if self._get_vegetable_radio(vegetable).is_checked():
                return vegetable

        return ""

    def select_fruit(self, fruit: str) -> None:
        """
        Select a fruit from the fruit dropdown.

        Args:
            fruit: Fruit option value to select.
        """
        logger.info("Selecting fruit: %s", fruit)
        self.fruit_dropdown.select_option(value=fruit)

    def get_selected_fruit(self) -> str:
        """
        Get the selected fruit value.

        Returns:
            Selected fruit option value.
        """
        logger.info("Getting selected fruit")
        return self.fruit_dropdown.input_value()

    def get_available_fruits(self) -> List[str]:
        """
        Get all available fruit option values from the fruit dropdown.

        Returns:
            List of fruit option values.
        """
        logger.info("Getting available fruits")

        fruit_values: List[str] = []
        options = self.fruit_dropdown.get_by_role("option").all()

        for option in options:
            value = option.get_attribute("value")
            if value is not None:
                fruit_values.append(value)

        logger.info("Available fruits: %s", fruit_values)
        return fruit_values

    def take_screenshot(self, test_name: str, screenshot_name: str) -> str:
        """
        Take a screenshot of the current page state.

        Args:
            test_name: Name of the test.
            screenshot_name: Name for the screenshot.

        Returns:
            Path to the saved screenshot.
        """
        logger.info("Taking screenshot for test '%s': %s", test_name, screenshot_name)

        return ScreenshotUtils.take_screenshot(
            self.page,
            f"{test_name}_{screenshot_name}",
        )

    def _get_checkbox(self, checkbox_number: int) -> Locator:
        """
        Get a checkbox locator by checkbox number.

        Args:
            checkbox_number: Checkbox number from 1 to 4.

        Returns:
            Playwright locator for the checkbox.

        Raises:
            ValueError: If the checkbox number is invalid.
        """
        if checkbox_number not in self._CHECKBOX_LABELS:
            raise ValueError(
                f"Invalid checkbox number '{checkbox_number}'. "
                f"Supported values: {list(self._CHECKBOX_LABELS.keys())}"
            )

        return self.checkboxes.nth(checkbox_number - 1)

    def _get_color_radio(self, color: str) -> Locator:
        """
        Get a color radio button locator by color name.

        Args:
            color: Color radio option.
                Supported values: green, blue, yellow, orange, purple.

        Returns:
            Playwright locator for the color radio button.

        Raises:
            ValueError: If the color is invalid.
        """
        if color not in self._COLOR_RADIO_INDEXES:
            raise ValueError(
                f"Invalid color radio option '{color}'. "
                f"Supported values: {list(self._COLOR_RADIO_INDEXES.keys())}"
            )

        return self.radio_buttons.nth(self._COLOR_RADIO_INDEXES[color])

    def _get_vegetable_radio(self, vegetable: str) -> Locator:
        """
        Get a vegetable radio button locator by vegetable name.

        Args:
            vegetable: Vegetable radio option.
                Supported values: lettuce, cabbage, pumpkin.

        Returns:
            Playwright locator for the vegetable radio button.

        Raises:
            ValueError: If the vegetable name is invalid.
        """
        if vegetable not in self._VEGETABLE_RADIO_INDEXES:
            raise ValueError(
                f"Invalid vegetable radio option '{vegetable}'. "
                f"Supported values: {list(self._VEGETABLE_RADIO_INDEXES.keys())}"
            )

        return self.radio_buttons.nth(self._VEGETABLE_RADIO_INDEXES[vegetable])

    @staticmethod
    def _get_text_content(locator: Locator) -> str:
        """
        Get normalized DOM text content from a locator.

        This intentionally uses text_content instead of inner_text because
        some headings on this demo page are visually transformed to uppercase.

        Args:
            locator: Playwright locator.

        Returns:
            Normalized text content, or an empty string if no text is found.
        """
        locator.wait_for(state="visible")
        text = locator.text_content()
        return text.strip() if text else ""