# Home Ready UK: landing-page smoke test plan (DRAFT, nothing live)

## Variants (separate URLs, `noindex`)
| URL | Headline | Message from the report |
|---|---|---|
| /a/ | Be ready for a power cut in 20 minutes | Report variant B ("in 20 minutes"; the brief's "10 minutes" isn't the report's figure, so 20 is used) |
| /b/ | Get ready once. Waste nothing. | Report variant C (answers the 25% "out of date" barrier [S1]) |
| /c/ | Help an older relative get ready | Report positioning: older relatives and carers |

All three link to the same free calculator, plan and guides, and have the same sign-up form and the same honest "what might come later" note (no features exist and no prices are set; the core stays free). The report's "fake door" price button (e.g. "App, £5.99 one-off: notify me") is left out until Phil approves showing a price.

## Split
- Run all three **at the same time** (not one after another), so weather and outage news hit them equally.
- Rotate which link goes in which post/group. Give each channel its own variant link, and track the channel by referrer in GoatCounter (cookieless). Check whether it keeps `?utm_source=` query strings before relying on them; unverified.
- Each form sends a hidden `tag=variant-a|b|c` so sign-ups can be counted per variant in the email tool.
- Measure: visits per variant (GoatCounter path count), confirmed sign-ups per variant (double opt-in confirmed only), and calculator visits from each variant (referrer).
- Go/no-go thresholds come from Section 9 of the report; don't change them after the fact.
- Small numbers: treat differences under about 2:1 with fewer than ~100 visits per variant as noise.

## Tool evaluation (no accounts created)
| Need | Option | Free tier (checked 15 Oct 2026) | Cookies on our site | Notes |
|---|---|---|---|---|
| Email sign-up | **Buttondown (recommended)** | Free for the first 100 subscribers | None (plain HTML form POST, no script) | Double opt-in mandatory by default. US-based, so it is a UK GDPR international transfer; check its DPA. |
| Email sign-up | MailerLite | 250 active subscribers, 2,500 emails/30 days (cut from 500 in June 2026) | Embed normally loads their script | EU-based (Lithuania). Double opt-in on by default. Good backup if we pass 100 sign-ups. |
| Email sign-up | Google Form / Tally free | Unlimited responses | Embedded forms set Google/Tally cookies; a link out avoids this | No double opt-in, no unsubscribe or sending. Fine for the survey, poor for a mailing list. |
| Visits | **GoatCounter (recommended)** | Free for "reasonable public usage", including personal and small-business sites | None; no IP or user ID stored | Can count with a no-JS pixel. Donations welcome; open-source, so it can be self-hosted. |
| Visits | Cloudflare Web Analytics | Free | None (cookieless beacon) | Simplest if hosting on Cloudflare Pages; less granular per-path/referrer reporting. |

**Recommendation:** Buttondown for sign-ups (no script, built-in double opt-in, 100 free is enough for a 6-week test; move to MailerLite if we pass it) and GoatCounter for visits. Both are placeholders in the code (`FORM_ACTION` and `GOAT` in build.py) and do nothing until switched on.

## Privacy
Draft at `/privacy.html`, with placeholders for controller name, contact, address and retention periods. The ICO data protection fee may apply to a controller that processes personal data; Phil should check at ico.org.uk before going live (not checked here).
