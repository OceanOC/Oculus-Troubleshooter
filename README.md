
# Oculus Troubleshooter

Makes finding Oculus files easy and allows to change some settings


## Why do I need this?

if you want to change settings from the debug tool you'd have to go through tons of files just to open it instead you'd just have to press 2 buttons with this program
## Installation

Run the Quest Troubleshooter from 
    
## Building from source

Requirements: Python 3.10 (should work in 3.8+)

1. Git the project and use venv in python

```bash
  pip install -U PyQt6
```
2. Run noquest.py with Admin Privileges

3. (Not needed) Install PyInstaller and run with these commands to get a EXE

```bash
    pip install PyInstaller

    python -m pyinstaller --noconfirm --onefile --windowed --name "Quest Troubleshooter" --clean --uac-admin --add-data "(path to PyQt6 folder)"  "(Path to noquest.py)"
```
