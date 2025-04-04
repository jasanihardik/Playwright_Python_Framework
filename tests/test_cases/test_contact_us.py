"""
Tests for the Contact Us page.
"""
import pytest
from playwright.sync_api import Page, expect

from pages.contact_us_page import ContactUsPage
from tests.test_data.test_data import ContactUsData
from utilities.logger import logger


@pytest.fixture
def contact_us_page(page: Page) -> ContactUsPage:
    """
    Fixture to create and navigate to the Contact Us page.
    
    Args:
        page: Playwright page fixture.
        
    Returns:
        ContactUsPage: Initialized Contact Us page.
    """
    contact_page = ContactUsPage(page)
    contact_page.navigate()
    return contact_page


def test_successful_submission(contact_us_page: ContactUsPage) -> None:
    """
    Test successful contact form submission.
    
    Args:
        contact_us_page: Contact Us page fixture.
    """
    logger.info("Starting test: test_successful_submission")
    
    # Get test data
    data = ContactUsData.valid_submission()
    
    # Fill and submit form
    contact_us_page.fill_contact_form(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        comment=data.comment
    )
    contact_us_page.submit_form()
    
    # Verify success message
    assert contact_us_page.is_success_message_displayed(), "Success message is not displayed"
    assert data.success_message in contact_us_page.get_success_message(), "Success message text is incorrect"
    
    # Take a screenshot of the success message
    contact_us_page.take_screenshot("test_successful_submission", "success_message")


def test_reset_form(contact_us_page: ContactUsPage) -> None:
    """
    Test form reset functionality.
    
    Args:
        contact_us_page: Contact Us page fixture.
    """
    logger.info("Starting test: test_reset_form")
    
    # Get test data
    data = ContactUsData.valid_submission()
    
    # Fill form
    contact_us_page.fill_contact_form(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        comment=data.comment
    )
    
    # Reset form
    contact_us_page.reset_form()
    
    # Verify all fields are empty
    assert contact_us_page.is_field_empty(contact_us_page._FIRST_NAME_FIELD), "First name field is not empty"
    assert contact_us_page.is_field_empty(contact_us_page._LAST_NAME_FIELD), "Last name field is not empty"
    assert contact_us_page.is_field_empty(contact_us_page._EMAIL_FIELD), "Email field is not empty"
    assert contact_us_page.is_field_empty(contact_us_page._COMMENT_FIELD), "Comment field is not empty"


def test_missing_email(contact_us_page: ContactUsPage) -> None:
    """
    Test form submission with missing email.
    
    Args:
        contact_us_page: Contact Us page fixture.
    """
    logger.info("Starting test: test_missing_email")
    
    # Get test data
    data = ContactUsData.missing_email()
    
    # Fill and submit form
    contact_us_page.fill_contact_form(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        comment=data.comment
    )
    contact_us_page.submit_form()
    
    # Verify error message (page should contain error text)
    error_text = contact_us_page.get_error_message()
    assert "Error: Invalid email address" in error_text, "Error message for invalid email is not displayed"
    
    # Take a screenshot of the error message
    contact_us_page.take_screenshot("test_missing_email", "error_message")


def test_missing_first_name(contact_us_page: ContactUsPage) -> None:
    """
    Test form submission with missing first name.
    
    Args:
        contact_us_page: Contact Us page fixture.
    """
    logger.info("Starting test: test_missing_first_name")
    
    # Get test data
    data = ContactUsData.missing_first_name()
    
    # Fill and submit form
    contact_us_page.fill_contact_form(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        comment=data.comment
    )
    contact_us_page.submit_form()
    
    # Verify error message (page should contain error text)
    error_text = contact_us_page.get_error_message()
    assert "error: all fields are required" in error_text.lower().strip(), "Error message for missing fields is not displayed"
    
    # Take a screenshot of the error message
    contact_us_page.take_screenshot("test_missing_first_name", "error_message")


def test_missing_all_fields(contact_us_page: ContactUsPage) -> None:
    """
    Test form submission with all fields missing.
    
    Args:
        contact_us_page: Contact Us page fixture.
    """
    logger.info("Starting test: test_missing_all_fields")
    
    # Get test data
    data = ContactUsData.missing_all_fields()
    
    # Fill and submit form (all empty)
    contact_us_page.fill_contact_form(
        first_name=data.first_name,
        last_name=data.last_name,
        email=data.email,
        comment=data.comment
    )
    contact_us_page.submit_form()
    
    # Verify error message (page should contain error text)
    error_text = contact_us_page.get_error_message()
    assert "error: all fields are required" in error_text.lower().strip(), "Error message for missing fields is not displayed"
    
    # Take a screenshot of the error message
    contact_us_page.take_screenshot("test_missing_all_fields", "error_message") 