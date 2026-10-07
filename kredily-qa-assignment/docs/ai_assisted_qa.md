# AI-Assisted QA

**Activity:** Generating Appium (Python/pytest) page objects and tests, plus the test-case matrix.
**Tool:** Claude (Anthropic)

## Prompt used
> I'm applying for a QA intern role. I have an Android HRMS app (Kredily) and need 5 automated journeys with
> Appium + pytest: valid login, invalid login, dashboard validation, attendance, and leave. I haven't inspected
> the app's resource IDs yet, so use resilient text/class-based locators with explicit waits, a page-object
> structure, screenshot-on-failure, and an HTML report. Also draft 20 manual test cases (positive/negative/edge).

## AI-generated output
The code in `automation/` and the matrix in `docs/test_cases.md` (initial version).

## What I changed / validated (fill in after running)
- [ ] Replaced text-based locators with stable `resource-id` / `content-desc` found in Appium Inspector
- [ ] Corrected labels to match the real UI (e.g. "Attendance" vs "Punch")
- [ ] Confirmed each assertion can fail (e.g. broke a locator to see the test go red)
- [ ] Removed/adjusted cases for features absent from this APK
- [ ] Ran the suite 3 times to check flakiness; tuned timeouts
- [ ] Things the AI got wrong: ______
