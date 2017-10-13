"""
Executable build script, modify and run this on the appropriate OS.
Run with 'python setup.py build'
"""

import sys
from cx_Freeze import setup, Executable
import opcode
import os


if sys.platform == 'win32':
    exe = Executable(
        'primecounter.py',
        targetName="primecounter.exe",
        base="Win32GUI",
        icon="img/logo.ico")
else:
    exe = Executable(
        'primecounter.py',
        targetName="primecounter",
        copyDependentFiles=True
    )

includefiles = ['data/', 'img/']

options = {
    'build_exe': {
        'includes': ['atexit', 'PySide.QtCore'],
        'include_files': includefiles,
        'excludes': []
    }
}

setup(
    name='Accenture Prime Counter',
    version='0.1',
    description='Accenture Prime Counter, developed by Ronald Olsthoorn',
    options=options,
    executables=[exe])
