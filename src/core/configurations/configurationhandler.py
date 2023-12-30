from django.conf import settings
from pathlib import Path
import ultraimport

BASE_APP_PATH = str(Path(__file__).resolve().parent.parent.parent.parent)

# Path to resources directory
RESOURCES_BASE_PATH = getattr(settings, "RESOURCES_BASE_PATH", BASE_APP_PATH + "/resources/")

# Path to web directory
WEB_BASE_PATH = getattr(settings, "WEB_BASE_PATH", BASE_APP_PATH + "/web/")

# Path to Configuration
config = ultraimport("__dir__/../../../config.py")
from config import CONFIGURATION as CONFIG

CONFIG = getattr(settings, "CONFIG", CONFIG)
