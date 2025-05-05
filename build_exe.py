"""
Build script for creating an executable with PyInstaller
Run with: python build_exe.py
"""
import PyInstaller.__main__
import os

# Run PyInstaller
PyInstaller.__main__.run([
    'git_helper.py',
    '--onefile',
    '--windowed',
    '--name=GitHelper',
    '--icon=NONE',
])

print("Build completed! Executable should be in the 'dist' folder.") 