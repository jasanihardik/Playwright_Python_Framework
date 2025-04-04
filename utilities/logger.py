"""
Logger utility module for the Playwright Automation Framework.
Provides logging functionality for the framework.
"""
import logging
import os
from datetime import datetime

from config.config import LOGGING_SETTINGS, DIRECTORY_PATHS


class Logger:
    """Logger class for the Playwright Automation Framework."""

    _instance = None

    def __new__(cls):
        """Create a singleton instance of the Logger class."""
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._setup_logger()
        return cls._instance

    def _setup_logger(self):
        """Set up the logger with the specified configuration."""
        # Create logs directory if it doesn't exist
        os.makedirs(DIRECTORY_PATHS["logs"], exist_ok=True)

        # Create log file name with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = os.path.join(DIRECTORY_PATHS["logs"], f"test_execution_{timestamp}.log")

        # Configure logger
        logging.basicConfig(
            level=getattr(logging, LOGGING_SETTINGS["log_level"]),
            format=LOGGING_SETTINGS["log_format"],
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger("PlaywrightFramework")
        self.logger.info("Logger initialized successfully.")

    def get_logger(self):
        """Return the logger instance."""
        return self.logger


# Create a singleton instance of the logger
logger = Logger().get_logger() 