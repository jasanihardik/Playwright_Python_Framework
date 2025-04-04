"""
Tests for the Login page.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from tests.test_data.test_data import LoginData
from utilities.logger import logger


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """
    Fixture to create and navigate to the Login page.
    
    Args:
        page: Playwright page fixture.
        
    Returns:
        LoginPage: Initialized Login page.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    return login_page


def test_page_loads(login_page: LoginPage) -> None:
    """
    Test that the login page loads correctly.
    
    Args:
        login_page: Login page fixture.
    """
    logger.info("Starting test: test_page_loads")
    
    # Verify login page loads correctly
    assert login_page.verify_login_page_loaded(), "Login page did not load correctly"
    
    # Verify login portal page title
    page_title = login_page.get_login_portal_title()
    assert "login portal" in page_title.lower(), f"Login portal title is incorrect: '{page_title}'"
    
    # Take a screenshot of the login page
    login_page.take_screenshot("test_page_loads", "login_page")


def test_successful_login(login_page: LoginPage, page: Page) -> None:
    """
    Test successful login.
    
    Args:
        login_page: Login page fixture.
        page: Playwright page fixture.
    """
    logger.info("Starting test: test_successful_login")
    
    # Get test data
    data = LoginData.valid_login()
    
    # Listen for the dialog (alert) to capture its message
    dialog_message = None
    
    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()
    
    page.once("dialog", handle_dialog)
    
    # Perform login
    login_page.login(
        username=data.username,
        password=data.password
    )
    
    # Wait a bit for the dialog to appear
    page.wait_for_timeout(1000)
    
    # Verify success message
    assert dialog_message is not None, "No dialog was shown"
    assert "validation succeeded" in dialog_message.lower() or "successful" in dialog_message.lower(), f"Login success message is incorrect: '{dialog_message}'"


def test_failed_login(login_page: LoginPage, page: Page) -> None:
    """
    Test failed login.
    
    Args:
        login_page: Login page fixture.
        page: Playwright page fixture.
    """
    logger.info("Starting test: test_failed_login")
    
    # Get test data
    data = LoginData.invalid_login()
    
    # Listen for the dialog (alert) to capture its message
    dialog_message = None
    
    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()
    
    page.once("dialog", handle_dialog)
    
    # Perform login with invalid credentials
    login_page.login(
        username=data.username,
        password=data.password
    )
    
    # Wait a bit for the dialog to appear
    page.wait_for_timeout(1000)
    
    # Verify error message
    assert dialog_message is not None, "No dialog was shown"
    assert "validation failed" in dialog_message.lower() or "incorrect" in dialog_message.lower(), f"Login failure message is incorrect: '{dialog_message}'"


def test_empty_credentials(login_page: LoginPage, page: Page) -> None:
    """
    Test login with empty credentials.
    
    Args:
        login_page: Login page fixture.
        page: Playwright page fixture.
    """
    logger.info("Starting test: test_empty_credentials")
    
    # Get test data
    data = LoginData.empty_credentials()
    
    # Listen for the dialog (alert) to capture its message
    dialog_message = None
    
    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()
    
    page.once("dialog", handle_dialog)
    
    # Perform login with empty credentials
    login_page.login(
        username=data.username,
        password=data.password
    )
    
    # Wait a bit for the dialog to appear
    page.wait_for_timeout(1000)
    
    # Verify error message
    assert dialog_message is not None, "No dialog was shown"
    assert "validation failed" in dialog_message.lower() or "incorrect" in dialog_message.lower(), f"Empty credentials message is incorrect: '{dialog_message}'"


def test_username_only(login_page: LoginPage, page: Page) -> None:
    """
    Test login with only username provided.
    
    Args:
        login_page: Login page fixture.
        page: Playwright page fixture.
    """
    logger.info("Starting test: test_username_only")
    
    # Get test data
    data = LoginData.username_only()
    
    # Listen for the dialog (alert) to capture its message
    dialog_message = None
    
    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()
    
    page.once("dialog", handle_dialog)
    
    # Perform login with only username
    login_page.login(
        username=data.username,
        password=data.password
    )
    
    # Wait a bit for the dialog to appear
    page.wait_for_timeout(1000)
    
    # Verify error message
    assert dialog_message is not None, "No dialog was shown"
    assert "validation failed" in dialog_message.lower() or "incorrect" in dialog_message.lower(), f"Username only message is incorrect: '{dialog_message}'"


def test_password_only(login_page: LoginPage, page: Page) -> None:
    """
    Test login with only password provided.
    
    Args:
        login_page: Login page fixture.
        page: Playwright page fixture.
    """
    logger.info("Starting test: test_password_only")
    
    # Get test data
    data = LoginData.password_only()
    
    # Listen for the dialog (alert) to capture its message
    dialog_message = None
    
    def handle_dialog(dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()
    
    page.once("dialog", handle_dialog)
    
    # Perform login with only password
    login_page.login(
        username=data.username,
        password=data.password
    )
    
    # Wait a bit for the dialog to appear
    page.wait_for_timeout(1000)
    
    # Verify error message
    assert dialog_message is not None, "No dialog was shown"
    assert "validation failed" in dialog_message.lower() or "incorrect" in dialog_message.lower(), f"Password only message is incorrect: '{dialog_message}'" 