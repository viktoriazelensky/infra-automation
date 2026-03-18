"""Tests for input handling and JSON saving."""


import json
import os
from unittest.mock import patch

from src.input_handler import save_to_json, get_user_input


def test_save_to_json():
    machines = [
        {"name": "web", "os": "Ubuntu", "cpu": 2, "ram": 2048},
        {"name": "db", "os": "CentOS", "cpu": 4, "ram": 4096},
    ]

    save_to_json(machines)

    assert os.path.exists("configs/instances.json")

    with open("configs/instances.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data == machines


def test_get_user_input_single_machine():
    user_inputs = [
        "webserver",
        "ubuntu",
        "2",
        "2048",
        "done"
    ]

    with patch("builtins.input", side_effect=user_inputs):
        machines = get_user_input()

    assert len(machines) == 1
    assert machines[0]["name"] == "webserver"
    assert machines[0]["os"] == "Ubuntu"
    assert machines[0]["cpu"] == 2
    assert machines[0]["ram"] == 2048


def test_get_user_input_multiple_machines():
    user_inputs = [
        "web",
        "ubuntu",
        "2",
        "2048",
        "db",
        "centos",
        "4",
        "4096",
        "done"
    ]

    with patch("builtins.input", side_effect=user_inputs):
        machines = get_user_input()

    assert len(machines) == 2
    assert machines[0]["name"] == "web"
    assert machines[0]["os"] == "Ubuntu"
    assert machines[0]["cpu"] == 2
    assert machines[0]["ram"] == 2048

    assert machines[1]["name"] == "db"
    assert machines[1]["os"] == "CentOS"
    assert machines[1]["cpu"] == 4
    assert machines[1]["ram"] == 4096
