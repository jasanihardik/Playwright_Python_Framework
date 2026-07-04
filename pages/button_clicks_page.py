"""
Page object for the Button Clicks page.
"""

from playwright.sync_api import Locator, Page, expect

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class ButtonClicksPage(BasePage):
    """Page object representing the Button Clicks page."""

    # Page text
    _PAGE_TITLE_TEXT = "Lets Get Clicking!"

    # Button text
    _SIMPLE_BUTTON_TEXT = "CLICK ME!"
    _MODAL_BUTTON_TEXT = "CLICK ME!!"
    _ACTION_BUTTON_TEXT = "CLICK ME!!!"

    # Modal title text
    _SIMPLE_BUTTON_MODAL_TITLE_TEXT = "Congratulations!"
    _MODAL_BUTTON_MODAL_TITLE_TEXT = "It’s that Easy!! Well I think it is....."
    _ACTION_BUTTON_MODAL_TITLE_TEXT = (
        "Well done! the Action Move & Click can become very useful!"
    )

    # Modal body text
    _SIMPLE_BUTTON_MODAL_BODY_TEXT = "Well done for successfully using the click() method!"
    _MODAL_BUTTON_MODAL_BODY_TEXT = "We can use JavaScript code if all else fails!"
    _ACTION_BUTTON_MODAL_BODY_TEXT = "Advanced user interactions"

    def __init__(self, page: Page) -> None:
        """
        Initialize the Button Clicks page.

        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["button_clicks"]

        # Role locator: page heading
        self.page_title: Locator = self.page.get_by_role(
            "heading",
            name=self._PAGE_TITLE_TEXT,
        )

        # Text locators: visible click controls on the page
        self.simple_button: Locator = self.page.get_by_text(
            self._SIMPLE_BUTTON_TEXT,
            exact=True,
        )

        self.modal_button: Locator = self.page.get_by_text(
            self._MODAL_BUTTON_TEXT,
            exact=True,
        )

        self.action_button: Locator = self.page.get_by_text(
            self._ACTION_BUTTON_TEXT,
            exact=True,
        )

    def navigate(self) -> None:
        """
        Navigate to the Button Clicks page.
        """
        logger.info(f"Navigating to Button Clicks page: {self.url}")

        self.navigate_to(self.url)
        expect(self.page_title).to_be_visible(timeout=10000)

    def get_page_title(self) -> str:
        """
        Get the page title.

        Returns:
            str: The page title.
        """
        logger.info("Getting Button Clicks page title")

        text = self.page_title.text_content()
        return text.strip() if text else ""

    def click_simple_button(self) -> None:
        """
        Click the simple button.
        """
        logger.info("Clicking simple button")

        self.simple_button.click()
        expect(self._simple_button_modal()).to_be_visible(timeout=5000)

    def is_simple_button_modal_displayed(self) -> bool:
        """
        Check if the simple button modal is displayed.

        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if simple button modal is displayed")

        return self._simple_button_modal().is_visible()

    def get_simple_button_modal_title(self) -> str:
        """
        Get the title of the simple button modal.

        Returns:
            str: The modal title.
        """
        logger.info("Getting simple button modal title")

        title = self._simple_button_modal().get_by_text(
            self._SIMPLE_BUTTON_MODAL_TITLE_TEXT,
            exact=True,
        )

        text = title.text_content()
        return text.strip() if text else ""

    def close_simple_button_modal(self) -> None:
        """
        Close the simple button modal.
        """
        logger.info("Closing simple button modal")

        modal = self._simple_button_modal()
        modal.get_by_role("button", name="Close").click()
        expect(modal).to_be_hidden(timeout=5000)

    def click_modal_button(self) -> None:
        """
        Click the modal button.
        """
        logger.info("Clicking modal button")

        self.modal_button.click()
        expect(self._modal_button_modal()).to_be_visible(timeout=5000)

    def is_modal_button_modal_displayed(self) -> bool:
        """
        Check if the modal button modal is displayed.

        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if modal button modal is displayed")

        return self._modal_button_modal().is_visible()

    def get_modal_button_modal_title(self) -> str:
        """
        Get the title of the modal button modal.

        Returns:
            str: The modal title.
        """
        logger.info("Getting modal button modal title")

        title = self._modal_button_modal().get_by_text(
            self._MODAL_BUTTON_MODAL_TITLE_TEXT,
            exact=True,
        )

        text = title.text_content()
        return text.strip() if text else ""

    def close_modal_button_modal(self) -> None:
        """
        Close the modal button modal.
        """
        logger.info("Closing modal button modal")

        modal = self._modal_button_modal()
        modal.get_by_role("button", name="Close").click()
        expect(modal).to_be_hidden(timeout=5000)

    def click_action_button(self) -> None:
        """
        Click the action button.
        """
        logger.info("Clicking action button")

        self.action_button.click()
        expect(self._action_button_modal()).to_be_visible(timeout=5000)

    def is_action_button_modal_displayed(self) -> bool:
        """
        Check if the action button modal is displayed.

        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if action button modal is displayed")

        return self._action_button_modal().is_visible()

    def get_action_button_modal_title(self) -> str:
        """
        Get the title of the action button modal.

        Returns:
            str: The modal title.
        """
        logger.info("Getting action button modal title")

        title = self._action_button_modal().get_by_text(
            self._ACTION_BUTTON_MODAL_TITLE_TEXT,
            exact=True,
        )

        text = title.text_content()
        return text.strip() if text else ""

    def close_action_button_modal(self) -> None:
        """
        Close the action button modal.
        """
        logger.info("Closing action button modal")

        modal = self._action_button_modal()
        modal.get_by_role("button", name="Close").click()
        expect(modal).to_be_hidden(timeout=5000)

    def _simple_button_modal(self) -> Locator:
        """
        Get the simple button modal.

        Returns:
            Locator for the simple button modal.
        """
        return self.page.get_by_role("dialog").filter(
            has_text=self._SIMPLE_BUTTON_MODAL_TITLE_TEXT,
        )

    def _modal_button_modal(self) -> Locator:
        """
        Get the modal button modal.

        Returns:
            Locator for the modal button modal.
        """
        return self.page.get_by_role("dialog").filter(
            has_text=self._MODAL_BUTTON_MODAL_TITLE_TEXT,
        )

    def _action_button_modal(self) -> Locator:
        """
        Get the action button modal.

        Returns:
            Locator for the action button modal.
        """
        return self.page.get_by_role("dialog").filter(
            has_text=self._ACTION_BUTTON_MODAL_TITLE_TEXT,
        )