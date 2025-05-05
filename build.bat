@echo off
echo Installing PyInstaller...
pip install pyinstaller
echo.
echo Building executable...
pyinstaller --onefile --windowed --name=GitHelper git_helper.py
echo.
echo Done! The executable is in the dist folder.
pause 