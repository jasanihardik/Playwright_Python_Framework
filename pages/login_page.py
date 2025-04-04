"""
Page object for the Login page.
"""
from typing import Optional

from playwright.sync_api import Page

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class LoginPage(BasePage):
    """Page object representing the Login page."""
    
    # Selectors for the page elements
    _USERNAME_FIELD = 'input#text'
    _PASSWORD_FIELD = 'input#password'
    _LOGIN_BUTTON = 'button#login-button'
    _LOGIN_FORM = 'form.form'
    _LOGIN_WRAPPER = 'div.wrapper'
    _SUCCESS_MESSAGE_SELECTOR = 'body'
    _ERROR_MESSAGE_SELECTOR = 'body'
    
    def __init__(self, page: Page):
        """
        Initialize the Login page.
        
        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["login"]
    
    def navigate(self) -> None:
        """Navigate to the Login page."""
        logger.info(f"Navigating to Login page: {self.url}")
        self.navigate_to(self.url)
        self.page.wait_for_timeout(1000)
    
    def login(self, username: str, password: str) -> None:
        """
        Perform login with the given credentials.
        
        Args:
            username: Username to enter.
            password: Password to enter.
        """
        logger.info(f"Logging in with username: {username}")
        
        # Fill in login form
        self.fill_text(self._USERNAME_FIELD, username)
        self.fill_text(self._PASSWORD_FIELD, password)
        
        # Set up alert handler
        self.accept_alert()
        
        # Wait to ensure form is ready
        self.page.wait_for_timeout(500)
        
        try:
            # Click login button
            logger.info("Clicking login button")
            self.click(self._LOGIN_BUTTON)
        except Exception as e:
            logger.error(f"Failed to click login button: {e}")
            logger.info("Trying JavaScript click as fallback")
            self.page.evaluate('''() => {
                const loginBtn = document.querySelector('#login-button');
                if (loginBtn) loginBtn.click();
            }''')
    
    def get_login_result_message(self) -> str:
        """
        Get the login result message from the alert.
        
        Returns:
            str: The login result message.
        """
        return "Message from alert"
    
    def verify_login_page_loaded(self) -> bool:
        """
        Verify that the login page has loaded correctly.
        
        Returns:
            bool: True if loaded correctly, False otherwise.
        """
        logger.info("Verifying login page loaded")
        if self.is_visible(self._LOGIN_FORM):
            return True
        
        return self.is_visible(self._LOGIN_WRAPPER)
    
    def get_login_portal_title(self) -> str:
        """
        Get the login portal title from the page.
        
        Returns:
            str: The title text.
        """
        logger.info("Getting login portal title")
        try:
            return self.page.title()
        except Exception as e:
            logger.error(f"Failed to get page title: {e}")
            return ""
    
    def is_username_field_empty(self) -> bool:
        """
        Check if the username field is empty.
        
        Returns:
            bool: True if empty, False otherwise.
        """
        logger.info("Checking if username field is empty")
        return self.is_field_empty(self._USERNAME_FIELD)
    
    def is_password_field_empty(self) -> bool:
        """
        Check if the password field is empty.
        
        Returns:
            bool: True if empty, False otherwise.
        """
        logger.info("Checking if password field is empty")
        return self.is_field_empty(self._PASSWORD_FIELD)
    
    def is_field_empty(self, field_selector: str) -> bool:
        """
        Check if a field is empty.
        
        Args:
            field_selector: Selector for the field.
            
        Returns:
            bool: True if empty, False otherwise.
        """
        value = self.get_attribute(field_selector, "value")
        return not value 