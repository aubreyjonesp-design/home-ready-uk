# Survey: Google Form build spec (DO NOT CREATE until Phil approves)

**Title:** Getting ready at home: a 4-minute survey
**Settings:** Do NOT collect email addresses. Don't limit to 1 response (that requires a Google sign-in). No "edit after submit". Show a progress bar. Use 3 sections. Target is under 5 minutes, with 15 short questions and only one free-text box.

## Intro text (section 1 description)
> Hello. I'm [Phil / Home Ready UK], an independent project (not part of the UK Government). I'm asking how UK households get ready for things like power cuts and water cuts, to help build a free, calm guide.
> It takes about 4 minutes. It is anonymous: we don't ask your name or any health details. You can stop at any time. Please don't include personal details in the free-text box.
> Privacy: answers are stored in Google Forms, used only for this research, and deleted [6] months after the survey closes. Only summary figures will be shared. Contact [CONTACT EMAIL]. Full notice: [PRIVACY URL].

**Q0 (required, checkbox):** "I am 18 or over, live in the UK and agree to take part." If it is left unticked, the form can't be submitted (required).

## Section 1: You and your home
| # | Question | Type | Options | Required |
|---|---|---|---|---|
| 1 | How prepared, if at all, do you feel your household is for a disruption lasting a few days, such as a power cut or water outage? | Multiple choice | Totally / Largely / Moderately / Slightly / Not at all / Don't know | Yes |
| 2 | In the last two years, has your home had a power cut, water outage or loss of heating lasting more than 12 hours? | Multiple choice | Yes / No / Not sure | Yes |
| 2b | Which ones? | Checkboxes | Power cut / Water outage / Loss of heating or gas | No. **Logic:** shown only if Q2 = Yes (put it in its own section; Q2 "Go to section based on answer") |
| 3 | If it happened again tomorrow, what would worry you most? (choose up to 3) | Checkboxes, response validation "Select at most 3" | No light / No heating / No water / Phone or internet / Food going off / Medication or medical equipment / Children / Pets / An older relative / Money or cash / Other | Yes |

## Section 2: What you have now
| # | Question | Type | Options | Required |
|---|---|---|---|---|
| 4 | Roughly how many litres of bottled drinking water do you have at home right now? | Multiple choice | 0 / Under 2 / 2-5 / 6-10 / 11-20 / More than 20 / Don't know | Yes |
| 5 | Which of these do you have at home? | Checkboxes | Torch / Battery or wind-up radio / Power bank / First aid kit / Cash / Paper list of numbers / Tin opener / Blankets or warm layers / None of these | Yes |
| 6 | Have you heard of the Priority Services Register? | Multiple choice | Yes, and registered / Yes, not registered / No | Yes |
| 7 | Do you know where your water stop tap, gas shut-off and fuse box are? | Multiple choice | All of them / Some / None | Yes |
| 8 | What has stopped you doing more to prepare? | Checkboxes | Cost / Things going out of date / Not knowing what to do / Stressful to think about / Space / Time / Don't think it's needed / Other | No |
| 9 | Where would you go first for advice on preparing? | Multiple choice | GOV.UK / Council / British Red Cross / News / Social media / Friends or family / Search engine / Other | Yes |

## Section 3: What would help
| # | Question | Type | Options | Required |
|---|---|---|---|---|
| 10 | Which would you be most likely to use? | Multiple-choice grid (rows = items, columns = 1st, 2nd, 3rd, 4th, 5th; "Limit to one response per column") | Free online checklist / Printable plan for the fridge / Phone app that works without signal / Short email course / Printed book | No |
| 11 | How important is it that a tool works with no internet or mobile signal? | Multiple choice | Very / Fairly / Not very / Not at all | Yes |
| 12 | Would you be comfortable storing a list of household medicines in an app if it stayed only on your phone? | Multiple choice | Yes / Only if it stayed on my phone / No / Not sure | No |
| 13 | Have you ever paid for a household-planning or checklist app or printable? | Multiple choice + "Other" (as "Yes, please say what") | No / Other: | No |
| 14 | If a calm, UK-specific preparedness app did everything you ticked, what is the most you'd pay as a one-off? | Multiple choice | £0 / £1-£3 / £4-£7 / £8-£15 / More than £15 | No |
| 15 | Has any preparedness advice you've seen felt alarmist, confusing or unhelpful? | Paragraph | (free text, ask for no personal details) | No |

**Confirmation message:** "Thank you. For the official advice, visit GOV.UK Prepare: https://prepare.campaign.gov.uk/ . Our free calculator: [SITE URL]/calculator.html". Ending with GOV.UK/Prepare mirrors the Cabinet Office survey.
**Optional mailing list:** no email field in the form. Link to the site's sign-up instead, so survey answers stay anonymous.
**Quotas to watch (from the report):** renters vs owners, flats, 65+, carers, households with children, people relying on medical equipment. If Phil wants to track these, add 2 optional demographic questions (age band; owner/renter/other). That's still under 5 minutes, but it's his call. Target 150+ responses.
