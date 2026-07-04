"""
Page object for the Contact Us page.
"""

from playwright.sync_api import Page

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class ContactUsPage(BasePage):
    """Page object representing the Contact Us page."""

    # Field names kept for test compatibility
    _FIRST_NAME_FIELD = "First Name"
    _LAST_NAME_FIELD = "Last Name"
    _EMAIL_FIELD = "Email Address"
    _COMMENT_FIELD = "Comments"

    # Button names
    _SUBMIT_BUTTON = "SUBMIT"
    _RESET_BUTTON = "RESET"

    # Message text
    _SUCCESS_MESSAGE = "Thank You for your Message!"

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

    def fill_contact_form(
        self,
        first_name: str,
        last_name: str,
        email: str,
        comment: str,
    ) -> None:
        """
        Fill in the contact form.

        Args:
            first_name: First name to enter.
            last_name: Last name to enter.
            email: Email to enter.
            comment: Comment to enter.
        """
        logger.info("Filling contact form")

        self.page.get_by_placeholder(self._FIRST_NAME_FIELD).fill(first_name)
        self.page.get_by_placeholder(self._LAST_NAME_FIELD).fill(last_name)
        self.page.get_by_placeholder(self._EMAIL_FIELD).fill(email)
        self.page.get_by_placeholder(self._COMMENT_FIELD).fill(comment)

    def submit_form(self) -> None:
        """Submit the contact form."""
        logger.info("Submitting contact form")
        self.page.get_by_role("button", name=self._SUBMIT_BUTTON).click()

    def reset_form(self) -> None:
        """Reset the contact form."""
        logger.info("Resetting contact form")
        self.page.get_by_role("button", name=self._RESET_BUTTON).click()

    def get_success_message(self) -> str:
        """
        Get the success message after form submission.

        Returns:
            str: The success message text.
        """
        logger.info("Getting success message")

        message = self.page.get_by_role(
            "heading",
            name=self._SUCCESS_MESSAGE,
        ).text_content()

        return message.strip() if message else ""

    def is_success_message_displayed(self) -> bool:
        """
        Check if the success message is displayed.

        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if success message is displayed")

        return self.page.get_by_role(
            "heading",
            name=self._SUCCESS_MESSAGE,
        ).is_visible()

    def get_error_message(self) -> str:
        """
        Get the error message when form submission fails.

        Returns:
            str: The error message text.
        """
        logger.info("Getting error message")

        # The WebDriverUniversity error page renders the validation error as
        # plain body text, not as a labelled alert or heading.
        error_message = self.page.locator("body").text_content()

        return error_message.strip() if error_message else ""

    def is_field_empty(self, field_selector: str) -> bool:
        """
        Check if a field is empty.

        Args:
            field_selector: Field placeholder text.

        Returns:
            bool: True if empty, False otherwise.
        """
        logger.info(f"Checking if field is empty: {field_selector}")

        value = self.page.get_by_placeholder(field_selector).input_value()

        return not value