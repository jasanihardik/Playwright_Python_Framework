"""
Page object for the Popup & Alerts page.
"""
from playwright.sync_api import Page, Dialog
from utilities.logger import logger
from pages.base_page import BasePage


class PopupAlertsPage(BasePage):
    """
    Page object for the Popup & Alerts page.
    """

    # URL
    _PAGE_URL = "https://webdriveruniversity.com/Popup-Alerts/index.html"
    
    # Selectors
    _PAGE_HEADER = "h1"
    
    # JavaScript Alert elements
    _JS_ALERT_BUTTON = "#button1"
    _JS_ALERT_TEXT = "#confirm-alert-text"
    
    # Modal Popup elements
    _MODAL_POPUP_BUTTON = "#button2"
    _MODAL_POPUP = "div.modal"
    _MODAL_POPUP_TITLE = ".modal-title"
    _MODAL_POPUP_BODY = ".modal-body"
    _MODAL_POPUP_CLOSE = ".modal-footer button"
    
    # JavaScript Confirm Box elements
    _JS_CONFIRM_BUTTON = "#button4"
    _JS_CONFIRM_TEXT = "#confirm-alert-text"
    
    # AJAX Loader elements
    _AJAX_LOADER_BUTTON = "#button3"
    _AJAX_SPINNER = "#loader"
    _AJAX_MODAL = "#myDiv"
    _AJAX_MODAL_TITLE = "#myDiv h1"
    _AJAX_MODAL_BODY = "#myDiv p"
    _AJAX_MODAL_CLOSE = "#myDiv .close"

    def __init__(self, page: Page) -> None:
        """
        Initialize the PopupAlertsPage class.
        
        Args:
            page: Playwright page object.
        """
        super().__init__(page)
    
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
        return self.get_text(self._PAGE_HEADER)
    
    def click_js_alert_button(self, dialog_handler) -> None:
        """
        Click the JavaScript Alert button.
        
        Args:
            dialog_handler: Function to handle the dialog.
        """
        logger.info("Clicking JavaScript Alert button")
        self.page.on("dialog", dialog_handler)
        self.click(self._JS_ALERT_BUTTON)
    
    def get_js_alert_text(self) -> str:
        """
        Get the JavaScript Alert result text.
        
        Returns:
            str: The alert result text.
        """
        logger.info("Getting JavaScript Alert result text")
        return self.get_text(self._JS_ALERT_TEXT)
    
    def click_modal_popup_button(self) -> None:
        """
        Click the Modal Popup button.
        """
        logger.info("Clicking Modal Popup button")
        self.click(self._MODAL_POPUP_BUTTON)
    
    def is_modal_popup_displayed(self) -> bool:
        """
        Check if the Modal Popup is displayed.
        
        Returns:
            bool: True if the Modal Popup is displayed, False otherwise.
        """
        logger.info("Checking if Modal Popup is displayed")
        return self.is_visible(self._MODAL_POPUP)
    
    def get_modal_popup_title(self) -> str:
        """
        Get the Modal Popup title.
        
        Returns:
            str: The Modal Popup title.
        """
        logger.info("Getting Modal Popup title")
        return self.get_text(self._MODAL_POPUP_TITLE)
    
    def get_modal_popup_body(self) -> str:
        """
        Get the Modal Popup body text.
        
        Returns:
            str: The Modal Popup body text.
        """
        logger.info("Getting Modal Popup body text")
        return self.get_text(self._MODAL_POPUP_BODY)
    
    def close_modal_popup(self) -> None:
        """
        Close the Modal Popup.
        """
        logger.info("Closing Modal Popup")
        self.click(self._MODAL_POPUP_CLOSE)
        self.wait_for_invisibility(self._MODAL_POPUP)
    
    def click_js_confirm_button(self, dialog_handler) -> None:
        """
        Click the JavaScript Confirm Box button.
        
        Args:
            dialog_handler: Function to handle the dialog.
        """
        logger.info("Clicking JavaScript Confirm Box button")
        self.page.on("dialog", dialog_handler)
        self.click(self._JS_CONFIRM_BUTTON)
    
    def get_js_confirm_text(self) -> str:
        """
        Get the JavaScript Confirm Box result text.
        
        Returns:
            str: The confirm box result text.
        """
        logger.info("Getting JavaScript Confirm Box result text")
        return self.get_text(self._JS_CONFIRM_TEXT)
    
    def click_ajax_loader_button(self) -> None:
        """
        Click the AJAX Loader button.
        """
        logger.info("Clicking AJAX Loader button")
        self.click(self._AJAX_LOADER_BUTTON)
    
    def wait_for_ajax_spinner(self) -> None:
        """
        Wait for the AJAX spinner to appear and disappear.
        """
        logger.info("Waiting for AJAX loader")
        # First navigate to the AJAX page that opens in a new tab
        self.page.wait_for_timeout(1000)  # Wait a moment to let the new tab open
        pages = self.page.context.pages
        if len(pages) > 1:
            # Use the latest opened page
            new_page = pages[-1]
            self.page = new_page
        
        # Wait for AJAX loader to appear
        logger.info("Waiting for AJAX spinner to appear")
        self.wait_for_selector(self._AJAX_SPINNER)
        
        # Wait for AJAX loader to disappear
        logger.info("Waiting for AJAX spinner to disappear")
        self.page.wait_for_timeout(5000)  # Wait up to 5 seconds for spinner to disappear
        
        # Wait for AJAX content to appear
        logger.info("Waiting for AJAX content to appear")
        self.wait_for_selector(self._AJAX_MODAL)
    
    def is_ajax_modal_displayed(self) -> bool:
        """
        Check if the AJAX Modal is displayed.
        
        Returns:
            bool: True if the AJAX Modal is displayed, False otherwise.
        """
        logger.info("Checking if AJAX Modal is displayed")
        return self.is_visible(self._AJAX_MODAL)
    
    def get_ajax_modal_title(self) -> str:
        """
        Get the AJAX Modal title.
        
        Returns:
            str: The AJAX Modal title.
        """
        logger.info("Getting AJAX Modal title")
        return self.get_text(self._AJAX_MODAL_TITLE)
    
    def get_ajax_modal_body(self) -> str:
        """
        Get the AJAX Modal body text.
        
        Returns:
            str: The AJAX Modal body text.
        """
        logger.info("Getting AJAX Modal body text")
        return self.get_text(self._AJAX_MODAL_BODY)
    
    def close_ajax_modal(self) -> None:
        """
        Close the AJAX Modal.
        """
        logger.info("Closing AJAX Modal")
        self.click(self._AJAX_MODAL_CLOSE)
        self.wait_for_invisibility(self._AJAX_MODAL)
    
    def wait_for_page_load(self) -> None:
        """
        Wait for the page to load completely.
        """
        logger.info("Waiting for Popup & Alerts page to load")
        self.wait_for_selector(self._PAGE_HEADER) 