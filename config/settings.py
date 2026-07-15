from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
