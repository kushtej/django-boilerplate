from django.conf import settings
import os
from pathlib import Path
import json
import sys

BASE_APP_PATH = str(Path(__file__).resolve().parent.parent.parent.parent)

# Path to resources directory
RESOURCES_BASE_PATH = getattr(settings, "RESOURCES_BASE_PATH", BASE_APP_PATH + "/resources/")

# Path to web directory
WEB_BASE_PATH = getattr(settings, "WEB_BASE_PATH", BASE_APP_PATH + "/web/")

# Path to Configuration
sys.path.insert(1, BASE_APP_PATH)
from config import CONFIGURATION

CONFIG = getattr(settings, "CONFIG", CONFIGURATION)
