"""
Loads a WSGI entry point from the *application_server* module after re-mounting
with Python 3
"""

import os
import sys

# inject/forward to Python3
INTERP = os.path.abspath(os.path.expanduser("/usr/bin/python3"))
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
from application_server import APP as application
