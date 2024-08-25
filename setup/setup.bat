@echo off
:: Create virtual environment
python3 -m venv .venv
:: Activate the virtual environment
call .venv\Scripts\activate.bat
:: Install dependencies
pip3 install -r requirements.txt
:: Deactivate the virtual environment
call .venv\Scripts\deactivate.bat
