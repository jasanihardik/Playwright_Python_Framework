#!/bin/bash

# Shell script for running Playwright tests with various options

# Default values
ALL=false
TEST_FILE=""
MODULE=""
TEST_CASE=""
BROWSER="chromium"
HEADLESS=false
NO_CLEANUP=false

# Function to display script usage
display_help() {
  echo "Usage: ./run_tests.sh [OPTIONS]"
  echo ""
  echo "Options:"
  echo "  --all                  Run all tests"
  echo "  --test FILENAME        Run a specific test file (e.g., test_login.py)"
  echo "  --module NAME          Run all tests in a specific module (e.g., contact_us)"
  echo "  --case NAME            Run a specific test case (requires --module)"
  echo "  --browser NAME         Specify browser: chromium, firefox, webkit (default: chromium)"
  echo "  --headless             Run tests in headless mode"
  echo "  --no-cleanup           Skip cleanup of old reports and screenshots"
  echo "  --help                 Display this help and exit"
  echo ""
  echo "Examples:"
  echo "  ./run_tests.sh --all"
  echo "  ./run_tests.sh --test test_login.py"
  echo "  ./run_tests.sh --module contact_us"
  echo "  ./run_tests.sh --module contact_us --case test_successful_submission"
  echo "  ./run_tests.sh --all --browser firefox"
  echo "  ./run_tests.sh --all --headless"
  echo "  ./run_tests.sh --all --no-cleanup"
}

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    --all)
      ALL=true
      shift
      ;;
    --test)
      TEST_FILE="$2"
      shift 2
      ;;
    --module)
      MODULE="$2"
      shift 2
      ;;
    --case)
      TEST_CASE="$2"
      shift 2
      ;;
    --browser)
      BROWSER="$2"
      shift 2
      ;;
    --headless)
      HEADLESS=true
      shift
      ;;
    --no-cleanup)
      NO_CLEANUP=true
      shift
      ;;
    --help)
      display_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      display_help
      exit 1
      ;;
  esac
done

# Check if we have at least one run option
if [ "$ALL" = false ] && [ -z "$TEST_FILE" ] && [ -z "$MODULE" ]; then
  echo "Error: No test selection option provided."
  echo "Please use --all, --test, or --module."
  echo ""
  display_help
  exit 1
fi

# Build the pytest command
PYTEST_CMD="python3 -m pytest"

# Add test selection options
if [ "$ALL" = true ]; then
  PYTEST_CMD="$PYTEST_CMD tests/test_cases/"
elif [ -n "$TEST_FILE" ]; then
  PYTEST_CMD="$PYTEST_CMD tests/test_cases/$TEST_FILE"
elif [ -n "$MODULE" ]; then
  if [ -n "$TEST_CASE" ]; then
    PYTEST_CMD="$PYTEST_CMD tests/test_cases/test_${MODULE}.py::${TEST_CASE}"
  else
    PYTEST_CMD="$PYTEST_CMD tests/test_cases/test_${MODULE}.py"
  fi
fi

# Add browser option
PYTEST_CMD="$PYTEST_CMD --browser-name=$BROWSER"

# Add headless option if needed
if [ "$HEADLESS" = true ]; then
  PYTEST_CMD="$PYTEST_CMD --headless=true"
fi

# Add HTML report option
TIMESTAMP=$(date '+%Y-%m-%d_%H-%M-%S')
REPORT_PATH="reports/playwright_report_${TIMESTAMP}.html"
PYTEST_CMD="$PYTEST_CMD --html=$REPORT_PATH"

# Create reports directory if it doesn't exist
mkdir -p reports

# Display test run summary
echo "============================================"
echo "Playwright Test Run"
echo "============================================"
echo "Date: $(date)"
echo "Browser: $BROWSER (Headless: $HEADLESS)"
if [ "$ALL" = true ]; then
  echo "Running: All tests"
elif [ -n "$TEST_FILE" ]; then
  echo "Running: $TEST_FILE"
elif [ -n "$MODULE" ]; then
  if [ -n "$TEST_CASE" ]; then
    echo "Running: $MODULE - $TEST_CASE"
  else
    echo "Running: All tests in $MODULE"
  fi
fi
echo "Report will be saved to: $REPORT_PATH"
echo "============================================"

# Run the tests
echo "Running tests..."
eval "$PYTEST_CMD"
TEST_EXIT_CODE=$?

# Print test run result
echo "============================================"
if [ $TEST_EXIT_CODE -eq 0 ]; then
  echo "Test run completed successfully!"
else
  echo "Test run completed with failures!"
fi
echo "Report saved to: $REPORT_PATH"
echo "============================================"

# Run cleanup script unless --no-cleanup was specified
if [ "$NO_CLEANUP" = false ]; then
  echo "Running cleanup..."
  python3 cleanup.py
fi

exit $TEST_EXIT_CODE 