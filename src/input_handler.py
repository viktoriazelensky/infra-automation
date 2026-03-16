import json
import os

from pydantic import ValidationError
from src.models import MachineConfig
from src.machine import Machine


def get_user_input():
    """
    Collect machine configuration parameters from the user.

    The function asks the user to enter machine name, operating system,
    CPU cores and RAM. The input is validated using the MachineConfig
    model. Valid machines are converted into Machine objects and stored
    in a list.

    The input process continues until the user types 'done'.
    """

    machines = []

    print("\n=== Machine Configuration Input ===")
    print("Type 'done' as machine name when you finish adding machines.\n")

    while True:
        name = input("Please enter machine name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        os_type = input("Please enter operating system(Ubuntu/CentOS): ")

        while True:
            try:
                cpu = int(input("Please enter CPU cores (whole number, e.g. 2, 4, 8): "))
                break
            except ValueError:
                print("Invalid CPU value. Please enter a whole number like 2, 4, or 8.")

        while True:
            try:
                ram = int(input("Please enter RAM in MB (e.g. 1024, 4096, 8192): "))
                break
            except ValueError:
                print("Invalid RAM value. Please enter a number in MB, for example 4096.")

        try:
            machine_config = MachineConfig(
                name=name,
                os=os_type,
                cpu=cpu,
                ram=ram
            )

            machine = Machine(
                machine_config.name,
                machine_config.os,
                machine_config.cpu,
                machine_config.ram
            )

            machine.log_creation()
            machines.append(machine.to_dict())
            print(f"Machine '{machine.name}' added successfully.\n")

        except ValidationError as e:
            print("Invalid input. Please check your values and try again.")
            print(e)
            print()

    return machines


def save_to_json(machines):
    """
    Save the collected machine configurations to a JSON file.

    The function creates the 'configs' directory if it does not exist
    and writes the machine configurations to configs/instances.json.
    """

    os.makedirs("configs", exist_ok=True)

    with open("configs/instances.json", "w", encoding="utf-8") as f:
        json.dump(machines, f, indent=4)

    print("Configuration saved to configs/instances.json")