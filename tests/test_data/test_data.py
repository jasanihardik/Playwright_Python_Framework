"""
Test data for the Playwright Automation Framework.
Contains test data for all test cases.
"""
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ContactUsData:
    """Test data for the Contact Us page tests."""
    first_name: str
    last_name: str
    email: str
    comment: str
    success_message: str = "Thank You for your Message!"
    
    @classmethod
    def valid_submission(cls) -> 'ContactUsData':
        """Return valid contact form data."""
        return cls(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            comment="This is a test message for the contact form."
        )
    
    @classmethod
    def missing_email(cls) -> 'ContactUsData':
        """Return contact form data with missing email."""
        return cls(
            first_name="Jane",
            last_name="Smith",
            email="",
            comment="This is a test message with missing email."
        )
    
    @classmethod
    def missing_first_name(cls) -> 'ContactUsData':
        """Return contact form data with missing first name."""
        return cls(
            first_name="",
            last_name="Johnson",
            email="johnson@example.com",
            comment="This is a test message with missing first name."
        )
    
    @classmethod
    def missing_all_fields(cls) -> 'ContactUsData':
        """Return contact form data with all fields missing."""
        return cls(
            first_name="",
            last_name="",
            email="",
            comment=""
        )


@dataclass
class LoginData:
    """Test data for the Login page tests."""
    username: str
    password: str
    
    @classmethod
    def valid_login(cls) -> 'LoginData':
        """Return valid login credentials."""
        return cls(
            username="webdriver",
            password="webdriver123"
        )
    
    @classmethod
    def invalid_login(cls) -> 'LoginData':
        """Return invalid login credentials."""
        return cls(
            username="invalid_user",
            password="invalid_password"
        )
    
    @classmethod
    def empty_credentials(cls) -> 'LoginData':
        """Return empty login credentials."""
        return cls(
            username="",
            password=""
        )
    
    @classmethod
    def username_only(cls) -> 'LoginData':
        """Return login data with only username."""
        return cls(
            username="webdriver",
            password=""
        )
    
    @classmethod
    def password_only(cls) -> 'LoginData':
        """Return login data with only password."""
        return cls(
            username="",
            password="webdriver123"
        )


@dataclass
class TodoData:
    """Test data for the To-Do List page tests."""
    items: List[str]
    
    @classmethod
    def single_item(cls) -> 'TodoData':
        """Return data with a single to-do item."""
        return cls(
            items=["Buy groceries"]
        )
    
    @classmethod
    def multiple_items(cls) -> 'TodoData':
        """Return data with multiple to-do items."""
        return cls(
            items=[
                "Complete Playwright framework",
                "Write automated tests",
                "Submit project",
                "Review code"
            ]
        )


@dataclass
class DropdownData:
    """Test data for the Dropdown, Checkboxes & Radio Buttons page tests."""
    dropdown_values: Dict[str, str]
    checkbox_values: List[str]
    radio_values: Dict[str, str]
    
    @classmethod
    def test_data(cls) -> 'DropdownData':
        """Return test data for dropdown, checkboxes and radio buttons."""
        return cls(
            dropdown_values={
                "dropdown1": "Python",
                "dropdown2": "TestNG",
                "dropdown3": "JavaScript"
            },
            checkbox_values=["option-1", "option-3"],
            radio_values={
                "green": "green",
                "blue": "blue",
                "yellow": "yellow"
            }
        ) 