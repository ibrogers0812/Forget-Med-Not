# tests/__init__.py

import os
import sys

# Add the app directory to the sys.path to ensure proper imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Optionally, any other setup code for your tests can go here
