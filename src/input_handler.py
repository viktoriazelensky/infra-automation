import json
import os

from pydantic import ValidationError
from src.models import MachineConfig


# This function collects machine configurations from the user.
# It asks for machine name, operating system, CPU cores and RAM.
# Valid machines are added to the list until the user enters 'done'.
def get_user_input():
    machines = []

    print("\n=== Machine Configuration Input ===")
    print("Type 'done' as machine name when you finish adding machines.\n")

    while True:
        name = input("Please enter machine name (or 'done' to finish): ").strip()

        if name.lower() == "done":
            break

        os_type = input("Please enter operating system: ")

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
            machine = MachineConfig(
                name=name,
                os=os_type,
                cpu=cpu,
                ram=ram
            )

            machines.append(machine.model_dump())
            print(f"Machine '{machine.name}' added successfully.\n")

        except ValidationError as e:
            print("Invalid input. Please check your values and try again.")
            print(e)
            print()

    return machines


# This function saves the collected machine configurations to JSON.
def save_to_json(machines):
    os.makedirs("configs", exist_ok=True)

    with open("configs/instances.json", "w", encoding="utf-8") as f:
        json.dump(machines, f, indent=4)

    print("Configuration saved to configs/instances.json")