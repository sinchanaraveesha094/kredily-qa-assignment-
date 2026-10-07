# Bug Reports

> Log only bugs you actually reproduced on the APK, with evidence from `evidence/`.
> The list below is areas worth probing (hypotheses, NOT confirmed bugs).

## Areas worth probing
- Login: error wording/leaks, whitespace/case handling, keyboard covering the Login button
- Back button after logout returning to an authenticated screen
- Leave date validation (end < start, past dates, overlap); balance not updating
- Attendance double check-in; location off/denied; timezone/time display
- Rotation/backgrounding mid-form losing input; no-network handling; endless spinners
- Text truncation on small screens; inconsistent date formats

## Template
```
ID:            BUG-001
Title:         <short, specific>
Module:        <Login / Attendance / Leave ...>
Environment:   <device/emulator, Android version, app version>
Severity:      Critical | Major | Minor | Trivial
Priority:      P1 | P2 | P3
Preconditions: <state before starting>
Steps to reproduce:
  1.
  2.
  3.
Expected result:
Actual result:
Evidence:      evidence/screenshots/BUG-001.png / evidence/videos/BUG-001.mp4
Notes:         <frequency, workaround, related TC ID>
```

## Bug Log
| ID | Title | Module | Severity | Linked TC | Evidence |
|---|---|---|---|---|---|
| BUG-001 | | | | | |
| BUG-002 | | | | | |
| BUG-003 | | | | | |
| BUG-004 | | | | | |
| BUG-005 | | | | | |
