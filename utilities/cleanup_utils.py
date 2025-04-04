"""
Cleanup utility module for the Playwright Automation Framework.
Provides functionality to clean up old reports and screenshots.
"""
import glob
import os
import shutil
from typing import List, Optional
from datetime import datetime

from config.config import DIRECTORY_PATHS, REPORTING_SETTINGS, SCREENSHOT_SETTINGS
from utilities.logger import logger


class CleanupUtils:
    """Cleanup utility class for the Playwright Automation Framework."""

    @staticmethod
    def cleanup_reports(max_reports: Optional[int] = None) -> None:
        """
        Clean up old reports, keeping only the specified number of most recent reports.
        
        Args:
            max_reports: Maximum number of reports to keep. Defaults to config value.
        """
        max_reports_to_keep = max_reports or REPORTING_SETTINGS["max_reports_to_keep"]
        reports_dir = DIRECTORY_PATHS["reports"]
        
        if not os.path.exists(reports_dir):
            logger.info(f"Reports directory does not exist: {reports_dir}")
            return
        
        logger.info(f"Cleaning up reports, keeping {max_reports_to_keep} most recent")
        
        # Get all HTML report files
        report_files = glob.glob(os.path.join(reports_dir, "*.html"))
        
        # Sort by modification time (newest first)
        report_files.sort(key=os.path.getmtime, reverse=True)
        
        # Delete older reports
        if len(report_files) > max_reports_to_keep:
            for old_report in report_files[max_reports_to_keep:]:
                try:
                    os.remove(old_report)
                    logger.info(f"Deleted old report: {old_report}")
                except Exception as e:
                    logger.error(f"Failed to delete report {old_report}: {str(e)}")

    @staticmethod
    def cleanup_logs(max_logs: Optional[int] = None) -> None:
        """
        Clean up old log files, keeping only the specified number of most recent logs.
        
        Args:
            max_logs: Maximum number of logs to keep. Defaults to the same as max_reports_to_keep.
        """
        max_logs_to_keep = max_logs or REPORTING_SETTINGS["max_reports_to_keep"]  # Use the same default as reports
        logs_dir = DIRECTORY_PATHS["logs"]
        
        if not os.path.exists(logs_dir):
            logger.info(f"Logs directory does not exist: {logs_dir}")
            return
        
        logger.info(f"Cleaning up logs, keeping {max_logs_to_keep} most recent")
        
        # Get all log files (specifically test execution logs)
        log_files = glob.glob(os.path.join(logs_dir, "test_execution_*.log"))
        
        # Sort by modification time (newest first)
        log_files.sort(key=os.path.getmtime, reverse=True)
        
        # Delete older logs
        if len(log_files) > max_logs_to_keep:
            for old_log in log_files[max_logs_to_keep:]:
                try:
                    os.remove(old_log)
                    logger.info(f"Deleted old log: {old_log}")
                except Exception as e:
                    logger.error(f"Failed to delete log {old_log}: {str(e)}")

    @staticmethod
    def cleanup_screenshots(strategy: str = "match_reports", max_screenshots: Optional[int] = None, 
                           reports_to_match: Optional[int] = None) -> None:
        """
        Clean up old screenshots based on the specified strategy.
        
        Args:
            strategy: The strategy to use for cleanup. Options:
                     - "match_reports": Keep screenshots that match report timestamps
                     - "last_execution": Keep only the most recent screenshots
            max_screenshots: Maximum number of screenshot folders to keep when using 'last_execution'.
            reports_to_match: Number of reports to match screenshots with when using 'match_reports'.
        """
        screenshots_dir = DIRECTORY_PATHS["screenshots"]
        
        if not os.path.exists(screenshots_dir):
            logger.info(f"Screenshots directory does not exist: {screenshots_dir}")
            return
        
        if strategy == "match_reports":
            CleanupUtils._cleanup_screenshots_match_reports(reports_to_match)
        elif strategy == "last_execution":
            CleanupUtils._cleanup_screenshots_last_execution(max_screenshots)
        else:
            logger.error(f"Unknown screenshot cleanup strategy: {strategy}")

    @staticmethod
    def _cleanup_screenshots_match_reports(reports_to_match: Optional[int] = None) -> None:
        """
        Clean up screenshots, keeping only those that match the timestamps of recent reports.
        
        Args:
            reports_to_match: Number of recent reports to match against. Defaults to config value.
        """
        num_reports = reports_to_match or REPORTING_SETTINGS["max_reports_to_keep"]
        reports_dir = DIRECTORY_PATHS["reports"]
        screenshots_dir = DIRECTORY_PATHS["screenshots"]
        
        logger.info(f"Cleaning up screenshots to match {num_reports} recent reports")
        
        # Get report timestamps from filenames
        report_files = glob.glob(os.path.join(reports_dir, "*.html"))
        report_files.sort(key=os.path.getmtime, reverse=True)
        report_timestamps = []
        
        for report in report_files[:num_reports]:
            # Try to extract timestamp from filename
            try:
                filename = os.path.basename(report)
                timestamp = filename.split("_", 1)[1].rsplit(".", 1)[0]
                report_timestamps.append(timestamp)
            except (IndexError, ValueError):
                # If timestamp can't be extracted, use file modification time
                mod_time = datetime.fromtimestamp(os.path.getmtime(report))
                timestamp = mod_time.strftime("%Y-%m-%d_%H-%M-%S")
                report_timestamps.append(timestamp)
        
        # Get all screenshot folders
        screenshot_folders = [d for d in os.listdir(screenshots_dir) 
                              if os.path.isdir(os.path.join(screenshots_dir, d))]
        
        # Delete folders that don't match any report timestamp
        for folder in screenshot_folders:
            match_found = False
            for timestamp in report_timestamps:
                if timestamp in folder:
                    match_found = True
                    break
            
            if not match_found:
                folder_path = os.path.join(screenshots_dir, folder)
                try:
                    shutil.rmtree(folder_path)
                    logger.info(f"Deleted screenshot folder: {folder_path}")
                except Exception as e:
                    logger.error(f"Failed to delete screenshot folder {folder_path}: {str(e)}")

    @staticmethod
    def _cleanup_screenshots_last_execution(max_screenshots: Optional[int] = None) -> None:
        """
        Clean up screenshots, keeping only the most recent ones.
        
        Args:
            max_screenshots: Maximum number of screenshot folders to keep. Defaults to config value.
        """
        max_to_keep = max_screenshots or SCREENSHOT_SETTINGS["max_screenshots_to_keep"]
        screenshots_dir = DIRECTORY_PATHS["screenshots"]
        
        logger.info(f"Cleaning up screenshots, keeping {max_to_keep} most recent folders")
        
        # Get all screenshot folders
        screenshot_folders = [os.path.join(screenshots_dir, d) for d in os.listdir(screenshots_dir) 
                             if os.path.isdir(os.path.join(screenshots_dir, d))]
        
        # Sort by creation time (newest first)
        screenshot_folders.sort(key=os.path.getctime, reverse=True)
        
        # Delete older folders
        if len(screenshot_folders) > max_to_keep:
            for old_folder in screenshot_folders[max_to_keep:]:
                try:
                    shutil.rmtree(old_folder)
                    logger.info(f"Deleted old screenshot folder: {old_folder}")
                except Exception as e:
                    logger.error(f"Failed to delete screenshot folder {old_folder}: {str(e)}") 