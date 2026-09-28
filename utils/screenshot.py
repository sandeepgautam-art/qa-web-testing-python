"""Saves screenshots into the screenshots/ folder."""
import re
from datetime import datetime
from pathlib import Path

SCREENSHOT_DIR = Path(__file__).resolve().parent.parent / "screenshots"


def take_screenshot(driver, test_name):
    """Save a PNG named <test_name>_<YYYY-MM-DD_HHMMSS>.png and return its Path."""
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    # Parametrized test names contain characters like [ ] that are awkward in filenames.
    safe_name = re.sub(r"[^\w\-]+", "_", test_name).strip("_")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    file_path = SCREENSHOT_DIR / f"{safe_name}_{timestamp}.png"
    driver.save_screenshot(str(file_path))
    return file_path
