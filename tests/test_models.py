"""Tests for MachineConfig validation logic."""


import pytest
from pydantic import ValidationError

from src.models import MachineConfig


def test_valid_machine_config_with_ubuntu():
    machine = MachineConfig(
        name="webserver",
        os="ubuntu",
        cpu=2,
        ram=2048
    )

    assert machine.name == "webserver"
    assert machine.os == "Ubuntu"
    assert machine.cpu == 2
    assert machine.ram == 2048


def test_valid_machine_config_with_centos():
    machine = MachineConfig(
        name="db-server",
        os="centos",
        cpu=8,
        ram=8192
    )

    assert machine.name == "db-server"
    assert machine.os == "CentOS"
    assert machine.cpu == 8
    assert machine.ram == 8192


def test_os_is_normalized_with_spaces():
    machine = MachineConfig(
        name="api-node",
        os="   ubuntu   ",
        cpu=4,
        ram=4096
    )

    assert machine.os == "Ubuntu"


def test_name_is_trimmed():
    machine = MachineConfig(
        name="   backend-node   ",
        os="ubuntu",
        cpu=2,
        ram=2048
    )

    assert machine.name == "backend-node"


def test_invalid_os_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="bad-machine",
            os="windows",
            cpu=2,
            ram=2048
        )


def test_empty_name_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="",
            os="ubuntu",
            cpu=2,
            ram=2048
        )


def test_name_with_only_spaces_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="     ",
            os="ubuntu",
            cpu=2,
            ram=2048
        )


def test_name_longer_than_63_characters_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="a" * 64,
            os="ubuntu",
            cpu=2,
            ram=2048
        )


def test_name_with_exactly_63_characters_is_valid():
    machine = MachineConfig(
        name="a" * 63,
        os="ubuntu",
        cpu=2,
        ram=2048
    )

    assert machine.name == "a" * 63


def test_cpu_must_be_greater_than_zero():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="bad-cpu",
            os="ubuntu",
            cpu=0,
            ram=2048
        )


def test_negative_cpu_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="negative-cpu",
            os="ubuntu",
            cpu=-2,
            ram=2048
        )


def test_ram_must_be_greater_than_zero():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="bad-ram",
            os="ubuntu",
            cpu=2,
            ram=0
        )


def test_negative_ram_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="negative-ram",
            os="ubuntu",
            cpu=2,
            ram=-1024
        )


def test_ram_above_maximum_raises_error():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="too-much-ram",
            os="ubuntu",
            cpu=2,
            ram=40000
        )


def test_ram_equal_to_maximum_is_valid():
    machine = MachineConfig(
        name="max-ram-node",
        os="ubuntu",
        cpu=4,
        ram=32768
    )

    assert machine.ram == 32768


def test_cpu_large_but_valid_value():
    machine = MachineConfig(
        name="big-cpu-node",
        os="centos",
        cpu=128,
        ram=8192
    )

    assert machine.cpu == 128


def test_extra_field_is_forbidden():
    with pytest.raises(ValidationError):
        MachineConfig(
            name="extra-field-node",
            os="ubuntu",
            cpu=2,
            ram=2048,
            disk=100
        )
