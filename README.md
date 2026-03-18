![Python](https://img.shields.io/badge/Python-3.11-purple)
![Pydantic](https://img.shields.io/badge/Pydantic-2.12.5-purple)
![Pytest](https://img.shields.io/badge/Pytest-9.0.2-purple)
![Pylint](https://img.shields.io/badge/Pylint-4.0.5-purple)

# Infra Automation Tool

A simple infrastructure automation tool written in Python.

This project simulates infrastructure provisioning by collecting machine configuration from the user and generating infrastructure definitions in JSON format.

---

## Features

- Interactive CLI for infrastructure configuration
- Machine validation using Pydantic
- JSON configuration generation
- Logging system (INFO / ERROR)
- Basic provisioning simulation
- Input normalization (handles spaces and formatting)

---

## Project Structure

infra-automation/  
├── configs/       – generated infrastructure configs  
├── logs/          – application logs  
├── scripts/       – provisioning bash scripts  
├── src/           – application source code  
│   ├── models.py  
│   ├── machine.py  
│   ├── logger.py  
│   └── input_handler.py  
├── tests/         – unit tests  
├── main.py        – application entry point  
├── requirements.txt  
└── README.md  

---

## Setup

1. Clone the repository
2. Create a virtual environment:
3. Activate it:
4. Install dependencies:

---

## How to Run

Run the application:

```bash
python main.py

Example CLI Session

=== Infra Automation Tool ===

=== Machine Configuration Input ===
Type 'done' as machine name when you finish adding machines.


Please enter machine name (or 'done' to finish): web-server
Please enter operating system (Ubuntu/CentOS): Ubuntu
Please enter CPU cores (whole number, e.g. 2, 4, 8): 2
Please enter RAM in MB (e.g. 1024, 4096, 8192): 2048

Provisioning web-server: Ubuntu, 2 CPU, 2048MB RAM
Starting provisioning script...
Provisioning simulated (Windows environment)


Please enter machine name (or 'done' to finish): db-server
Please enter operating system (Ubuntu/CentOS): centos
Please enter CPU cores (whole number, e.g. 2, 4, 8): 8
Please enter RAM in MB (e.g. 1024, 4096, 8192): 8192

Provisioning db-server: CentOS, 8 CPU, 8192MB RAM
Starting provisioning script...
Provisioning simulated (Windows environment)


Please enter machine name (or 'done' to finish): app-server
Please enter operating system (Ubuntu/CentOS): Ubuntu
Please enter CPU cores (whole number, e.g. 2, 4, 8): 4
Please enter RAM in MB (e.g. 1024, 4096, 8192): 4096

Provisioning app-server: Ubuntu, 4 CPU, 4096MB RAM
Starting provisioning script...
Provisioning simulated (Windows environment)


Please enter machine name (or 'done' to finish): done
Configuration saved to configs/instances.json

Machine configurations created:
{'name': 'web-server', 'os': 'Ubuntu', 'cpu': 2, 'ram': 2048}
{'name': 'db-server', 'os': 'CentOS', 'cpu': 8, 'ram': 8192}
{'name': 'app-server', 'os': 'Ubuntu', 'cpu': 4, 'ram': 4096}


Example Output (JSON)

[
  {
    "name": "web-server",
    "os": "Ubuntu",
    "cpu": 2,
    "ram": 2048
  },
  {
    "name": "db-server",
    "os": "CentOS",
    "cpu": 8,
    "ram": 8192
  },
  {
    "name": "app-server",
    "os": "Ubuntu",
    "cpu": 4,
    "ram": 4096
  }
  
]


Saved to:

configs/instances.json

Provisioning

The project includes a basic provisioning script example:

scripts/setup_nginx.sh

Provisioning is simulated when running on Windows.

Validation Rules

Only two operating systems are allowed:

Ubuntu

CentOS

Input is normalized (spaces are removed)

CPU must be a positive integer

RAM must be within allowed limits


**Author:**
