import os
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)


def get_logger(name):
    # Get a logger instance for the given name
    return logging.getLogger(name)


def get_base_path():
    # Get the correct base path whether running as script or frozen exe
    if getattr(sys, "frozen", False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


def is_running_in_docker():
    # Check if the application is running inside a Docker container
    return os.path.exists("/.dockerenv")
