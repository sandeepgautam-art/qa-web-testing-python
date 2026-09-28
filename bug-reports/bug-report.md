# Defect Reports

## Defect Report Template

Copy this table for every new defect.

| Field | What to write |
|---|---|
| Bug ID | Unique id, e.g. BUG-001 |
| Title | One-line summary: what is wrong and where |
| Module | Login / Product / Cart / Checkout / Logout |
| Environment | Browser + version, OS, URL, date tested |
| Preconditions | State needed before the steps start |
| Steps to Reproduce | Numbered, exact steps anyone can follow |
| Expected Result | What should happen (based on requirement / common sense) |
| Actual Result | What really happened |
| Severity | Impact on the product: Critical / High / Medium / Low |
| Priority | Urgency to fix: High / Medium / Low |
| Status | New / Assigned / In Progress / Fixed / Retest / Closed / Reopened / Rejected |
| Evidence | Screenshot / video / log file name |
| Notes | Extra context, workaround, related test case id |

---

## Sample / Demonstration Defects

> **These five reports are made-up examples written to show the defect-reporting format.
> They are NOT bugs that were found in SauceDemo, and no screenshot exists for them.**
> The environment values are placeholders.

### BUG-001 (Sample) - Cart badge does not update after adding a product

| Field | Value |
|---|---|
| Title | Cart badge count stays at 0 after clicking "Add to cart" |
| Module | Product / Cart |
| Environment | Chrome <version>, <OS>, <application URL> (placeholder) |
| Preconditions | User is logged in with an empty cart |
| Steps to Reproduce | 1. Open the Products page. 2. Click "Add to cart" on any product. 3. Look at the cart icon. |
| Expected Result | Cart badge shows 1 and the button changes to "Remove". |
| Actual Result | Button changes to "Remove" but no badge is shown. |
| Severity | High |
| Priority | High |
| Status | New (sample) |
| Evidence | None - demonstration only |
| Notes | Related test case: TC_PROD_18. Severity is High because users cannot see how many items they have. |

### BUG-002 (Sample) - Missing validation message for empty postal code

| Field | Value |
|---|---|
| Title | No error is shown when postal code is empty and Continue is clicked |
| Module | Checkout |
| Environment | Chrome <version>, <OS>, <application URL> (placeholder) |
| Preconditions | User is on checkout step one with an item in the cart |
| Steps to Reproduce | 1. Enter first name and last name. 2. Leave postal code empty. 3. Click Continue. |
| Expected Result | Error "Postal Code is required" is shown and the user stays on step one. |
| Actual Result | The overview page opens without any message. |
| Severity | Medium |
| Priority | Medium |
| Status | New (sample) |
| Evidence | None - demonstration only |
| Notes | Related test case: TC_CHK_33. Shows a missing-validation defect. |

### BUG-003 (Sample) - Incorrect navigation from "Continue Shopping"

| Field | Value |
|---|---|
| Title | "Continue Shopping" opens the login page instead of the Products page |
| Module | Cart |
| Environment | Firefox <version>, <OS>, <application URL> (placeholder) |
| Preconditions | User is logged in and on the cart page |
| Steps to Reproduce | 1. Open the cart. 2. Click "Continue Shopping". |
| Expected Result | The Products page is displayed. |
| Actual Result | The login page is displayed and the session is lost. |
| Severity | High |
| Priority | High |
| Status | New (sample) |
| Evidence | None - demonstration only |
| Notes | Related test case: TC_CART_26. Shows an incorrect-navigation defect. |

### BUG-004 (Sample) - Product price differs between listing and cart

| Field | Value |
|---|---|
| Title | Price in cart does not match the price on the Products page |
| Module | Cart |
| Environment | Chrome <version>, <OS>, <application URL> (placeholder) |
| Preconditions | User is logged in |
| Steps to Reproduce | 1. Note the price of a product on the Products page. 2. Add it to the cart. 3. Open the cart and compare prices. |
| Expected Result | Both prices are identical. |
| Actual Result | The cart shows a different price. |
| Severity | Critical |
| Priority | High |
| Status | New (sample) |
| Evidence | None - demonstration only |
| Notes | Related test case: TC_CART_24. Critical severity because it affects money. |

### BUG-005 (Sample) - Very long input breaks the checkout layout

| Field | Value |
|---|---|
| Title | 100+ character first name overflows the form and hides the Continue button |
| Module | Checkout |
| Environment | Chrome <version>, <OS>, <application URL> (placeholder) |
| Preconditions | User is on checkout step one |
| Steps to Reproduce | 1. Paste a 100-character string into First Name. 2. Fill the other fields. 3. Look at the form. |
| Expected Result | Text stays inside the field (or the field limits its length). |
| Actual Result | Text overflows and the Continue button is hidden. |
| Severity | Low |
| Priority | Low |
| Status | New (sample) |
| Evidence | None - demonstration only |
| Notes | Related test case: TC_CHK_40. Shows a boundary / invalid-input defect. |

---

## Real Defects Found During Testing

_None recorded yet._ Only add a defect here after you have reproduced it yourself
on the live site and saved a screenshot in `screenshots/` (use `git add -f` if you
want to commit that file).
