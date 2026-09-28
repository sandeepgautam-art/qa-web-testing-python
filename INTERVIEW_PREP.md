# Interview Preparation

## 60-second explanation
"I built a QA project for SauceDemo, a demo shopping site. I wrote 40 manual test cases covering login, products,
cart, checkout and logout, including negative and validation cases like invalid credentials, a locked user and
empty checkout fields. I then automated 30 of them with Python, Selenium and Pytest using the Page Object Model.
It has reusable fixtures in conftest.py, explicit waits instead of sleeps, test data in a CSV, a config file for
the URL and browser, automatic screenshots when a test fails, and an HTML report from pytest-html. I also wrote
a defect report template with sample defects, clearly labelled as examples."

## 2-minute explanation
"The project has two parts. First, manual testing: a CSV of 40 test cases with preconditions, steps, data,
expected result, priority and severity. I did not fill in results I had not executed, so unexecuted cases say
'Not Executed'.

Second, automation. Each page has a page-object class (login, products, cart, checkout, checkout complete) that
stores locators and user actions, and all of them inherit a BasePage with explicit-wait helpers. The tests never
touch raw Selenium; they call methods like login_page.login(). In conftest.py I created a driver fixture that
starts Chrome through a driver factory and always quits it afterwards, plus fixtures for the page objects and for
a logged-in Products page, so tests don't repeat setup.

Login and checkout negative tests are data-driven: they use pytest parametrize with rows from test_data.csv, so
one function covers several scenarios. Tests carry markers - smoke for the core journeys, regression for the whole
suite, negative and validation for error paths. A pytest hook in conftest.py takes a screenshot whenever a test
fails and attaches it to the pytest-html report. Configuration lives in config.ini, and I kept the virtual
environment, screenshots and reports out of Git. Future improvements I'd add are CI with GitHub Actions,
cross-browser runs and parallel execution - these are not implemented yet."

## Resume entry
**Web Application Testing & QA Automation | Python, Selenium, Pytest**
- Designed and documented 40 functional, negative and validation manual test cases (login, cart, checkout) with priority and severity, plus a defect report template.
- Automated 30 test cases using Selenium WebDriver, Python and Pytest with the Page Object Model, data-driven tests from CSV, and smoke/regression markers.
- Implemented reusable fixtures in conftest.py, explicit waits, automatic failure screenshots and pytest-html reporting.

## Interview questions and answers

### Project and testing basics
1. **Walk me through your project.** Use the 60-second answer above.
2. **Why SauceDemo?** It is a stable, public demo site built for practice, with a locked-out user for negative tests and no real data.
3. **Test scenario vs test case?** A scenario is a high-level thing to verify ("login works"). A test case is the detailed version: preconditions, steps, data, expected result.
4. **Severity vs priority?** Severity = how badly the defect affects the product. Priority = how soon it should be fixed. Wrong price in the cart: high severity and high priority. Typo in a rarely seen footer: low severity, low priority. A misspelt company name on the home page: low severity, high priority.
5. **Bug life cycle?** New -> Assigned -> In Progress -> Fixed -> Retest -> Closed. If the retest fails it is Reopened; invalid reports are Rejected; repeats are marked Duplicate.
6. **What goes into a good bug report?** Clear title, environment, preconditions, exact steps, expected vs actual result, severity/priority, evidence and notes - see `bug-report.md`.
7. **Functional testing?** Checking the application does what the requirements say - e.g. adding a product updates the cart.
8. **Negative testing?** Using invalid input or unexpected actions to check the app handles them safely - e.g. wrong password, locked user.
9. **Validation testing?** Checking input rules such as required fields - the empty first name / postal code tests.
10. **Smoke testing?** A quick check that the main flows work before deeper testing. Mine: `pytest -m smoke`.
11. **Regression testing?** Re-running existing tests after a change to make sure nothing broke. Mine: the full suite, marker `regression`.
12. **Positive vs negative test?** Positive uses valid data and expects success; negative uses invalid data and expects a proper error.
13. **Boundary testing example?** Very long text or whitespace-only names in checkout fields (TC_CHK_39/40).
14. **Did you find any bugs?** Be honest: "No real defects yet; the five in my report are labelled samples showing the format. If I find one I record it with a screenshot."

### Python
15. **Why Python for automation?** Simple readable syntax, strong Selenium/Pytest support, quick to write.
16. **What OOP concepts did you use?** Classes for page objects, inheritance (every page extends BasePage), encapsulation (locators and actions grouped per page).
17. **What is a virtual environment and why use it?** An isolated Python environment so this project's package versions don't clash with other projects; created with `python3 -m venv venv`.
18. **What is requirements.txt?** A list of the libraries to install with `pip install -r requirements.txt`, so anyone can recreate the setup.

### Selenium
19. **What is Selenium WebDriver?** A library that controls a real browser through code - open pages, click, type, read text.
20. **Explicit vs implicit vs fluent wait?** Explicit waits for one condition on one element (WebDriverWait). Implicit applies a default wait to every element lookup. Fluent is an explicit wait with custom polling and ignored exceptions. I use explicit waits only and avoid `time.sleep()` because sleeps are slow and flaky.
21. **CSS selector vs XPath?** CSS is faster and shorter; XPath can match by visible text and move up to a parent. I used IDs and CSS mostly, and XPath to open a product by its visible name.
22. **Locators you know?** ID, name, class name, tag name, link text, CSS selector, XPath.
23. **What does webdriver-manager do?** Downloads the chromedriver that matches the installed Chrome. If it fails, my factory falls back to Selenium Manager.
24. **What causes flaky tests and how did you reduce them?** Timing and unstable locators. I used explicit waits, stable IDs/CSS, and a fresh browser per test.
25. **Why disable Chrome's password pop-up?** It can cover the page and block clicks, so it is turned off via Chrome prefs in the driver factory.

### Pytest
26. **What is a fixture?** A reusable setup/teardown function. My `driver` fixture starts Chrome, yields it to the test, then quits it - even when the test fails.
27. **What is conftest.py?** A special file where shared fixtures and hooks live; pytest finds it automatically, no imports needed.
28. **How does the screenshot-on-failure work?** A `pytest_runtest_makereport` hook checks each test result; on failure it saves a PNG with the test name and timestamp and adds it to the HTML report.
29. **What is parametrize?** It runs one test function with several data sets. I use it for invalid logins and checkout validation, reading rows from the CSV.
30. **What are markers?** Labels on tests (`smoke`, `regression`) so you can run subsets: `pytest -m smoke`. They are registered in `pytest.ini`.
31. **Assertion examples from your tests?** `assert login_page.get_error_message() == data["expected_message"]`, `assert products_page.get_cart_count() == 1`, `assert round(item_total + tax, 2) == total`.
32. **How do you generate the report?** `python3 -m pytest --html=reports/test-report.html --self-contained-html`.

### Page Object Model, Git, CI/CD
33. **What is POM and why use it?** One class per page holding locators and actions. Tests become readable and a UI change is fixed in one file.
34. **Why a BasePage?** To keep the explicit-wait helper methods in one place instead of copying them into every page.
35. **What is in .gitignore and why?** venv, caches, IDE files, screenshots and reports - they are generated or machine-specific.
36. **Basic Git commands you used?** `git init`, `git add`, `git commit`, `git branch`, `git push`, `git status`, `git log`.
37. **What is CI/CD and how would you add it here?** CI runs tests automatically on every push. I'd add a GitHub Actions workflow that installs requirements and runs `pytest` headless (`HEADLESS=true`). This is a planned improvement, not implemented.
38. **How would you scale the suite?** Parallel runs with pytest-xdist, Selenium Grid, more browsers, API tests for the backend.
