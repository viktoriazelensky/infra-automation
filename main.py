"""Entry point for the Infra Automation Tool."""


from src.input_handler import get_user_input, save_to_json
from src.logger import logger

logger.info("Application started")


def main():
    """Run the main application workflow."""
    print("=== Infra Automation Tool ===")

    machines = get_user_input()

    if not machines:
        print("No machines were added.")
        return

    save_to_json(machines)

    print("\nMachine configurations created:")
    for machine in machines:
        print(machine)

    logger.info("Provisioning process finished")


if __name__ == "__main__":
    main()
