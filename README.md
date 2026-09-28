# Web Application Testing & QA Automation using Python

## Project Overview
A fresher-level Quality Engineering project that tests the demo shop
[SauceDemo](https://www.saucedemo.com/) in two ways:

1. **Manual testing** - 40 documented test cases (`test-cases/test-cases.csv`).
2. **Automation testing** - 30 automated test cases written with Python, Selenium WebDriver and Pytest,
   using the Page Object Model.

> **Honesty note:** this repository contains **no pre-filled execution results**. Every manual test case is
> marked `Not Executed` until *you* run it. The automated results appear only in the report you generate
> yourself. The five defects in `bug-reports/bug-report.md` are labelled sample/demonstration defects.

## Objective
Shows these QA skills: test case design, positive / negative / validation testing, defect reporting,
Selenium automation, Pytest fixtures, Page Object Model, explicit waits, screenshots on failure,
HTML reporting and Git/GitHub project organisation.

## Application Under Test
SauceDemo is a free demo e-commerce site made for testing practice. Modules covered: Login, Logout,
Product listing, Product details, Add/Remove from cart, Cart, Checkout, form validation, Order completion.
Demo credentials (`standard_user`, `locked_out_user`, password `secret_sauce`) are published on the
site's own login page. No real personal data is used.

## Technologies
Python 3 | Selenium WebDriver | Pytest | pytest-html | webdriver-manager | Git/GitHub | VS Code

## Project Structure
```
qa-web-testing-python/
├── README.md               this file
├── requirements.txt        libraries to install
├── pytest.ini              pytest settings + marker names
├── .gitignore
├── config/config.ini       base_url, browser, headless, timeout
├── pages/                  Page Object Model
│   ├── base_page.py        shared explicit-wait helpers (click, type, get_text ...)
│   ├── login_page.py
│   ├── products_page.py    products list + product details
│   ├── cart_page.py
│   ├── checkout_page.py    checkout step one + overview
│   └── checkout_complete_page.py
├── tests/
│   ├── conftest.py         fixtures (driver, page objects) + screenshot hook
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/
│   ├── config_reader.py    reads config.ini
│   ├── data_reader.py      reads test-data/test_data.csv
│   ├── driver_factory.py   creates the Chrome driver
│   └── screenshot.py       saves screenshots
├── test-data/test_data.csv
├── test-cases/test-cases.csv
├── bug-reports/bug-report.md
├── screenshots/            failure screenshots appear here
├── reports/                HTML report appears here
└── INTERVIEW_PREP.md       explanations, resume bullets, Q&A
```

## Manual Testing
`test-cases/test-cases.csv` has 40 cases: Login (12), Logout (1), Product (9), Cart (6), Checkout (12).
Columns: Test Case ID, Module, Test Scenario, Preconditions, Test Steps, Test Data, Expected Result,
Actual Result, Status, Priority, Severity (+ an `Automation Reference` column linking to the Pytest test).
30 cases are automated; 10 are manual-only (sorting, direct-URL access, boundary inputs and so on).
Fill in *Actual Result* and *Status* as you execute them.

## Automation Testing
30 automated test cases (24 test functions; some use `@pytest.mark.parametrize` to run one function with several
data rows from `test_data.csv`):

| File | Test cases |
|---|---|
| test_login.py | 9 - valid login, invalid username/password, 3 empty-field variants, locked user, dismiss error, logout |
| test_products.py | 7 - page loads, products displayed, details match, back navigation, add one, add many, remove |
| test_cart.py | 4 - cart opens, correct product/price/quantity, remove item, continue shopping |
| test_checkout.py | 10 - page opens, valid info, 4 validation variants, cancel, totals, complete order, cart empty after order |

Key techniques: fixtures in `conftest.py`, data-driven tests from CSV, explicit waits, meaningful assertions,
and pytest markers (`smoke`, `regression`, `negative`, `validation`).

## Testing Types (only what this project really demonstrates)
- **Functional testing** - login, cart, checkout behave as specified.
- **UI testing** - product names, prices, images, buttons and page titles are present and correct.
- **Positive testing** - valid login, valid checkout information, successful order.
- **Negative testing** - invalid credentials, locked user, missing checkout data.
- **Validation testing** - required-field messages on login and checkout.
- **Smoke testing** - `pytest -m smoke` runs a small set of core journeys (login, add to cart, checkout, order, logout).
- **Regression testing** - every test carries the `regression` marker, so `pytest -m regression` re-runs the whole suite after any change.

## Page Object Model (POM) in simple words
Each web page gets its own Python class that holds (1) the locators of that page and (2) the actions a user can do
on it. Tests call `login_page.login(...)` instead of raw Selenium code. If the site changes a locator you fix it
in one place instead of in every test.

## Explicit waits
`WebDriverWait` + expected conditions (`visibility_of_element_located`, `element_to_be_clickable`,
`presence_of_all_elements_located`, `invisibility_of_element_located`) wait only as long as needed and stop as
soon as the condition is true. `time.sleep()` always waits the full time (slow) and can still be too short (flaky).
The project contains no `time.sleep()` calls and no implicit wait.

## Test Execution
Run every command from the project root folder.

**1. Create the virtual environment** (keeps this project's libraries separate from your system Python)
```bash
python3 -m venv venv
```
**2. Activate it**
```bash
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows (Command Prompt)
.\venv\Scripts\Activate.ps1     # Windows (PowerShell)
```
Your prompt now starts with `(venv)`.

**3. Install dependencies (inside the venv)**
```bash
pip install -r requirements.txt
```
**4. Run the tests**
```bash
python3 -m pytest                     # all tests   (Windows: python -m pytest)
python3 -m pytest -m smoke            # smoke tests only
python3 -m pytest tests/test_login.py # one file
HEADLESS=true python3 -m pytest       # no visible browser window (macOS/Linux)
```
**5. Run with an HTML report**
```bash
python3 -m pytest --html=reports/test-report.html --self-contained-html
```
Requirements: Python 3.9+, Google Chrome installed, internet access.
In VS Code: install the *Python* extension, choose the `venv` interpreter (Ctrl/Cmd+Shift+P -> *Python: Select Interpreter*),
then run the commands in the built-in terminal.

## Screenshots
`tests/conftest.py` contains a `pytest_runtest_makereport` hook. After each test phase pytest calls it; if the
test failed and used the `driver` fixture, `utils/screenshot.py` saves
`screenshots/<test_name>_<YYYY-MM-DD_HHMMSS>.png` (for example
`test_valid_login_2026-09-28_103000.png`) and the image is also embedded in the HTML report.

## Test Reports
`reports/test-report.html` (created by the command above) is one self-contained file you can open in any browser.
It lists each test's name, result, duration, failure details and the failure screenshot.

## Defect Reporting
`bug-reports/bug-report.md` holds the template (Bug ID, Title, Module, Environment, Preconditions, Steps,
Expected, Actual, Severity, Priority, Status, Evidence, Notes), five clearly labelled **sample** defects and an
empty **Real Defects Found During Testing** section for verified findings only.

## What is (and is not) committed to Git
- `venv/`, caches, IDE files: never committed.
- `screenshots/*.png` and `reports/*.html`: **ignored**, because they change on every run, differ per machine
  (the report includes machine details) and bloat the repository. The folders stay via `.gitkeep`.
  After a real run you may commit one report as proof with `git add -f reports/test-report.html`.
- No passwords/keys exist; the demo credentials are public.

## Suggested commit messages
```
feat: add Selenium WebDriver setup and configuration
feat: implement page objects for login, products, cart and checkout
test: add login and logout test cases
test: add products, cart and checkout automation
docs: add manual test cases, bug report template and README
```

## Compatibility notes
- Chrome must be installed. `webdriver-manager` downloads a matching chromedriver; if that download fails the
  code falls back to Selenium Manager (built into Selenium 4.6+).
- Chrome may show a "change your password" pop-up for demo users; the driver options disable it.
- If SauceDemo changes its HTML or error wording, update the locators in `pages/` or the expected messages in
  `test-data/test_data.csv`.
- On Linux servers/containers Chrome may need `--no-sandbox`; add it in `utils/driver_factory.py`.

## Future Improvements (NOT implemented)
API testing | Database testing | GitHub Actions CI/CD | Cross-browser testing | Parallel execution (pytest-xdist) |
Selenium Grid | Allure reporting
