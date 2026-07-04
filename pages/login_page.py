"""
Page object for the Login page.
"""

from playwright.sync_api import Locator, Page, expect

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class LoginPage(BasePage):
    """
    Page object representing the Login page.

    This page object uses Playwright locators such as get_by_placeholder()
    and get_by_role() instead of raw CSS selectors.
    """

    def __init__(self, page: Page) -> None:
        """
        Initialize the Login page.

        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["login"]

        self.username_field: Locator = self.page.get_by_placeholder("Username")
        self.password_field: Locator = self.page.get_by_placeholder("Password")
        self.login_button: Locator = self.page.get_by_role("button", name="Login")

    def navigate(self) -> None:
        """
        Navigate to the Login page.
        """
        logger.info("Navigating to Login page: %s", self.url)
        self.navigate_to(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Perform login with the given credentials.

        Args:
            username: Username to enter.
            password: Password to enter.
        """
        logger.info("Logging in with username: %s", username)

        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_login_result_message(self) -> str:
        """
        Get the login result message.

        Returns:
            Placeholder login result message.

        Notes:
            Current tests capture the browser alert directly from the test
            using Playwright's dialog event handling.
        """
        return "Message from alert"

    def verify_login_page_loaded(self) -> bool:
        """
        Verify that the login page has loaded correctly.

        Returns:
            True if the login page fields and login button are visible,
            otherwise False.
        """
        logger.info("Verifying login page loaded")

        try:
            expect(self.username_field).to_be_visible()
            expect(self.password_field).to_be_visible()
            expect(self.login_button).to_be_visible()
            return True
        except AssertionError:
            logger.exception("Login page did not load correctly")
            return False

    def get_login_portal_title(self) -> str:
        """
        Get the browser page title.

        Returns:
            Browser page title.
        """
        logger.info("Getting login portal title")

        try:
            return self.page.title()
        except Exception as error:
            logger.error("Failed to get page title: %s", error)
            return ""

    def is_username_field_empty(self) -> bool:
        """
        Check whether the username field is empty.

        Returns:
            True if the username field is empty, otherwise False.
        """
        logger.info("Checking if username field is empty")
        return self.is_field_empty(self.username_field)

    def is_password_field_empty(self) -> bool:
        """
        Check whether the password field is empty.

        Returns:
            True if the password field is empty, otherwise False.
        """
        logger.info("Checking if password field is empty")
        return self.is_field_empty(self.password_field)

    @staticmethod
    def is_field_empty(field: Locator) -> bool:
        """
        Check whether a field is empty.

        Args:
            field: Playwright locator for the input field.

        Returns:
            True if the field value is empty, otherwise False.
        """
        value = field.input_value()
        return value == ""