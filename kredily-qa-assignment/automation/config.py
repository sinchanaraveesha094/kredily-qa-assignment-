import os

APPIUM_URL = os.getenv("APPIUM_URL", "http://127.0.0.1:4723")
DEVICE_NAME = os.getenv("DEVICE_NAME", "emulator-5554")
APK_PATH = os.getenv("APK_PATH", os.path.abspath("kredily.apk"))
EMAIL = os.getenv("KREDILY_EMAIL", "")
PASSWORD = os.getenv("KREDILY_PASSWORD", "")
DEFAULT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "20"))
SCREENSHOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evidence", "screenshots"))
