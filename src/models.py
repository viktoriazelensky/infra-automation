from pydantic import BaseModel, Field, StrictInt, field_validator


class MachineConfig(BaseModel):
    # Allowed operating systems supported by this project.
    # Restricting the list helps prevent arbitrary or invalid user input.
    ALLOWED_OS = [
        "Ubuntu",
        "Debian",
        "CentOS",
        "Rocky Linux",
        "AlmaLinux",
        "Fedora",
        "Alpine",
        "Arch Linux",
        "Oracle Linux",
        "Windows Server",
    ]

    name: str
    os: str
    cpu: StrictInt = Field(gt=0, le=224)
    ram: StrictInt = Field(gt=0, le=32768)

    # Model configuration:
    # forbid any extra fields that are not defined in this model
    model_config = {
        "extra": "forbid"
    }

    # Validate machine name:
    # removes leading/trailing spaces and ensures the name is not empty
    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("Machine name cannot be empty")

        return cleaned_value

    # Validate operating system:
    # normalizes user input and checks if the OS is in the supported list
    @field_validator("os")
    @classmethod
    def validate_os(cls, value: str) -> str:
        normalized_value = value.strip().lower()

        for os_name in cls.ALLOWED_OS:
            if normalized_value == os_name.lower():
                return os_name

        raise ValueError("Unsupported operating system")