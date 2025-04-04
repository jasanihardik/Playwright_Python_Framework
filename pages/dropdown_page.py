"""
Page object for the Dropdown, Checkboxes & Radio Buttons page.
"""
from typing import Optional, List

from playwright.sync_api import Page, expect

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class DropdownPage(BasePage):
    """Page object representing the Dropdown, Checkboxes & Radio Buttons page."""
    
    # Selectors for the page elements
    _PAGE_HEADER = 'h1'
    
    # Dropdown selectors
    _DROPDOWN_MENU_HEADER = '#dropdown-checkboxes-radiobuttons h2'
    _DROPDOWN_1 = '#dropdowm-menu-1'  # Note: There is a typo in the actual ID ("dropdowm" instead of "dropdown")
    _DROPDOWN_2 = '#dropdowm-menu-2'  # This is the correct ID from the page
    _DROPDOWN_3 = '#dropdowm-menu-3'  # This is the correct ID from the page
    
    # Checkbox selectors
    _CHECKBOX_HEADER = 'div.checkbox-div h2'
    _CHECKBOX_1 = 'input[value="option-1"]'
    _CHECKBOX_2 = 'input[value="option-2"]'
    _CHECKBOX_3 = 'input[value="option-3"]'
    _CHECKBOX_4 = 'input[value="option-4"]'
    
    # Radio button selectors
    _RADIO_BUTTON_HEADER = 'div.radio-buttons-div h2'
    _RADIO_BUTTON_GREEN = 'input[value="green"]'
    _RADIO_BUTTON_BLUE = 'input[value="blue"]'
    _RADIO_BUTTON_YELLOW = 'input[value="yellow"]'
    _RADIO_BUTTON_ORANGE = 'input[value="orange"]'
    _RADIO_BUTTON_PURPLE = 'input[value="purple"]'
    
    # Selected & Disabled selectors
    _SELECTED_DISABLED_HEADER = 'div.selected-disabled h2'
    _DROPDOWN_FRUIT = '#fruit-selects'
    _RADIO_BUTTON_LETTUCE = 'input[value="lettuce"]'
    _RADIO_BUTTON_CABBAGE = 'input[value="cabbage"]'
    _RADIO_BUTTON_PUMPKIN = 'input[value="pumpkin"]'
    _CHECKBOX_OPTION_1 = 'input.section-disabled[value="option-1"]'
    _CHECKBOX_OPTION_2 = 'input.section-disabled[value="option-2"]'
    
    def __init__(self, page: Page):
        """
        Initialize the Dropdown page.
        
        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["dropdown"]
    
    def navigate(self) -> None:
        """Navigate to the Dropdown page."""
        logger.info(f"Navigating to Dropdown page: {self.url}")
        self.navigate_to(self.url)
        # Give the page time to fully load
        self.page.wait_for_timeout(1000)
    
    def get_page_header(self) -> str:
        """
        Get the page header text.
        
        Returns:
            str: The page header text.
        """
        logger.info("Getting page header text")
        return self.get_text(self._PAGE_HEADER)
    
    # Dropdown methods
    def select_dropdown_1_value(self, value: str) -> List[str]:
        """
        Select a value from the first dropdown.
        
        Args:
            value: Value to select.
            
        Returns:
            List[str]: List of selected values.
        """
        logger.info(f"Selecting value '{value}' from dropdown 1")
        return self.select_option(self._DROPDOWN_1, value=value)
    
    def select_dropdown_2_value(self, value: str) -> List[str]:
        """
        Select a value from the second dropdown.
        
        Args:
            value: Value to select.
            
        Returns:
            List[str]: List of selected values.
        """
        logger.info(f"Selecting value '{value}' from dropdown 2")
        return self.select_option(self._DROPDOWN_2, value=value)
    
    def select_dropdown_3_value(self, value: str) -> List[str]:
        """
        Select a value from the third dropdown.
        
        Args:
            value: Value to select.
            
        Returns:
            List[str]: List of selected values.
        """
        logger.info(f"Selecting value '{value}' from dropdown 3")
        return self.select_option(self._DROPDOWN_3, value=value)
    
    def get_dropdown_1_value(self) -> Optional[str]:
        """
        Get the selected value from the first dropdown.
        
        Returns:
            Optional[str]: The selected value or None.
        """
        logger.info("Getting selected value from dropdown 1")
        # Use JavaScript evaluation to reliably get the selected value
        return self.page.evaluate('''() => {
            const dropdown = document.querySelector("#dropdowm-menu-1");
            return dropdown ? dropdown.value : null;
        }''')
    
    def get_dropdown_2_value(self) -> Optional[str]:
        """
        Get the selected value from the second dropdown.
        
        Returns:
            Optional[str]: The selected value or None.
        """
        logger.info("Getting selected value from dropdown 2")
        # Use JavaScript evaluation to reliably get the selected value
        return self.page.evaluate('''() => {
            const dropdown = document.querySelector("#dropdowm-menu-2");
            return dropdown ? dropdown.value : null;
        }''')
    
    def get_dropdown_3_value(self) -> Optional[str]:
        """
        Get the selected value from the third dropdown.
        
        Returns:
            Optional[str]: The selected value or None.
        """
        logger.info("Getting selected value from dropdown 3")
        # Use JavaScript evaluation to reliably get the selected value
        return self.page.evaluate('''() => {
            const dropdown = document.querySelector("#dropdowm-menu-3");
            return dropdown ? dropdown.value : null;
        }''')
    
    # Checkbox methods
    def check_checkbox_1(self) -> None:
        """Check the first checkbox."""
        logger.info("Checking checkbox 1")
        self.check(self._CHECKBOX_1)
    
    def check_checkbox_2(self) -> None:
        """Check the second checkbox."""
        logger.info("Checking checkbox 2")
        self.check(self._CHECKBOX_2)
    
    def check_checkbox_3(self) -> None:
        """Check the third checkbox."""
        logger.info("Checking checkbox 3")
        self.check(self._CHECKBOX_3)
    
    def check_checkbox_4(self) -> None:
        """Check the fourth checkbox."""
        logger.info("Checking checkbox 4")
        self.check(self._CHECKBOX_4)
    
    def uncheck_checkbox_1(self) -> None:
        """Uncheck the first checkbox."""
        logger.info("Unchecking checkbox 1")
        self.uncheck(self._CHECKBOX_1)
    
    def uncheck_checkbox_2(self) -> None:
        """Uncheck the second checkbox."""
        logger.info("Unchecking checkbox 2")
        self.uncheck(self._CHECKBOX_2)
    
    def uncheck_checkbox_3(self) -> None:
        """Uncheck the third checkbox."""
        logger.info("Unchecking checkbox 3")
        self.uncheck(self._CHECKBOX_3)
    
    def uncheck_checkbox_4(self) -> None:
        """Uncheck the fourth checkbox."""
        logger.info("Unchecking checkbox 4")
        self.uncheck(self._CHECKBOX_4)
    
    def is_checkbox_1_checked(self) -> bool:
        """
        Check if the first checkbox is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if checkbox 1 is checked")
        return self.is_checked(self._CHECKBOX_1)
    
    def is_checkbox_2_checked(self) -> bool:
        """
        Check if the second checkbox is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if checkbox 2 is checked")
        return self.is_checked(self._CHECKBOX_2)
    
    def is_checkbox_3_checked(self) -> bool:
        """
        Check if the third checkbox is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if checkbox 3 is checked")
        return self.is_checked(self._CHECKBOX_3)
    
    def is_checkbox_4_checked(self) -> bool:
        """
        Check if the fourth checkbox is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if checkbox 4 is checked")
        return self.is_checked(self._CHECKBOX_4)
    
    # Radio button methods
    def select_radio_button_green(self) -> None:
        """Select the green radio button."""
        logger.info("Selecting green radio button")
        self.click(self._RADIO_BUTTON_GREEN)
    
    def select_radio_button_blue(self) -> None:
        """Select the blue radio button."""
        logger.info("Selecting blue radio button")
        self.click(self._RADIO_BUTTON_BLUE)
    
    def select_radio_button_yellow(self) -> None:
        """Select the yellow radio button."""
        logger.info("Selecting yellow radio button")
        self.click(self._RADIO_BUTTON_YELLOW)
    
    def select_radio_button_orange(self) -> None:
        """Select the orange radio button."""
        logger.info("Selecting orange radio button")
        self.click(self._RADIO_BUTTON_ORANGE)
    
    def select_radio_button_purple(self) -> None:
        """Select the purple radio button."""
        logger.info("Selecting purple radio button")
        self.click(self._RADIO_BUTTON_PURPLE)
    
    def is_radio_button_green_checked(self) -> bool:
        """
        Check if the green radio button is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if green radio button is checked")
        return self.is_checked(self._RADIO_BUTTON_GREEN)
    
    def is_radio_button_blue_checked(self) -> bool:
        """
        Check if the blue radio button is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if blue radio button is checked")
        return self.is_checked(self._RADIO_BUTTON_BLUE)
    
    def is_radio_button_yellow_checked(self) -> bool:
        """
        Check if the yellow radio button is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if yellow radio button is checked")
        return self.is_checked(self._RADIO_BUTTON_YELLOW)
    
    def is_radio_button_orange_checked(self) -> bool:
        """
        Check if the orange radio button is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if orange radio button is checked")
        return self.is_checked(self._RADIO_BUTTON_ORANGE)
    
    def is_radio_button_purple_checked(self) -> bool:
        """
        Check if the purple radio button is checked.
        
        Returns:
            bool: True if checked, False otherwise.
        """
        logger.info("Checking if purple radio button is checked")
        return self.is_checked(self._RADIO_BUTTON_PURPLE)
    
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
        # For disabled options, Playwright will silently fail
        # Instead, we'll use JavaScript to check if the option is disabled first
        is_disabled = self.page.evaluate(f'''() => {{
            const dropdown = document.querySelector("{self._DROPDOWN_FRUIT}");
            if (!dropdown) return true;
            
            const option = Array.from(dropdown.options).find(opt => opt.value === "{value}");
            return option ? option.disabled : true;
        }}''')
        
        if is_disabled:
            logger.warning(f"Option '{value}' is disabled and cannot be selected")
            return []
            
        return self.select_option(self._DROPDOWN_FRUIT, value=value)
    
    def get_selected_fruit(self) -> Optional[str]:
        """
        Get the selected fruit from the dropdown.
        
        Returns:
            Optional[str]: The selected fruit or None.
        """
        logger.info("Getting selected fruit")
        # Use JavaScript evaluation to reliably get the selected value
        return self.page.evaluate('''() => {
            const dropdown = document.querySelector("#fruit-selects");
            return dropdown ? dropdown.value : null;
        }''')
    
    def is_radio_button_lettuce_enabled(self) -> bool:
        """
        Check if the lettuce radio button is enabled.
        
        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info("Checking if lettuce radio button is enabled")
        # Use JavaScript directly to check if it's disabled
        return not self.page.evaluate('''() => {
            const element = document.querySelector("input[value='lettuce']");
            return element ? element.disabled : true;
        }''')
    
    def is_radio_button_cabbage_enabled(self) -> bool:
        """
        Check if the cabbage radio button is enabled.
        
        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info("Checking if cabbage radio button is enabled")
        # Use JavaScript directly to check if it's disabled
        return not self.page.evaluate('''() => {
            const element = document.querySelector("input[value='cabbage']");
            return element ? element.disabled : true;
        }''')
    
    def is_radio_button_pumpkin_enabled(self) -> bool:
        """
        Check if the pumpkin radio button is enabled.
        
        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info("Checking if pumpkin radio button is enabled")
        # Use JavaScript directly to check if it's disabled
        return not self.page.evaluate('''() => {
            const element = document.querySelector("input[value='pumpkin']");
            return element ? element.disabled : true;
        }''')
    
    def is_checkbox_option_1_enabled(self) -> bool:
        """
        Check if checkbox option 1 is enabled.
        
        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info("Checking if checkbox option 1 is enabled")
        # Use JavaScript directly to check if it's disabled
        return not self.page.evaluate('''() => {
            const element = document.querySelector("input.section-disabled[value='option-1']");
            return element ? element.disabled : true;
        }''')
    
    def is_checkbox_option_2_enabled(self) -> bool:
        """
        Check if checkbox option 2 is enabled.
        
        Returns:
            bool: True if enabled, False otherwise.
        """
        logger.info("Checking if checkbox option 2 is enabled")
        # Use JavaScript directly to check if it's disabled
        return not self.page.evaluate('''() => {
            const element = document.querySelector("input.section-disabled[value='option-2']");
            return element ? element.disabled : true;
        }''') 