# Playwright Python Automation Framework

A robust and reusable UI automation framework built with **Python**, **Playwright**, **Pytest**, and the **Page Object Model (POM)** design pattern.

This framework is designed for practicing and maintaining scalable UI automation using clean page objects, reusable utilities, centralized configuration, structured test data, reports, logs, screenshots, and shell-based test execution.

---

## Features

* **Page Object Model (POM)**: Clean separation between test logic and page interactions
* **Python 3.13 Support**: Updated setup for modern Python versions
* **Playwright + Pytest**: UI automation using Playwright with Pytest-based execution
* **Browser Support**: Chromium and Firefox supported locally
* **WebKit Note**: WebKit requires a supported operating system. On macOS 13, use Chromium and Firefox locally
* **Reporting**: HTML reports generated after test execution
* **Screenshots**: Automatic screenshots on test failures
* **Logging**: Centralized logging for easier debugging
* **Configuration Management**: Browser, URL, timeout, and path settings managed through a central config file
* **Test Data Management**: Organized test data structure
* **Headless Mode**: Supports headless browser execution
* **Shell Script Runner**: Convenient `run_tests.sh` script for common test execution options
* **Cleanup Utility**: Manages reports, logs, and screenshots to keep the workspace clean

---

## Prerequisites

Before running this framework, make sure the following are installed:

* Python 3.13
* pip
* Git
* Bash-compatible terminal
* macOS, Linux, or Windows

Recommended local setup:

```bash
python3.13 --version
pip --version
git --version
```

---

## Project Structure

```text
Playwright_Python_Framework/
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
│   │   └── test_popup_alerts.py  # Popup and alerts tests
│   ├── test_data/                # Test data files
│   │   └── test_data.py          # Test data classes
│   └── conftest.py               # Pytest fixtures and configuration
├── utilities/
│   ├── browser_factory.py        # Playwright browser initialization factory
│   ├── logger.py                 # Logging utilities
│   ├── screenshot_utils.py       # Screenshot utilities
│   └── cleanup_utils.py          # Report and screenshot cleanup utilities
├── reports/                      # Test execution reports
├── logs/                         # Execution logs
├── screenshots/                  # Test screenshots organized by timestamp folders
├── run_tests.sh                  # Shell script for running tests
├── cleanup.py                    # Script for cleaning old reports, logs, and screenshots
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies
```

---

## Recommended `requirements.txt`

For Python 3.13, use updated package versions instead of the older 2023 dependency pins.

```txt
playwright==1.61.0
pytest==9.1.1
pytest-playwright==0.8.0
pytest-html==4.2.0
pytest-xdist==3.8.0
python-dotenv==1.2.2
allure-pytest==2.16.0
PyYAML==6.0.3
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jasanihardik/Playwright_Python_Framework.git
cd Playwright_Python_Framework
```

### 2. Create and activate a virtual environment

```bash
python3.13 -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Upgrade pip, setuptools, and wheel

```bash
python -m pip install --upgrade pip setuptools wheel
```

### 4. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install Playwright browsers

For local execution on macOS 13, install Chromium and Firefox:

```bash
python -m playwright install chromium firefox
```

To install all supported browsers on a supported operating system:

```bash
python -m playwright install
```

### 6. Verify installation

```bash
python --version
python -m playwright --version
pytest --version
```

---

## Browser Support Notes

This framework supports browser-based execution using Playwright.

Recommended local browsers:

```bash
python -m playwright install chromium firefox
```

Run tests on Chromium:

```bash
python -m pytest --browser chromium
```

Run tests on Firefox:

```bash
python -m pytest --browser firefox
```

Run tests on both Chromium and Firefox:

```bash
python -m pytest --browser chromium --browser firefox
```

### WebKit Note

WebKit may not work on older macOS versions with the latest Playwright releases. If WebKit installation fails with an error similar to:

```text
Playwright does not support webkit on mac13
```

continue with Chromium and Firefox locally:

```bash
python -m playwright install chromium firefox
```

WebKit testing can be added later using a supported OS or CI environment.

---

## Configuration

All framework-level settings are managed from:

```text
config/config.py
```

You can modify:

* Base URL
* Browser type
* Headless mode
* Window size
* Timeout values
* Report paths
* Screenshot paths
* Log paths

---

## Running Tests

### Using the Shell Script

The framework includes a shell script named `run_tests.sh` for easier test execution.

Make the script executable:

```bash
chmod +x run_tests.sh
```

Show help:

```bash
./run_tests.sh --help
```

Run all tests:

```bash
./run_tests.sh --all
```

Run a specific test file:

```bash
./run_tests.sh --test test_login.py
```

Run all tests in a specific module:

```bash
./run_tests.sh --module contact_us
```

Run a specific test case:

```bash
./run_tests.sh --module contact_us --case test_successful_submission
```

Run tests using Firefox:

```bash
./run_tests.sh --all --browser firefox
```

Run tests in headless mode:

```bash
./run_tests.sh --all --headless
```

Skip cleanup of old reports and screenshots:

```bash
./run_tests.sh --all --no-cleanup
```

---

## Running Tests with Pytest

Run all tests:

```bash
python -m pytest
```

Run a specific test file:

```bash
python -m pytest tests/test_cases/test_contact_us.py
```

Run with Chromium:

```bash
python -m pytest --browser chromium
```

Run with Firefox:

```bash
python -m pytest --browser firefox
```

Run with multiple browsers:

```bash
python -m pytest --browser chromium --browser firefox
```

Run in headed mode:

```bash
python -m pytest --headed
```

Run with verbose output:

```bash
python -m pytest -v
```

Run tests in parallel:

```bash
python -m pytest -n auto
```

---

## Reports and Screenshots Management

### HTML Reports

The HTML report is automatically generated in the `reports` directory after test execution.

By default, the framework keeps the latest reports to avoid unnecessary disk usage.

### Screenshots

The framework handles screenshots in two ways:

1. **Failure Screenshots**: Captured automatically when a test fails
2. **Diagnostic Screenshots**: Captured manually during test execution for debugging

Screenshots are organized into timestamp-based folders, for example:

```text
screenshots/2025-03-25_21-43-39/
```

This makes it easier to match screenshots with the corresponding test execution report.

---

## Cleanup Utility

The framework includes a cleanup utility for managing reports, logs, and screenshots.

Run cleanup manually:

```bash
python cleanup.py
```

Specify the number of reports/logs to keep:

```bash
python cleanup.py --reports 10
```

Keep only the latest screenshots:

```bash
python cleanup.py --screenshots last_execution
```

Organize screenshots to match reports:

```bash
python cleanup.py --screenshots match_reports
```

Specify the maximum number of screenshots to keep:

```bash
python cleanup.py --max-screenshots 20
```

Specify the number of reports to match screenshots with:

```bash
python cleanup.py --reports-to-match 3
```

---

## Implemented Test Scenarios

### 1. Contact Us Form

* Successful form submission
* Reset form functionality
* Form validation for missing email
* Form validation for missing name

### 2. Login Portal

* Successful login
* Failed login
* Empty credentials
* Username only
* Password only

### 3. To-Do List

* Adding new items
* Marking items as complete
* Deleting items
* Multiple operations

### 4. Button Clicks

* Simple button click
* Hover button
* Action click button
* Multiple modal interactions

### 5. Dropdown, Checkboxes, and Radio Buttons

* Selecting dropdown values
* Checkbox functionality
* Radio button selection
* Disabled elements

### 6. Popup and Alerts

* JavaScript alerts
* Modal popups
* JavaScript confirm boxes
* Accept and dismiss alert flows

---

## Target Website

This framework is designed to work with WebDriverUniversity.com, a website created for practicing UI automation.

It includes multiple automation-friendly components such as forms, login pages, buttons, dropdowns, checkboxes, radio buttons, popups, alerts, and to-do list workflows.

---

## Troubleshooting

### PyYAML installation fails on Python 3.13

If you see an error like:

```text
AttributeError: 'build_ext' object has no attribute 'cython_sources'
```

make sure `requirements.txt` uses a newer PyYAML version:

```txt
PyYAML==6.0.3
```

Then recreate the virtual environment:

```bash
rm -rf venv
python3.13 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

### WebKit fails on macOS 13

If Playwright shows:

```text
Playwright does not support webkit on mac13
```

install Chromium and Firefox only:

```bash
python -m playwright install chromium firefox
```

Then run tests with:

```bash
python -m pytest --browser chromium
```

or:

```bash
python -m pytest --browser firefox
```

---

## Recommended Local Setup Summary

For Python 3.13 and macOS 13:

```bash
git clone https://github.com/jasanihardik/Playwright_Python_Framework.git
cd Playwright_Python_Framework

python3.13 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

python -m playwright install chromium firefox

python -m pytest --browser chromium
```

---

## License

This project is licensed under the MIT License.
