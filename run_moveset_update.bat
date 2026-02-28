@echo off
echo ========================================
echo POKEMON COMPREHENSIVE MOVESET UPDATER
echo ========================================
echo.

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo Trying py launcher...
    py --version >nul 2>&1
    if errorlevel 1 (
        echo ERROR: Python is not installed or not in PATH
        echo Please install Python 3.6 or higher
        echo Or try: python3 execute_moveset_update.py
        pause
        exit /b 1
    )
    set PYTHON_CMD=py
) else (
    set PYTHON_CMD=python
)

echo Python found!
echo.

echo Running moveset update...
echo This may take a few minutes...
echo.

%PYTHON_CMD% execute_moveset_update.py

echo.
echo ========================================
echo UPDATE COMPLETE
echo ========================================
echo.
echo Please check the output above for any errors.
echo If successful, test compilation with: make
echo.
pause
