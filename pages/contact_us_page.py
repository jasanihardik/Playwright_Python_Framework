"""
Page object for the Contact Us page.
"""
from typing import Optional

from playwright.sync_api import Page

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class ContactUsPage(BasePage):
    """Page object representing the Contact Us page."""
    
    # Selectors for the page elements
    _FIRST_NAME_FIELD = 'input[name="first_name"]'
    _LAST_NAME_FIELD = 'input[name="last_name"]'
    _EMAIL_FIELD = 'input[name="email"]'
    _COMMENT_FIELD = 'textarea[name="message"]'
    _SUBMIT_BUTTON = 'input[type="submit"]'
    _RESET_BUTTON = 'input[type="reset"]'
    _SUCCESS_MESSAGE = 'div#contact_reply h1'
    _ERROR_MESSAGE = 'body'
    
    def __init__(self, page: Page):
        """
        Initialize the Contact Us page.
        
        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["contact_us"]
    
    def navigate(self) -> None:
        """Navigate to the Contact Us page."""
        logger.info(f"Navigating to Contact Us page: {self.url}")
        self.navigate_to(self.url)
    
    def fill_contact_form(self, first_name: str, last_name: str, email: str, comment: str) -> None:
        """
        Fill in the contact form.
        
        Args:
            first_name: First name to enter.
            last_name: Last name to enter.
            email: Email to enter.
            comment: Comment to enter.
        """
        logger.info("Filling contact form")
        
        self.fill_text(self._FIRST_NAME_FIELD, first_name)
        self.fill_text(self._LAST_NAME_FIELD, last_name)
        self.fill_text(self._EMAIL_FIELD, email)
        self.fill_text(self._COMMENT_FIELD, comment)
    
    def submit_form(self) -> None:
        """Submit the contact form."""
        logger.info("Submitting contact form")
        self.click(self._SUBMIT_BUTTON)
    
    def reset_form(self) -> None:
        """Reset the contact form."""
        logger.info("Resetting contact form")
        self.click(self._RESET_BUTTON)
    
    def get_success_message(self) -> str:
        """
        Get the success message after form submission.
        
        Returns:
            str: The success message text.
        """
        logger.info("Getting success message")
        return self.get_text(self._SUCCESS_MESSAGE)
    
    def is_success_message_displayed(self) -> bool:
        """
        Check if the success message is displayed.
        
        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if success message is displayed")
        return self.is_visible(self._SUCCESS_MESSAGE)
    
    def get_error_message(self) -> str:
        """
        Get the error message when form submission fails.
        
        Returns:
            str: The error message text.
        """
        logger.info("Getting error message")
        return self.get_text(self._ERROR_MESSAGE)
    
    def is_field_empty(self, field_selector: str) -> bool:
        """
        Check if a field is empty.
        
        Args:
            field_selector: Selector for the field.
            
        Returns:
            bool: True if empty, False otherwise.
        """
        logger.info(f"Checking if field is empty: {field_selector}")
        value = self.get_attribute(field_selector, "value")
        return not value 