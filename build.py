# Generates the static pages. Run: python3 build.py
import os
CHECKED="15 October 2026"
PLAN_DOCX="https://prepare.campaign.gov.uk/wp-content/uploads/sites/196/2025/09/HMG-Household_Emergency_Plan_WORD-1.docx"
P="https://prepare.campaign.gov.uk"
def page(path,title,body,desc,bodyclass=""):
    depth=path.count("/"); r="../"*depth
    nav=[("index.html","Home"),("calculator.html","Kit calculator"),("plan.html","Household plan"),("guides/index.html","Guides"),("about.html","About and trust")]
    links="".join(f'<li><a href="{r}{h}"{" aria-current=\"page\"" if h==path else ""}>{t}</a></li>' for h,t in nav)
    html=f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Home Ready UK</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{r}assets/style.css">
</head>
<body{f' class="{bodyclass}"' if bodyclass else ''}>
<a class="skip" href="#main">Skip to main content</a>
<header class="site"><div class="wrap">
<a class="brand" href="{r}index.html">Home Ready UK</a>
<nav aria-label="Main"><ul>{links}</ul></nav>
</div>
<p class="indep"><strong>Independent. Not part of the UK Government.</strong> We follow the official advice at <a href="{P}/">GOV.UK Prepare</a>.</p></header>
<main id="main" tabindex="-1"><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<p><strong>In danger now? Call 999.</strong> Power cut: call 105 (England, Scotland, Wales) or 03457 643643 (Northern Ireland). Smell gas: call 0800 111 999 (Great Britain).</p>
<p>Home Ready UK is independent. It is not part of the UK Government, the British Red Cross or any energy or water company. We follow the official advice at <a href="{P}/">GOV.UK Prepare</a>. No cookies, no trackers, no adverts.</p>
<p><a href="{r}about.html">About, editorial and affiliate policy</a> · <a href="{r}privacy.html">Privacy</a></p>
</div></footer>
</body>
</html>
'''
    os.makedirs(os.path.dirname(path) or ".",exist_ok=True)
    open(path,"w").write(html)

def sources(items):
    return '<h2 id="sources">Sources</h2>\n<ul class="sources">'+"".join(f'<li><a href="{u}">{t}</a></li>' for t,u in items)+f'</ul>\n<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time>. Some text on this page is adapted from GOV.UK Prepare, Crown copyright, used under the <a href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/">Open Government Licence v3.0</a>.</p>'

# ---------- HOME ----------
page("index.html","Calm, simple preparation for UK homes",f'''
<h1>Get your home ready for a power cut, water cut or cold snap. Calmly.</h1>
<p class="lead">Simple steps, in plain English, that follow the official UK advice. Use what you already eat, so nothing goes to waste.</p>
<p class="note">Most emergencies in UK homes are short. A few cheap, simple things make them much easier to cope with. You can build up your kit bit by bit.</p>

<h2>Start here</h2>
<div class="cards">
<div class="card"><h3><a href="calculator.html">3-day kit and water calculator</a></h3><p>Tell us who lives with you. Get a checklist and how much water to keep. Nothing is saved.</p></div>
<div class="card"><h3><a href="plan.html">One-page household plan</a></h3><p>Write down the numbers and details you need when the lights go out. Print it for the fridge. Large print too.</p></div>
<div class="card"><h3><a href="guides/index.html">What to do guides</a></h3><p>Power cut, no water, no gas or heating, and getting extra help through the Priority Services Register.</p></div>
</div>

<h2>Why we made this</h2>
<p>In a 2026 UK Government survey, half of adults (50%) said they felt only slightly or not at all prepared for an emergency. Water was the biggest gap: only 4% had 3 or more days of bottled water at home. The most common reasons people gave were cost, not wanting things to go out of date, and not knowing what to do.<sup><a href="#s1">[1]</a></sup></p>
<p>So we keep it simple, low cost and low waste. We point you to the official advice, and help you keep it up over time.</p>

<h2>For older relatives and carers</h2>
<p>Everything here prints clearly and has a large-print version. You can fill in a plan for someone you look after, and check whether they could get free extra help from their energy and water companies through the <a href="guides/priority-services-register.html">Priority Services Register</a>.</p>

<h2 id="notify">Get a reminder now and then</h2>
<p>We plan to send a short, calm reminder a few times a year, such as “check your torch batteries before winter”. No spam.</p>
<form class="card" action="#" method="post" onsubmit="return false;" aria-describedby="todo-note">
<!-- TODO: sign-up does nothing yet. Before going live: choose a provider, double opt-in, privacy notice, Phil's approval to publish. -->
<p id="todo-note" class="todo">Not working yet. This sign-up is a placeholder (TODO) and does not send or store anything.</p>
<label for="email">Email address <span class="hint">We will only use it for reminders.</span></label>
<input type="email" id="email" name="email" autocomplete="email">
<p><button type="submit" disabled aria-disabled="true">Notify me (coming soon)</button></p>
</form>

<h2>Sources</h2>
<ol class="sources"><li id="s1">Cabinet Office, <a href="https://www.gov.uk/government/statistics/uk-public-survey-of-risk-perception-resilience-and-preparedness-2026/uk-public-survey-of-risk-perception-resilience-and-preparedness-2026-headline-findings-html">UK Public Survey of Risk Perception, Resilience and Preparedness 2026: headline findings</a> (online panel, 10,791 UK adults, published 19 August 2026). Water figure based on 3 litres per person per day.</li></ol>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time>.</p>
''',"Calm, plain-English help to get your UK home ready for power cuts, water cuts and cold weather, following GOV.UK advice.")

# ---------- CALCULATOR ----------
page("calculator.html","3-day kit and water calculator",f'''
<h1>3-day kit and water calculator</h1>
<p class="lead">Tell us who lives in your home. We will make a checklist and work out how much bottled water to keep.</p>
<p class="note">This runs only in your browser. Nothing you type is saved or sent anywhere. It works without internet once the page has loaded.</p>

<form id="calc" class="noprint" novalidate>
<fieldset><legend>Who lives with you?</legend>
<label for="adults">Adults and teenagers</label><input type="number" id="adults" min="0" max="20" value="2" inputmode="numeric">
<label for="children">Children (about 1 to 12 years)</label><input type="number" id="children" min="0" max="20" value="0" inputmode="numeric">
<label for="babies">Babies (under 1)</label><input type="number" id="babies" min="0" max="10" value="0" inputmode="numeric">
<label for="dogs">Dogs</label><input type="number" id="dogs" min="0" max="10" value="0" inputmode="numeric">
<label for="cats">Cats and other small pets</label><input type="number" id="cats" min="0" max="20" value="0" inputmode="numeric">
<label for="days">How many days? <span class="hint">GOV.UK talks about an emergency lasting “a few days”. 3 is a good start.</span></label>
<select id="days"><option>1</option><option>2</option><option selected>3</option><option>4</option><option>5</option><option>7</option></select>
</fieldset>
<fieldset><legend>Anything extra to plan for? (tick any)</legend>
<label class="check"><input type="checkbox" id="meds"> Someone takes regular medicine</label>
<label class="check"><input type="checkbox" id="power"> Someone uses medical equipment that needs power</label>
<label class="check"><input type="checkbox" id="waterdev"> Someone uses medical equipment that needs water</label>
<label class="check"><input type="checkbox" id="mobility"> Someone has limited mobility or uses a wheelchair</label>
<label class="check"><input type="checkbox" id="sensory"> Someone is deaf, has a hearing loss, or is blind or partially sighted</label>
<label class="check"><input type="checkbox" id="cognitive"> Someone has dementia, a learning disability or finds change hard</label>
<label class="check"><input type="checkbox" id="older"> Someone is older or lives alone</label>
<label class="check"><input type="checkbox" id="assist"> We have an assistance dog</label>
</fieldset>
<p><button type="submit">Make my checklist</button></p>
</form>

<div id="result" aria-live="polite" tabindex="-1"></div>

<h2>Where the water figures come from</h2>
<p>GOV.UK Prepare says there is no standard figure, because emergencies vary and people use different amounts. It says the World Health Organization recommends <strong>at least 2.5 to 3 litres of drinking water per person per day</strong> for survival, and that <strong>10 litres per person per day</strong> is more comfortable, as it also covers basic cooking and washing. You may need extra water for baby formula, medical devices and pets.<sup><a href="#sources">[1]</a></sup></p>
<p>We use 3 litres a day for the minimum. For babies we count a person’s share and remind you to keep ready-to-feed formula. Pet amounts are a rough guide only (about 1 litre a day per dog, 0.25 litres per cat or small pet); ask your vet if unsure. GOV.UK suggests buying sealed bottled water rather than filling your own containers.<sup><a href="#sources">[2]</a></sup></p>
<p>Build it up over time. Buy the food and drink you normally use, and eat the oldest first, so nothing is wasted.</p>
{sources([("1. GOV.UK Prepare: Get prepared for emergencies (emergency kit and water)",P+"/get-prepared-for-emergencies/"),("2. GOV.UK Prepare: Water supply interruptions or outages",P+"/be-informed-about-hazards/water-supply-interruptions-or-outages/"),("3. GOV.UK Prepare: Advice for disabled people and carers",P+"/get-prepared-for-emergencies/advice-for-disabled-persons-and-carers/"),("4. British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit")])}
<script src="assets/calc.js"></script>
''',"Work out how much water and what to keep for a 3-day emergency kit, using GOV.UK figures. Runs in your browser and saves nothing.")

# ---------- PLAN ----------
def plan(path,large):
    rows=lambda labels:"".join(f'<tr><th scope="row">{l}</th><td><div class="line"></div></td></tr>' for l in labels)
    other="plan.html" if large else "plan-large-print.html"
    page(path,"Household emergency plan"+(" (large print)" if large else ""),f'''
<h1>Our household emergency plan{" (large print)" if large else ""}</h1>
<p class="noprint">Fill this in by hand after printing. Keep it on the fridge or with your torch. <a href="{other}">{"Standard print version" if large else "Large print version"}</a>.</p>
<p class="noprint"><button type="button" onclick="window.print()">Print this plan</button></p>
<p class="note noprint">The UK Government has its own, fuller plan you can download: <a href="{PLAN_DOCX}">GOV.UK household emergency plan (Word document)</a>. Our page is a short, one-page version that follows it.</p>
<table><caption class="meta">Important numbers</caption><tbody>
<tr><th scope="row">Emergency</th><td>999</td></tr>
<tr><th scope="row">Power cut</th><td>105 (England, Scotland, Wales) / 03457 643643 (N. Ireland)</td></tr>
<tr><th scope="row">Smell gas</th><td>0800 111 999 (Great Britain)</td></tr>
{rows(["Water company","Energy supplier","Family or friend","Neighbour","GP / pharmacy","Home insurance (policy no.)"])}
</tbody></table>
<table><caption class="meta">Our home</caption><tbody>
{rows(["Water stop tap is","Gas shut-off is","Fuse box (consumer unit) is","Torch, radio and kit are","Meeting place if we can’t get home","Radio station and frequency","On the Priority Services Register? (who / which company)"])}
</tbody></table>
<table><caption class="meta">People who need extra help</caption><tbody>
{rows(["Name and what help they need","Regular medicines (name, dose)","Medical equipment and back-up battery"])}
</tbody></table>
<p class="meta">Check this plan every 6 months. Last checked by us: <time datetime="2026-10-15">{CHECKED}</time>. Based on <a href="{P}/get-prepared-for-emergencies/">GOV.UK Prepare</a> (Crown copyright, Open Government Licence v3.0). Home Ready UK is independent of government.</p>
''',"A printable one-page household emergency plan, with a large-print version, based on GOV.UK advice.","large" if large else "")
plan("plan.html",False); plan("plan-large-print.html",True)

# ---------- GUIDES ----------
G=[("power-cut","Power cut"),("water-outage","No water (water outage)"),("gas-heating","No gas or heating"),("priority-services-register","Priority Services Register")]
page("guides/index.html","Guides","<h1>Guides</h1><p class=\"lead\">Short, calm guides for when things stop working.</p><ul class=\"tick\">"+"".join(f'<li><a href="{s}.html">{t}</a></li>' for s,t in G)+f"</ul><p class=\"meta\">All guides last checked {CHECKED}.</p>","Short guides: power cut, water outage, gas and heating, Priority Services Register.")

page("guides/power-cut.html","Power cut: what to do",f'''
<h1>Power cut: what to do</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">Most power cuts in the UK are short and local. A little planning makes them much easier.</p>
<div class="note call"><p><strong>Report a power cut: call 105</strong> (free, England, Scotland and Wales). In Northern Ireland call 03457 643643. If someone is in danger, call 999.</p></div>
<h2>Get ready now</h2>
<ul class="tick">
<li>Keep a torch (battery or wind-up) and spare batteries where you can find them in the dark. Torches are safer than candles.</li>
<li>Keep a charged power bank for your phone, and a battery or wind-up radio.</li>
<li>Write 105 and other key numbers on paper. Your phone or internet may not work. Use our <a href="../plan.html">one-page plan</a>.</li>
<li>Keep some bottled water and food that does not need cooking, plus a tin opener.</li>
<li>Remember: gas boilers, heat pumps and home internet usually need power too.</li>
<li>If you rely on a landline or a personal alarm (telecare), ask your provider if it works in a power cut. They may offer a back-up battery.</li>
<li>If you or someone you care for could need extra help, join the <a href="priority-services-register.html">Priority Services Register</a>.</li>
<li>Find your “load block” letter at <a href="https://www.powercut105.com/">powercut105.com</a>. It would only matter in the unlikely case of planned rota power cuts.</li>
</ul>
<h2>During a power cut</h2>
<ul class="tick">
<li>Check if neighbours have power too. If only your home is off, check your fuse box (trip switches).</li>
<li>Call 105 or check <a href="https://www.powercut105.com/">powercut105.com</a> for updates.</li>
<li>Switch off things that could be dangerous when power comes back, such as cookers and heaters. Leave one light on so you know when it is back.</li>
<li>Keep the fridge and freezer closed to keep food cold for longer. See the Food Standards Agency advice on <a href="https://www.food.gov.uk/safety-hygiene/food-safety-in-a-power-cut-advice-for-consumers">food safety in a power cut</a>.</li>
<li>Wrap up warm. Check on older neighbours or anyone who lives alone.</li>
<li>Never use a barbecue, camping stove or generator indoors. They can give off carbon monoxide.</li>
</ul>
{sources([("GOV.UK Prepare: Power cuts",P+"/be-informed-about-hazards/power-cuts/"),("Power cut 105 (Energy Networks Association)","https://www.powercut105.com/"),("National Grid: Power cuts","https://www.nationalgrid.co.uk/power-cuts"),("Food Standards Agency: Food safety in a power cut","https://www.food.gov.uk/safety-hygiene/food-safety-in-a-power-cut-advice-for-consumers"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit")])}
''',"What to do before and during a power cut in the UK. Call 105.")

page("guides/water-outage.html","No water: what to do",f'''
<h1>No water: what to do</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">Water cuts are usually fixed quickly. Your water company is the best place for news if it lasts longer.</p>
<h2>Get ready now</h2>
<ul class="tick">
<li>Keep some sealed bottled water. GOV.UK says at least 2.5 to 3 litres per person per day to drink, and 10 litres per person per day to be more comfortable. Use our <a href="../calculator.html">calculator</a> to work out your amount.</li>
<li>GOV.UK suggests buying bottled water rather than filling your own containers.</li>
<li>Find out who your water company is. <a href="https://www.water.org.uk/customers/find-your-supplier">Water UK: find your supplier</a>.</li>
<li>Know where your stop tap is, so you can turn the water off if a pipe leaks.</li>
<li>If someone needs extra water for health reasons, or uses medical equipment that needs water, join your water company’s <a href="priority-services-register.html">Priority Services Register</a> and talk to their care team about a plan.</li>
<li>Rain butt water is fine for flushing the toilet, but do not drink it.</li>
</ul>
<h2>During a water outage</h2>
<ul class="tick">
<li>Check your water company’s website or social media for updates and where to collect bottled water.</li>
<li>If you are on the Priority Services Register, your water company should arrange water for you. If it doesn’t arrive, contact them.</li>
<li>Save bottled water for drinking, cooking, washing hands and making baby formula.</li>
<li>Use hand sanitiser and wet wipes to stay clean.</li>
<li>Check on neighbours who may struggle to collect water.</li>
</ul>
{sources([("GOV.UK Prepare: Water supply interruptions or outages",P+"/be-informed-about-hazards/water-supply-interruptions-or-outages/"),("GOV.UK Prepare: Get prepared for emergencies",P+"/get-prepared-for-emergencies/"),("Water UK: Find your water supplier","https://www.water.org.uk/customers/find-your-supplier"),("Discover Water (water industry information)","https://www.discoverwater.co.uk/"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit")])}
''',"What to do before and during a water outage in the UK, with GOV.UK water figures.")

page("guides/gas-heating.html","No gas or heating: what to do",f'''
<h1>No gas or heating: what to do</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<div class="note call"><p><strong>If you smell gas or think there is a leak, call 0800 111 999</strong> (free, 24 hours, Great Britain). Open doors and windows, do not use light switches or flames, and turn off the gas at the meter if you can. In Northern Ireland, use the gas emergency number on your gas bill.</p></div>
<h2>Get ready now</h2>
<ul class="tick">
<li>Have your boiler and gas appliances checked by a <a href="https://www.gassaferegister.co.uk/">Gas Safe registered engineer</a>.</li>
<li>Fit a carbon monoxide alarm that meets British or European standards (look for BS Kitemark or EN 50291).</li>
<li>Know where your gas shut-off is. Write it on your <a href="../plan.html">plan</a>.</li>
<li>Keep warm layers, blankets and hot water bottles handy.</li>
<li>Keep enough medicine and food in case it is hard to get out in cold weather.</li>
<li>If you or someone you care for would struggle without heat, join the <a href="priority-services-register.html">Priority Services Register</a>.</li>
</ul>
<h2>If your heating stops</h2>
<ul class="tick">
<li>Check whether it is just you. If your power is also off, it may be a power cut (call 105). Most boilers need electricity.</li>
<li>Stay in one room and keep the door shut. Wear layers, a hat and socks. Have warm drinks.</li>
<li>Never use a gas cooker, barbecue or camping heater to heat your home.</li>
<li>Check on older people, babies and anyone unwell. They feel the cold most.</li>
<li>Know the signs of being too cold. Call 111 for advice, or 999 in an emergency.</li>
</ul>
{sources([("GOV.UK Prepare: Cold weather, snow and ice",P+"/be-informed-about-hazards/cold-weather-snow-ice/"),("National Gas: Emergency contacts (0800 111 999)","https://www.nationalgas.com/emergency-contacts"),("Gas Safe Register","https://www.gassaferegister.co.uk/"),("Met Office: Keeping your home warm in winter","https://weather.metoffice.gov.uk/warnings-and-advice/seasonal-advice/your-home/keeping-your-home-warm-in-winter"),("British Red Cross: Prepare for emergencies","https://www.redcross.org.uk/get-help/prepare-for-emergencies")])}
''',"What to do if you lose gas or heating, and how to stay safe from carbon monoxide.")

page("guides/priority-services-register.html","Priority Services Register",f'''
<h1>The Priority Services Register</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">A free service from energy and water companies for people who need extra help, especially when supplies are cut off.</p>
<h2>Who it is for</h2>
<p>You may be able to join if, for example, you are of pensionable age, disabled, have a long-term health condition, rely on medical equipment, have young children, or need extra help for a while (such as after an operation). Check the exact rules at <a href="https://www.thepsr.co.uk/">thepsr.co.uk</a>.</p>
<h2>What you might get</h2>
<ul class="tick">
<li>Advance warning of planned power or water cuts.</li>
<li>Priority support in a power cut, or bottled water delivered in a water outage.</li>
<li>Bills and letters in large print, braille or other formats, and a password scheme so you know a caller is genuine.</li>
</ul>
<h2>How to join</h2>
<ul class="tick">
<li>Contact your <strong>energy supplier</strong> (the company you pay bills to). Not sure who it is? Look at a bill, or use <a href="https://www.findmysupplier.energy/">Find My Supplier</a>.</li>
<li>Contact your <strong>water company</strong> too. They keep a separate register. <a href="https://www.water.org.uk/customers/find-your-supplier">Find your water company</a>.</li>
<li>Your electricity network operator (the company you call on 105) can also add you.</li>
<li>Caring for someone? Ask if they are registered, and help them sign up.</li>
<li>In Scotland, see <a href="https://psrscotland.com/">PSR Scotland</a>. In Northern Ireland these are called Customer Care Registers.</li>
</ul>
{sources([("The Priority Services Register","https://www.thepsr.co.uk/"),("GOV.UK Prepare: Get prepared for emergencies (PSR section)",P+"/get-prepared-for-emergencies/"),("Find My Supplier (gas)","https://www.findmysupplier.energy/"),("Power cut 105","https://www.powercut105.com/"),("Water UK: Find your water supplier","https://www.water.org.uk/customers/find-your-supplier"),("PSR Scotland","https://psrscotland.com/")])}
''',"What the Priority Services Register is, who can join and how, for energy and water.")

# ---------- ABOUT ----------
page("about.html","About and trust",f'''
<h1>About Home Ready UK</h1>
<h2>Independent</h2>
<p>We are independent. We are not part of the UK Government, the British Red Cross, any charity, or any energy or water company. We are not paid by them. We use no Red Cross logos or emblems.</p>
<h2>What we believe</h2>
<ul class="tick">
<li><strong>No alarmism.</strong> Most emergencies are short. We don’t use countdowns, scary pictures or “disaster” language.</li>
<li><strong>Official advice first.</strong> We follow <a href="{P}/">GOV.UK Prepare</a> and link to it. If we differ, the official advice wins.</li>
<li><strong>Low cost, low waste.</strong> Build up slowly. Use what you already eat and drink, and use the oldest first.</li>
<li><strong>For everyone.</strong> Plain English, large print, easy to print, and usable with a keyboard or screen reader.</li>
</ul>
<h2>How we source and check</h2>
<ul class="tick">
<li>Every guide lists its sources and a “last checked” date.</li>
<li>We use official and expert sources: GOV.UK, energy networks (105), water companies, the Food Standards Agency and the British Red Cross.</li>
<li>We never make up figures. Survey numbers come only from the published report, with a link.</li>
<li>We aim to recheck every page at least every 6 months, and soon after official advice changes.</li>
<li>We write in our own words. Where we use GOV.UK text, it is Crown copyright, used under the <a href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/">Open Government Licence v3.0</a>.</li>
<li>Spotted a mistake? <!-- TODO: add contact address before launch --> A contact address will be added before launch.</li>
</ul>
<h2>Privacy</h2>
<p>This site uses no cookies, no trackers, no analytics and no outside fonts. The calculator runs in your browser and saves nothing. We never ask for health details.</p>
<h2>Affiliate and advertising policy</h2>
<p>We have <strong>no affiliate links and no adverts</strong> right now. If we ever add them, each one will be clearly labelled <strong>“Ad”</strong>, and they will never appear inside the core safety advice. Following our advice never requires buying anything from us.</p>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time>.</p>
''',"Who we are, our editorial policy, how we check sources, privacy and affiliate policy.")
print("built")

# ---------- SMOKE-TEST LANDING VARIANTS (/a /b /c) ----------
# TODO before publishing (needs Phil's approval):
#  1. Replace FORM_ACTION with the Buttondown embed URL once an account exists.
#  2. Uncomment the GoatCounter line (cookieless, no IP stored) once a site code exists.
FORM_ACTION="#"  # TODO e.g. https://buttondown.com/api/emails/embed-subscribe/<username>
GOAT='<!-- TODO analytics (cookieless): <script data-goatcounter="https://<code>.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script> -->'
V={
 "a":("Be ready for a power cut in 20 minutes",
      "A short, free checklist that follows the official UK advice. Find your torch, write down 105, and you are most of the way there."),
 "b":("Get ready once. Waste nothing.",
      "Keep a few days of food and water by buying what you already eat and using the oldest first. Free, simple, and based on GOV.UK advice."),
 "c":("Help an older relative get ready",
      "Simple steps, large print and a one-page plan you can fill in together, including free extra help from their energy and water companies."),
}
for k,(h,sub) in V.items():
    page(f"{k}/index.html",h,f'''
<h1>{h}</h1>
<p class="lead">{sub}</p>
<p><a class="btn" href="../calculator.html">Try the free kit and water calculator</a></p>
<p>No sign-up needed. It runs in your browser and saves nothing.</p>

<h2>What you get today, free</h2>
<ul class="tick">
<li><a href="../calculator.html">3-day kit and water calculator</a></li>
<li><a href="../plan.html">One-page household plan</a> (and <a href="../plan-large-print.html">large print</a>)</li>
<li><a href="../guides/index.html">Guides</a>: power cut, no water, no heating, Priority Services Register</li>
</ul>

<h2 id="notify">Get a calm reminder a few times a year</h2>
<form class="card" action="{FORM_ACTION}" method="post" onsubmit="return false;">
<!-- TODO: not connected. Enable only after Phil approves the email provider and publishing. -->
<p class="todo">Not working yet (TODO). This form does not send or store anything.</p>
<input type="hidden" name="tag" value="variant-{k}">
<label for="email-{k}">Email address <span class="hint">Only used for reminders. Unsubscribe any time.</span></label>
<input type="email" id="email-{k}" name="email" autocomplete="email">
<p class="hint">We will email you once to confirm. See our <a href="../privacy.html">privacy notice</a>.</p>
<p><button type="submit" disabled aria-disabled="true">Notify me</button></p>
</form>

<h2>What might come later</h2>
<p>We are testing whether people want more, such as seasonal reminders or a phone app that works without signal. <strong>None of this exists yet</strong>, and we have not set any prices. If we ever charge for anything, the core advice and calculator will stay free.</p>
{GOAT}
''',sub)
    s=open(f"{k}/index.html").read().replace('<meta name="description"','<meta name="robots" content="noindex">\n<meta name="description"')
    open(f"{k}/index.html","w").write(s)

# ---------- PRIVACY NOTICE (DRAFT) ----------
page("privacy.html","Privacy notice",f'''
<h1>Privacy notice</h1>
<p class="todo">DRAFT. Not yet reviewed. Replace every [PLACEHOLDER] before publishing.</p>
<h2>Who we are</h2>
<p>Home Ready UK is run by [CONTROLLER NAME] ("we"), the data controller. Contact: [CONTACT EMAIL], [POSTAL ADDRESS].</p>
<h2>What we collect and why</h2>
<table><thead><tr><th scope="col">What</th><th scope="col">Why</th><th scope="col">Legal basis (UK GDPR)</th><th scope="col">How long</th></tr></thead><tbody>
<tr><td>Your email address, the date you signed up, and which page you signed up on</td><td>To send occasional reminders and updates you asked for</td><td>Consent (Article 6(1)(a))</td><td>Until you unsubscribe, or [12] months after our last email if we stop the service</td></tr>
<tr><td>Survey answers (if you take our survey). We do not ask your name or health details.</td><td>To understand what would help households</td><td>Consent</td><td>Deleted [6] months after the survey closes; only summary figures kept</td></tr>
<tr><td>Anonymous visit counts (page, referrer, browser type, country). No cookies, no IP address stored.</td><td>To see which pages are useful</td><td>Legitimate interests (Article 6(1)(f))</td><td>[24] months</td></tr>
</tbody></table>
<p>The calculator runs only in your browser. What you type is never sent to us or stored.</p>
<h2>Who helps us</h2>
<ul class="tick">
<li>[EMAIL PROVIDER, e.g. Buttondown] stores email addresses and sends our emails. It may store data outside the UK under safeguards approved for UK transfers.</li>
<li>[ANALYTICS, e.g. GoatCounter] counts visits without cookies.</li>
<li>[SURVEY TOOL, e.g. Google Forms] collects survey answers.</li>
<li>[HOSTING, e.g. GitHub Pages] hosts this website and may keep short-term server logs.</li>
</ul>
<p>We never sell your data or use it for advertising.</p>
<h2>Your rights</h2>
<p>You can ask to see, correct or delete your data, or withdraw consent at any time (every email has an unsubscribe link). Contact [CONTACT EMAIL]. If you are unhappy, you can complain to the <a href="https://ico.org.uk/make-a-complaint/">Information Commissioner's Office (ICO)</a>.</p>
<p class="meta">Draft dated <time datetime="2026-10-15">{CHECKED}</time>.</p>
''',"How Home Ready UK uses your information. Draft.")
print("variants built")
