class Machine:
    """
    Represents a virtual machine configuration in the infrastructure simulator.

    This class stores machine parameters such as name, operating system,
    CPU and RAM, and provides utility methods for serialization and logging.
    """

    def __init__(self, name, os, cpu, ram):
        """
        Initialize a Machine object with its configuration parameters.
        """
        self.name = name
        self.os = os
        self.cpu = cpu
        self.ram = ram

    def to_dict(self):
        """
        Convert the Machine object into a dictionary format
        so it can be stored in JSON configuration files.
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
        print(f"Provisioning {self.name}: {self.os}, {self.cpu} CPU, {self.ram}MB RAM")