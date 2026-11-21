# Figma completion instructions

These frames and links are pending. Open the [editable design](https://www.figma.com/design/sUCAuJ5j1WEXdGBJKSc8QJ) with the Figma account that has edit access. Keep the existing launcher, role workspaces and working journeys. The existing prototype uses synthetic sample data.

1. In the Layers panel, duplicate a role workspace or calendar frame for each group below. Move copies into free canvas space, rename them as listed, and keep the existing 900 px-wide layout, dark TutorBridge header, light surface, white content card, and primary/secondary button styles. Use vertical auto layout in the card. Remove any inherited text, personal details and interactions that are irrelevant to the new state.
2. Place the heading and helper text above the form or state message. Place the primary action first and recovery actions next. Keep demo controls labelled `Preview …` so they are visibly distinct from product actions.
3. For every button below, select its button layer, open **Prototype**, add **On click → Navigate to**, and choose the specified target. Inspect interactions copied from the template and remove obsolete ones. Keep **Start** as the existing entry point and add **Sign in** and **Create account** buttons to it.
4. Open **Present** from Start and run the walkthroughs below. Record which paths actually worked before changing the Issue checklist.

## Account entry and recovery

| New frame | Card layout and English copy | Buttons and destinations |
| --- | --- | --- |
| Sign in | Heading **Sign in to TutorBridge**. Stack **Email address** and **Password** fields. Helper **Use the email address on your account.** Use two explicitly labelled demo account presets to simulate the stored role. The production sign-in form does not ask the user to choose a role. | **Demo teacher account** → Sign in loading (teacher); **Demo student account** → Sign in loading (student); **Preview invalid credentials** → Sign in error; **Create account** → Create account. |
| Sign in loading — teacher / student | Make a separate frame per role with **Signing in…** and **Checking your account.** Keep submission inactive. | **Continue demo** → existing **T Home** / **S Home**, respectively. In production, navigate only after reading and validating the stored profile role. |
| Sign in error | Same field order. Inline error **Email or password is incorrect.** Preserve the sample email only. | **Try again** → Sign in; **Create account** → Create account. |
| Create account | Heading **Create your TutorBridge account**. Stack **Full name**, **Email address**, **Account role** (Teacher / Student), **Password**, **Confirm password**. Helper **Use 12–128 characters.** | **Create teacher demo account** or **Create student demo account** → corresponding Account created frame; **Preview password error** → Registration error; **Sign in** → Sign in. |
| Registration error | Duplicate account form. Inline copy **Use 12–128 characters for your password.** Keep the non-password fields. | **Edit details** → Create account. |
| Account created — teacher / student | Two confirmation frames. Heading **Account created** and helper **Sign in to open your workspace.** | **Sign in** → Sign in. During the demo, select the sample account matching the registration scenario; production uses the stored role for routing. |
| Session expired | Neutral header and message-only card. Heading **Your session expired** and helper **Sign in again to continue. No unfinished action will be sent automatically.** | **Sign in again** → Sign in. Add **Preview expired session** on both calendars and the student assignment detail. After sign-in, go to the role workspace; require deliberate re-entry for writes. |
| Access denied — student | Message-only card. Heading **You can’t access this item** and helper **Open Assignments to return to work shared with your account.** Omit protected titles, names, filenames and URLs. | **Back to assignments** → existing **S Homework**. Add **Preview access denied** to the assignment list and **Preview download denied** to the assignment detail, both pointing here. |

## Calendar states for both roles

Duplicate the corresponding **T Calendar** or **S Calendar** for each row. Keep their role header, timezone and existing lesson navigation. Create separate targets per role so recovery always stays in the correct workspace.

| New frame | Card layout and English copy | Buttons and destinations |
| --- | --- | --- |
| Calendar filters | Place a filter row above results: **From**, **To**, **Status**. Status options: **Any status**, **Pending**, **Approved**, **Rejected**, **Cancelled**. Add **Times shown in Europe/Istanbul (UTC+03:00).** Sample matching preset: 26–27 November, Pending. Empty preset: 28–29 November, Approved. | Existing calendar **Filters** → matching filter form; **Apply filters** → Calendar loading (match); **Preview no matches** → Calendar loading (empty); **Preview failed request** → Calendar loading (failure); **Preview invalid range** → Calendar invalid range; **Clear filters** → original unfiltered role calendar. |
| Calendar invalid range | Duplicate filter form, preserve dates. Show **From must be earlier than To.** under the date row. Date bounds may be omitted; use offset-aware instants and the SRS overlap rule. | **Edit dates** → Calendar filters; **Clear filters** → original role calendar. |
| Calendar loading — match / empty / failure | Duplicate per outcome. Heading **Loading lessons…**, helper **Your selected filters are still applied.** Show muted placeholder rows and disable repeated Apply. | **Continue demo** → Calendar results, Calendar empty, or Calendar retry respectively. |
| Calendar results | Keep filter summary and show Thursday’s pending booking with the correct participant and time. | **Clear filters** → original role calendar; **Edit filters** → Calendar filters; **Open lesson** → the role’s existing pending booking detail. |
| Calendar empty | Same filter summary. Heading **No lessons match these filters** with helper **Choose another date range or clear the filters.** | **Clear filters** → original role calendar; **Edit filters** → Calendar filters. |
| Calendar retry | Keep the filter summary. Heading **Couldn’t load lessons** and helper **Your filters are saved. Try again.** | **Retry** → Calendar loading (match), retaining the selected preset; **Edit filters** → Calendar filters. |

## Present-mode checks for Toprak

- Register a teacher and a student, exercise the password error, and sign in with each matching demo preset. Confirm the destination uses the corresponding stored role scenario.
- In each calendar, apply date/status filters, see loading and results, then try no matches, invalid range, clear filters and retry after failure.
- Open an expired-session example and sign in again. Confirm it reaches the role workspace without rerunning an unfinished write. Open denied metadata and file examples and confirm recovery goes to Assignments without displaying protected details.
- Walk the existing invitation, lesson decision/cancellation and assignment preview journeys. Check reviewer access from your own account.
