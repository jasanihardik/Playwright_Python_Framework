#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test cases for the Checkboxes and Radio Buttons page on WebdriverUniversity.
These tests validate the functionality of checkboxes, radio buttons, disabled elements, and dropdowns.
"""

import logging
import pytest
from pages.checkboxes_radio_page import CheckboxesRadioPage

logger = logging.getLogger("PlaywrightFramework")


@pytest.fixture
def checkboxes_radio_page(page) -> CheckboxesRadioPage:
    """
    Fixture to create and navigate to the Checkboxes and Radio Buttons page.
    
    Args:
        page: Playwright page fixture
        
    Returns:
        CheckboxesRadioPage: An initialized and navigated CheckboxesRadioPage object
    """
    checkbox_page = CheckboxesRadioPage(page)
    checkbox_page.navigate()
    return checkbox_page


def test_page_loads(checkboxes_radio_page: CheckboxesRadioPage) -> None:
    """
    Test that the Checkboxes and Radio Buttons page loads correctly.
    
    Args:
        checkboxes_radio_page: CheckboxesRadioPage fixture
    """
    logger.info("Starting test: test_page_loads")
    
    # Verify the page title
    page_title = checkboxes_radio_page.get_page_title()
    assert "Dropdown Menu(s), Checkboxe(s) & Radio Button(s)" in page_title, f"Page title is incorrect: '{page_title}'"
    
    # Verify section headers
    checkbox_header = checkboxes_radio_page.get_checkbox_header()
    assert "Checkboxe(s)" in checkbox_header, f"Checkbox header is incorrect: '{checkbox_header}'"
    
    radio_header = checkboxes_radio_page.get_radio_button_header()
    assert "Radio Button(s)" in radio_header, f"Radio button header is incorrect: '{radio_header}'"
    
    disabled_header = checkboxes_radio_page.get_selected_disabled_header()
    assert "Selected & Disabled" in disabled_header, f"Selected & Disabled header is incorrect: '{disabled_header}'"
    
    fruit_header = checkboxes_radio_page.get_fruit_dropdown_header()
    assert "Dropdown Menu(s)" in fruit_header, f"Dropdown Menu(s) header is incorrect: '{fruit_header}'"
    
    # Take a screenshot
    checkboxes_radio_page.take_screenshot("test_page_loads", "page_loaded")


def test_checkbox_functionality(checkboxes_radio_page: CheckboxesRadioPage) -> None:
    """
    Test the functionality of checkboxes.
    
    Args:
        checkboxes_radio_page: CheckboxesRadioPage fixture
    """
    logger.info("Starting test: test_checkbox_functionality")
    
    # Get initial states
    initial_states = checkboxes_radio_page.get_all_checkboxes_state()
    logger.info(f"Initial checkbox states: {initial_states}")
    
    # Verify checkbox 1 is initially unchecked
    assert not initial_states["checkbox_1"], "Checkbox 1 should be unchecked initially"
    
    # Verify checkbox 3 is initially checked
    assert initial_states["checkbox_3"], "Checkbox 3 should be checked initially"
    
    # Check checkbox 1
    checkboxes_radio_page.check_checkbox(1)
    assert checkboxes_radio_page.is_checkbox_checked(1), "Checkbox 1 should be checked after checking"
    
    # Uncheck checkbox 3
    checkboxes_radio_page.uncheck_checkbox(3)
    assert not checkboxes_radio_page.is_checkbox_checked(3), "Checkbox 3 should be unchecked after unchecking"
    
    # Toggle checkbox 2
    initial_state_2 = checkboxes_radio_page.is_checkbox_checked(2)
    checkboxes_radio_page.toggle_checkbox(2)
    assert checkboxes_radio_page.is_checkbox_checked(2) != initial_state_2, "Checkbox 2 should have toggled state"
    
    # Toggle checkbox 4
    initial_state_4 = checkboxes_radio_page.is_checkbox_checked(4)
    checkboxes_radio_page.toggle_checkbox(4)
    assert checkboxes_radio_page.is_checkbox_checked(4) != initial_state_4, "Checkbox 4 should have toggled state"
    
    # Get final states and take screenshot
    final_states = checkboxes_radio_page.get_all_checkboxes_state()
    logger.info(f"Final checkbox states: {final_states}")
    checkboxes_radio_page.take_screenshot("test_checkbox_functionality", "final_states")


def test_radio_button_selection(checkboxes_radio_page: CheckboxesRadioPage) -> None:
    """
    Test the functionality of radio buttons.
    
    Args:
        checkboxes_radio_page: CheckboxesRadioPage fixture
    """
    logger.info("Starting test: test_radio_button_selection")
    
    # Get initial selection (should be none or platform dependent)
    initial_selection = checkboxes_radio_page.get_selected_radio_button()
    logger.info(f"Initial radio button selection: {initial_selection}")
    
    # Select each radio button and verify
    colors = ["green", "blue", "yellow", "orange", "purple"]
    for color in colors:
        checkboxes_radio_page.select_radio_button(color)
        selected_color = checkboxes_radio_page.get_selected_radio_button()
        assert selected_color == color, f"Radio button {color} was not selected correctly, got {selected_color}"
        
        # Take a screenshot after each selection
        checkboxes_radio_page.take_screenshot("test_radio_button_selection", f"selected_{color}")


def test_disabled_elements(checkboxes_radio_page: CheckboxesRadioPage) -> None:
    """
    Test the functionality of disabled elements.
    
    Args:
        checkboxes_radio_page: CheckboxesRadioPage fixture
    """
    logger.info("Starting test: test_disabled_elements")
    
    # Verify cabbage is disabled
    assert checkboxes_radio_page.is_radio_disabled("cabbage"), "Cabbage radio button should be disabled"
    
    # Verify lettuce and pumpkin are not disabled
    assert not checkboxes_radio_page.is_radio_disabled("lettuce"), "Lettuce radio button should not be disabled"
    assert not checkboxes_radio_page.is_radio_disabled("pumpkin"), "Pumpkin radio button should not be disabled"
    
    # Verify pumpkin is initially selected
    initial_selection = checkboxes_radio_page.get_selected_vegetable_radio()
    assert initial_selection == "pumpkin", f"Initial vegetable selection should be pumpkin, got {initial_selection}"
    
    # Try to select lettuce (should work)
    checkboxes_radio_page.select_vegetable_radio("lettuce")
    selected_veg = checkboxes_radio_page.get_selected_vegetable_radio()
    assert selected_veg == "lettuce", f"Lettuce radio button was not selected correctly, got {selected_veg}"
    
    # Try to select cabbage (should not work, stays on lettuce)
    checkboxes_radio_page.select_vegetable_radio("cabbage")
    selected_veg = checkboxes_radio_page.get_selected_vegetable_radio()
    assert selected_veg == "lettuce", f"Selection should not have changed from lettuce when selecting disabled cabbage, got {selected_veg}"
    
    # Take a screenshot
    checkboxes_radio_page.take_screenshot("test_disabled_elements", "final_state")


def test_fruit_dropdown(checkboxes_radio_page: CheckboxesRadioPage) -> None:
    """
    Test the functionality of the fruit dropdown.
    
    Args:
        checkboxes_radio_page: CheckboxesRadioPage fixture
    """
    logger.info("Starting test: test_fruit_dropdown")
    
    # Get available fruits
    available_fruits = checkboxes_radio_page.get_available_fruits()
    logger.info(f"Available fruits: {available_fruits}")
    
    # Verify we have the expected fruits
    expected_fruits = ["apple", "orange", "pear", "grape"]
    for fruit in expected_fruits:
        assert fruit in available_fruits, f"Expected fruit {fruit} not found in dropdown"
    
    # Verify initial selection (should be grape)
    initial_selection = checkboxes_radio_page.get_selected_fruit()
    assert initial_selection == "grape", f"Initial fruit selection should be grape, got {initial_selection}"
    
    # Select each fruit and verify
    for fruit in ["apple", "pear", "grape"]:  # Skip orange as it's disabled
        checkboxes_radio_page.select_fruit(fruit)
        selected_fruit = checkboxes_radio_page.get_selected_fruit()
        assert selected_fruit == fruit, f"Fruit {fruit} was not selected correctly, got {selected_fruit}"
        
        # Take a screenshot after each selection
        checkboxes_radio_page.take_screenshot("test_fruit_dropdown", f"selected_{fruit}") 