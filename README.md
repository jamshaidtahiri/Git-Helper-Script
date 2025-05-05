# Git Helper

A simple GUI tool that automates the Git workflow:
1. Select your Git repository
2. Automatically adds all files (`git add -A`)
3. Uses "new commit" as the commit message
4. Pushes changes to GitHub

## Building the Executable

You can build the executable using either PyInstaller (recommended) or py2exe.

### Option 1: Using PyInstaller (Recommended)

```
# Install PyInstaller
pip install pyinstaller

# Build the executable
python build_exe.py
```

Or run PyInstaller directly:

```
pyinstaller --onefile --windowed --name=GitHelper git_helper.py
```

### Option 2: Using py2exe

```
# Install dependencies
pip install py2exe setuptools

# Build the executable
python setup.py py2exe
```

Both methods will create a `dist` folder containing the standalone executable.

## Usage

1. Run the executable
2. Select your Git repository folder
3. The tool will automatically:
   - Add all files
   - Commit with message "new commit"
   - Push to GitHub

## Requirements

- Git must be installed and configured on your system
- You must have already set up remote repository access (SSH keys or credentials cached)

## Troubleshooting

- If you receive authentication errors, ensure your Git credentials are properly configured
- The tool assumes you're pushing to a remote named "origin" 