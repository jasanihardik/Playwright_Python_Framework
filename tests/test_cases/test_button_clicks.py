"""
Test cases for the Button Clicks page.
"""
import pytest
from playwright.sync_api import Page

from pages.button_clicks_page import ButtonClicksPage
from utilities.logger import logger


@pytest.fixture
def button_clicks_page(page: Page) -> ButtonClicksPage:
    """
    Fixture to create a Button Clicks page object.
    
    Args:
        page: Playwright page object.
    
    Returns:
        ButtonClicksPage: Button Clicks page object.
    """
    return ButtonClicksPage(page)


class TestButtonClicks:
    """Test cases for the Button Clicks page."""
    
    def test_navigate_to_button_clicks_page(self, button_clicks_page: ButtonClicksPage) -> None:
        """
        Test navigating to the Button Clicks page.
        
        Args:
            button_clicks_page: Button Clicks page object.
        """
        logger.info("Starting test_navigate_to_button_clicks_page")
        # Navigate to the Button Clicks page
        button_clicks_page.navigate()
        
        # Get the page title
        page_title = button_clicks_page.get_page_title()
        logger.info(f"Page title: {page_title}")
        
        # Verify the page title contains expected text
        expected_title = "Lets Get Clicking"
        assert expected_title.lower() in page_title.lower(), f"Expected '{expected_title}' to be in '{page_title}'"
        
        logger.info("test_navigate_to_button_clicks_page completed")
    
    def test_simple_button_click(self, button_clicks_page: ButtonClicksPage) -> None:
        """
        Test clicking the simple button and verify the modal.
        
        Args:
            button_clicks_page: Button Clicks page object.
        """
        logger.info("Starting test_simple_button_click")
        # Navigate to the Button Clicks page
        button_clicks_page.navigate()
        
        # Click the simple button
        button_clicks_page.click_simple_button()
        
        # Verify the modal is displayed
        assert button_clicks_page.is_simple_button_modal_displayed(), "Simple button modal is not displayed"
        
        # Get the modal title
        modal_title = button_clicks_page.get_simple_button_modal_title()
        logger.info(f"Modal title: {modal_title}")
        
        # Verify the modal title - the actual title is "Congratulations!"
        expected_title = "Congratulations"
        assert expected_title.lower() in modal_title.lower(), f"Expected '{expected_title}' to be in '{modal_title}'"
        
        # Close the modal
        button_clicks_page.close_simple_button_modal()
        
        # Verify the modal is closed
        assert not button_clicks_page.is_simple_button_modal_displayed(), "Simple button modal is still displayed"
        
        logger.info("test_simple_button_click completed")
    
    def test_modal_button_click(self, button_clicks_page: ButtonClicksPage) -> None:
        """
        Test clicking the modal button and verify the modal.
        
        Args:
            button_clicks_page: Button Clicks page object.
        """
        logger.info("Starting test_modal_button_click")
        # Navigate to the Button Clicks page
        button_clicks_page.navigate()
        
        # Click the modal button
        button_clicks_page.click_modal_button()
        
        # Verify the modal is displayed
        assert button_clicks_page.is_modal_button_modal_displayed(), "Modal button modal is not displayed"
        
        # Get the modal title
        modal_title = button_clicks_page.get_modal_button_modal_title()
        logger.info(f"Modal title: {modal_title}")
        
        # Verify the modal title - the actual title includes "It's that Easy!! Well I think it is....."
        # Fix the string comparison by using part of the title
        assert "Easy" in modal_title, f"Expected 'Easy' to be in '{modal_title}'"
        
        # Close the modal
        button_clicks_page.close_modal_button_modal()
        
        # Verify the modal is closed
        assert not button_clicks_page.is_modal_button_modal_displayed(), "Modal button modal is still displayed"
        
        logger.info("test_modal_button_click completed")
    
    def test_action_button_click(self, button_clicks_page: ButtonClicksPage) -> None:
        """
        Test clicking the action button and verify the modal.
        
        Args:
            button_clicks_page: Button Clicks page object.
        """
        logger.info("Starting test_action_button_click")
        # Navigate to the Button Clicks page
        button_clicks_page.navigate()
        
        # Click the action button
        button_clicks_page.click_action_button()
        
        # Verify the modal is displayed
        assert button_clicks_page.is_action_button_modal_displayed(), "Action button modal is not displayed"
        
        # Get the modal title
        modal_title = button_clicks_page.get_action_button_modal_title()
        logger.info(f"Modal title: {modal_title}")
        
        # Verify the modal title
        expected_title = "Well Done"
        assert expected_title.lower() in modal_title.lower(), f"Expected '{expected_title}' to be in '{modal_title}'"
        
        # Close the modal
        button_clicks_page.close_action_button_modal()
        
        # Verify the modal is closed
        assert not button_clicks_page.is_action_button_modal_displayed(), "Action button modal is still displayed"
        
        logger.info("test_action_button_click completed")
    
    def test_all_buttons(self, button_clicks_page: ButtonClicksPage) -> None:
        """
        Test clicking all buttons and verify their modals.
        
        Args:
            button_clicks_page: Button Clicks page object.
        """
        logger.info("Starting test_all_buttons")
        # Navigate to the Button Clicks page
        button_clicks_page.navigate()
        
        # Test simple button
        button_clicks_page.click_simple_button()
        assert button_clicks_page.is_simple_button_modal_displayed(), "Simple button modal is not displayed"
        modal_title = button_clicks_page.get_simple_button_modal_title()
        expected_title = "Congratulations"
        assert expected_title.lower() in modal_title.lower(), f"Expected '{expected_title}' to be in '{modal_title}'"
        button_clicks_page.close_simple_button_modal()
        assert not button_clicks_page.is_simple_button_modal_displayed(), "Simple button modal is still displayed"
        
        # Test modal button
        button_clicks_page.click_modal_button()
        assert button_clicks_page.is_modal_button_modal_displayed(), "Modal button modal is not displayed"
        modal_title = button_clicks_page.get_modal_button_modal_title()
        # Fix the string comparison by using part of the title
        assert "Easy" in modal_title, f"Expected 'Easy' to be in '{modal_title}'"
        button_clicks_page.close_modal_button_modal()
        assert not button_clicks_page.is_modal_button_modal_displayed(), "Modal button modal is still displayed"
        
        # Test action button
        button_clicks_page.click_action_button()
        assert button_clicks_page.is_action_button_modal_displayed(), "Action button modal is not displayed"
        modal_title = button_clicks_page.get_action_button_modal_title()
        expected_title = "Well Done"
        assert expected_title.lower() in modal_title.lower(), f"Expected '{expected_title}' to be in '{modal_title}'"
        button_clicks_page.close_action_button_modal()
        assert not button_clicks_page.is_action_button_modal_displayed(), "Action button modal is still displayed"
        
        logger.info("test_all_buttons completed") 