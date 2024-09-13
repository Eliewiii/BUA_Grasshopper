@echo off
REM Define the path to the virtual environment
SET VENV_PATH=venv

REM Activate the virtual environment
IF EXIST "%VENV_PATH%\Scripts\activate.bat" (
    call "%VENV_PATH%\Scripts\activate.bat"
) ELSE (
    echo Virtual environment not found at %VENV_PATH%.
    exit /b 1
)

REM Install the package
echo Installing the package...
pip install .

REM Run the post-install command to handle dataset download
echo Running the dataset update script...
update-datasets

REM Deactivate the virtual environment
echo Deactivating the virtual environment...
deactivate

echo Installation and setup complete.
pause