"""Pydantic models for validating machine configuration data."""

from typing import ClassVar
from pydantic import BaseModel, Field, StrictInt, field_validator


class MachineConfig(BaseModel):
    """Validation model for a single machine configuration."""
    ALLOWED_OS: ClassVar[list[str]] = [
        "Ubuntu",
        "CentOS",
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


    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        """Validate and normalize the machine name."""
        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("Machine name cannot be empty")

        if len(cleaned_value) > 63:
            raise ValueError("Machine name cannot be longer than 63 characters")

        return cleaned_value

    @field_validator("os")
    @classmethod
    def validate_os(cls, value: str) -> str:
        """Validate and normalize the operating system value."""
        normalized_value = "".join(value.split()).lower()

        for os_name in cls.ALLOWED_OS:
            if normalized_value == os_name.lower():
                return os_name

        raise ValueError("Unsupported operating system")
