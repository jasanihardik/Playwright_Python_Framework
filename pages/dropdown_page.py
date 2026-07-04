"""
Page object for the Dropdown, Checkboxes & Radio Buttons page.
"""

from typing import List, Optional

from playwright.sync_api import Locator, Page, expect

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class DropdownPage(BasePage):
    """Page object representing the Dropdown, Checkboxes & Radio Buttons page."""

    # Page text
    _PAGE_HEADER = "Dropdown Menu(s), Checkboxe(s) & Radio Button(s)"

    # Dropdown indexes
    _DROPDOWN_1 = 0
    _DROPDOWN_2 = 1
    _DROPDOWN_3 = 2
    _DROPDOWN_FRUIT = 3

    # Checkbox indexes
    _CHECKBOX_1 = 0
    _CHECKBOX_2 = 1
    _CHECKBOX_3 = 2
    _CHECKBOX_4 = 3

    # Color radio button indexes
    _RADIO_BUTTON_GREEN = 0
    _RADIO_BUTTON_BLUE = 1
    _RADIO_BUTTON_YELLOW = 2
    _RADIO_BUTTON_ORANGE = 3
    _RADIO_BUTTON_PURPLE = 4

    # Selected & disabled radio button indexes
    _RADIO_BUTTON_LETTUCE = 5
    _RADIO_BUTTON_CABBAGE = 6
    _RADIO_BUTTON_PUMPKIN = 7

    # Disabled checkbox indexes, only used by skipped disabled-elements test
    _CHECKBOX_OPTION_1 = 4
    _CHECKBOX_OPTION_2 = 5

    # Fruit option labels
    _FRUIT_LABELS = {
        "apple": "Apple",
        "orange": "Orange",
        "pear": "Pear",
        "grape": "Grape",
    }

    def __init__(self, page: Page):
        """
        Initialize the Dropdown page.

        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["dropdown"]

        self.page_header: Locator = self.page.get_by_role(
            "heading",
            name=self._PAGE_HEADER,
        )

        self.dropdowns: Locator = self.page.get_by_role("combobox")
        self.checkboxes: Locator = self.page.get_by_role("checkbox")
        self.radio_buttons: Locator = self.page.get_by_role("radio")

    def navigate(self) -> None:
        """Navigate to the Dropdown page."""
        logger.info(f"Navigating to Dropdown page: {self.url}")
        self.navigate_to(self.url)
        expect(self.page_header).to_be_visible(timeout=10000)

    def get_page_header(self) -> str:
        """
        Get the page header text.

        Returns:
            str: The page header text.
        """
        logger.info("Getting page header text")

        text = self.page_header.text_content()
        return text.strip() if text else ""

    # Dropdown methods
    def select_dropdown_1_value(self, value: str) -> List[str]:
        """
        Select a value from the first dropdown.

        Args:
            value: Value to select.

        Returns:
            List[str]: List of selected values.
        """
        return self._select_dropdown_value(self._DROPDOWN_1, value)

    def select_dropdown_2_value(self, value: str) -> List[str]:
        """
        Select a value from the second dropdown.

        Args:
            value: Value to select.

        Returns:
            List[str]: List of selected values.
        """
        return self._select_dropdown_value(self._DROPDOWN_2, value)

    def select_dropdown_3_value(self, value: str) -> List[str]:
        """
        Select a value from the third dropdown.

        Args:
            value: Value to select.

        Returns:
            List[str]: List of selected values.
        """
        return self._select_dropdown_value(self._DROPDOWN_3, value)

    def get_dropdown_1_value(self) -> Optional[str]:
        """
        Get the selected value from the first dropdown.

        Returns:
            Optional[str]: The selected value or None.
        """
        return self._get_dropdown_value(self._DROPDOWN_1)

    def get_dropdown_2_value(self) -> Optional[str]:
        """
        Get the selected value from the second dropdown.

        Returns:
            Optional[str]: The selected value or None.
        """
        return self._get_dropdown_value(self._DROPDOWN_2)

    def get_dropdown_3_value(self) -> Optional[str]:
        """
        Get the selected value from the third dropdown.

        Returns:
            Optional[str]: The selected value or None.
        """
        return self._get_dropdown_value(self._DROPDOWN_3)

    # Checkbox methods
    def check_checkbox_1(self) -> None:
        """Check the first checkbox."""
        self._set_checkbox_state(self._CHECKBOX_1, checked=True)

    def check_checkbox_2(self) -> None:
        """Check the second checkbox."""
        self._set_checkbox_state(self._CHECKBOX_2, checked=True)

    def check_checkbox_3(self) -> None:
        """Check the third checkbox."""
        self._set_checkbox_state(self._CHECKBOX_3, checked=True)

    def check_checkbox_4(self) -> None:
        """Check the fourth checkbox."""
        self._set_checkbox_state(self._CHECKBOX_4, checked=True)

    def uncheck_checkbox_1(self) -> None:
        """Uncheck the first checkbox."""
        self._set_checkbox_state(self._CHECKBOX_1, checked=False)

    def uncheck_checkbox_2(self) -> None:
        """Uncheck the second checkbox."""
        self._set_checkbox_state(self._CHECKBOX_2, checked=False)

    def uncheck_checkbox_3(self) -> None:
        """Uncheck the third checkbox."""
        self._set_checkbox_state(self._CHECKBOX_3, checked=False)

    def uncheck_checkbox_4(self) -> None:
        """Uncheck the fourth checkbox."""
        self._set_checkbox_state(self._CHECKBOX_4, checked=False)

    def is_checkbox_1_checked(self) -> bool:
        """
        Check if the first checkbox is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_checkbox_checked(self._CHECKBOX_1)

    def is_checkbox_2_checked(self) -> bool:
        """
        Check if the second checkbox is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_checkbox_checked(self._CHECKBOX_2)

    def is_checkbox_3_checked(self) -> bool:
        """
        Check if the third checkbox is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_checkbox_checked(self._CHECKBOX_3)

    def is_checkbox_4_checked(self) -> bool:
        """
        Check if the fourth checkbox is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_checkbox_checked(self._CHECKBOX_4)

    # Radio button methods
    def select_radio_button_green(self) -> None:
        """Select the green radio button."""
        self._select_radio_button(self._RADIO_BUTTON_GREEN)

    def select_radio_button_blue(self) -> None:
        """Select the blue radio button."""
        self._select_radio_button(self._RADIO_BUTTON_BLUE)

    def select_radio_button_yellow(self) -> None:
        """Select the yellow radio button."""
        self._select_radio_button(self._RADIO_BUTTON_YELLOW)

    def select_radio_button_orange(self) -> None:
        """Select the orange radio button."""
        self._select_radio_button(self._RADIO_BUTTON_ORANGE)

    def select_radio_button_purple(self) -> None:
        """Select the purple radio button."""
        self._select_radio_button(self._RADIO_BUTTON_PURPLE)

    def is_radio_button_green_checked(self) -> bool:
        """
        Check if the green radio button is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_radio_button_checked(self._RADIO_BUTTON_GREEN)

    def is_radio_button_blue_checked(self) -> bool:
        """
        Check if the blue radio button is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_radio_button_checked(self._RADIO_BUTTON_BLUE)

    def is_radio_button_yellow_checked(self) -> bool:
        """
        Check if the yellow radio button is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_radio_button_checked(self._RADIO_BUTTON_YELLOW)

    def is_radio_button_orange_checked(self) -> bool:
        """
        Check if the orange radio button is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_radio_button_checked(self._RADIO_BUTTON_ORANGE)

    def is_radio_button_purple_checked(self) -> bool:
        """
        Check if the purple radio button is checked.

        Returns:
            bool: True if checked, False otherwise.
        """
        return self._is_radio_button_checked(self._RADIO_BUTTON_PURPLE)

    # Selected & Disabled methods
    def select_fruit(self, value: str) -> List[str]:
        """
        Select a fruit from the dropdown.

        Args:
            value: Value to select.

        Returns:
            List[str]: List of selected values.
        """
        logger.info(f"Selecting fruit '{value}'")

        fruit_dropdown = self.dropdowns.nth(self._DROPDOWN_FRUIT)
        fruit_label = self._FRUIT_LABELS.get(value, value)

        fruit_option = fruit_dropdown.get_by_role(
            "option",
            name=fruit_label,
            exact=True,
        )

        if fruit_option.is_disabled():
            logger.warning(f"Option '{value}' is disabled and cannot be selected")
            return []

        return fruit_dropdown.select_option(value=value)

    def get_selected_fruit(self) -> Optional[str]:
        """
        Get the selected fruit from the dropdown.

        Returns:
            Optional[str]: The selected fruit or None.
        """
        logger.info("Getting selected fruit")
        return self._get_dropdown_value(self._DROPDOWN_FRUIT)

    def is_radio_button_lettuce_enabled(self) -> bool:
        """
        Check if the lettuce radio button is enabled.

        Returns:
            bool: True if enabled, False otherwise.
        """
        return self._is_radio_button_enabled(self._RADIO_BUTTON_LETTUCE)

    def is_radio_button_cabbage_enabled(self) -> bool:
        """
        Check if the cabbage radio button is enabled.

        Returns:
            bool: True if enabled, False otherwise.
        """
        return self._is_radio_button_enabled(self._RADIO_BUTTON_CABBAGE)

    def is_radio_button_pumpkin_enabled(self) -> bool:
        """
        Check if the pumpkin radio button is enabled.

        Returns:
            bool: True if enabled, False otherwise.
        """
        return self._is_radio_button_enabled(self._RADIO_BUTTON_PUMPKIN)

    def is_checkbox_option_1_enabled(self) -> bool:
        """
        Check if checkbox option 1 is enabled.

        Returns:
            bool: True if enabled, False otherwise.
        """
        return self._is_checkbox_enabled(self._CHECKBOX_OPTION_1)

    def is_checkbox_option_2_enabled(self) -> bool:
        """
        Check if checkbox option 2 is enabled.

        Returns:
            bool: True if enabled, False otherwise.
        """
        return self._is_checkbox_enabled(self._CHECKBOX_OPTION_2)

    # Private reusable helpers
    def _select_dropdown_value(self, dropdown_index: int, value: str) -> List[str]:
        """
        Select a value from a dropdown by dropdown index.

        Args:
            dropdown_index: Dropdown index on the page.
            value: Value to select.

        Returns:
            List[str]: List of selected values.
        """
        logger.info(f"Selecting value '{value}' from dropdown index {dropdown_index}")
        return self.dropdowns.nth(dropdown_index).select_option(value=value)

    def _get_dropdown_value(self, dropdown_index: int) -> Optional[str]:
        """
        Get selected dropdown value by dropdown index.

        Args:
            dropdown_index: Dropdown index on the page.

        Returns:
            Optional[str]: Selected dropdown value.
        """
        logger.info(f"Getting selected value from dropdown index {dropdown_index}")
        return self.dropdowns.nth(dropdown_index).input_value()

    def _set_checkbox_state(self, checkbox_index: int, checked: bool) -> None:
        """
        Set checkbox state by checkbox index.

        Args:
            checkbox_index: Checkbox index on the page.
            checked: Desired checkbox state.
        """
        logger.info(f"Setting checkbox index {checkbox_index} to checked={checked}")

        checkbox = self.checkboxes.nth(checkbox_index)

        if checked:
            checkbox.check()
        else:
            checkbox.uncheck()

    def _is_checkbox_checked(self, checkbox_index: int) -> bool:
        """
        Check if a checkbox is checked by index.

        Args:
            checkbox_index: Checkbox index on the page.

        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info(f"Checking if checkbox index {checkbox_index} is checked")
        return self.checkboxes.nth(checkbox_index).is_checked()

    def _is_checkbox_enabled(self, checkbox_index: int) -> bool:
        """
        Check if a checkbox is enabled by index.

        Args:
            checkbox_index: Checkbox index on the page.

        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info(f"Checking if checkbox index {checkbox_index} is enabled")

        if self.checkboxes.count() <= checkbox_index:
            logger.warning(f"Checkbox index {checkbox_index} is not present on the page")
            return False

        return self.checkboxes.nth(checkbox_index).is_enabled()

    def _select_radio_button(self, radio_index: int) -> None:
        """
        Select a radio button by index.

        Args:
            radio_index: Radio button index on the page.
        """
        logger.info(f"Selecting radio button index {radio_index}")
        self.radio_buttons.nth(radio_index).check()

    def _is_radio_button_checked(self, radio_index: int) -> bool:
        """
        Check if a radio button is checked by index.

        Args:
            radio_index: Radio button index on the page.

        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info(f"Checking if radio button index {radio_index} is checked")
        return self.radio_buttons.nth(radio_index).is_checked()

    def _is_radio_button_enabled(self, radio_index: int) -> bool:
        """
        Check if a radio button is enabled by index.

        Args:
            radio_index: Radio button index on the page.

        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info(f"Checking if radio button index {radio_index} is enabled")
        return self.radio_buttons.nth(radio_index).is_enabled()