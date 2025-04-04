# Playwright Automation Framework

A robust, reusable Playwright automation framework built with Python and the Page Object Model (POM) design pattern.

## Features

* **Page Object Model**: Clean separation of test logic from page interactions
* **Cross-browser Support**: Run tests on Chromium, Firefox, and Webkit
* **Reporting**: Detailed HTML reports with screenshots for failed tests
* **Logging**: Comprehensive logging for easier debugging
* **Configurability**: Easily configurable through a central config file
* **Test Data Management**: Organized test data structures
* **Screenshots**: Automatic screenshots on test failures
* **Headless Mode**: Support for headless browser execution
* **Shell Script**: Convenient test runner script with various options
* **Cleanup Utility**: Manages reports, logs, and screenshots to maintain a clean workspace

## Prerequisites

* Python 3.8 or higher
* Playwright browsers installed (will be installed automatically with the setup)

## Project Structure

```
Playwright_Framework/
├── config/
│   └── config.py                 # Central configuration file
├── pages/
│   ├── base_page.py              # Base page class with common methods
│   ├── home_page.py              # HomePage object
│   ├── contact_us_page.py        # ContactUsPage object
│   ├── login_page.py             # LoginPage object
│   ├── todo_list_page.py         # TodoListPage object
│   ├── button_clicks_page.py     # ButtonClicksPage object
│   ├── dropdown_page.py          # DropdownPage object
│   └── popup_alerts_page.py      # PopupAlertsPage object
├── tests/
│   ├── test_cases/               # Test case files
│   │   ├── test_contact_us.py    # Contact form tests
│   │   ├── test_login.py         # Login tests
│   │   ├── test_todo_list.py     # Todo List tests
│   │   ├── test_button_clicks.py # Button Clicks tests
│   │   ├── test_dropdown.py      # Dropdown tests
│   │   └── test_popup_alerts.py  # Popup & Alerts tests
│   ├── test_data/                # Test data files
│   │   └── test_data.py          # Test data classes
│   └── conftest.py               # Pytest fixtures and configuration
├── utilities/
│   ├── browser_factory.py        # Playwright browser initialization factory
│   ├── logger.py                 # Logging utilities
│   ├── screenshot_utils.py       # Screenshot utilities
│   └── cleanup_utils.py          # Report and screenshot cleanup utilities
├── reports/                      # Test execution reports (latest 5 preserved)
├── logs/                         # Execution logs
├── screenshots/                  # Test screenshots organized by timestamp folders
├── run_tests.sh                  # Shell script for running tests
├── cleanup.py                    # Script for cleaning up old reports and screenshots
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies
```

## Installation

1. Clone the repository:  
```  
git clone https://github.com/jasanihardik/Playwright_Python.git  
cd Playwright_Framework  
```
2. Create and activate a virtual environment (recommended):  
```  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```
3. Install dependencies:  
```  
pip install -r requirements.txt  
```
4. Install Playwright browsers:  
```  
playwright install  
```

## Configuration

All configuration settings are in the `config/config.py` file. You can modify:

* Base URL
* Browser settings (type, headless mode, window size)
* Timeouts
* Directory paths

## Running Tests

### Using the Shell Script

The framework includes a convenient shell script (`run_tests.sh`) that provides various options for running tests.

```
# Make the script executable (if not already)
chmod +x run_tests.sh

# Show help
./run_tests.sh --help

# Run all tests
./run_tests.sh --all

# Run a specific test file
./run_tests.sh --test test_login.py

# Run all tests in a specific module
./run_tests.sh --module contact_us

# Run a specific test case
./run_tests.sh --module contact_us --case test_successful_submission

# Specify a browser
./run_tests.sh --all --browser firefox

# Run in headless mode
./run_tests.sh --all --headless

# Skip cleanup of old reports and screenshots
./run_tests.sh --all --no-cleanup
```

### Using pytest Commands

If you prefer to use pytest commands directly:

#### Run all tests:

```
python -m pytest
```

#### Run specific test file:

```
python -m pytest tests/test_cases/test_contact_us.py
```

#### Run with specific browser:

```
python -m pytest --browser-name=firefox
```

#### Run in headless mode:

```
python -m pytest --headless=true
```

#### Run with verbose output:

```
python -m pytest -v
```

## Reports and Screenshots Management

### HTML Reports

The HTML report is automatically generated in the `reports` directory after each test run. By default, only the last 5 reports are kept to save disk space.

### Screenshots Management

The framework handles screenshots in two ways:

1. **Test Failure Screenshots**: Automatically captured when a test fails
2. **Diagnostic Screenshots**: Manually captured during test execution for debugging

All screenshots are organized into timestamp-based folders that correspond to test reports (e.g., `screenshots/2025-03-25_21-43-39/`). This keeps screenshots neatly organized and makes it easy to correlate them with test reports.

### Cleanup Utility

The framework includes a cleanup utility that manages reports, logs, and screenshots. By default, it keeps only the 5 most recent items of each type:

```
# Run cleanup manually
./cleanup.py

# Specify number of items to keep (applies to reports and logs)
./cleanup.py --reports 10

# Choose screenshot handling strategy
./cleanup.py --screenshots last_execution  # Keep only latest screenshots
./cleanup.py --screenshots match_reports   # Organize screenshots to match reports (default)

# Specify number of screenshots to keep (for last_execution option)
./cleanup.py --max-screenshots 20

# Specify number of reports to match screenshots with (for match_reports option)
./cleanup.py --reports-to-match 3
```

## Implemented Test Scenarios

1. **Contact Us Form**  
   * Successful form submission  
   * Reset form functionality  
   * Form validation (missing email, missing name)
2. **Login Portal**  
   * Successful login  
   * Failed login  
   * Empty credentials  
   * Username only  
   * Password only
3. **To-Do List**  
   * Adding new items  
   * Marking items as complete  
   * Deleting items  
   * Multiple operations
4. **Button Clicks**  
   * Simple button click  
   * Hover button  
   * Action click button  
   * Multiple modal interactions
5. **Dropdown, Checkboxes & Radio Buttons**  
   * Selecting dropdown values  
   * Checkbox functionality  
   * Radio button selection  
   * Disabled elements
6. **Popup & Alerts**  
   * JavaScript alerts  
   * Modal popups  
   * JavaScript confirm boxes (accept/dismiss)

## Target Website

This framework is designed to work with WebDriverUniversity.com, a website specifically created for learning automation. It contains various UI elements and functionality perfect for practice without bot detection issues.

## License

This project is licensed under the MIT License. 