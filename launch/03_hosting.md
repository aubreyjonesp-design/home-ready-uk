# Free hosting recommendation (nothing created)

**Recommended: GitHub Pages, new public repo `home-ready-uk` under `aubreyjonesp-design`.** It's free for public repos and the site is already plain static files with no build step. URL: `https://aubreyjonesp-design.github.io/home-ready-uk/` (all links are relative, so they work in a sub-folder). HTTPS is free. GitHub may keep server logs; it sets no cookies on the site.

Steps (only after Phil approves):
1. Create the public repo `aubreyjonesp-design/home-ready-uk` (empty).
2. Push the contents of `/workspace/prep_site/` except `launch/`, `shots/` and `build.py` (or keep build.py; it's harmless). Add an empty `.nojekyll`.
3. Settings → Pages → Deploy from branch `main`, folder `/ (root)`.
4. Fill in the privacy placeholders, connect Buttondown (`FORM_ACTION`) and GoatCounter (`GOAT`) in build.py, rebuild and push.
5. Rerun the checks against the live URL.

Alternatives: **Cloudflare Pages** (free; built-in cookieless Web Analytics; good if a domain goes on Cloudflare later) or **Netlify free** (fine, but its free-tier limits have changed often; check before use).

## Domain: not needed now
For a 6-week validation, the github.io address is enough and costs nothing. Buy a domain only if the test passes, or if Phil feels a proper address will noticeably raise trust in community groups (it may).
- homereadyuk.co.uk, homereadyuk.uk and homereadyuk.com all appeared **unregistered** in RDAP lookups on 15 Oct 2026 (this can change).
- Price: **Porkbun's .co.uk page shows US$5.66 a year (registration and renewal)**, checked 15 Oct 2026. Third-party price trackers list Cloudflare Registrar at about US$5.30 a year at cost (not checked on Cloudflare's own page; it needs a login). Roughly £4–5 a year in sterling (approximate conversion, not quoted by a registrar). .uk is a similar price.
- Nothing bought.
