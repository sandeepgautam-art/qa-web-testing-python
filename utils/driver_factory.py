"""Creates the Selenium WebDriver used by every test."""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from utils import config_reader

PAGE_LOAD_TIMEOUT_SECONDS = 30


def _build_chrome_options(headless):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
        # Headless Chrome has no window to maximize, so set a size instead.
        options.add_argument("--window-size=1920,1080")
    # Stop Chrome's "save password / password breach" pop-ups from covering
    # the page and blocking clicks during tests.
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        },
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return options


def _build_chrome_service():
    """Use webdriver-manager to fetch a matching chromedriver.

    If that fails (for example no internet to the driver download site),
    fall back to Selenium's built-in Selenium Manager (Selenium 4.6+).
    """
    try:
        from webdriver_manager.chrome import ChromeDriverManager

        return Service(ChromeDriverManager().install())
    except Exception as error:  # noqa: BLE001 - any failure -> fallback
        print(f"webdriver-manager failed ({error}); using Selenium Manager.")
        return Service()


def create_driver():
    """Start the browser named in config.ini and return the driver."""
    browser = config_reader.get_browser()
    if browser != "chrome":
        raise ValueError(
            f"Unsupported browser '{browser}'. Only 'chrome' is implemented; "
            "add a branch here to support others."
        )

    driver = webdriver.Chrome(
        service=_build_chrome_service(),
        options=_build_chrome_options(config_reader.is_headless()),
    )
    driver.maximize_window()
    # Only a page-load limit here. Element waiting is done with explicit
    # WebDriverWait in the page objects (mixing implicit + explicit waits
    # can cause unpredictable delays).
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT_SECONDS)
    return driver
