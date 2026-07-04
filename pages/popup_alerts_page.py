"""
Page object for the Popup & Alerts page.
"""

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage
from utilities.logger import logger
from utilities.screenshot_utils import ScreenshotUtils


class PopupAlertsPage(BasePage):
    """Page object for the Popup & Alerts page."""

    # URL
    _PAGE_URL = "https://webdriveruniversity.com/Popup-Alerts/index.html"

    # Visible text
    _PAGE_HEADER = "Annoying Popup & Alerts!"
    _CLICK_ME_TEXT = "CLICK ME!"

    # Card headings
    _JS_ALERT_CARD_HEADER = "JavaScript Alert"
    _MODAL_POPUP_CARD_HEADER = "Modal Popup"
    _AJAX_LOADER_CARD_HEADER = "Ajax Loader"
    _JS_CONFIRM_CARD_HEADER = "JavaScript Confirm Box"

    # Stable fallback selectors for elements that do not expose useful roles
    _JS_CONFIRM_TEXT = "#confirm-alert-text"
    _MODAL_POPUP = "div.modal"
    _MODAL_POPUP_TITLE = ".modal-title"
    _MODAL_POPUP_BODY = ".modal-body"
    _AJAX_SPINNER = "#loader"
    _AJAX_CONTENT = "#myDiv"
    _AJAX_MODAL_TITLE = "#myDiv h1"
    _AJAX_MODAL_BODY = "#myDiv p"

    def __init__(self, page: Page) -> None:
        """
        Initialize the PopupAlertsPage class.

        Args:
            page: Playwright page object.
        """
        super().__init__(page)

        self.page_header: Locator = self.page.get_by_role(
            "heading",
            name=self._PAGE_HEADER,
        )

        self.js_alert_button: Locator = self._get_click_me_button_for_card(
            self._JS_ALERT_CARD_HEADER,
        )

        self.modal_popup_button: Locator = self._get_click_me_button_for_card(
            self._MODAL_POPUP_CARD_HEADER,
        )

        self.ajax_loader_button: Locator = self._get_click_me_button_for_card(
            self._AJAX_LOADER_CARD_HEADER,
        )

        self.js_confirm_button: Locator = self._get_click_me_button_for_card(
            self._JS_CONFIRM_CARD_HEADER,
        )

    def navigate(self) -> None:
        """
        Navigate to the Popup & Alerts page.
        """
        logger.info(f"Navigating to Popup & Alerts page: {self._PAGE_URL}")
        self.navigate_to(self._PAGE_URL)
        self.wait_for_page_load()

    def get_page_header(self) -> str:
        """
        Get the page header text.

        Returns:
            str: The header text.
        """
        logger.info("Getting page header text")

        text = self.page_header.text_content()
        return text.strip() if text else ""

    def click_js_alert_button(self, dialog_handler) -> None:
        """
        Click the JavaScript Alert button.

        Args:
            dialog_handler: Function to handle the dialog.
        """
        logger.info("Clicking JavaScript Alert button")

        self.page.on("dialog", dialog_handler)
        self.js_alert_button.click()

    def get_js_alert_text(self) -> str:
        """
        Get the JavaScript Alert result text.

        Returns:
            str: The alert result text.
        """
        logger.info("Getting JavaScript Alert result text")

        text = self.page.locator(self._JS_CONFIRM_TEXT).text_content()
        return text.strip() if text else ""

    def click_modal_popup_button(self) -> None:
        """
        Click the Modal Popup button.
        """
        logger.info("Clicking Modal Popup button")
        self.modal_popup_button.click()

    def is_modal_popup_displayed(self) -> bool:
        """
        Check if the Modal Popup is displayed.

        Returns:
            bool: True if the Modal Popup is displayed, False otherwise.
        """
        logger.info("Checking if Modal Popup is displayed")

        modal_popup = self.page.locator(self._MODAL_POPUP)

        try:
            expect(modal_popup).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def get_modal_popup_title(self) -> str:
        """
        Get the Modal Popup title.

        Returns:
            str: The Modal Popup title.
        """
        logger.info("Getting Modal Popup title")

        text = self.page.locator(self._MODAL_POPUP_TITLE).text_content()
        return text.strip() if text else ""

    def get_modal_popup_body(self) -> str:
        """
        Get the Modal Popup body text.

        Returns:
            str: The Modal Popup body text.
        """
        logger.info("Getting Modal Popup body text")

        text = self.page.locator(self._MODAL_POPUP_BODY).text_content()
        return text.strip() if text else ""

    def close_modal_popup(self) -> None:
        """
        Close the Modal Popup.
        """
        logger.info("Closing Modal Popup")

        close_button = self.page.locator(self._MODAL_POPUP).get_by_role(
            "button",
            name="Close",
        )
        close_button.click()

    def click_js_confirm_button(self, dialog_handler) -> None:
        """
        Click the JavaScript Confirm Box button.

        Args:
            dialog_handler: Function to handle the dialog.
        """
        logger.info("Clicking JavaScript Confirm Box button")

        self.page.on("dialog", dialog_handler)
        self.js_confirm_button.click()

    def get_js_confirm_text(self) -> str:
        """
        Get the JavaScript Confirm Box result text.

        Returns:
            str: The confirm box result text.
        """
        logger.info("Getting JavaScript Confirm Box result text")

        confirm_text = self.page.locator(self._JS_CONFIRM_TEXT)
        expect(confirm_text).to_be_visible(timeout=5000)

        text = confirm_text.text_content()
        return text.strip() if text else ""

    def click_ajax_loader_button(self) -> None:
        """
        Click the AJAX Loader button.
        """
        logger.info("Clicking AJAX Loader button")

        self.ajax_loader_button.click()
        self.page.wait_for_load_state("domcontentloaded")

    def wait_for_ajax_spinner(self) -> None:
        """
        Wait for the AJAX spinner to appear and disappear.
        """
        logger.info("Waiting for AJAX loader")

        ajax_spinner = self.page.locator(self._AJAX_SPINNER)
        ajax_content = self.page.locator(self._AJAX_CONTENT)

        logger.info("Waiting for AJAX spinner to appear")
        expect(ajax_spinner).to_be_visible(timeout=5000)

        logger.info("Waiting for AJAX spinner to disappear")
        expect(ajax_spinner).to_be_hidden(timeout=15000)

        logger.info("Waiting for AJAX content to appear")
        expect(ajax_content).to_be_visible(timeout=15000)

    def is_ajax_modal_displayed(self) -> bool:
        """
        Check if the AJAX Modal is displayed.

        Returns:
            bool: True if the AJAX Modal is displayed, False otherwise.
        """
        logger.info("Checking if AJAX Modal is displayed")

        ajax_content = self.page.locator(self._AJAX_CONTENT)

        try:
            expect(ajax_content).to_be_visible(timeout=5000)
            return True
        except AssertionError:
            return False

    def get_ajax_modal_title(self) -> str:
        """
        Get the AJAX Modal title.

        Returns:
            str: The AJAX Modal title.
        """
        logger.info("Getting AJAX Modal title")

        text = self.page.locator(self._AJAX_MODAL_TITLE).text_content()
        return text.strip() if text else ""

    def get_ajax_modal_body(self) -> str:
        """
        Get the AJAX Modal body text.

        Returns:
            str: The AJAX Modal body text.
        """
        logger.info("Getting AJAX Modal body text")

        text = self.page.locator(self._AJAX_MODAL_BODY).text_content()
        return text.strip() if text else ""

    def close_ajax_modal(self) -> None:
        """
        Close the AJAX Modal.
        """
        logger.info("Closing AJAX Modal")

        ajax_content = self.page.locator(self._AJAX_CONTENT)
        close_button = ajax_content.get_by_text("Close", exact=True)
        close_button.click()

    def wait_for_page_load(self) -> None:
        """
        Wait for the page to load completely.
        """
        logger.info("Waiting for Popup & Alerts page to load")
        expect(self.page_header).to_be_visible(timeout=5000)

    def take_screenshot(self, test_name: str, screenshot_name: str) -> str:
        """
        Take a screenshot of the current page state.

        Args:
            test_name: Name of the test.
            screenshot_name: Name for the screenshot.

        Returns:
            str: Path to the saved screenshot.
        """
        logger.info(f"Taking screenshot for test: {test_name}, {screenshot_name}")

        return ScreenshotUtils.take_screenshot(
            self.page,
            f"{test_name}_{screenshot_name}",
        )

    def _get_click_me_button_for_card(self, card_heading: str) -> Locator:
        """
        Get the CLICK ME control inside a specific card section.

        Args:
            card_heading: Visible heading text of the card.

        Returns:
            Locator for the CLICK ME control inside that card.
        """
        card = self.page.get_by_role(
            "heading",
            name=card_heading,
        ).locator("xpath=ancestor::div[contains(@class, 'thumbnail')]")

        return card.get_by_text(self._CLICK_ME_TEXT, exact=True)