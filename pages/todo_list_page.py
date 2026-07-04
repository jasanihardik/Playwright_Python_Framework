"""
Page object for the To-Do List page.
"""

from typing import List

from playwright.sync_api import Locator, Page, expect

from config.config import PAGE_URLS
from pages.base_page import BasePage
from utilities.logger import logger


class TodoListPage(BasePage):
    """Page object representing the To-Do List page."""

    # Page text / placeholder values
    _TODO_HEADER = "TO-DO LIST"
    _ADD_TODO_INPUT = "Add new todo"

    def __init__(self, page: Page):
        """
        Initialize the To-Do List page.

        Args:
            page: Playwright page object.
        """
        super().__init__(page)
        self.url = PAGE_URLS["to_do_list"]

        self.todo_header: Locator = self.page.get_by_role(
            "heading",
            name=self._TODO_HEADER,
        )
        self.add_todo_input: Locator = self.page.get_by_placeholder(
            self._ADD_TODO_INPUT,
        )
        self.todo_items: Locator = self.page.get_by_role("listitem")

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

        self.add_todo_input.fill(item_text)
        self.add_todo_input.press("Enter")

    def get_todo_items(self) -> List[str]:
        """
        Get all to-do items.

        Returns:
            List[str]: List of to-do item texts.
        """
        logger.info("Getting all to-do items")

        items = []
        for item in self.todo_items.all():
            text = item.text_content()
            if text and text.strip():
                items.append(text.strip())

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

        return self.todo_items.filter(has_text=item_text).count() > 0

    def complete_todo_item(self, item_text: str) -> None:
        """
        Mark a to-do item as completed.

        Args:
            item_text: Text of the to-do item to complete.
        """
        logger.info(f"Completing to-do item: {item_text}")

        todo_item = self.todo_items.filter(has_text=item_text).first
        todo_item.click()

    def is_todo_item_completed(self, item_text: str) -> bool:
        """
        Check if a to-do item is completed.

        Args:
            item_text: Text of the to-do item to check.

        Returns:
            bool: True if the item is completed, False otherwise.
        """
        logger.info(f"Checking if to-do item is completed: {item_text}")

        todo_item = self.todo_items.filter(has_text=item_text).first

        is_completed = todo_item.evaluate(
            """element => {
                const style = window.getComputedStyle(element);
                return element.classList.contains("completed")
                    || style.textDecoration.includes("line-through");
            }"""
        )

        logger.info(f"Item completion status: {is_completed}")
        return bool(is_completed)

    def delete_todo_item(self, item_text: str) -> None:
        """
        Delete a to-do item.

        Args:
            item_text: Text of the to-do item to delete.
        """
        logger.info(f"Deleting to-do item: {item_text}")

        todo_item = self.todo_items.filter(has_text=item_text).first
        todo_item.hover()
        delete_icon = todo_item.locator("span")
        delete_icon.click()

        expect(todo_item).to_be_hidden(timeout=3000)

    def get_todo_header_text(self) -> str:
        """
        Get the header text of the To-Do List page.

        Returns:
            str: The header text.
        """
        logger.info("Getting To-Do List header text")

        text = self.todo_header.text_content()
        return text.strip() if text else ""