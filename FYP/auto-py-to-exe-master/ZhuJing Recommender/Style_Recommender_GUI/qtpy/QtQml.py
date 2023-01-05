# -----------------------------------------------------------------------------
# Copyright © 2009- The Spyder Development Team
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
"""Provides QtQml classes and functions."""

# Local imports
from . import PYQT5, PYQT6, PYSIDE2, PYSIDE6, PythonQtError

if PYQT5:
    from PyQt5.QtQml import *
elif PYQT6:
    from PyQt6.QtQml import *
elif PYSIDE6:
    from PySide6.QtQml import *
elif PYSIDE2:
    from PySide2.QtQml import *
else:
    raise PythonQtError('No Qt bindings could be found')
