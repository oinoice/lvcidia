@echo off

REM Check if the venv directory exists
if not exist ".venv" (
    echo Setting up virtual environment...
    python -m venv .venv
    .venv\Scripts\pip install requests
    .venv\Scripts\pip install python-dotenv
)

REM Activate the virtual environment and run the script with arguments
call .venv\Scripts\activate
python main.py %*
call .venv\Scripts\deactivate.bat
pause
