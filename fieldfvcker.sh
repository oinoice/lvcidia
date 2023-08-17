#!/bin/bash

# Check if the venv directory exists
if [ ! -d ".venv" ]; then
    echo "Setting up virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install requests python-dotenv
else
    source .venv/bin/activate
fi

# Source the .env file if it exists
if [ -f ".env" ]; then
    set -a
    source .env
    set +a
fi

# Run the main script with arguments
python3 main.py "$@"
deactivate
