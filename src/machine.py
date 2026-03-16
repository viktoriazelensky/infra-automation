import os
import subprocess

from src.logger import logger


class Machine:
    """
    Represents a virtual machine configuration in the infrastructure tool.

    Stores machine parameters and provides utility methods for logging
    and provisioning simulation.
    """

    def __init__(self, name, os_name, cpu, ram):
        """
        Initialize Machine object with configuration parameters.
        """
        self.name = name
        self.os = os_name
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        """
        Convert the Machine object to dictionary format.
        This allows the configuration to be saved into a JSON file.
        """
        return {
            "name": self.name,
            "os": self.os,
            "cpu": self.cpu,
            "ram": self.ram
        }

    def log_creation(self):
        """
        Log or display a message indicating that the machine
        provisioning process has started.
        """
        message = f"Provisioning {self.name}: {self.os}, {self.cpu} CPU, {self.ram}MB RAM"

        print()
        print(message)

        logger.info(message)

    def provision(self):
        """
        Execute the provisioning script or simulate provisioning on Windows.
        """
        print("Starting provisioning script...")

        try:
            if os.name == "posix":
                subprocess.run(["bash", "scripts/setup_nginx.sh"], check=True)
                logger.info("Provisioning script executed successfully")
            else:
                print("Provisioning simulated (Windows environment)")
                logger.info("Provisioning simulated on Windows")

        except subprocess.CalledProcessError as e:
            print(f"Provisioning failed: {e}")
            logger.error(f"Provisioning failed: {e}")