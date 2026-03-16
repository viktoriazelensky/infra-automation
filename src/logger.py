import logging
import os


"""
Configure and return the application logger.

The logger writes provisioning events and errors to a log file
located in the logs directory.
"""


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/provisioning.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger("infra-automation")


logger = setup_logger()