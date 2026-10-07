# Kredily HRMS – Intern QA Engineer Assignment

Covers: functional testing, bug reporting, Appium automation, API testing, AI-assisted QA.

## Repo layout
| Path | Contents |
|---|---|
| `docs/test_cases.md` | 20 manual test cases (positive / negative / edge) + result column |
| `docs/bug_reports.md` | Bug report template + areas to probe + bug log |
| `docs/ai_assisted_qa.md` | Prompt, AI output, what was changed/validated |
| `docs/qa_summary.md` | Final QA summary |
| `automation/` | Appium + pytest suite (5 journeys), HTML report in `automation/reports/` |
| `api/Kredily_API.postman_collection.json` | Postman collection (positive + negative) |
| `evidence/` | Screenshots and screen recordings |

## Setup (automation)
Prerequisites: Node 18+, Java 17, Android SDK (platform-tools), Python 3.10+, an emulator or USB device.

```bash
npm i -g appium
appium driver install uiautomator2
python -m venv .venv && source .venv/bin/activate
pip install -r automation/requirements.txt

# download the APK
curl -o automation/kredily.apk https://download.aiagent.kredily.com/static/kredily-mobile-v2.apk

# start Appium (terminal 1)
appium

# run tests (terminal 2)
cd automation
export APK_PATH=$(pwd)/kredily.apk
export KREDILY_EMAIL='peoplekredily1@yopmail.com'
export KREDILY_PASSWORD='Pass@9865'
pytest --html=reports/report.html --self-contained-html
```
Optional env vars: `DEVICE_NAME`, `APPIUM_URL` (default `http://127.0.0.1:4723`).
Failed tests save a screenshot to `evidence/screenshots/`.

**Important:** locators in `automation/pages/` are text/class based because the APK's resource IDs were not
inspected. Open the app in Appium Inspector and tighten them (marked `VERIFY`).

## API testing
Import `api/Kredily_API.postman_collection.json` into Postman and set `base_url`, `email`, `password`.
Endpoints are placeholders until confirmed by capturing the app's traffic (Postman proxy / mitmproxy / Charles).
Run with Newman: `newman run api/Kredily_API.postman_collection.json`.
