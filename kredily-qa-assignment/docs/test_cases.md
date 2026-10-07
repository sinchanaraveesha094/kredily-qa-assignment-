# Test Cases – Kredily HRMS Android

Legend: P = Positive, N = Negative, E = Edge. Status: Pass / Fail / Blocked / Not Run.
**Actual and Status must be filled in after executing each case on a device.**

| ID | Module | Type | Scenario | Steps | Expected Result | Actual | Status |
|---|---|---|---|---|---|---|---|
| TC01 | Login | P | Login with valid credentials | Open app → enter valid email/password → tap Login | Dashboard opens; user name shown | | Not Run |
| TC02 | Login | N | Wrong password | Valid email + wrong password → Login | Error message; stays on login | | Not Run |
| TC03 | Login | N | Unregistered email | Unknown email + any password → Login | Error message; no account-existence leak | | Not Run |
| TC04 | Login | N | Both fields empty | Tap Login with blank fields | Validation messages; no crash | | Not Run |
| TC05 | Login | N | Empty password only | Valid email, blank password → Login | "Password required" validation | | Not Run |
| TC06 | Login | N | Malformed email (`abc@`) | Enter malformed email → Login | Format validation or auth failure, no crash | | Not Run |
| TC07 | Login | E | Leading/trailing spaces in email | `" email "` + valid password | Trimmed and logged in, or clear error | | Not Run |
| TC08 | Login | E | Email in different case | `PEOPLEKREDILY1@YOPMAIL.COM` + valid password | Login succeeds | | Not Run |
| TC09 | Login | E | Special chars / SQL string | `' OR 1=1 --` in both fields | Rejected; no crash, no bypass | | Not Run |
| TC10 | Login | P | Password masking / show-hide toggle | Type password; tap eye icon if present | Masked by default; toggle works | | Not Run |
| TC11 | Session | P | Session persists after restart | Login → kill app → reopen | Still logged in (or defined behaviour) | | Not Run |
| TC12 | Session | P | Logout | Profile/menu → Logout | Returns to login; Back does not reopen session | | Not Run |
| TC13 | Dashboard | P | Dashboard loads key widgets | Login → inspect home | Attendance, leave, etc. render; no spinner hang | | Not Run |
| TC14 | Dashboard | E | No network | Login → airplane mode → refresh | Friendly offline message; no crash | | Not Run |
| TC15 | Attendance | P | Check-in | Attendance → Check In (grant location) | Success message; time recorded | | Not Run |
| TC16 | Attendance | N | Check-in with location denied | Deny location → Check In | Clear permission message | | Not Run |
| TC17 | Attendance | E | Double check-in / check-out first | Tap Check In twice; or Check Out first | Blocked or handled with message | | Not Run |
| TC18 | Leave | P | View balance and apply leave | Leave → Apply → valid type/dates/reason → Submit | Request created as Pending; balance consistent | | Not Run |
| TC19 | Leave | N | End date before start date | Apply leave with To < From | Validation error; cannot submit | | Not Run |
| TC20 | Leave | E | Overlapping / exceeding-balance leave | Apply on already-requested dates / too many days | Blocked with message (or LOP warning) | | Not Run |
