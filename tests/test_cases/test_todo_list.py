"""
Tests for the To-Do List page.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.todo_list_page import TodoListPage
from tests.test_data.test_data import TodoData
from utilities.logger import logger


@pytest.fixture
def todo_list_page(page: Page) -> TodoListPage:
    """
    Fixture to create and navigate to the To-Do List page.
    
    Args:
        page: Playwright page fixture.
        
    Returns:
        TodoListPage: Initialized To-Do List page.
    """
    todo_page = TodoListPage(page)
    todo_page.navigate()
    return todo_page


def test_page_loads(todo_list_page: TodoListPage) -> None:
    """
    Test that the To-Do List page loads correctly.
    
    Args:
        todo_list_page: To-Do List page fixture.
    """
    logger.info("Starting test: test_page_loads")
    
    # Verify To-Do List page loads correctly
    header_text = todo_list_page.get_todo_header_text()
    assert "TO-DO LIST" in header_text.upper(), "To-Do List header text is incorrect"
    
    # Take a screenshot of the To-Do List page
    todo_list_page.take_screenshot("test_page_loads", "todo_list_page")


def test_add_single_item(todo_list_page: TodoListPage) -> None:
    """
    Test adding a single to-do item.
    
    Args:
        todo_list_page: To-Do List page fixture.
    """
    logger.info("Starting test: test_add_single_item")
    
    # Get test data
    data = TodoData.single_item()
    todo_item = data.items[0]
    
    # Add to-do item
    todo_list_page.add_todo_item(todo_item)
    
    # Verify item is added
    assert todo_list_page.is_todo_item_exists(todo_item), f"To-do item '{todo_item}' not found"
    
    # Verify the item is in the list of all items
    todo_items = todo_list_page.get_todo_items()
    assert todo_item in todo_items, f"To-do item '{todo_item}' not in the list of items"
    
    # Take a screenshot after adding the item
    todo_list_page.take_screenshot("test_add_single_item", "added_item")


def test_add_multiple_items(todo_list_page: TodoListPage) -> None:
    """
    Test adding multiple to-do items.
    
    Args:
        todo_list_page: To-Do List page fixture.
    """
    logger.info("Starting test: test_add_multiple_items")
    
    # Get test data
    data = TodoData.multiple_items()
    
    # Add all to-do items
    for item in data.items:
        todo_list_page.add_todo_item(item)
    
    # Verify all items are added
    for item in data.items:
        assert todo_list_page.is_todo_item_exists(item), f"To-do item '{item}' not found"
    
    # Verify the items are in the list of all items
    todo_items = todo_list_page.get_todo_items()
    for item in data.items:
        assert item in todo_items, f"To-do item '{item}' not in the list of items"
    
    # Take a screenshot after adding all items
    todo_list_page.take_screenshot("test_add_multiple_items", "added_items")


def test_complete_item(todo_list_page: TodoListPage) -> None:
    """
    Test completing a to-do item.
    
    Args:
        todo_list_page: To-Do List page fixture.
    """
    logger.info("Starting test: test_complete_item")
    
    # Get test data
    data = TodoData.single_item()
    todo_item = data.items[0]
    
    # Add to-do item
    todo_list_page.add_todo_item(todo_item)
    
    # Verify item is added
    assert todo_list_page.is_todo_item_exists(todo_item), f"To-do item '{todo_item}' not found"
    
    # Complete the to-do item
    todo_list_page.complete_todo_item(todo_item)
    
    # Verify the item is completed
    assert todo_list_page.is_todo_item_completed(todo_item), f"To-do item '{todo_item}' is not completed"
    
    # Take a screenshot after completing the item
    todo_list_page.take_screenshot("test_complete_item", "completed_item")


def test_delete_item(todo_list_page: TodoListPage) -> None:
    """
    Test deleting a to-do item.
    
    Args:
        todo_list_page: To-Do List page fixture.
    """
    logger.info("Starting test: test_delete_item")
    
    # Get test data
    data = TodoData.single_item()
    todo_item = data.items[0]
    
    # Add to-do item
    todo_list_page.add_todo_item(todo_item)
    
    # Verify item is added
    assert todo_list_page.is_todo_item_exists(todo_item), f"To-do item '{todo_item}' not found"
    
    # Delete the to-do item
    todo_list_page.delete_todo_item(todo_item)
    
    # Verify the item is deleted
    assert not todo_list_page.is_todo_item_exists(todo_item), f"To-do item '{todo_item}' still exists after deletion"
    
    # Take a screenshot after deleting the item
    todo_list_page.take_screenshot("test_delete_item", "after_deletion")


def test_multiple_operations(todo_list_page: TodoListPage) -> None:
    """
    Test multiple operations on to-do items.
    
    Args:
        todo_list_page: To-Do List page fixture.
    """
    logger.info("Starting test: test_multiple_operations")
    
    # Get test data
    data = TodoData.multiple_items()
    
    # Add all to-do items
    for item in data.items:
        todo_list_page.add_todo_item(item)
    
    # Verify all items are added
    for item in data.items:
        assert todo_list_page.is_todo_item_exists(item), f"To-do item '{item}' not found"
    
    # Complete the first and third items
    todo_list_page.complete_todo_item(data.items[0])
    todo_list_page.complete_todo_item(data.items[2])
    
    # Verify the items are completed
    assert todo_list_page.is_todo_item_completed(data.items[0]), f"To-do item '{data.items[0]}' is not completed"
    assert todo_list_page.is_todo_item_completed(data.items[2]), f"To-do item '{data.items[2]}' is not completed"
    
    # Delete the second item
    todo_list_page.delete_todo_item(data.items[1])
    
    # Verify the item is deleted
    assert not todo_list_page.is_todo_item_exists(data.items[1]), f"To-do item '{data.items[1]}' still exists after deletion"
    
    # Verify remaining items
    assert todo_list_page.is_todo_item_exists(data.items[0]), f"To-do item '{data.items[0]}' should still exist"
    assert todo_list_page.is_todo_item_exists(data.items[2]), f"To-do item '{data.items[2]}' should still exist"
    assert todo_list_page.is_todo_item_exists(data.items[3]), f"To-do item '{data.items[3]}' should still exist"
    
    # Take a screenshot after multiple operations
    todo_list_page.take_screenshot("test_multiple_operations", "after_operations") 