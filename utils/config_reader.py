"""Reads settings from config/config.ini so nothing is hard-coded."""
import configparser
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_FILE = PROJECT_ROOT / "config" / "config.ini"


def _load_config():
    parser = configparser.ConfigParser()
    if not parser.read(CONFIG_FILE):
        raise FileNotFoundError(f"Config file not found: {CONFIG_FILE}")
    return parser


_config = _load_config()


def get_base_url():
    return _config.get("application", "base_url")


def get_browser():
    return _config.get("browser", "browser").strip().lower()


def is_headless():
    """HEADLESS environment variable (if set) overrides config.ini."""
    env_value = os.environ.get("HEADLESS")
    if env_value is not None:
        return env_value.strip().lower() == "true"
    return _config.getboolean("browser", "headless", fallback=False)


def get_timeout():
    return _config.getint("settings", "timeout", fallback=10)
