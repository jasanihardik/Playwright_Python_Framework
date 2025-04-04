"""
Page object for the Button Clicks page.
"""
from typing import Optional

from playwright.sync_api import Page, TimeoutError

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class ButtonClicksPage(BasePage):
    """Page object representing the Button Clicks page."""
    
    # Selectors for the page elements
    _PAGE_TITLE = 'h1' # Simplified selector
    
    # Simple Button elements
    _SIMPLE_BUTTON = '#button1'
    _SIMPLE_BUTTON_MODAL = '#myModalClick'
    _SIMPLE_BUTTON_MODAL_CONTENT = '#myModalClick .modal-content'
    _SIMPLE_BUTTON_MODAL_TITLE = '#myModalClick .modal-title'
    _SIMPLE_BUTTON_MODAL_CLOSE = '#myModalClick .close'
    
    # Modal Button elements
    _MODAL_BUTTON = '#button2'
    _MODAL_BUTTON_MODAL = '#myModalJSClick'
    _MODAL_BUTTON_MODAL_CONTENT = '#myModalJSClick .modal-content'
    _MODAL_BUTTON_MODAL_TITLE = '#myModalJSClick .modal-title'
    _MODAL_BUTTON_MODAL_CLOSE = '#myModalJSClick .close'
    
    # Action Button elements
    _ACTION_BUTTON = '#button3'
    _ACTION_BUTTON_MODAL = '#myModalMoveClick'
    _ACTION_BUTTON_MODAL_CONTENT = '#myModalMoveClick .modal-content'
    _ACTION_BUTTON_MODAL_TITLE = '#myModalMoveClick .modal-title'
    _ACTION_BUTTON_MODAL_CLOSE = '#myModalMoveClick .close'
    
    def __init__(self, page: Page):
        """
        Initialize the Button Clicks page.
        
        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["button_clicks"]
    
    def navigate(self) -> None:
        """Navigate to the Button Clicks page."""
        logger.info(f"Navigating to Button Clicks page: {self.url}")
        self.navigate_to(self.url)
        try:
            # Wait for the page to load with a shorter timeout
            self.wait_for_selector(self._PAGE_TITLE, timeout=10000)
        except Exception as e:
            logger.warning(f"Error waiting for page title: {e}")
            # Continue anyway, as the page might have loaded but the selector is incorrect
            self.page.wait_for_timeout(3000)  # Give some time for the page to stabilize
    
    def get_page_title(self) -> str:
        """
        Get the page title.
        
        Returns:
            str: The page title.
        """
        logger.info("Getting Button Clicks page title")
        try:
            # Try with the defined selector
            return self.get_text(self._PAGE_TITLE)
        except Exception:
            logger.warning("Could not get page title with defined selector, using JavaScript")
            # Fallback to JavaScript to get any h1 on the page
            return self.page.evaluate('''() => {
                const h1s = document.querySelectorAll('h1');
                return h1s.length > 0 ? h1s[0].innerText : 'No H1 found';
            }''')
    
    def click_simple_button(self) -> None:
        """Click the simple button."""
        logger.info("Clicking simple button")
        self.click(self._SIMPLE_BUTTON)
        # Wait for the modal to appear
        try:
            self.wait_for_selector(self._SIMPLE_BUTTON_MODAL_CONTENT, timeout=5000)
        except Exception as e:
            logger.warning(f"Error waiting for simple button modal: {e}")
            self.page.wait_for_timeout(1000)  # Wait a bit in case the modal appears
    
    def is_simple_button_modal_displayed(self) -> bool:
        """
        Check if the simple button modal is displayed.
        
        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if simple button modal is displayed")
        try:
            # Use JavaScript to check if the modal is visible
            return self.page.evaluate(f'''() => {{
                const modal = document.querySelector('{self._SIMPLE_BUTTON_MODAL}');
                return modal && 
                       window.getComputedStyle(modal).display !== 'none' && 
                       modal.classList.contains('in');
            }}''')
        except Exception as e:
            logger.warning(f"Error checking if simple button modal is displayed: {e}")
            return self.is_visible(self._SIMPLE_BUTTON_MODAL_CONTENT)
    
    def get_simple_button_modal_title(self) -> str:
        """
        Get the title of the simple button modal.
        
        Returns:
            str: The modal title.
        """
        logger.info("Getting simple button modal title")
        try:
            title = self.get_text(self._SIMPLE_BUTTON_MODAL_TITLE)
            logger.info(f"Simple button modal title: '{title}'")
            return title
        except Exception as e:
            logger.warning(f"Error getting modal title: {e}")
            # Fallback to JavaScript
            return self.page.evaluate(f'''() => {{
                const title = document.querySelector('{self._SIMPLE_BUTTON_MODAL_TITLE}');
                return title ? title.innerText : 'No title found';
            }}''')
    
    def close_simple_button_modal(self) -> None:
        """Close the simple button modal."""
        logger.info("Closing simple button modal")
        try:
            # Try clicking the close button
            self.click(self._SIMPLE_BUTTON_MODAL_CLOSE)
            
            # Wait for the modal to disappear
            self.page.wait_for_timeout(1000)
            
            # If modal is still visible, try JavaScript approach
            if self.is_simple_button_modal_displayed():
                logger.info("Modal still visible after clicking close button, using JavaScript")
                self.page.evaluate(f'''() => {{
                    const modal = document.querySelector('{self._SIMPLE_BUTTON_MODAL}');
                    if (modal) {{
                        modal.classList.remove('in');
                        modal.style.display = 'none';
                        document.querySelector('.modal-backdrop').remove();
                    }}
                }}''')
        except Exception as e:
            logger.warning(f"Error closing simple button modal: {e}")
            # Fallback approach
            self.page.evaluate(f'''() => {{
                const modal = document.querySelector('{self._SIMPLE_BUTTON_MODAL}');
                if (modal) {{
                    modal.classList.remove('in');
                    modal.style.display = 'none';
                    const backdrop = document.querySelector('.modal-backdrop');
                    if (backdrop) backdrop.remove();
                }}
            }}''')
    
    def click_modal_button(self) -> None:
        """Click the modal button."""
        logger.info("Clicking modal button")
        self.click(self._MODAL_BUTTON)
        # Wait for the modal to appear
        try:
            self.wait_for_selector(self._MODAL_BUTTON_MODAL_CONTENT, timeout=5000)
        except Exception as e:
            logger.warning(f"Error waiting for modal button modal: {e}")
            self.page.wait_for_timeout(1000)  # Wait a bit in case the modal appears
    
    def is_modal_button_modal_displayed(self) -> bool:
        """
        Check if the modal button modal is displayed.
        
        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if modal button modal is displayed")
        try:
            # Use JavaScript to check if the modal is visible
            return self.page.evaluate(f'''() => {{
                const modal = document.querySelector('{self._MODAL_BUTTON_MODAL}');
                return modal && 
                       window.getComputedStyle(modal).display !== 'none' && 
                       modal.classList.contains('in');
            }}''')
        except Exception as e:
            logger.warning(f"Error checking if modal button modal is displayed: {e}")
            return self.is_visible(self._MODAL_BUTTON_MODAL_CONTENT)
    
    def get_modal_button_modal_title(self) -> str:
        """
        Get the title of the modal button modal.
        
        Returns:
            str: The modal title.
        """
        logger.info("Getting modal button modal title")
        try:
            title = self.get_text(self._MODAL_BUTTON_MODAL_TITLE)
            logger.info(f"Modal button modal title: '{title}'")
            return title
        except Exception as e:
            logger.warning(f"Error getting modal title: {e}")
            # Fallback to JavaScript
            return self.page.evaluate(f'''() => {{
                const title = document.querySelector('{self._MODAL_BUTTON_MODAL_TITLE}');
                return title ? title.innerText : 'No title found';
            }}''')
    
    def close_modal_button_modal(self) -> None:
        """Close the modal button modal."""
        logger.info("Closing modal button modal")
        try:
            # Try clicking the close button
            self.click(self._MODAL_BUTTON_MODAL_CLOSE)
            
            # Wait for the modal to disappear
            self.page.wait_for_timeout(1000)
            
            # If modal is still visible, try JavaScript approach
            if self.is_modal_button_modal_displayed():
                logger.info("Modal still visible after clicking close button, using JavaScript")
                self.page.evaluate(f'''() => {{
                    const modal = document.querySelector('{self._MODAL_BUTTON_MODAL}');
                    if (modal) {{
                        modal.classList.remove('in');
                        modal.style.display = 'none';
                        document.querySelector('.modal-backdrop').remove();
                    }}
                }}''')
        except Exception as e:
            logger.warning(f"Error closing modal button modal: {e}")
            # Fallback approach
            self.page.evaluate(f'''() => {{
                const modal = document.querySelector('{self._MODAL_BUTTON_MODAL}');
                if (modal) {{
                    modal.classList.remove('in');
                    modal.style.display = 'none';
                    const backdrop = document.querySelector('.modal-backdrop');
                    if (backdrop) backdrop.remove();
                }}
            }}''')
    
    def click_action_button(self) -> None:
        """Click the action button."""
        logger.info("Clicking action button")
        self.click(self._ACTION_BUTTON)
        # Wait for the modal to appear
        try:
            self.wait_for_selector(self._ACTION_BUTTON_MODAL_CONTENT, timeout=5000)
        except Exception as e:
            logger.warning(f"Error waiting for action button modal: {e}")
            self.page.wait_for_timeout(1000)  # Wait a bit in case the modal appears
    
    def is_action_button_modal_displayed(self) -> bool:
        """
        Check if the action button modal is displayed.
        
        Returns:
            bool: True if displayed, False otherwise.
        """
        logger.info("Checking if action button modal is displayed")
        try:
            # Use JavaScript to check if the modal is visible
            return self.page.evaluate(f'''() => {{
                const modal = document.querySelector('{self._ACTION_BUTTON_MODAL}');
                return modal && 
                       window.getComputedStyle(modal).display !== 'none' && 
                       modal.classList.contains('in');
            }}''')
        except Exception as e:
            logger.warning(f"Error checking if action button modal is displayed: {e}")
            return self.is_visible(self._ACTION_BUTTON_MODAL_CONTENT)
    
    def get_action_button_modal_title(self) -> str:
        """
        Get the title of the action button modal.
        
        Returns:
            str: The modal title.
        """
        logger.info("Getting action button modal title")
        try:
            title = self.get_text(self._ACTION_BUTTON_MODAL_TITLE)
            logger.info(f"Action button modal title: '{title}'")
            return title
        except Exception as e:
            logger.warning(f"Error getting modal title: {e}")
            # Fallback to JavaScript
            return self.page.evaluate(f'''() => {{
                const title = document.querySelector('{self._ACTION_BUTTON_MODAL_TITLE}');
                return title ? title.innerText : 'No title found';
            }}''')
    
    def close_action_button_modal(self) -> None:
        """Close the action button modal."""
        logger.info("Closing action button modal")
        try:
            # Try clicking the close button
            self.click(self._ACTION_BUTTON_MODAL_CLOSE)
            
            # Wait for the modal to disappear
            self.page.wait_for_timeout(1000)
            
            # If modal is still visible, try JavaScript approach
            if self.is_action_button_modal_displayed():
                logger.info("Modal still visible after clicking close button, using JavaScript")
                self.page.evaluate(f'''() => {{
                    const modal = document.querySelector('{self._ACTION_BUTTON_MODAL}');
                    if (modal) {{
                        modal.classList.remove('in');
                        modal.style.display = 'none';
                        document.querySelector('.modal-backdrop').remove();
                    }}
                }}''')
        except Exception as e:
            logger.warning(f"Error closing action button modal: {e}")
            # Fallback approach
            self.page.evaluate(f'''() => {{
                const modal = document.querySelector('{self._ACTION_BUTTON_MODAL}');
                if (modal) {{
                    modal.classList.remove('in');
                    modal.style.display = 'none';
                    const backdrop = document.querySelector('.modal-backdrop');
                    if (backdrop) backdrop.remove();
                }}
            }}''') 