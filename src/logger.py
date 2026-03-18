"""Configure and return the application logger.
The logger writes provisioning events and errors to a log file
located in the logs directory.
"""

import logging
import os


def setup_logger():
    """Create and configure the application logger."""
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/provisioning.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger("infra-automation")


logger = setup_logger()
