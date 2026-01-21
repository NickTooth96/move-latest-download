#!/bin/bash

# Linux installer script for move-latest-download

# Make the main script executable
chmod +x "$(realpath ../main.py)"

# Create a symbolic link to the main script in /usr/local/bin
sudo ln -s "$(realpath ../main.py)" /usr/local/bin/mvld

echo "move-latest-download installed successfully!"