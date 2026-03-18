"""Tests for Machine class functionality."""


from unittest.mock import patch

from src.machine import Machine


def test_machine_creation():
    machine = Machine("webserver", "Ubuntu", 2, 2048)

    assert machine.name == "webserver"
    assert machine.os == "Ubuntu"
    assert machine.cpu == 2
    assert machine.ram == 2048


def test_to_dict_returns_correct_dictionary():
    machine = Machine("db-server", "CentOS", 4, 4096)

    result = machine.to_dict()

    assert result == {
        "name": "db-server",
        "os": "CentOS",
        "cpu": 4,
        "ram": 4096
    }


def test_log_creation_prints_message(capsys):
    machine = Machine("api-node", "Ubuntu", 8, 8192)

    machine.log_creation()

    captured = capsys.readouterr()

    assert "Provisioning api-node: Ubuntu, 8 CPU, 8192MB RAM" in captured.out


def test_provision_simulates_on_windows(capsys):
    machine = Machine("win-node", "Ubuntu", 2, 2048)

    with patch("src.machine.os.name", "nt"):
        machine.provision()

    captured = capsys.readouterr()

    assert "Starting provisioning script..." in captured.out
    assert "Provisioning simulated (Windows environment)" in captured.out


def test_provision_runs_bash_script_on_posix():
    machine = Machine("linux-node", "Ubuntu", 2, 2048)

    with patch("src.machine.os.name", "posix"):
        with patch("src.machine.subprocess.run") as mock_run:
            machine.provision()

    mock_run.assert_called_once_with(
        ["bash", "scripts/setup_nginx.sh"],
        check=True
    )
