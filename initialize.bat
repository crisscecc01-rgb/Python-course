@echo off
SET VENV_NAME=pk_venv

if not exist %VENV_NAME% (
    echo [INFO] Creation Virtual Environment...
    py -m venv %VENV_NAME%
    if %errorlevel% neq 0 (
        echo [ERROR] Venc creation not possible. Verify Python installation.
        pause
        exit /b %errorlevel%
    )
)

echo [INFO] Starting virtual environment...
call %VENV_NAME%\Scripts\activate
if %errorlevel% neq 0 (
    echo [ERROR] Starting VENV not possible.
    pause
    exit /b %errorlevel%
)

if exist requirements.txt (
    echo [INFO] Verify installation packages from requirements
    pip install -r requirements.txt
) else (
    echo [WARNING] requirements.txt not found. Skip installation
)

echo [INFO] Starting main.py
py main.py

if %errorlevel% neq 0 (
    echo [ERROR] Pokèmon Game ended with an error.
    pause
)
deactivate