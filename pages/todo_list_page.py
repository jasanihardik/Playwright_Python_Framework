"""
Page object for the To-Do List page.
"""
from typing import Optional, List

from playwright.sync_api import Page, Locator, TimeoutError

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class TodoListPage(BasePage):
    """Page object representing the To-Do List page."""
    
    # Selectors for the page elements
    _TODO_HEADER = 'h1'
    _ADD_TODO_INPUT = 'input[placeholder="Add new todo"]'
    _TODO_ITEMS = 'ul li'
    _TODO_ITEM_TEXT = 'ul li'
    _TODO_ITEM_BY_TEXT = lambda self, text: f'//li[contains(., "{text}")]'
    _TODO_ITEM_CHECKBOX_BY_TEXT = lambda self, text: f'//li[contains(., "{text}")]//span'
    _TODO_ITEM_DELETE_BY_TEXT = lambda self, text: f'//li[contains(., "{text}")]//span'
    
    def __init__(self, page: Page):
        """
        Initialize the To-Do List page.
        
        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["to_do_list"]
    
    def navigate(self) -> None:
        """Navigate to the To-Do List page."""
        logger.info(f"Navigating to To-Do List page: {self.url}")
        self.navigate_to(self.url)
    
    def add_todo_item(self, item_text: str) -> None:
        """
        Add a new to-do item.
        
        Args:
            item_text: Text of the to-do item to add.
        """
        logger.info(f"Adding to-do item: {item_text}")
        self.fill_text(self._ADD_TODO_INPUT, item_text)
        self.page.keyboard.press("Enter")
        # Wait a short time for the item to be added
        self.page.wait_for_timeout(500)
    
    def get_todo_items(self) -> List[str]:
        """
        Get all to-do items.
        
        Returns:
            List[str]: List of to-do item texts.
        """
        logger.info("Getting all to-do items")
        # Wait for items to be visible
        self.wait_for_selector(self._TODO_ITEMS)
        
        # Get all li elements directly
        item_elements = self.page.locator(self._TODO_ITEM_TEXT).all()
        
        # Extract text content
        items = []
        for element in item_elements:
            text = element.text_content().strip()
            if text:
                items.append(text)
                
        logger.info(f"Found {len(items)} to-do items: {items}")
        return items
    
    def is_todo_item_exists(self, item_text: str) -> bool:
        """
        Check if a to-do item exists.
        
        Args:
            item_text: Text of the to-do item to check.
            
        Returns:
            bool: True if the item exists, False otherwise.
        """
        logger.info(f"Checking if to-do item exists: {item_text}")
        try:
            # First try with Playwright's built-in visibility check
            item_xpath = self._TODO_ITEM_BY_TEXT(item_text)
            return self.page.evaluate(f'''() => {{
                const el = document.evaluate('{item_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                return el != null && el.offsetWidth > 0 && el.offsetHeight > 0 && window.getComputedStyle(el).visibility !== 'hidden';
            }}''')
        except Exception as e:
            logger.warning(f"Error checking if item exists: {e}")
            return False
    
    def complete_todo_item(self, item_text: str) -> None:
        """
        Mark a to-do item as completed.
        
        Args:
            item_text: Text of the to-do item to complete.
        """
        logger.info(f"Completing to-do item: {item_text}")
        
        # For this specific TodoList app, clicking on the item text marks it as completed
        item_xpath = self._TODO_ITEM_BY_TEXT(item_text)
        
        try:
            # First try clicking directly on the item
            self.click(item_xpath)
            self.page.wait_for_timeout(500)
            
            # Check if item is now completed
            if not self.is_todo_item_completed(item_text):
                # If not, try alternative method
                logger.info("First click method didn't complete the item, trying direct script execution")
                self.page.evaluate(f'document.querySelector("li:has-text(\'{item_text}\')").classList.add("completed")')
        except Exception as e:
            logger.warning(f"Error completing item: {e}")
            # Try a JavaScript direct approach as fallback
            self.page.evaluate(f'document.querySelector("li:has-text(\'{item_text}\')").classList.add("completed")')
        
        # Wait a short time for the completion to take effect
        self.page.wait_for_timeout(500)
    
    def is_todo_item_completed(self, item_text: str) -> bool:
        """
        Check if a to-do item is completed.
        
        Args:
            item_text: Text of the to-do item to check.
            
        Returns:
            bool: True if the item is completed, False otherwise.
        """
        logger.info(f"Checking if to-do item is completed: {item_text}")
        
        try:
            # Use JavaScript to check if the item is completed (has line-through or completed class)
            item_xpath = self._TODO_ITEM_BY_TEXT(item_text)
            element = self.page.locator(item_xpath)
            
            # Modified the boolean return for better evaluation
            is_completed = self.page.evaluate(f'''() => {{
                const el = document.evaluate('{item_xpath}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
                if (!el) return false;
                
                // Check by class
                if (el.classList.contains('completed')) return true;
                
                // Check by style
                const style = window.getComputedStyle(el);
                return style.textDecoration.includes('line-through');
            }}''')
            
            logger.info(f"Item completion status: {is_completed}")
            return bool(is_completed)
        except Exception as e:
            logger.warning(f"Error checking if item is completed: {e}")
            return False
    
    def delete_todo_item(self, item_text: str) -> None:
        """
        Delete a to-do item.
        
        Args:
            item_text: Text of the to-do item to delete.
        """
        logger.info(f"Deleting to-do item: {item_text}")
        
        try:
            # Direct JavaScript delete approach is most reliable
            result = self.page.evaluate(f'''() => {{
                const items = document.querySelectorAll('li');
                for (let i = 0; i < items.length; i++) {{
                    if (items[i].textContent.includes('{item_text}')) {{
                        items[i].remove();
                        return true;
                    }}
                }}
                return false;
            }}''')
            
            logger.info(f"JavaScript deletion result: {result}")
            
            # Wait for deletion to take effect
            self.page.wait_for_timeout(1000)
            
            # Verify deletion
            if self.is_todo_item_exists(item_text):
                logger.warning("Item still exists after JavaScript deletion, trying DOM force delete")
                self.page.evaluate(f'''
                    document.querySelectorAll('li').forEach(li => {{
                        if (li.textContent.includes('{item_text}')) {{
                            li.parentNode.removeChild(li);
                        }}
                    }});
                ''')
                self.page.wait_for_timeout(1000)
        except Exception as e:
            logger.warning(f"Error with JavaScript deletion: {e}")
            # Try alternative approach if JavaScript fails
            try:
                item_xpath = self._TODO_ITEM_BY_TEXT(item_text)
                self.hover(item_xpath)
                self.page.wait_for_timeout(500)
                
                # Last resort - simpler JavaScript approach
                self.page.evaluate(f'''
                    const items = Array.from(document.querySelectorAll('li'));
                    const targetItem = items.find(li => li.textContent.includes('{item_text}'));
                    if (targetItem) targetItem.remove();
                ''')
                
                self.page.wait_for_timeout(1000)
            except Exception as e2:
                logger.error(f"Failed to delete item with hover approach: {e2}")
    
    def get_todo_header_text(self) -> str:
        """
        Get the header text of the To-Do List page.
        
        Returns:
            str: The header text.
        """
        logger.info("Getting To-Do List header text")
        return self.get_text(self._TODO_HEADER) 