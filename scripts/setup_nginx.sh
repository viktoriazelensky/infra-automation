#!/bin/bash

echo "Starting Nginx setup..."

if command -v nginx >/dev/null 2>&1; then
    echo "Nginx is already installed."
else
    echo "Nginx is not installed. Installing Nginx..."

    sudo apt update
    sudo apt install -y nginx

    if command -v nginx >/dev/null 2>&1; then
        echo "Nginx installation completed successfully."
    else
        echo "Nginx installation failed."
        exit 1
    fi
fi

echo "Nginx setup process finished."