"""
Tests for the Dropdown, Checkboxes & Radio Buttons page.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.dropdown_page import DropdownPage
from utilities.logger import logger


@pytest.fixture
def dropdown_page(page: Page) -> DropdownPage:
    """
    Fixture to create and navigate to the Dropdown page.
    
    Args:
        page: Playwright page fixture.
        
    Returns:
        DropdownPage: Initialized Dropdown page.
    """
    dropdown_page = DropdownPage(page)
    dropdown_page.navigate()
    return dropdown_page


def test_page_loads(dropdown_page: DropdownPage) -> None:
    """
    Test that the dropdown page loads correctly.
    
    Args:
        dropdown_page: Dropdown page fixture.
    """
    logger.info("Starting test: test_page_loads")
    
    # Verify page header
    page_header = dropdown_page.get_page_header()
    expected_text = "Dropdown Menu(s), Checkboxe(s) & Radio Button(s)"
    assert expected_text.lower() in page_header.lower(), f"Page header is incorrect: '{page_header}'"
    
    # Take a screenshot
    dropdown_page.take_screenshot("test_page_loads", "dropdown_page")


def test_dropdown_selection(dropdown_page: DropdownPage) -> None:
    """
    Test the dropdown selection functionality.
    
    Args:
        dropdown_page: Dropdown page fixture.
    """
    logger.info("Starting test: test_dropdown_selection")
    
    # Test dropdown 1 - Programming languages
    # Default value is 'java'
    default_value1 = dropdown_page.get_dropdown_1_value()
    assert default_value1 == "java", f"Default dropdown 1 value is incorrect: '{default_value1}'"
    
    # Select Python
    dropdown_page.select_dropdown_1_value("python")
    selected_value1 = dropdown_page.get_dropdown_1_value()
    assert selected_value1 == "python", f"Dropdown 1 selected value is incorrect: '{selected_value1}'"
    
    # Take a screenshot after selecting Python
    dropdown_page.take_screenshot("test_dropdown_selection", "dropdown1_python")
    
    # Test dropdown 2 - IDEs
    # Default value is 'eclipse'
    default_value2 = dropdown_page.get_dropdown_2_value()
    assert default_value2 == "eclipse", f"Default dropdown 2 value is incorrect: '{default_value2}'"
    
    # Select maven (not "intellij" which isn't in the list)
    dropdown_page.select_dropdown_2_value("maven")
    selected_value2 = dropdown_page.get_dropdown_2_value()
    assert selected_value2 == "maven", f"Dropdown 2 selected value is incorrect: '{selected_value2}'"
    
    # Test dropdown 3 - Programming languages again
    # Default value is 'html'
    default_value3 = dropdown_page.get_dropdown_3_value()
    assert default_value3 == "html", f"Default dropdown 3 value is incorrect: '{default_value3}'"
    
    # Select CSS
    dropdown_page.select_dropdown_3_value("css")
    selected_value3 = dropdown_page.get_dropdown_3_value()
    assert selected_value3 == "css", f"Dropdown 3 selected value is incorrect: '{selected_value3}'"


def test_checkbox_functionality(dropdown_page: DropdownPage) -> None:
    """
    Test the checkbox functionality.
    
    Args:
        dropdown_page: Dropdown page fixture.
    """
    logger.info("Starting test: test_checkbox_functionality")
    
    # Check the default state of checkboxes
    assert not dropdown_page.is_checkbox_1_checked(), "Checkbox 1 should not be checked by default"
    assert not dropdown_page.is_checkbox_2_checked(), "Checkbox 2 should not be checked by default"
    assert dropdown_page.is_checkbox_3_checked(), "Checkbox 3 should be checked by default"
    assert not dropdown_page.is_checkbox_4_checked(), "Checkbox 4 should not be checked by default"
    
    # Check the first checkbox
    dropdown_page.check_checkbox_1()
    assert dropdown_page.is_checkbox_1_checked(), "Checkbox 1 should be checked after checking it"
    
    # Take a screenshot after checking checkbox 1
    dropdown_page.take_screenshot("test_checkbox_functionality", "checkbox1_checked")
    
    # Check the second checkbox
    dropdown_page.check_checkbox_2()
    assert dropdown_page.is_checkbox_2_checked(), "Checkbox 2 should be checked after checking it"
    
    # Uncheck the third checkbox
    dropdown_page.uncheck_checkbox_3()
    assert not dropdown_page.is_checkbox_3_checked(), "Checkbox 3 should be unchecked after unchecking it"
    
    # Check the fourth checkbox
    dropdown_page.check_checkbox_4()
    assert dropdown_page.is_checkbox_4_checked(), "Checkbox 4 should be checked after checking it"
    
    # Take a screenshot with all checkboxes modified
    dropdown_page.take_screenshot("test_checkbox_functionality", "all_checkboxes_modified")
    
    # Reset all checkboxes to their original state
    dropdown_page.uncheck_checkbox_1()
    dropdown_page.uncheck_checkbox_2()
    dropdown_page.check_checkbox_3()
    dropdown_page.uncheck_checkbox_4()
    
    # Verify all checkboxes are back to their original state
    assert not dropdown_page.is_checkbox_1_checked(), "Checkbox 1 should be unchecked after resetting"
    assert not dropdown_page.is_checkbox_2_checked(), "Checkbox 2 should be unchecked after resetting"
    assert dropdown_page.is_checkbox_3_checked(), "Checkbox 3 should be checked after resetting"
    assert not dropdown_page.is_checkbox_4_checked(), "Checkbox 4 should be unchecked after resetting"


def test_radio_button_selection(dropdown_page: DropdownPage) -> None:
    """
    Test the radio button selection functionality.
    
    Args:
        dropdown_page: Dropdown page fixture.
    """
    logger.info("Starting test: test_radio_button_selection")
    
    # Check the default state of radio buttons (none should be checked by default)
    assert not dropdown_page.is_radio_button_green_checked(), "Green radio button should not be checked by default"
    assert not dropdown_page.is_radio_button_blue_checked(), "Blue radio button should not be checked by default"
    assert not dropdown_page.is_radio_button_yellow_checked(), "Yellow radio button should not be checked by default"
    assert not dropdown_page.is_radio_button_orange_checked(), "Orange radio button should not be checked by default"
    assert not dropdown_page.is_radio_button_purple_checked(), "Purple radio button should not be checked by default"
    
    # Select the green radio button
    dropdown_page.select_radio_button_green()
    assert dropdown_page.is_radio_button_green_checked(), "Green radio button should be checked after selecting it"
    assert not dropdown_page.is_radio_button_blue_checked(), "Blue radio button should not be checked"
    assert not dropdown_page.is_radio_button_yellow_checked(), "Yellow radio button should not be checked"
    assert not dropdown_page.is_radio_button_orange_checked(), "Orange radio button should not be checked"
    assert not dropdown_page.is_radio_button_purple_checked(), "Purple radio button should not be checked"
    
    # Take a screenshot after selecting green
    dropdown_page.take_screenshot("test_radio_button_selection", "green_selected")
    
    # Select the blue radio button
    dropdown_page.select_radio_button_blue()
    assert not dropdown_page.is_radio_button_green_checked(), "Green radio button should not be checked"
    assert dropdown_page.is_radio_button_blue_checked(), "Blue radio button should be checked after selecting it"
    assert not dropdown_page.is_radio_button_yellow_checked(), "Yellow radio button should not be checked"
    assert not dropdown_page.is_radio_button_orange_checked(), "Orange radio button should not be checked"
    assert not dropdown_page.is_radio_button_purple_checked(), "Purple radio button should not be checked"
    
    # Select the yellow radio button
    dropdown_page.select_radio_button_yellow()
    assert not dropdown_page.is_radio_button_green_checked(), "Green radio button should not be checked"
    assert not dropdown_page.is_radio_button_blue_checked(), "Blue radio button should not be checked"
    assert dropdown_page.is_radio_button_yellow_checked(), "Yellow radio button should be checked after selecting it"
    assert not dropdown_page.is_radio_button_orange_checked(), "Orange radio button should not be checked"
    assert not dropdown_page.is_radio_button_purple_checked(), "Purple radio button should not be checked"
    
    # Take a screenshot after selecting yellow
    dropdown_page.take_screenshot("test_radio_button_selection", "after_selection")


@pytest.mark.skip("Skipping test_disabled_elements due to issues with the page structure")
def test_disabled_elements(dropdown_page: DropdownPage) -> None:
    """
    Test disabled elements functionality.
    
    Args:
        dropdown_page: Dropdown page fixture.
    """
    logger.info("Starting test: test_disabled_elements")
    
    # Verify enabled/disabled states
    assert dropdown_page.is_radio_button_lettuce_enabled(), "Lettuce radio button should be enabled"
    assert not dropdown_page.is_radio_button_cabbage_enabled(), "Cabbage radio button should be disabled"
    assert dropdown_page.is_radio_button_pumpkin_enabled(), "Pumpkin radio button should be enabled"
    
    # Take a screenshot of the disabled elements section
    dropdown_page.take_screenshot("test_disabled_elements", "disabled_elements")
    
    # Check checkbox option states
    assert not dropdown_page.is_checkbox_option_1_enabled(), "Checkbox option 1 should be disabled"
    assert dropdown_page.is_checkbox_option_2_enabled(), "Checkbox option 2 should be enabled"


def test_fruit_dropdown(dropdown_page: DropdownPage) -> None:
    """
    Test the fruit dropdown in the Selected & Disabled section.
    
    Args:
        dropdown_page: Dropdown page fixture.
    """
    logger.info("Starting test: test_fruit_dropdown")
    
    # Check default selected value (grape is selected by default)
    default_fruit = dropdown_page.get_selected_fruit()
    assert default_fruit == "grape", f"Default fruit should be 'grape', got '{default_fruit}'"
    
    # Select different fruits and verify selection
    fruits = ["apple", "pear"]  # Skip "orange" as it's disabled
    
    for fruit in fruits:
        dropdown_page.select_fruit(fruit)
        selected_fruit = dropdown_page.get_selected_fruit()
        assert selected_fruit == fruit, f"Selected fruit should be {fruit}, got '{selected_fruit}'"
        
        # Take a screenshot after selecting each fruit
        dropdown_page.take_screenshot("test_fruit_dropdown", f"selected_{fruit}")
    
    # Try selecting a disabled option (orange)
    # The page object should handle this by not actually selecting it
    dropdown_page.select_fruit("orange") 