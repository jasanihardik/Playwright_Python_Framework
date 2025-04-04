#!/usr/bin/env python
"""
Cleanup script for the Playwright Automation Framework.
Provides functionality to clean up old reports and screenshots.
"""
import argparse
import sys

from utilities.cleanup_utils import CleanupUtils
from utilities.logger import logger


def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Cleanup old reports and screenshots.")
    
    parser.add_argument(
        "--reports", 
        type=int, 
        help="Number of most recent reports to keep",
        default=5
    )
    
    parser.add_argument(
        "--screenshots", 
        choices=["match_reports", "last_execution"],
        help="Screenshot cleanup strategy",
        default="match_reports"
    )
    
    parser.add_argument(
        "--max-screenshots", 
        type=int, 
        help="Maximum number of screenshot folders to keep when using 'last_execution' strategy",
        default=5
    )
    
    parser.add_argument(
        "--reports-to-match", 
        type=int, 
        help="Number of reports to match screenshots with when using 'match_reports' strategy",
        default=5
    )
    
    return parser.parse_args()


def main():
    """Main function to run the cleanup process."""
    args = parse_arguments()
    
    logger.info("Starting cleanup process")
    
    # Cleanup reports
    CleanupUtils.cleanup_reports(args.reports)
    
    # Cleanup logs
    CleanupUtils.cleanup_logs(args.reports)
    
    # Cleanup screenshots
    CleanupUtils.cleanup_screenshots(
        strategy=args.screenshots,
        max_screenshots=args.max_screenshots,
        reports_to_match=args.reports_to_match
    )
    
    logger.info("Cleanup process completed")


if __name__ == "__main__":
    main() 