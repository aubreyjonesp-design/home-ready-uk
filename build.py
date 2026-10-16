# Generates the static pages. Run: python3 build.py
import os
CHECKED="15 October 2026"
CHECKED_ISO="2026-10-15"
SITE="https://aubreyjonesp-design.github.io/home-ready-uk/"
PAGES=[]
FORM_ACTION="https://buttondown.com/api/emails/embed-subscribe/homereadyuk"  # Buttondown, double opt-in
GOAT='<script data-goatcounter="https://homereadyuk.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'  # cookieless, no IPs stored
def signup(tag,uid,r):
    return f'''<form class="card" action="{FORM_ACTION}" method="post">
<input type="hidden" name="embed" value="1">
<input type="hidden" name="tag" value="{tag}">
<label for="{uid}">Email address <span class="hint">Only used for reminders. Unsubscribe any time.</span></label>
<input type="email" id="{uid}" name="email" autocomplete="email" required>
<p class="hint">By signing up you agree to us emailing you as described in our <a href="{r}privacy.html">privacy notice</a>. We will send you a confirmation email first. Please click the link in it to finish signing up.</p>
<p><button type="submit">Notify me</button></p>
</form>'''
PLAN_DOCX="https://prepare.campaign.gov.uk/wp-content/uploads/sites/196/2025/09/HMG-Household_Emergency_Plan_WORD-1.docx"
P="https://prepare.campaign.gov.uk"
def page(path,title,body,desc,bodyclass=""):
    depth=path.count("/"); r="../"*depth
    nav=[("index.html","Home"),("calculator.html","Kit calculator"),("plan.html","Household plan"),("guides/index.html","Guides"),("about.html","About and trust")]
    url=SITE+("" if path=="index.html" else path.replace("index.html",""))
    art=path.startswith("guides/") and path!="guides/index.html"
    import json
    if path=="index.html": j={"@context":"https://schema.org","@type":"WebSite","name":"Home Ready UK","url":SITE,"inLanguage":"en-GB","description":desc}
    elif art: j={"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"url":url,"inLanguage":"en-GB","dateModified":CHECKED_ISO,"author":{"@type":"Organization","name":"Home Ready UK"},"publisher":{"@type":"Organization","name":"Home Ready UK"},"mainEntityOfPage":url}
    else: j=None
    gsv='<meta name="google-site-verification" content="sUd5YCAQW63Z3yPZjdy5cawJS1ivCue-UsI5S-QF3aw" />\n' if path=="index.html" else ""
    ld=f'<script type="application/ld+json">{json.dumps(j,ensure_ascii=False)}</script>\n' if j else ""
    if not path.startswith(("a/","b/","c/")): PAGES.append(url)
    links="".join(f'<li><a href="{r}{h}"{" aria-current=\"page\"" if h==path else ""}>{t}</a></li>' for h,t in nav)
    html=f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Home Ready UK</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
{gsv}<meta property="og:type" content="{'article' if art else 'website'}">
<meta property="og:site_name" content="Home Ready UK">
<meta property="og:locale" content="en_GB">
<meta property="og:title" content="{title} | Home Ready UK">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
{ld}<link rel="stylesheet" href="{r}assets/style.css">
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
<p>Home Ready UK is independent. It is not part of the UK Government, the British Red Cross or any energy or water company. We follow the official advice at <a href="{P}/">GOV.UK Prepare</a>. No cookies, no adverts. We count visits without identifying anyone.</p>
<p><a href="{r}about.html">About, editorial and affiliate policy</a> · <a href="{r}privacy.html">Privacy</a></p>
</div></footer>
{GOAT}
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
{signup("home","email","")}

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
<tr><th scope="row">Flooding</th><td>Floodline 0345 988 1188 (England, Scotland, Wales) / Flooding Incident Line 0300 2000 100 (N. Ireland)</td></tr>
<tr><th scope="row">NHS advice</th><td>111</td></tr>
{rows(["Water company","Energy supplier","Family or friend","Neighbour","GP / pharmacy","Home insurance (policy no.)"])}
</tbody></table>
<table><caption class="meta">Our home</caption><tbody>
{rows(["Water stop tap is","Gas shut-off is","Fuse box (consumer unit) is","Torch, radio, kit and cash are","Meeting place if we can’t get home","Radio station and frequency","On the Priority Services Register? (who / which company)"])}
</tbody></table>
<table><caption class="meta">People who need extra help</caption><tbody>
{rows(["Name and what help they need","Regular medicines (name, dose)","Allergies (who, what)","Medical equipment and back-up battery"])}
</tbody></table>
<table><caption class="meta">Supplies and seasonal checks</caption><tbody>
{rows(["First aid kit and medicines list are kept","Food store is kept (next date check)","Water butt (not for drinking) is","Flood warnings signed up? Grab bag is","Cold weather: who we check on","Hot weather: coolest room / who we check on"])}
</tbody></table>
<p class="meta">Check this plan every 6 months. Last checked by us: <time datetime="2026-10-15">{CHECKED}</time>. Based on <a href="{P}/get-prepared-for-emergencies/">GOV.UK Prepare</a> (Crown copyright, Open Government Licence v3.0). Home Ready UK is independent of government.</p>
''',"A printable "+("large-print " if large else "")+"household emergency plan for numbers, medicines, first aid, food, flooding, cold and hot weather, based on GOV.UK advice.","large" if large else "")
plan("plan.html",False); plan("plan-large-print.html",True)

BTHC="https://www.gov.uk/government/publications/beat-the-heat-resources-for-hot-weather/beat-the-heat-keep-cool-at-home-checklist"
CIBSE="https://www.cibse.org/policy-advocacy/news/how-to-keep-your-space-cool-during-a-heatwave-with-cibses-practical-advice-for-residents-and-homeowners/"
def ready(h,items,intro="Do these now, while things are calm. Each one only takes a few minutes or a small cost."):
    return f'<div class="card"><h2 id="get-ready">{h}</h2><p>{intro}</p><ul class="tick">'+"".join(f"<li>{i}</li>" for i in items)+"</ul></div>\n"
R={}
R["extreme-heat"]=ready("Get ready before summer",[
"<strong>Find your coolest room.</strong> Note which rooms stay coolest on a warm day, usually away from the sun. UKHSA says to move to a cooler part of the house, especially for sleeping.",
"<strong>Fit or check blinds and curtains</strong> on sunny windows, especially south, east and west facing. UKHSA suggests internal blinds or curtains. CIBSE says reflective films on windows can also help.",
"<strong>Shade windows from the outside if you can.</strong> UKHSA says external shutters, roller blinds or awnings are very effective, and plants outside can shade south-facing windows. CIBSE says external shading works far better than inside blinds, and even a fabric screen fixed outside a window helps.",
"<strong>Check your fan works in spring</strong>, or buy one before demand rises. Remember UKHSA’s advice: use fans only when the air is below 35°C, and do not aim them straight at your body.",
"<strong>Get an indoor thermometer.</strong> The NHS says to check the temperature of rooms, especially where people at higher risk live and sleep.",
"<strong>Check how your medicines must be stored.</strong> UKHSA says some must be kept below 25°C or in the fridge. Ask your pharmacist if you are unsure, and keep taking them unless told otherwise.",
"<strong>Get a refillable water bottle for each person</strong>, and keep some sealed bottled water in case hot weather affects water supplies (see our <a href=\"water-outage.html\">no water guide</a>).",
"<strong>Pack a summer kit:</strong> sunscreen of at least SPF 30 with 4 or 5 star UVA protection (UKHSA, citing the NHS), wide-brimmed hats, sunglasses, light loose clothes, and a spray bottle or cold packs for cooling skin.",
"<strong>Agree who you will check on</strong>, such as an older neighbour or relative, and how (a call or a visit each day in hot weather). Ask someone to check on you if you are at higher risk.",
"<strong>Sign up for warnings.</strong> Use the Met Office app to set alerts for your area, or subscribe to Met Office email alerts on the <a href=\"https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings\">warnings page</a>. In England, <a href=\"https://www.gov.uk/guidance/weather-health-alerting-system\">register for UKHSA Heat-Health Alerts</a>.",
"<strong>Plan shade and water for pets.</strong> Dogs Trust says make sure your dog has shade and plenty of fresh water all day.",
"<strong>Fit a water butt before a dry spell.</strong> During a hosepipe ban, water companies such as Essex &amp; Suffolk Water say you can still use collected rainwater. See our <a href=\"rainwater.html\">rainwater guide</a>.",
"<strong>Plan travel and work around hot days.</strong> GOV.UK Prepare says allow extra time for journeys, as heat can damage roads and slow trains, and take extra water. Plan active jobs for early morning or evening.",
"<strong>Think longer term.</strong> If your home overheats (for example a top-floor flat or windows that barely open), GOV.UK Prepare says contact your local council, letting agency or Citizens Advice. The NHS says council environmental health teams can inspect a rented home for excess heat. If you are insulating or refurbishing, UKHSA says ask installers about reducing overheating. New homes in England must meet <a href=\"https://www.gov.uk/government/publications/overheating-approved-document-o\">Building Regulations Part O (overheating)</a>."])
R["food-storage"]=ready("Get ready now",[
"<strong>Add a few extra tins and packets</strong> of food you already eat to your next shop. Put them at the back of the cupboard.",
"<strong>Keep a manual tin opener</strong> with your store (British Red Cross).",
"<strong>Buy a fridge thermometer.</strong> The FSA says it tells you if your fridge has got too warm in a power cut.",
"<strong>Find a clean box with a lid</strong> for storing food outside in cold weather if the power goes off (FSA).",
"<strong>Keep your freezer well filled.</strong> The FSA says a full freezer stays frozen for longer than a half-full one.",
"<strong>If you have a baby</strong>, keep some ready-to-feed formula (GOV.UK Prepare). <strong>If you have pets</strong>, keep a few days of their food.",
"<strong>Set a reminder</strong> every few months to check dates and move older food to the front."])
R["flooding"]=ready("Get ready now",[
"<strong>Check your flood risk</strong> using the links below for your nation.",
"<strong>Sign up for free flood warnings</strong> (England, Scotland, Wales), online or by calling Floodline on 0345 988 1188.",
"<strong>Write your flood plan</strong>: who to call, where you would go, and how to turn off gas, electricity and water. Use the GOV.UK personal flood plan or our <a href=\"../plan.html\">household plan</a>.",
"<strong>Pack a grab bag</strong>: medicines, first aid kit, torch, bottled water, warm waterproof clothes, baby items and copies of documents.",
"<strong>Put documents in sealed waterproof bags</strong> and keep valuables upstairs or up high (GOV.UK Prepare).",
"<strong>Check your home insurance covers flooding</strong>, and write the policy number and helpline on your plan.",
"<strong>Save key numbers</strong>, such as your council, insurer and utilities (nidirect suggests a list of useful contacts).",
"<strong>Tell neighbours</strong>, especially older or vulnerable people, and join the <a href=\"priority-services-register.html\">Priority Services Register</a> if you need extra help."])
R["cold-weather"]=ready("Get ready now",[
"<strong>Book a boiler and heating check</strong> with a Gas Safe registered engineer before winter (GOV.UK Prepare, British Red Cross).",
"<strong>Fit or test a carbon monoxide alarm</strong> that meets British or European Standards (BS Kitemark or EN 50291) (GOV.UK Prepare).",
"<strong>Find your stop tap and check it works.</strong> The Met Office says check it every six months, and insulate pipes in the loft and other cold spots.",
"<strong>Keep a WaterSafe plumber’s number</strong> by the boiler or stop tap (Met Office).",
"<strong>Draught-proof doors and windows</strong> with draught excluders or by sealing small gaps (UKHSA, British Red Cross).",
"<strong>Stock up on medicines and food</strong> in case it is hard to get out, and agree who could fetch them for you (GOV.UK Prepare).",
"<strong>Get a snow shovel and some grit</strong> (the Red Cross says sand or cat litter also works).",
"<strong>Pack a car winter kit</strong>: torch, phone charger, warm clothes and blankets, high-visibility clothing, jump leads, food and drink, a snow shovel and a first aid kit (GOV.UK Prepare).",
"<strong>Get your flu and COVID-19 vaccines</strong> if you are eligible.",
"<strong>Sign up for warnings:</strong> Met Office app alerts, and UKHSA Cold-Health Alerts in England.",
"<strong>Check you are getting the help you are entitled to</strong> with heating costs (below), and join the <a href=\"priority-services-register.html\">Priority Services Register</a> if eligible."])
R["first-aid"]=ready("Get ready now",[
"<strong>Put together or check your first aid kit</strong> using the list below, and replace anything out of date.",
"<strong>Write a paper list</strong> of everyone’s medicines, allergies and GP details, and keep it with your kit or on your <a href=\"../plan.html\">plan</a>.",
"<strong>Put a small kit in the car</strong> and in your grab bag (British Red Cross).",
"<strong>Download the free British Red Cross first aid app</strong> while you have signal. It works without internet.",
"<strong>Book a free or low-cost first aid session</strong> (see the end of this page).",
"<strong>If you are deaf or cannot speak on the phone, register for emergencySMS now</strong>: text the word register to 999 (Relay UK)."])
R["rainwater"]=ready("Get ready now",[
"<strong>If you rent or own a leasehold flat, check</strong> your tenancy or lease, or ask your landlord, before fitting a water butt.",
"<strong>Fit a water butt to a downpipe</strong> on a firm, level stand, with a leaf filter and a close-fitting lid (RHS, UKHSA).",
"<strong>Make sure children cannot climb in</strong> or open the lid.",
"<strong>Label it “not drinking water”</strong> and keep bottled water for drinking (see our <a href=\"water-outage.html\">no water guide</a>).",
"<strong>Never connect it to your mains pipes</strong> (Water Regs UK).",
"<strong>Fit it before a dry spell.</strong> During a hosepipe ban, Essex &amp; Suffolk Water says you can still use collected rainwater."])

NRR="https://www.gov.uk/government/publications/national-risk-register-2026"
# ---------- GUIDES ----------
G=[("power-cut","Power cut"),("water-outage","No water (water outage)"),("gas-heating","No gas or heating"),("priority-services-register","Priority Services Register"),("grow-your-own","Grow some of your own food"),("rainwater","Collecting rainwater safely"),("first-aid","First aid at home"),("food-storage","Storing food for emergencies"),("flooding","Flooding: before, during and after"),("cold-weather","Cold weather: staying warm and well"),("extreme-heat","Extreme heat: staying safe in hot weather"),("leaving-home","Leaving home quickly, or staying inside safely"),("fire-and-carbon-monoxide","Fire and carbon monoxide safety"),("phones-internet-down","When phones and the internet are down"),("cash-and-banking","When cards and banking stop"),("storms","Storms and high winds"),("illness-at-home","Illness at home: flu, norovirus and pandemics"),("hospital-backup-plan","If you’re suddenly in hospital: a carer’s back-up plan"),("fuel-and-heating-oil","Fuel shortages and heating oil"),("run-hide-tell","Terrorism: Run, Hide, Tell")]
page("guides/index.html","Guides","<h1>Guides</h1><p class=\"lead\">Short, calm guides for when things stop working.</p><ul class=\"tick\">"+"".join(f'<li><a href="{s}.html">{t}</a></li>' for s,t in G)+f"</ul><p class=\"meta\">All guides last checked {CHECKED}.</p>","Short guides: power cut, water outage, gas and heating, Priority Services Register, growing food, rainwater, first aid, food storage, flooding, cold weather and extreme heat.")

RHSW="https://www.rhs.org.uk/garden-jobs/water-collecting-storing-and-using"
page("guides/grow-your-own.html","Grow some of your own food",f'''
<h1>Grow some of your own food</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">Growing a little food is satisfying, cuts waste and can save some money. It adds to your stored food. It does not replace it.</p>
<div class="note"><p><strong>Be realistic.</strong> Most crops take weeks or months to grow, and a garden gives most of its food in summer and autumn. Growing your own will not feed a household through a short emergency such as a power cut or a few days of bad weather. For that, keep a few days of food and water you already eat. Use our <a href="../calculator.html">kit and water calculator</a>.</p></div>

<h2>Easy crops for small spaces</h2>
<p>You do not need a garden. Pots, troughs and grow bags on a patio, balcony or sunny windowsill all work. The RHS suggests containers at least 45cm (18in) deep and wide where you can, otherwise you will need to water and feed more often.</p>
<ul class="tick">
<li><strong>Windowsill:</strong> herbs such as basil, parsley and chives, pea shoots and “cut and come again” salad leaves. Salad leaves can grow in containers only 10 to 15cm deep.</li>
<li><strong>Balcony or patio pots:</strong> tomatoes, chillies, dwarf beans, radishes, beetroot, carrots in a deep pot, spinach, chard and lettuce.</li>
<li><strong>Bigger pots or a small bed:</strong> potatoes in a large bag or tub, runner beans up a cane, courgettes.</li>
<li>Use peat-free compost and pots with drainage holes. Pots dry out quickly, so water often in summer. Collected rainwater is ideal for established plants (see our <a href="rainwater.html">rainwater guide</a>).</li>
<li>On a balcony, check weight limits and any rules in your lease or tenancy, and make sure pots cannot fall.</li>
</ul>

<h2>A simple UK growing year</h2>
<p>Timings vary across the UK. The north and high ground are usually a few weeks later than the south. Always check the seed packet.</p>
<table><caption class="meta">Rough guide for common easy crops</caption>
<thead><tr><th scope="col">Season</th><th scope="col">What you might do</th></tr></thead><tbody>
<tr><th scope="row">Late winter (Feb to Mar)</th><td>Plan, buy seed and compost. Sow chillies and tomatoes indoors on a warm windowsill. Chit seed potatoes.</td></tr>
<tr><th scope="row">Spring (Mar to May)</th><td>Sow salad leaves, radishes, peas, beetroot and carrots. Plant potatoes. Sow beans and courgettes indoors in late spring.</td></tr>
<tr><th scope="row">Early summer (late May to Jun)</th><td>Once frosts have passed, move tomatoes, beans and courgettes outside. Keep sowing salad every few weeks.</td></tr>
<tr><th scope="row">Summer (Jul to Aug)</th><td>Main picking season. Water regularly. Sow more salad and some winter crops, such as chard.</td></tr>
<tr><th scope="row">Autumn (Sep to Nov)</th><td>Lift potatoes and the last crops. Save seed. Store and preserve. Plant garlic.</td></tr>
<tr><th scope="row">Winter (Dec to Jan)</th><td>Little grows. Pick hardy crops such as kale and leeks. Clean pots and plan for next year.</td></tr>
</tbody></table>

<h2>Storing and preserving the harvest</h2>
<ul class="tick">
<li>Gardens often give too much at once. Share it, or store it.</li>
<li><strong>Freezing:</strong> Garden Organic says many vegetables, such as peas, beans, broccoli and leeks, freeze well if blanched in boiling water first. Tomatoes are best cooked into a sauce first. Follow the Food Standards Agency’s advice on <a href="https://www.gov.uk/government/publications/how-to-chill-freeze-and-defrost-food-safely/how-to-chill-freeze-and-defrost-food-safely">chilling, freezing and defrosting food safely</a>.</li>
<li><strong>Cool, dark storage:</strong> some crops, such as potatoes and squash, keep for a while somewhere cool, dark and dry. Check them often and use any damaged ones first.</li>
<li><strong>Jams, chutneys and pickles:</strong> use a trusted, tested recipe and clean jars. Do not guess with home bottling or canning of low-acid vegetables.</li>
<li>A freezer relies on power. In a power cut, keep it closed (see our <a href="power-cut.html">power cut guide</a>).</li>
</ul>

<h2>Allotments</h2>
<p>An allotment gives you much more space at a low yearly rent. In England and Wales, <a href="https://www.gov.uk/apply-allotment">apply through your local council</a>. GOV.UK says the council will either offer you a plot or, in many cases, add your name to a waiting list. Some lists are long, so it is worth applying early. In Scotland and Northern Ireland, contact your local council. Allotment societies and the <a href="https://thenas.org.uk/">National Allotment Society</a> can also help.</p>

<h2>Saving your own seed</h2>
<ul class="tick">
<li>Easy seeds to start with include peas, beans, lettuce and tomatoes.</li>
<li>The RHS says to save seed only from healthy plants, collect it on a dry day when it is ripe, dry it well, then store it in labelled paper envelopes in an airtight container somewhere cool and dry.</li>
<li>Seed from F1 hybrid varieties (it says on the packet) may not grow true to the parent plant.</li>
<li>Garden Organic’s <a href="https://www.gardenorganic.org.uk/what-we-do/hsl">Heritage Seed Library</a> shares older varieties with its members.</li>
</ul>

<h2>The costs</h2>
<p>Growing can save some money, especially on herbs and salad, but it is not free. You will need seeds, compost, pots and perhaps tools, canes and netting, and water in dry spells. Allotments have a yearly rent set locally. Start small with a few things you like to eat, reuse pots and containers, and swap seeds and plants with neighbours. Prices vary a lot, so we do not give figures here.</p>
{sources([("RHS: Vegetables in containers","https://www.rhs.org.uk/vegetables/containers"),("RHS: Vegetable seeds sowing guide","https://www.rhs.org.uk/vegetables/seeds-sowing"),("RHS: Grow your own","https://www.rhs.org.uk/advice/grow-your-own"),("RHS: Seed collecting and storing","https://www.rhs.org.uk/propagation/seed-collecting-storing"),("Garden Organic: Harvesting and storing vegetables","https://www.gardenorganic.org.uk/expert-advice/garden-management/harvesting-and-storage/harvesting-and-storing-vegetables"),("Garden Organic: Heritage Seed Library","https://www.gardenorganic.org.uk/what-we-do/hsl"),("Food Standards Agency (GOV.UK): How to chill, freeze and defrost food safely","https://www.gov.uk/government/publications/how-to-chill-freeze-and-defrost-food-safely/how-to-chill-freeze-and-defrost-food-safely"),("GOV.UK: Apply for an allotment","https://www.gov.uk/apply-allotment"),("National Allotment Society","https://thenas.org.uk/"),("GOV.UK Prepare: Get prepared for emergencies",P+"/get-prepared-for-emergencies/")])}
''',"Realistic help to grow some of your own food in the UK, even on a windowsill or balcony. It adds to your stored food, not replaces it.")

page("guides/rainwater.html","Collecting rainwater safely",f'''
<h1>Collecting rainwater safely</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">A water butt saves mains water and is handy for the garden and for flushing the toilet if your water goes off. But it is not drinking water.</p>
<div class="note call"><p><strong>Do not drink untreated rainwater</strong>, or use it for cooking, brushing teeth or making baby formula. Rain picks up bird and animal droppings, dirt and pollution from roofs and gutters. In a water outage, use bottled water or water from your water company. See our <a href="water-outage.html">no water guide</a>.</p></div>

{R["rainwater"]}<h2>Water butts and sizes</h2>
<ul class="tick">
<li>A water butt connects to a gutter downpipe on your house, garage, shed or greenhouse. The RHS calls a 240-litre butt “standard”. Smaller and slimline butts are available for tight spaces, and you can link several together.</li>
<li>Even a small roof collects a lot. The RHS says the roof of a small shed in dry south-east England can collect 2,500 to 3,500 litres a year.</li>
<li>Stand the butt on a firm, level stand so a watering can fits under the tap. Fit a leaf filter and a close-fitting lid.</li>
</ul>

<h2>Good uses for rainwater</h2>
<ul class="tick">
<li><strong>The garden:</strong> established plants, pots and houseplants. The RHS advises not using it on seedlings, as it may carry diseases that harm them.</li>
<li><strong>Flushing the toilet</strong> in a water outage: pour a bucket into the bowl or the cistern.</li>
<li><strong>Outdoor cleaning</strong>, such as washing the car, bikes or tools.</li>
<li>Avoid spraying stored water as a fine mist. The NHS says Legionnaires’ disease is caught by breathing in tiny water droplets containing the bacteria, and the RHS advises not to use stored water for misting or sprinklers if it is above 20°C.</li>
</ul>

<h2>What filtering and boiling do, and don’t, do</h2>
<ul class="tick">
<li><strong>Leaf filters and screens</strong> keep out leaves and debris. They do not make water safe to drink.</li>
<li><strong>Boiling</strong> kills or inactivates germs. The Drinking Water Inspectorate (DWI) says bringing water to a rolling boil kills bacteria and viruses and is effective against parasites such as Cryptosporidium.</li>
<li><strong>Boiling does not remove chemicals</strong>, dirt or pollution. Water companies issue a “do not drink” notice, rather than a “boil water” notice, when water may contain things that boiling cannot remove.</li>
<li>Not all home water filters can be relied on to remove germs. Rainwater for drinking needs proper treatment, testing and upkeep, to the standards that apply to private water supplies. That is a job for specialists, not a household water butt.</li>
<li>If you ever need to boil tap water, follow the DWI advice on <a href="https://www.dwi.gov.uk/receiving-a-boil-water-notice/">boil water notices</a>.</li>
</ul>

<h2>Is it legal?</h2>
<p>Yes. The RHS says collecting rainwater from roofs is perfectly legal in the UK. If you rent, or own a leasehold flat, check your tenancy agreement or lease, or ask your landlord or managing agent, before fitting a butt or changing gutters and downpipes.</p>

<h2>Keep it clean: algae and mosquitoes</h2>
<ul class="tick">
<li>Keep a close-fitting lid on. The RHS says this keeps out plant disease spores and discourages algae. UKHSA advises a well-fitted lid on water butts to stop mosquitoes breeding.</li>
<li>Keep gutters clear and use the water regularly so it does not sit for long.</li>
<li>Clean the butt once a year with warm water and a little washing-up liquid, and empty and clean it if it smells.</li>
<li>Empty or turn over buckets and other containers that collect rain.</li>
<li>Place butts out of direct sun if you can, to keep the water cooler.</li>
<li>Make sure young children cannot climb in or open the lid.</li>
</ul>

<h2>Keep it separate from your mains water</h2>
<ul class="tick">
<li>Never connect a water butt or rainwater pipe to your mains water pipes, even with a hose. Dirty water can flow backwards (backflow) and contaminate drinking water in your home and your neighbours’ homes.</li>
<li>Water Regs UK says other water sources such as rainwater must never be connected directly to mains drinking water, and you should tell your water company if your home has both. Mains back-up needs a proper air gap.</li>
<li>Whole-house rainwater systems that supply toilets or washing machines must meet the <a href="https://www.legislation.gov.uk/uksi/1999/1148/contents/made">Water Supply (Water Fittings) Regulations 1999</a>. Use an approved plumber and keep pipes labelled.</li>
</ul>
{sources([("RHS: Collecting, storing and reusing water",RHSW),("RHS: Managing water in your garden","https://www.rhs.org.uk/gardening-for-the-environment/water"),("Drinking Water Inspectorate: Receiving a boil water notice","https://www.dwi.gov.uk/receiving-a-boil-water-notice/"),("Drinking Water Inspectorate: Protecting your private water supply (rainwater harvesting)","https://www.dwi.gov.uk/private-water-supplies/customers-receiving-pws/protecting-your-private-water-supply/"),("South East Water: Boil water and do not drink notices","https://www.southeastwater.co.uk/help/works-and-outages/our-promise-to-you-if-your-water-supply-is-interrupted/"),("UKHSA (GOV.UK): Mosquito control","https://www.gov.uk/government/publications/mosquito-control"),("NHS: Legionnaires’ disease","https://www.nhs.uk/conditions/legionnaires-disease/"),("Water Regs UK: Connecting mains water to other water sources","https://www.waterregsuk.co.uk/topics/all-faqs/can-mains-water-supplies-be-connected-to-installations-also-supplied-by-another-alternative-source-of-water/"),("Water Supply (Water Fittings) Regulations 1999 (legislation.gov.uk)","https://www.legislation.gov.uk/uksi/1999/1148/contents/made"),("GOV.UK Prepare: Water supply interruptions or outages",P+"/be-informed-about-hazards/water-supply-interruptions-or-outages/"),("Essex & Suffolk Water: Temporary Use Ban (hosepipe ban)","https://www.eswater.co.uk/temporaryuseban")])}
''',"How to collect rainwater safely in the UK: water butts, safe uses, why it is not drinking water, and keeping it separate from mains.")

page("guides/first-aid.html","First aid at home",f'''
<h1>First aid at home</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">A simple first aid kit and a few basic steps can help while you wait for help, especially during a power cut or a cold snap. This page sums up the official advice and links to it in full.</p>
<div class="note call"><p><strong>This guide does not replace first aid training.</strong> It is a short summary of advice from the NHS, St John Ambulance and the British Red Cross. Always follow the full official page and the instructions of the 999 call handler. If someone is seriously ill or injured, call 999.</p></div>

{R["first-aid"]}<h2>Your home first aid kit</h2>
<p>You can buy a ready-made kit or put one together in a clean, waterproof box, says St John Ambulance. NHS and St John lists include:</p>
<ul class="tick">
<li>Plasters in different sizes (waterproof if possible)</li>
<li>Sterile dressings, including an eye pad</li>
<li>Roller (crêpe) bandages and a triangular bandage for a sling</li>
<li>Medical tape, safety pins, scissors and tweezers</li>
<li>Disposable gloves (latex-free if you can)</li>
<li>Cleansing wipes or antiseptic, and eyewash</li>
<li>A thermometer</li>
<li>A foil (aluminium) blanket, and a face shield for rescue breaths</li>
</ul>
<p>NHS advice also suggests a small medicine cabinet for common illnesses, such as painkillers like paracetamol or ibuprofen. Ask your pharmacist what suits your household, as medicines can interact.</p>

<h3>Storing and checking it</h3>
<ul class="tick">
<li>Keep medicines out of sight and reach of children. The NHS says a high, lockable cupboard in a cool, dry place is ideal.</li>
<li>Keep medicines in their original packs with the leaflet, and follow the dose on the pack.</li>
<li>Check expiry dates regularly. Many sterile kit items have dates too. Replace anything out of date.</li>
<li>Do not put old medicines in the bin or down the toilet. Take them to a pharmacy to be disposed of safely.</li>
</ul>

<h3>A kit for the car or a go-bag</h3>
<p>The British Red Cross suggests keeping a first aid kit in your car, and putting essential medicines, spare glasses and a paper list of emergency numbers in a small bag you can grab and go. See our <a href="../calculator.html">kit calculator</a>.</p>

<h3>A paper list of medicines and allergies</h3>
<p>Write down each person’s regular medicines (name and dose), any allergies, and their GP details. Keep it on paper at home with your kit. The NHS says paramedics find it helpful if you collect the person’s medicines and tell them about any allergies. Our <a href="../plan.html">printable household plan</a> has space for this. Nothing you write is stored on this website.</p>

<h2>Basic first aid</h2>
<p>These are short summaries. Tap each link to read the full official steps, with pictures and videos.</p>

<h3>Burns and scalds (including from candles and camping stoves)</h3>
<ul class="tick">
<li>Cool the burn under cool running water for 20 minutes, as soon as you can. If there is no running water, the NHS says you can use cool bottled water or a wet towel.</li>
<li>Remove clothing or jewellery near the burn, but not anything stuck to it.</li>
<li>Once cooled, lay cling film over it loosely. Do not wrap it round.</li>
<li>Do not use ice, creams, oils or butter, and do not burst blisters.</li>
<li>Call 999 or go to A&amp;E if the burn is large or deep, on the face, genitals or bottom, or caused by chemicals or electricity. Call 111 if you are not sure.</li>
</ul>
<p>Read more: <a href="https://www.nhs.uk/conditions/burns-and-scalds/">NHS: Burns and scalds</a> · <a href="https://www.sja.org.uk/first-aid-advice/burns-and-scalds/">St John Ambulance: Burns and scalds</a>. The NHS also warns that using camping stoves or barbecues indoors can cause carbon monoxide to build up (see below).</p>

<h3>Cuts and bleeding</h3>
<ul class="tick">
<li>Wash your hands and put on gloves if you have them.</li>
<li>Press firmly on the wound with a dressing or clean folded cloth. If something is stuck in it, do not pull it out. Press either side of it instead.</li>
<li>Raise an injured arm or leg if you can. If blood comes through, add another pad on top.</li>
<li>Call 999 if the bleeding will not stop, or blood spurts out.</li>
<li>For small cuts, clean with water, pat dry and cover with a plaster or dressing.</li>
</ul>
<p>Read more: <a href="https://www.nhs.uk/conditions/cuts-and-grazes/">NHS: Cuts and grazes</a> · <a href="https://www.sja.org.uk/first-aid-advice/severe-bleeding/">St John Ambulance: Severe bleeding</a></p>

<h3>Cold and hypothermia</h3>
<p>Signs include shivering, pale cold skin, slurred speech, slow breathing, tiredness or confusion. A baby may be cold, floppy and unusually quiet. The NHS says to go to A&amp;E or call 999 if you think someone has hypothermia. While you wait:</p>
<ul class="tick">
<li>Move them somewhere warm or sheltered. Remove wet clothes and wrap them in blankets, with their head covered.</li>
<li>If they are fully awake, give a warm non-alcoholic drink and sugary food like chocolate.</li>
<li>Stay with them. Do not use a hot bath, hot water bottle or heat lamp, do not rub their limbs, and do not give alcohol.</li>
</ul>
<p>Read more: <a href="https://www.nhs.uk/conditions/hypothermia/">NHS: Hypothermia</a> · <a href="https://www.sja.org.uk/first-aid-advice/hypothermia/">St John Ambulance: Hypothermia</a> · <a href="https://www.redcross.org.uk/first-aid/learn-first-aid/hypothermia">British Red Cross: Hypothermia</a></p>

<h3>Carbon monoxide</h3>
<p>You cannot see or smell carbon monoxide. The NHS lists symptoms including headache, dizziness, feeling or being sick, weakness, tiredness and confusion, chest and muscle pain, and shortness of breath. Symptoms may ease when you go outside.</p>
<ul class="tick">
<li>Stop using the appliance if you can, and get everyone outside into fresh air.</li>
<li>Call 111 for advice. Call 999 if someone is struggling to breathe, suddenly confused, unconscious, weak, or has chest or muscle pain.</li>
<li>Do not go back inside until you have had advice. Never use a barbecue or camping stove indoors.</li>
</ul>
<p>Read more: <a href="https://www.nhs.uk/conditions/carbon-monoxide-poisoning/">NHS: Carbon monoxide poisoning</a> · <a href="https://www.sja.org.uk/first-aid-advice/carbon-monoxide-poisoning/">St John Ambulance: Carbon monoxide poisoning</a>. See also our <a href="gas-heating.html">no gas or heating guide</a>.</p>

<h3>Choking (adults)</h3>
<ul class="tick">
<li>Ask “Are you choking?” Encourage them to cough.</li>
<li>If that fails, give up to 5 sharp back blows between the shoulder blades, while they lean forward.</li>
<li>If that fails, give up to 5 abdominal thrusts.</li>
<li>If it is still blocked, call 999 and keep repeating back blows and thrusts. If they become unresponsive, start CPR.</li>
</ul>
<p>Babies and children need different steps. Read more: <a href="https://www.sja.org.uk/first-aid-advice/choking/">St John Ambulance: Choking</a> · <a href="https://www.sja.org.uk/first-aid-advice/child-choking/">Choking child</a> · <a href="https://www.sja.org.uk/first-aid-advice/baby-choking/">Choking baby</a> · <a href="https://www.redcross.org.uk/first-aid/learn-first-aid/choking">British Red Cross: Choking</a></p>

<h3>Is someone unresponsive?</h3>
<p>St John Ambulance uses a quick check called DR ABC: Danger, Response, Airway, Breathing, Circulation. First make sure it is safe. Then gently shake their shoulders and ask loudly “Are you OK?” If they do not respond in any way, they are unresponsive. Tilt their head back and lift the chin, then look, listen and feel for normal breathing for no more than 10 seconds. Occasional gasps are not normal breathing.</p>
<p>Read more: <a href="https://www.sja.org.uk/first-aid-advice/primary-survey/">St John Ambulance: The primary survey (DR ABC)</a></p>

<h3>Not breathing normally: CPR</h3>
<ul class="tick">
<li>Call 999 (or get someone else to) and put the phone on speaker. Send a helper for a defibrillator if there is one.</li>
<li>Push hard and fast in the middle of the chest, at 100 to 120 a minute. The call handler will help you.</li>
<li>If you are trained, give 2 rescue breaths after every 30 compressions. If not, keep doing chest compressions.</li>
</ul>
<p>Read more: <a href="https://www.sja.org.uk/first-aid-advice/cpr/">St John Ambulance: How to do CPR</a> · <a href="https://www.redcross.org.uk/first-aid/learn-first-aid/unresponsive-and-not-breathing">British Red Cross: Unresponsive and not breathing</a></p>

<h3>Unresponsive but breathing: recovery position</h3>
<p>Roll them onto their side and tilt their head back, so their airway stays open and any vomit can drain. Call 999 and keep checking them until help arrives.</p>
<p>Read more: <a href="https://www.sja.org.uk/first-aid-advice/recovery-position/">St John Ambulance: Recovery position</a> · <a href="https://www.redcross.org.uk/first-aid/learn-first-aid/unresponsive-and-breathing">British Red Cross: Unresponsive and breathing</a></p>

<h3>Sprains and strains</h3>
<p>For the first 2 to 3 days, the NHS suggests PRICE: Protect, Rest, Ice (an ice pack or frozen peas in a tea towel, up to 20 minutes every 2 to 3 hours), Compression with a bandage, and Elevate. A pharmacist can advise on painkillers. Get help from 111 if it is very painful, very swollen, or you cannot put weight on it.</p>
<p>Read more: <a href="https://www.nhs.uk/conditions/sprains-and-strains/">NHS: Sprains and strains</a> · <a href="https://www.redcross.org.uk/first-aid/learn-first-aid/strains-and-sprains">British Red Cross: Strains and sprains</a></p>

<h2>999, 111 or a pharmacist?</h2>
<ul class="tick">
<li><strong>999</strong> is for life-threatening emergencies, such as someone not breathing, heavy bleeding that will not stop, or a severe burn. Tell the call handler where you are, what happened and your phone number.</li>
<li><strong>NHS 111</strong> (call 111 or use <a href="https://111.nhs.uk/">111 online</a>) is for when you need help fast but it is not life-threatening, or you are not sure whether to call 999. Call 111 for a child under 5.</li>
<li><strong>A pharmacist</strong> can advise on minor illnesses, minor injuries and medicines, with no appointment.</li>
</ul>

<h3>If you are deaf or cannot speak on the phone</h3>
<ul class="tick">
<li><strong>999 BSL:</strong> a free video relay service for deaf British Sign Language users, through the <a href="https://999bsl.co.uk/">999 BSL website or app</a>.</li>
<li><strong>Relay UK:</strong> call <strong>18000</strong> from the Relay UK app or a textphone to reach 999 through a relay assistant.</li>
<li><strong>emergencySMS:</strong> you must register first. Text the word <strong>register</strong> to 999, then reply <strong>yes</strong> when asked. In an emergency, text 999 with the service you need, what is happening and exactly where you are. Relay UK says this is slower than a call, so use it only if you have no other option. Wait for a reply before assuming it has been received. See <a href="https://www.relayuk.bt.com/how-to-use-relay-uk/contact-999-using-relay-uk.html">Relay UK: Contact 999</a>.</li>
</ul>

<h2>Learn first aid for free or at low cost</h2>
<ul class="tick">
<li><strong>British Red Cross first aid apps</strong> (free, work without internet): a general app and a baby and child app. See <a href="https://www.redcross.org.uk/first-aid/first-aid-apps">Red Cross first aid apps</a>.</li>
<li><strong>British Red Cross free workshop for adults</strong>, online or face to face, for community members and groups. Availability is currently reduced. See <a href="https://www.redcross.org.uk/get-involved/teaching-resources/community-education-workshops/first-aid-workshop-for-adults">free first aid workshop</a>.</li>
<li><strong>British Red Cross public courses</strong> (paid): four-hour courses in first aid for adults, and for babies and children. See <a href="https://www.redcross.org.uk/first-aid/book-a-first-aid-course">Red Cross first aid courses</a>.</li>
<li><strong>St John Ambulance free awareness sessions</strong> for community groups in England (at least 6 people, no certificate). See <a href="https://www.sja.org.uk/first-aid-awareness-sessions/">St John free sessions</a>. St John’s first aid app has been withdrawn, so use their <a href="https://www.sja.org.uk/first-aid-advice/">first aid advice pages</a> instead.</li>
</ul>
{sources([("NHS: Burns and scalds","https://www.nhs.uk/conditions/burns-and-scalds/"),("NHS: Cuts and grazes","https://www.nhs.uk/conditions/cuts-and-grazes/"),("NHS: Hypothermia","https://www.nhs.uk/conditions/hypothermia/"),("NHS: Carbon monoxide poisoning","https://www.nhs.uk/conditions/carbon-monoxide-poisoning/"),("NHS: Sprains and strains","https://www.nhs.uk/conditions/sprains-and-strains/"),("NHS: When to call 999","https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-call-999/"),("NHS: When to use 111","https://www.nhs.uk/nhs-services/urgent-and-emergency-care-services/when-to-use-111/"),("NHS: How pharmacies can help","https://www.nhs.uk/nhs-services/pharmacies/how-pharmacies-can-help/"),("NHS Black Country ICB: Keep a well-stocked medicine cabinet at home","https://blackcountry.icb.nhs.uk/your-health/find-right-service-you/self-care/keep-well-stocked-medicine-cabinet-home"),("St John Ambulance: What to put in a first aid kit","https://shop.sja.org.uk/pages/what-to-put-in-a-first-aid-kit"),("HSE: What to put in your first aid kit (checking expiry dates)","https://www.hse.gov.uk/simple-health-safety/firstaid/what-to-put-in-your-first-aid-kit.htm"),("St John Ambulance: First aid advice","https://www.sja.org.uk/first-aid-advice/"),("St John Ambulance: Primary survey (DR ABC)","https://www.sja.org.uk/first-aid-advice/primary-survey/"),("St John Ambulance: How to do CPR","https://www.sja.org.uk/first-aid-advice/cpr/"),("St John Ambulance: Recovery position","https://www.sja.org.uk/first-aid-advice/recovery-position/"),("St John Ambulance: Choking","https://www.sja.org.uk/first-aid-advice/choking/"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit"),("British Red Cross: Learn first aid","https://www.redcross.org.uk/first-aid/learn-first-aid"),("Relay UK: Contact 999 using Relay UK","https://www.relayuk.bt.com/how-to-use-relay-uk/contact-999-using-relay-uk.html"),("999 BSL emergency video relay","https://999bsl.co.uk/")])}
''',"First aid at home in the UK: what to keep in your kit, basic steps for burns, bleeding, cold, carbon monoxide, choking and CPR, and when to call 999 or 111.")

FSAPC="https://www.gov.uk/government/publications/food-safety-in-a-power-cut-advice-for-consumers/food-safety-in-a-power-cut-advice-for-consumers"
FFC="https://www.gov.uk/government/publications/home-food-fact-checker/home-food-fact-checker"
page("guides/food-storage.html","Storing food for emergencies",f'''
<h1>Storing food for emergencies</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">A small store of food you already eat makes a power cut, water cut or snowed-in week much easier. Build it up slowly and use it, so nothing goes to waste.</p>
<div class="note"><p>GOV.UK Prepare does not give a set amount of food to keep. It says how much you need depends on your own circumstances. It suggests food that does not need cooking, such as ready-to-eat tinned meat, fruit or vegetables, plus a tin opener.</p></div>

{R["food-storage"]}<h2>Keep a rotation store</h2>
<ul class="tick">
<li>Buy a few extra of the long-life foods you normally eat. Put new ones at the back and use the oldest first.</li>
<li>Check dates when you buy and when you put things away. The Food Standards Agency (FSA) says a <strong>use-by</strong> date is about safety, and a <strong>best before</strong> date is about quality. Food can be eaten after its best before date, but may not taste as good.</li>
<li>The British Red Cross suggests keeping 3 days’ supply of bottled water and long-life, ready-to-eat food, with a tin opener. Use our <a href="../calculator.html">kit calculator</a> for water amounts.</li>
</ul>

<h2>Tins and dried food</h2>
<ul class="tick">
<li>Tins are useful because, the FSA says, many tinned foods are safe to eat without heating. Check the label, as it depends on the product.</li>
<li>A shallow dent is usually fine. The FSA says do not eat food from a deeply dented, rusty or bulging can.</li>
<li>Once a tin is open, do not store food in it. Put leftovers in a bowl or container in the fridge.</li>
<li>Store dried and cupboard foods in a clean, dry place and follow any storage instructions on the pack.</li>
</ul>

<h2>Food that needs no cooking</h2>
<p>Electric and induction hobs will not work in a power cut. The FSA says a camping stove or barbecue can be used, but most are designed for outdoor use only. Never use them indoors, because of the risk of carbon monoxide (see our <a href="first-aid.html">first aid guide</a>). Good no-cook options include ready-to-eat tins, crackers, cereal bars, nut butter and dried fruit, if your household can eat them.</p>

<h2>Food safety in a power cut</h2>
<p>From the FSA’s power cut advice:</p>
<ul class="tick">
<li>A power cut of less than 4 hours is unlikely to affect chilled or frozen food.</li>
<li>Keep fridge and freezer doors closed. A fridge should stay cold for up to 4 hours. A full freezer should stay frozen for up to 48 hours (24 hours if half full). These are estimates and vary by appliance.</li>
<li>A fridge thermometer helps. In a power cut, food can be kept in a fridge below 8°C. If it reaches 8°C or above, throw away chilled food (such as food with a use-by date, “keep refrigerated” products and leftovers) after 4 hours, unless the power comes back within 4 hours.</li>
<li>If it is cold outside (below 8°C), you can store food outside in a clean, sealed box, out of the sun and away from animals.</li>
<li>Eat in this order: fridge food first, then defrosted food that needs no cooking, then perishable food kept at room temperature, then tins, jars and dried food.</li>
<li>Take extra care for young children, pregnant women, older people and anyone with a health condition.</li>
</ul>
<p>Never use the “sniff test” for food with a use-by date. The FSA says you cannot smell the bugs that cause food poisoning. Read the full <a href="{FSAPC}">FSA power cut advice</a>.</p>

<h2>Special diets and allergies</h2>
<ul class="tick">
<li>Store foods that everyone in your home can safely eat, and keep them separate if someone has a food allergy or coeliac disease.</li>
<li>Check labels each time you buy. The FSA says food businesses must tell you if they use any of the 14 regulated allergens.</li>
<li>If someone uses an adrenaline auto-injector, the FSA says it is important to carry it with them.</li>
<li>Write any allergies on your <a href="../plan.html">household plan</a>.</li>
</ul>

<h2>Babies</h2>
<p>GOV.UK Prepare says ready-made (“ready-to-feed”) formula is best for emergencies, because you may not be able to boil water or sterilise bottles. The FSA says making up powdered formula safely needs boiled water. The NHS says ready-to-feed formula costs more and must be used more quickly once opened. Keep nappies and wipes too.</p>

<h2>Pets</h2>
<p>GOV.UK Prepare reminds you not to forget food for pets, and says you may need extra water for them. Keep a few days of your pet’s usual food and any medicines. Ask your vet if you are unsure what your pet needs.</p>
{sources([("Food Standards Agency (GOV.UK): Food safety in a power cut",FSAPC),("Food Standards Agency (GOV.UK): Home Food Fact Checker",FFC),("Food Standards Agency (GOV.UK): Food allergy and intolerance","https://www.gov.uk/government/publications/food-allergy-and-intolerance-advice-for-consumers/food-allergy-and-intolerance-advice-for-consumers"),("GOV.UK Prepare: Get prepared for emergencies",P+"/get-prepared-for-emergencies/"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit"),("NHS: How to make up baby formula","https://www.nhs.uk/baby/breastfeeding-and-bottle-feeding/bottle-feeding/making-up-baby-formula/"),("NHS: Types of formula","https://www.nhs.uk/baby/breastfeeding-and-bottle-feeding/bottle-feeding/types-of-formula/")])}
''',"How to keep a small, low-waste food store for emergencies in the UK, and keep food safe in a power cut, following FSA and GOV.UK advice.")

page("guides/flooding.html","Flooding: before, during and after",f'''
<h1>Flooding: before, during and after</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">Flooding can happen from rivers, the sea, heavy rain and groundwater, sometimes far from a river. A little planning reduces the damage and the worry.</p>
<div class="note call"><p><strong>If you are in danger, call 999.</strong> Never walk or drive through flood water. GOV.UK Prepare says driving through flood water is the number one cause of death in floods.</p></div>

{R["flooding"]}<h2>Check your risk and get free warnings</h2>
<ul class="tick">
<li><strong>England:</strong> the Environment Agency. <a href="https://check-for-flooding.service.gov.uk/">Check for flooding</a>, <a href="https://www.gov.uk/check-long-term-flood-risk">check your long-term risk</a> and <a href="https://www.gov.uk/get-flood-warnings">sign up for free flood warnings</a>.</li>
<li><strong>Scotland:</strong> SEPA. <a href="https://beta.sepa.scot/flooding/">SEPA flooding</a> and <a href="https://myfloodline.sepa.scot/register">sign up to Floodline</a>.</li>
<li><strong>Wales:</strong> Natural Resources Wales (NRW). <a href="https://naturalresources.wales/floodwarnings?lang=en">Check flood warnings</a> and <a href="https://naturalresources.wales/flooding/sign-up-to-receive-flood-warnings/?lang=en">sign up for warnings</a>.</li>
<li><strong>Northern Ireland:</strong> there is no Floodline warning service. GOV.UK says to use flood maps to check your risk. See <a href="https://www.infrastructure-ni.gov.uk/topics/rivers-and-flooding">Department for Infrastructure: Rivers and flooding</a> and <a href="https://www.nidirect.gov.uk/articles/flooding">nidirect: Flooding</a>. To report flooding in Northern Ireland, call the <strong>Flooding Incident Line on 0300 2000 100</strong> (24 hours).</li>
</ul>
<p><strong>Floodline: 0345 988 1188</strong> (24 hours; textphone 0345 602 6340) for England, Scotland and Wales. GOV.UK lists 0345 numbers as UK-wide numbers that are charged, not free. You can sign up for warnings by phone. If you have a disability or need extra help, you can ask Floodline to send warnings to a friend or relative too. Warnings do not cover surface water (flash) flooding.</p>
<p>The warning levels are: <strong>Flood alert</strong> (be prepared), <strong>Flood warning</strong> (take action now) and <strong>Severe flood warning</strong> (danger to life).</p>

<h2>Make a flood plan</h2>
<ul class="tick">
<li>Use the <a href="https://www.gov.uk/government/publications/personal-flood-plan">GOV.UK personal flood plan</a>, or the flood section of our <a href="../plan.html">household plan</a>.</li>
<li>Know how to turn off your gas, electricity and water.</li>
<li>Agree where you would go, and how you will contact each other. Plan for pets and medicines.</li>
<li>Pack a grab bag: medicines, a first aid kit, important documents in sealed waterproof bags, a torch, bottled water, warm waterproof clothes and baby items.</li>
<li>Keep valuable and sentimental things upstairs or up high.</li>
<li>If your risk is high, look at <a href="https://www.gov.uk/prepare-for-flooding/protect-your-property">ways to protect your property</a>, such as flood barriers or air brick covers.</li>
<li>Let neighbours know about the risk, especially older or vulnerable people, and join the <a href="priority-services-register.html">Priority Services Register</a> if you need extra help.</li>
</ul>

<h2>When a flood is coming or happening</h2>
<ul class="tick">
<li>Turn off gas, electricity and water if it is safe. <strong>Do not touch electrical switches or plugs if you are standing in water.</strong></li>
<li>Move people, pets, cars and important things to safety, for example upstairs or to higher ground.</li>
<li>Put flood protection in place if you have it. Block sinks, baths and toilets, and unplug washing machines and dishwashers.</li>
<li>If the emergency services tell you to leave, leave. Delaying puts you and rescuers at risk.</li>
<li>Stay in a high place with a way out if you cannot leave.</li>
</ul>

<h2>After a flood</h2>
<ul class="tick">
<li>Only go back when the emergency services say it is safe.</li>
<li>Do not turn on gas, electricity or water until your supplier or a qualified engineer has checked them. If you smell gas, call 0800 111 999 (Great Britain).</li>
<li>Take photos and video of the damage and mark the water level on the wall. Talk to your insurer before you throw things away or start repairs.</li>
<li>Do not use tap water if it changes colour, taste or smell. Contact your water company. Do not eat food that has touched flood water.</li>
<li>GOV.UK says to throw away fridge food if the power was off for more than 4 hours, and freezer food if it was off for more than 24 hours.</li>
<li>If you rent, your landlord is responsible for repairs. If you are not insured or cannot live at home, contact your local council.</li>
</ul>

<h2>Health risks of flood water</h2>
<p>The UK Health Security Agency (UKHSA) says flood water can contain sewage and pollutants, and can hide sharp objects and open manholes. Its advice includes:</p>
<ul class="tick">
<li>Wear rubber boots, waterproof gloves and an apron when cleaning up. Cover cuts with waterproof plasters.</li>
<li>Wash your hands well with warm soapy water after touching flood water or anything it has touched. Use bottled water if your water supply is affected.</li>
<li>Clean hard surfaces with hot water and detergent. Clean and disinfect kitchen items before use, and throw away wooden boards and utensils that touched flood water. Wash fabrics at 60°C.</li>
<li>Never use petrol or diesel generators indoors, and keep heaters and dryers well ventilated, because of carbon monoxide.</li>
<li>Get gas or oil heating checked by a qualified engineer before you use it.</li>
<li>Feeling tired, anxious or unable to sleep is normal after a flood. Talk to your GP, call NHS 111, or contact the Samaritans.</li>
</ul>

<h2>Insurance basics</h2>
<ul class="tick">
<li>Check your home insurance covers flood damage, and keep the policy number on your plan.</li>
<li><a href="https://www.floodre.co.uk/">Flood Re</a> is a joint scheme between the government and insurers that helps make flood cover more affordable for homes at high risk. You buy insurance in the usual way. Your insurer can pass the flood part of the policy to Flood Re. Use the Flood Re tool to check if your home qualifies. Prices and terms are set by insurers.</li>
<li>The <a href="https://www.abi.org.uk/policy-and-guidance/general-insurance/flooding">Association of British Insurers</a> has advice on flood claims.</li>
</ul>
{sources([("GOV.UK Prepare: Flooding",P+"/be-informed-about-hazards/flooding/"),("GOV.UK: Get flood warnings by text, phone or email (Floodline)","https://www.gov.uk/get-flood-warnings"),("GOV.UK: What to do before or during a flood","https://www.gov.uk/help-during-flood"),("GOV.UK: What to do after a flood","https://www.gov.uk/after-flood"),("GOV.UK: Personal flood plan","https://www.gov.uk/government/publications/personal-flood-plan"),("GOV.UK: Call charges","https://www.gov.uk/call-charges"),("UKHSA (GOV.UK): Flooding and health: advice for the public","https://www.gov.uk/government/publications/flooding-and-health-public-advice/flooding-and-health-advice-for-the-public"),("SEPA: Flooding","https://beta.sepa.scot/flooding/"),("SEPA: Sign up to Floodline","https://myfloodline.sepa.scot/register"),("Natural Resources Wales: Check flood warnings","https://naturalresources.wales/floodwarnings?lang=en"),("Natural Resources Wales: What to do in a flood","https://naturalresources.wales/flooding/what-to-do-in-a-flood/?lang=en"),("nidirect: Flooding","https://www.nidirect.gov.uk/articles/flooding"),("nidirect: Preparing for a flood","https://www.nidirect.gov.uk/articles/preparing-flood"),("nidirect: What to do if a flood happens","https://www.nidirect.gov.uk/articles/what-do-if-flood-happens"),("Department for Infrastructure (NI): Rivers and flooding","https://www.infrastructure-ni.gov.uk/topics/rivers-and-flooding"),("Flood Re: How Flood Re works","https://www.floodre.co.uk/how-flood-re-works/"),("British Red Cross: Floods in the UK","https://www.redcross.org.uk/get-help/prepare-for-emergencies/how-to-prepare-for-floods-and-flooding")])}
''',"Flooding in the UK: free flood warnings in England, Scotland, Wales and Northern Ireland, Floodline, a flood plan, staying safe, health risks and Flood Re.")

page("guides/cold-weather.html","Cold weather: staying warm and well",f'''
<h1>Cold weather: staying warm and well</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">Cold weather can affect anyone’s health, and some people are at higher risk. A few simple steps help keep you, your home and your neighbours safe.</p>
<div class="note call"><p><strong>Hypothermia is a medical emergency.</strong> If you think someone has it, call 999 or go to A&amp;E. See our <a href="first-aid.html">first aid guide</a>.</p></div>

{R["cold-weather"]}<h2>Warnings and alerts</h2>
<ul class="tick">
<li><strong>Met Office weather warnings</strong> (yellow, amber, red) cover snow, ice, wind and rain across the UK. Red means dangerous weather is expected and you should act now. See <a href="https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings">Met Office UK warnings</a>.</li>
<li><strong>Cold-Health Alerts</strong> come from the UK Health Security Agency (UKHSA) with the Met Office. They warn when cold is likely to affect health, mainly between 1 November and 31 March. They are aimed at health and care services but anyone can view them or sign up. See the <a href="https://www.gov.uk/guidance/weather-health-alerting-system">Weather-Health Alerting System</a> and <a href="https://ukhsa-dashboard.data.gov.uk/weather-health-alerts">current alerts</a>.</li>
</ul>

<h2>Who is most at risk</h2>
<p>UKHSA lists people aged 65 and over, people with long-term health conditions, pregnant women, young children (especially aged 5 and under), people with learning disabilities, people at risk of falls, people who live alone, are housebound or have low mobility, and people in deprived circumstances.</p>

<h2>Keeping warm (UKHSA advice)</h2>
<ul class="tick">
<li>Try to heat rooms you spend a lot of time in, such as the living room or bedroom, to at least 18°C.</li>
<li>Reduce draughts, for example with draught excluders. Keep bedroom windows closed at night.</li>
<li>Wear several thin layers rather than one thick one.</li>
<li>Try not to sit still for more than an hour or so. Stretching your arms and legs helps.</li>
<li>Wear shoes with good grip when it is icy.</li>
<li>If bad weather is forecast, check you have enough medicine and food. Find someone who could fetch them if you cannot go out.</li>
<li>Get your flu and COVID-19 vaccines if you are eligible (see <a href="https://www.nhs.uk/live-well/seasonal-health/keep-warm-keep-well/">NHS winter health</a>).</li>
<li>Have heating and cooking appliances checked by a Gas Safe registered engineer, and fit a carbon monoxide alarm. See our <a href="gas-heating.html">no gas or heating guide</a>.</li>
</ul>

<h2>Frozen and burst pipes</h2>
<p>From the Met Office:</p>
<ul class="tick">
<li>Know where your stop tap is and check it works. It is often under the kitchen sink.</li>
<li>If a pipe is frozen, turn off the stop tap. Thaw it slowly with hot water bottles or towels soaked in hot water. <strong>Never use a naked flame or blowtorch.</strong></li>
<li>If a pipe bursts, turn off the stop tap and the boiler, open taps to drain the system (save some water in a bucket for flushing and hand washing), and soak up water with towels.</li>
<li>If water has leaked near electrics, do not touch them. Switch them off at the fuse box.</li>
<li>Use a <a href="https://www.watersafe.org.uk/">WaterSafe</a> approved plumber for repairs.</li>
</ul>

<h2>Check on neighbours</h2>
<p>UKHSA says older neighbours, family and friends may need extra support in cold weather. Keep in touch, ask if they feel unwell or need practical help, and see if they need help stocking up on food and medicine if bad weather is forecast. If you are worried about someone’s health, contact a pharmacist, a GP or NHS 111.</p>

<h2>Priority Services Register</h2>
<p>If you or someone you care for is older, disabled, has a long-term health condition or relies on medical equipment, you may be able to join your energy and water companies’ free <a href="priority-services-register.html">Priority Services Register</a> for extra help in a power cut or water cut.</p>

<h2>Help with heating costs</h2>
<p>These are the official figures for winter 2026 to 2027, from GOV.UK, nidirect and mygov.scot. Check the links for full rules.</p>
<ul class="tick">
<li><strong>Winter Fuel Payment</strong> (England, Wales and Northern Ireland): if you were born on or before 27 June 1960, you could get between £100 and £300. Most people get it automatically. If your income is over £35,000, HMRC will take it back. See <a href="https://www.gov.uk/winter-fuel-payment">GOV.UK</a> or <a href="https://www.nidirect.gov.uk/articles/winter-fuel-payment">nidirect</a>.</li>
<li><strong>Cold Weather Payment</strong> (England, Wales and Northern Ireland): £25 for each 7-day period of very cold weather (average 0°C or below) between 1 November 2026 and 31 March 2027, if you get certain benefits such as Pension Credit or some Universal Credit claims. It is paid automatically. See <a href="https://www.gov.uk/cold-weather-payment">GOV.UK Cold Weather Payment</a> and <a href="https://www.gov.uk/cold-weather-payment/eligibility">who can get it</a>.</li>
<li><strong>Scotland:</strong> there is no Winter Fuel Payment or Cold Weather Payment. Instead, <a href="https://www.mygov.scot/pension-age-winter-heating-payment">Pension Age Winter Heating Payment</a> (between £105.55 and £316.70) and <a href="https://www.mygov.scot/winter-heating-payment">Winter Heating Payment</a> (currently £62, for people on certain benefits, whatever the weather).</li>
<li>GOV.UK also mentions the Warm Home Discount (£150 off bills if you get Pension Credit or live in a low-income household), and help from your local council.</li>
<li><strong>Beware of scams.</strong> These payments are made automatically. Nobody will text or email asking for your bank details.</li>
</ul>
{sources([("UKHSA (GOV.UK): Top tips for keeping warm and well this winter","https://www.gov.uk/government/publications/keeping-warm-and-well-staying-safe-in-cold-weather/top-tips-for-keeping-warm-and-well-this-winter"),("UKHSA (GOV.UK): Weather-Health Alerting System","https://www.gov.uk/guidance/weather-health-alerting-system"),("UKHSA data dashboard: Weather-health alerts","https://ukhsa-dashboard.data.gov.uk/weather-health-alerts"),("Met Office: UK weather warnings","https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings"),("Met Office: What to do if you have a frozen or burst pipe","https://weather.metoffice.gov.uk/warnings-and-advice/seasonal-advice/your-home/frozen-or-burst-pipes"),("GOV.UK Prepare: Cold weather, snow and ice",P+"/be-informed-about-hazards/cold-weather-snow-ice/"),("NHS: Winter vaccinations and winter health","https://www.nhs.uk/live-well/seasonal-health/keep-warm-keep-well/"),("British Red Cross: How to prepare for snow and cold weather","https://www.redcross.org.uk/get-help/prepare-for-emergencies/snow-and-winter"),("GOV.UK: Winter Fuel Payment","https://www.gov.uk/winter-fuel-payment"),("GOV.UK: Cold Weather Payment","https://www.gov.uk/cold-weather-payment"),("GOV.UK: Cold Weather Payment eligibility","https://www.gov.uk/cold-weather-payment/eligibility"),("nidirect: Winter Fuel Payment","https://www.nidirect.gov.uk/articles/winter-fuel-payment"),("mygov.scot: Pension Age Winter Heating Payment","https://www.mygov.scot/pension-age-winter-heating-payment"),("mygov.scot: Winter Heating Payment","https://www.mygov.scot/winter-heating-payment"),("Priority Services Register","https://www.thepsr.co.uk/")])}
''',"Cold weather in the UK: Met Office warnings, UKHSA Cold-Health Alerts, keeping warm, frozen pipes, checking on neighbours and help with heating costs.")

BTH="https://www.gov.uk/government/publications/beat-the-heat-resources-for-hot-weather/beat-the-heat-staying-safe-in-hot-weather"
page("guides/extreme-heat.html","Extreme heat: staying safe in hot weather",f'''
<h1>Extreme heat: staying safe in hot weather</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">Many people enjoy hot weather, but too much heat can make anyone unwell. Simple steps keep you, your home and the people around you safer.</p>
<div class="note call"><p><strong>Heatstroke is a medical emergency. Call 999</strong> if someone has a very high temperature, hot skin that is not sweating, fast breathing or heartbeat, confusion, a fit or loses consciousness, or is still unwell after 30 minutes of cooling down.</p></div>

{R["extreme-heat"]}<h2>Warnings and alerts</h2>
<ul class="tick">
<li><strong>Met Office Extreme Heat warnings</strong> cover the whole UK. Like other Met Office warnings, they are based on the likely impact, not a set temperature. The Met Office says amber and red extreme heat warnings can be issued. Red means dangerous weather is expected, with a risk to life: act now. See <a href="https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings">Met Office UK warnings</a> and the <a href="https://weather.metoffice.gov.uk/guides/warnings">warnings guide</a>.</li>
<li><strong>Heat-Health Alerts</strong> come from the UK Health Security Agency (UKHSA) with the Met Office. They cover <strong>England only</strong>. The main season runs from 1 June to 30 September, with extra alerts outside it if needed. They are aimed at health and care services, but anyone can view or sign up for them:
<ul>
<li><strong>Yellow:</strong> heat likely to affect mainly people who are particularly vulnerable, or a less certain forecast that could get worse.</li>
<li><strong>Amber:</strong> impacts likely across the whole health service, with the whole population potentially at risk.</li>
<li><strong>Red:</strong> significant risk to life, even for healthy people. It is issued with a red Extreme Heat warning.</li>
</ul>
See the <a href="https://weather.metoffice.gov.uk/warnings-and-advice/seasonal-advice/heat-health-alert-service">Heat-Health Alert service</a> and <a href="https://ukhsa-dashboard.data.gov.uk/weather-health-alerts">current alerts</a>.</li>
</ul>

<h2>Who is most at risk</h2>
<p>UKHSA lists people aged 65 and over, babies and children aged 5 and under, and pregnant women. It also includes people with heart or breathing problems, dementia, diabetes, kidney disease, Parkinson’s disease or mobility problems, and people on certain medicines. Others at risk are people with serious mental health problems, people who are already ill and dehydrated, and people with alcohol or drug dependence. So are people who are active or work outside, people experiencing homelessness, and people who live alone.</p>

<h2>Keeping your home cool (UKHSA “Beat the heat”)</h2>
<ul class="tick">
<li>Close blinds and curtains on windows in direct sun during the day. Close outside shutters if you have them.</li>
<li>Open windows, if it is safe, when the air outside feels cooler than inside, for example at night. Try to get air flowing through.</li>
<li>Use electric fans if the air temperature is below 35°C, but do not aim them directly at your body.</li>
<li>Check the heating is off, and turn off lights and equipment you are not using.</li>
<li>Move to a cooler room, especially for sleeping. Libraries, places of worship or supermarkets may be cooler than your home.</li>
<li>Stay out of the sun between 11am and 3pm, and plan activity for the early morning or evening.</li>
</ul>

<h2>Heat exhaustion or heatstroke?</h2>
<p><strong>Heat exhaustion</strong> (NHS): tiredness, dizziness, headache, feeling or being sick, heavy sweating with pale clammy skin, cramps, a high temperature, intense thirst and irritability. It usually does not need emergency help if the person cools down within 30 minutes:</p>
<ul class="tick">
<li>Move them somewhere cool and remove unnecessary clothing.</li>
<li>Give plenty of water, or a sports or rehydration drink.</li>
<li>Spray or sponge their skin with cool water and fan them. Cold packs wrapped in cloth under the armpits or on the neck help too.</li>
<li>Stay with them. Call 111 if you are struggling to treat it or need advice.</li>
</ul>
<p><strong>Heatstroke</strong> is an emergency. Call 999 for the signs in the box at the top. While you wait, the NHS says to wrap them in a cool wet sheet, or fan or sponge them with cold water. If they become unresponsive, follow our <a href="first-aid.html">first aid guide</a> (recovery position or CPR). Read more: <a href="https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/">NHS: Heat exhaustion and heatstroke</a> · <a href="https://www.sja.org.uk/first-aid-advice/heatstroke/">St John Ambulance: Heatstroke</a>.</p>

<h2>Drinks and medicines</h2>
<ul class="tick">
<li>Drink fluids regularly. UKHSA says enough that your pee is a pale straw colour. Water, diluted squash and lower-fat milk are good choices. Limit alcohol, which dehydrates you.</li>
<li>Keep taking your prescribed medicines unless a health professional tells you otherwise. Some medicines must be stored below 25°C or in the fridge, so check the pack.</li>
<li>The NHS says people on several medicines, or medicines that may make heat worse, are at higher risk. <strong>Ask a pharmacist</strong> if you are unsure about your medicines in the heat, or call 111.</li>
</ul>

<h2>Checking on others, children, babies and pets</h2>
<ul class="tick">
<li>Check on family, friends and neighbours at higher risk, and ask them to check on you if you are at risk.</li>
<li><strong>Never leave babies, children, older people or pets alone in a parked car</strong> or other small closed space. UKHSA says they can get dangerously hot very quickly.</li>
<li>Shade prams with a parasol, keep air flowing, remove extra clothing and check babies often. Children should not do hard exercise on very hot days.</li>
<li>Dogs Trust says winding a window down is not enough, and a dog could die in a hot car in minutes. Walk dogs at cooler times of day. If you see a dog showing signs of heatstroke in a hot car, the RSPCA says call 999.</li>
<li>If your dog overheats, the RSPCA says “cool first, transport second”: stop exercise, get it into shade, pour cool (not ice-cold) water over its body but not its head, then take it to a vet.</li>
</ul>

<h2>Swimming and cold water shock</h2>
<p>Rivers, lakes and the sea are often much colder than they look, even in summer. The RNLI says water below 15°C can cause cold water shock, which affects your breathing and movement and can lead to drowning. It says average UK and Ireland sea temperatures are just 12°C.</p>
<ul class="tick">
<li>If you fall in, the RNLI says: take a minute, as the first effects pass in less than a minute. Relax and float, then call for help or swim to safety if you can.</li>
<li>UKHSA advises swimming only where there are lifeguards, never after alcohol, always with someone else, and getting out as soon as you feel cold.</li>
<li>Wear a buoyancy aid or life jacket for boating, fishing or activities at the water’s edge.</li>
</ul>

<h2>Wildfires and barbecues</h2>
<ul class="tick">
<li>The National Fire Chiefs Council (NFCC) says only have barbecues and campfires in designated areas, never leave them unattended, and put them out fully with water.</li>
<li>Keep a barbecue on a flat surface that cannot burn, well away from fences, sheds and plants, with water nearby. Never use one indoors or on a balcony, and never use petrol or other flammable liquids to light it.</li>
<li>Take litter home. Glass bottles can focus the sun and start a fire. Put cigarettes out properly.</li>
<li>Follow any local restrictions and the advice of the emergency services. GOV.UK has <a href="https://www.gov.uk/guidance/statutory-guidelines-on-disposable-bbqs">current guidance</a> saying disposable barbecues should not be sold during the present drought and heatwave conditions in Great Britain.</li>
<li>If you see a wildfire, the NFCC says move to a place of safety and call 999. Do not assume someone else has reported it.</li>
</ul>

<h2>Hosepipe bans and saving water</h2>
<p>Ofwat says water companies can bring in a hosepipe ban (a “Temporary Use Ban”) when supplies are low after long dry spells. There is still enough water to drink and wash. You cannot use a hosepipe for things like watering the garden, filling a paddling pool or washing the car, but you can use a watering can or bucket. Ofwat says breaking the rules can lead to a fine of up to £1,000. Check your water company’s website for local rules and exemptions. Collected rainwater is ideal for the garden: see our <a href="rainwater.html">rainwater guide</a>.</p>

<h2>Power cuts in hot weather</h2>
<p>UKHSA says to look out for advice if power or water supplies are likely to be affected. Fans and fridges stop working in a power cut, so keep a battery or wind-up torch and radio and a charged power bank, and keep fridge and freezer doors closed. Call 105 to report a power cut. See our <a href="power-cut.html">power cut guide</a> and <a href="food-storage.html">food storage guide</a>.</p>
{sources([("UKHSA (GOV.UK): Beat the heat: staying safe in hot weather",BTH),("UKHSA (GOV.UK): Weather-Health Alerting System","https://www.gov.uk/guidance/weather-health-alerting-system"),("Met Office: Heat-Health Alert service","https://weather.metoffice.gov.uk/warnings-and-advice/seasonal-advice/heat-health-alert-service"),("Met Office: Weather warnings guide","https://weather.metoffice.gov.uk/guides/warnings"),("Met Office: Why the Met Office is launching a new extreme heat warning (2021)","https://www.metoffice.gov.uk/blog/2021/why-the-met-office-is-launching-a-new-extreme-heat-warning"),("Met Office: UK weather warnings","https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings"),("UKHSA data dashboard: Weather-health alerts","https://ukhsa-dashboard.data.gov.uk/weather-health-alerts"),("NHS: Heat exhaustion and heatstroke","https://www.nhs.uk/conditions/heat-exhaustion-heatstroke/"),("NHS: Heatwave: how to cope in hot weather","https://www.nhs.uk/live-well/seasonal-health/heatwave-how-to-cope-in-hot-weather/"),("St John Ambulance: Heatstroke","https://www.sja.org.uk/first-aid-advice/heatstroke/"),("GOV.UK Prepare: Hot weather",P+"/be-informed-about-hazards/hot-weather/"),("RNLI: Cold water shock","https://rnli.org/safety/know-the-risks/cold-water-shock"),("RSPCA: Heatstroke in dogs","https://www.rspca.org.uk/adviceandwelfare/pets/dogs/health/heatstroke"),("Dogs Trust: Hot weather","https://www.dogstrust.org.uk/dog-advice/life-with-your-dog/seasonal/hot-weather"),("NFCC: Wildfire prevention advice","https://nfcc.org.uk/our-services/campaigns/wildfire-aware/wildfire-prevention-advice/"),("GOV.UK: Statutory guidelines on disposable BBQs","https://www.gov.uk/guidance/statutory-guidelines-on-disposable-bbqs"),("Ofwat: Hosepipe bans","https://www.ofwat.gov.uk/hose-pipe-bans-what-are-they-and-what-they-mean-for-the-public/"),("UKHSA (GOV.UK): Beat the heat: keep cool at home checklist",BTHC),("CIBSE: How to keep your space cool during a heatwave",CIBSE),("GOV.UK: Overheating: Approved Document O","https://www.gov.uk/government/publications/overheating-approved-document-o"),("Essex & Suffolk Water: Temporary Use Ban (hosepipe ban)","https://www.eswater.co.uk/temporaryuseban")])}
''',"Extreme heat in the UK: Met Office warnings, UKHSA Heat-Health Alerts, keeping cool, heatstroke, pets, cold water shock, wildfires and hosepipe bans.")

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
<p class="meta">Last checked: <time datetime="2026-10-16">{CHECKED}</time></p>
<p class="lead">Most water cuts are fixed quickly. Longer cuts are rare, but they do happen, so it is worth a little planning. Your water company is the best place for news.</p>
<div class="card"><h2 id="how-likely">How likely is a long water cut?</h2>
<p>The UK government’s <a href="{NRR}">National Risk Register 2026</a> looks at a rare “reasonable worst case”, not an everyday water cut. Its worst case for <strong>“Water infrastructure failure or loss of drinking water”</strong> is <strong>likelihood 4 (5–25%)</strong> and <strong>impact 5 (Catastrophic)</strong>. Likelihood here means the chance of this happening at least once in 5 years.</p>
<p>In the government’s words, it imagines “the loss of piped drinking water and impact to wastewater services for over one million people”. It says “residents would likely have to leave the area, and some may require evacuation”, and that “repair of the infrastructure could take months”.</p>
<p>The register also says “all risks in the NSRA are relatively low likelihood events”. You do not need to store months of water. The steps below help with a short cut, and help you cope well if you are ever asked to leave.</p></div>
<h2 id="get-ready">Get ready now</h2>
<ul class="tick">
<li><strong>Keep some sealed bottled water.</strong> GOV.UK says at least 2.5 to 3 litres per person per day to drink, and 10 litres per person per day to be more comfortable. Use our <a href="../calculator.html">calculator</a> to work out your amount. GOV.UK says “there is no standard figure” for how many days to store, because emergencies vary.</li>
<li><strong>Buy sealed bottled water</strong> rather than filling your own containers. GOV.UK says bottled water is sealed in a food-grade bottle, so it stays safe for longer.</li>
<li><strong>Store it well and use it in turn.</strong> Bristol Water advises keeping bottled water in a cool, shaded place away from direct sunlight. Do not keep it somewhere warm, like a car: the water can taste odd or turn green, and then you should not drink it. Check the date on the bottles, use the oldest first, and replace them as you go.</li>
<li><strong>Find out who your water company is.</strong> Use <a href="https://www.water.org.uk/customers/find-your-supplier">Water UK: find your supplier</a>, then follow it on social media or sign up for its text updates.</li>
<li><strong>Join your water company’s Priority Services Register</strong> if you or someone you care for needs extra help. Water companies use it to deliver bottled water to people who can’t collect it. See our <a href="priority-services-register.html">Priority Services Register guide</a>.</li>
<li>If someone uses <strong>medical equipment that needs water</strong> (for example home dialysis), GOV.UK says to talk to your care team about a plan for a water cut.</li>
<li><strong>Keep handy supplies.</strong> CCW, the water consumer body, suggests hand sanitiser, wet wipes, waterless soap, dry shampoo and disposable plates, cups and cutlery.</li>
<li>If you have space, a <strong>water butt</strong> gives you water for flushing the toilet. Do not drink it (see our <a href="rainwater.html">rainwater guide</a>).</li>
<li>Know where your <strong>stop tap</strong> is, so you can turn the water off if a pipe leaks.</li>
<li>Keep a <strong>bag ready in case you need to leave</strong>, with medicines and important documents (see our <a href="../plan.html">household plan</a>).</li>
</ul>
<h2 id="during">During a water cut</h2>
<ul class="tick">
<li>Check your water company’s website, text updates or social media. Ofwat says your company should tell you where to get another supply and when it expects water to be back.</li>
<li>Save bottled water for drinking, cooking, washing hands and making baby formula. If you cannot boil water, GOV.UK suggests ready-to-use baby formula.</li>
<li>Check on neighbours who may struggle to collect water.</li>
</ul>
<h2 id="longer">If it lasts longer</h2>
<h3>Bottled water stations</h3>
<ul class="tick">
<li>Ofwat says that if the piped supply fails, water companies must provide at least 10 litres of water per person per day within the first 24 hours, and keep this up until the supply is back. This can be bottled water, a water tanker (bowser) or a standpipe.</li>
<li>Companies often set up <strong>bottled water stations</strong>. Your water company’s website and social media will say where they are and when they are open.</li>
<li>If you are on the Priority Services Register, your water company should arrange water for you. If it doesn’t arrive, contact them. If you are not registered but need help, CCW says to contact your water company anyway. Help may be slower than if you were already registered.</li>
<li>Staff and delivery drivers should carry ID. If you are unsure, CCW says to ask them to wait outside while you call the number on your water bill.</li>
</ul>
<h3>Toilets without flushing</h3>
<ul class="tick">
<li>While the water is off, your toilet will not refill after you flush it.</li>
<li>South West Water and Bristol Water advise flushing with water from a water butt or your stored water: fill a bucket and pour it into the bowl.</li>
<li>Do not flush wet wipes. South West Water says to put them in the bin.</li>
</ul>
<h3>Keeping clean</h3>
<ul class="tick">
<li>To wash your hands, GOV.UK says to fill a large clean bowl, like a washing-up bowl, with water and add soap or household disinfectant.</li>
<li>Hand sanitiser, wet wipes and dry shampoo help you stay clean and save water.</li>
<li>Use disposable plates and cutlery so you don’t need to wash up.</li>
<li>Soft and fizzy drinks from the cupboard are safe to drink. GOV.UK says not to drink milk or fresh fruit juice that smells off.</li>
</ul>
<h3>If you are asked to leave</h3>
<div class="note call"><p><strong>If the authorities ask you to leave, go.</strong> The National Risk Register says: “It is important for people not to delay evacuating properties, buildings or general locality if asked to by the responding authorities.”</p></div>
<ul class="tick">
<li>Follow instructions from your water company, the council and the emergency services. Check for <a href="https://www.gov.uk/alerts">Emergency Alerts</a> on your phone.</li>
<li>Take your bag, with medicines and important documents, and any pets.</li>
<li>Before you go, turn off your water at the stop tap.</li>
</ul>
<h2 id="after">When the water comes back</h2>
<ul class="tick">
<li>It may look cloudy or discoloured. GOV.UK says to run the cold tap nearest your stop tap (often under the kitchen sink) for a while. If it doesn’t clear, contact your water company.</li>
<li>You may be entitled to compensation. CCW says your water company must consider this after an incident.</li>
</ul>
{sources([("Cabinet Office: National Risk Register 2026",NRR),("GOV.UK Prepare: Water supply interruptions or outages",P+"/be-informed-about-hazards/water-supply-interruptions-or-outages/"),("GOV.UK Prepare: Get prepared for emergencies",P+"/get-prepared-for-emergencies/"),("Ofwat: Supply interruptions","https://www.ofwat.gov.uk/households/supply-and-standards/supply-interruptions/"),("CCW: What to expect if a water or sewerage incident affects your home","https://www.ccw.org.uk/advice-and-support/households/water-sewerage-incidents-home/"),("South West Water: Preparing for an incident","https://www.southwestwater.co.uk/household/help-support/in-your-area/preparing-for-an-incident"),("Bristol Water: Bottled water","https://www.bristolwater.co.uk/incident-management/bottled-water"),("Water UK: Find your water supplier","https://www.water.org.uk/customers/find-your-supplier"),("GOV.UK: Emergency Alerts","https://www.gov.uk/alerts"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit")])}
''',"What to do before, during and after a water cut in the UK, including longer outages, with GOV.UK and Ofwat advice.")

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
<li>Spotted a mistake? Email <a href="mailto:homereadyuk@mail.grokbot.com">homereadyuk@mail.grokbot.com</a>.</li>
</ul>
<h2>Privacy</h2>
<p>This site uses no cookies, no advertising trackers and no outside fonts. We count visits with GoatCounter, which uses no cookies and stores no IP addresses. The calculator runs in your browser and saves nothing. We never ask for health details.</p>
<h2>Affiliate and advertising policy</h2>
<p>We have <strong>no affiliate links and no adverts</strong> right now. If we ever add them, each one will be clearly labelled <strong>“Ad”</strong>, and they will never appear inside the core safety advice. Following our advice never requires buying anything from us.</p>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time>.</p>
''',"Who we are, our editorial policy, how we check sources, privacy and affiliate policy.")
print("built")

# ---------- SMOKE-TEST LANDING VARIANTS (/a /b /c) ----------
# TODO before publishing (needs Phil's approval):
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
{signup("variant-"+k,"email-"+k,"../")}

<h2>What might come later</h2>
<p>We are testing whether people want more, such as seasonal reminders or a phone app that works without signal. <strong>None of this exists yet</strong>, and we have not set any prices. If we ever charge for anything, the core advice and calculator will stay free.</p>
''',sub)
    s=open(f"{k}/index.html").read().replace('<meta name="description"','<meta name="robots" content="noindex">\n<meta name="description"')
    open(f"{k}/index.html","w").write(s)

# ---------- PRIVACY NOTICE (DRAFT) ----------
page("privacy.html","Privacy notice",f'''
<h1>Privacy notice</h1>
<h2>Who we are</h2>
<p>Home Ready UK is run by Philip Aubrey-Jones ("we"), who is the data controller. You can contact us by email at <a href="mailto:homereadyuk@mail.grokbot.com">homereadyuk@mail.grokbot.com</a>. We deal with all privacy questions by email.</p>
<h2>What we collect and why</h2>
<table><thead><tr><th scope="col">What</th><th scope="col">Why</th><th scope="col">Legal basis (UK GDPR)</th><th scope="col">How long</th></tr></thead><tbody>
<tr><td>Your email address, the date you signed up, and which page you signed up on</td><td>To send occasional reminders and updates you asked for</td><td>Consent (Article 6(1)(a))</td><td>Until you unsubscribe. If we stop the service, we delete the list within 3 months.</td></tr>
<tr><td>Survey answers (if you take our survey). We do not ask your name or health details.</td><td>To understand what would help households</td><td>Consent</td><td>Deleted 6 months after the survey closes. Only summary figures are kept.</td></tr>
<tr><td>Visit counts only (page, referring site, browser type, country). No cookies, no IP addresses, nothing that identifies you.</td><td>To see which pages are useful</td><td>Legitimate interests (Article 6(1)(f))</td><td>Kept only as totals, which cannot identify anyone</td></tr>
</tbody></table>
<p>The calculator runs only in your browser. What you type is never sent to us or stored.</p>
<h2>Who helps us</h2>
<ul class="tick">
<li>Buttondown stores email addresses and sends our emails. When you sign up, you go to a Buttondown page to confirm. It is based in the USA, so your email address is stored outside the UK, under safeguards approved for UK data transfers.</li>
<li>GoatCounter counts visits without cookies and does not store IP addresses.</li>
<li>Google Forms collects survey answers. We do not collect names or email addresses in the survey.</li>
<li>GitHub Pages hosts this website. GitHub may keep short-term technical logs to run and protect the service.</li>
</ul>
<p>We never sell your data or use it for advertising.</p>
<h2>Your rights</h2>
<p>You can ask to see, correct or delete your data, or withdraw consent at any time (every email has an unsubscribe link). Email <a href="mailto:homereadyuk@mail.grokbot.com">homereadyuk@mail.grokbot.com</a>. We will reply within one month. If you are unhappy, you can complain to the <a href="https://ico.org.uk/make-a-complaint/">Information Commissioner's Office (ICO)</a>.</p>
<p class="meta">Last updated: <time datetime="2026-10-15">{CHECKED}</time>.</p>
''',"How Home Ready UK uses your information.")
print("variants built")
# ---------- NINE NEW GUIDES ----------
NRRPDF="https://assets.publishing.service.gov.uk/media/6a50d66b1228eb26a4cab76c/National_Risk_Register_2026.pdf"
SRC_NRR=("Cabinet Office: National Risk Register 2026",NRR)
RI="Do these now, while things are calm. You can do them bit by bit."
def ul(items): return '<ul class="tick">'+"".join(f"<li>{i}</li>" for i in items)+"</ul>\n"
def nrrbox(text): return f'<div class="card"><h2 id="how-likely">What the National Risk Register says</h2>{text}<p class="meta">The <a href="{NRR}">National Risk Register 2026</a> describes rare, national “reasonable worst cases”. In its own words, “all risks in the NSRA are relatively low likelihood events.” Likelihood is the chance of the worst case happening at least once in 5 years (2 years for malicious risks).</p></div>\n'
def guide(slug,title,lead,body,srcs,desc):
    page(f"guides/{slug}.html",title,f'''
<h1>{title}</h1>
<p class="meta">Last checked: <time datetime="2026-10-16">{CHECKED}</time></p>
<p class="lead">{lead}</p>
{body}
{sources(srcs)}
''',desc)

# 1 Leaving home quickly
guide("leaving-home","Leaving home quickly, or staying inside safely",
"Sometimes the safest thing is to leave your home. Other times you will be told to go indoors and stay there. A little planning makes both much easier.",
nrrbox("<p>Evacuation comes up across many risks. For example, the register’s worst case for loss of water says “residents would likely have to leave the area”. It advises: “It is important for people not to delay evacuating properties, buildings or general locality if asked to by the responding authorities.”</p><p>It also says people may be asked to “‘go in, stay in and tune in’ to local radio stations or check official sources of information online”.</p>")+
ready("Get ready now",[
"<strong>Pack a grab bag.</strong> GOV.UK Prepare suggests keeping things you would need if asked to leave quickly in a spare bag. The British Red Cross suggests: medicines, a phone charger or power bank, cash and bank cards, a paper list of contact numbers, spare glasses, weather-appropriate clothing, water and snacks, and baby and pet supplies.",
"<strong>Keep documents together.</strong> GOV.UK Prepare suggests keeping your plan with passports, birth certificates and insurance papers, so they are easy to gather if you are asked to evacuate. The Red Cross suggests copies in a waterproof bag.",
"<strong>Keep enough medicine</strong> for several days, plus paper instructions and charged back-up batteries for any medical equipment (GOV.UK Prepare).",
"<strong>Know how to turn off your gas, electricity and water.</strong> GOV.UK Prepare says you will need to do this if you have to leave your home. Write where they are on your <a href=\"../plan.html\">household plan</a>.",
"<strong>Agree a meeting place</strong> close to home, in case you can’t get back or phones are down. Ready Scotland says it should have shelter and be accessible for everyone in your household.",
"<strong>Plan for anyone who can’t leave on their own.</strong> Ready Scotland says you may need extra planning if someone has a disability, a long-term condition or uses medical equipment. See GOV.UK Prepare’s <a href=\""+P+"/get-prepared-for-emergencies/advice-for-disabled-persons-and-carers/\">advice for disabled people and carers</a>.",
"<strong>Get pets ready.</strong> The RSPCA suggests suitable carriers, a supply of food, and a watertight bag with microchip numbers, vet and vaccination details and a photo of your pet. GOV.UK’s flood plan says many evacuation centres will let you bring your pet.",
"<strong>Make sure you can get Emergency Alerts</strong> on your mobile phone, and keep a battery or wind-up radio (see our <a href=\"phones-internet-down.html\">phones and internet guide</a>).",
],RI)+
'<h2 id="leave">If you are asked to leave</h2>\n'+ul([
"Go when you are asked. Do not wait to see what happens. The register says delaying “may put individuals’ own lives at risk, as well as putting emergency responders in danger”.",
"Take your grab bag, medicines and pets. Turn off gas, electricity and water if it is safe and you have time.",
"Follow official advice on where to go: the council, emergency services, local radio and <a href=\"https://www.gov.uk/alerts\">Emergency Alerts</a>.",
"<strong>If your home is on fire, get out and take nothing.</strong> GOV.UK Prepare says you should not take anything with you. See our <a href=\"fire-and-carbon-monoxide.html\">fire guide</a>.",
])+
'<h2 id="stay-in">If you are told to go in, stay in, tune in</h2>\n<p>This is the usual advice for a chemical, smoke or radiation incident nearby.</p>\n'+ul([
"<strong>Go in.</strong> UKHSA says to go into any building as soon as possible (not the one where the incident is). A car does not protect you well enough.",
"<strong>Stay in.</strong> Close doors and windows. Turn off fans and air conditioning, and close vents, including trickle vents in windows, if you can (UKHSA).",
"<strong>Tune in.</strong> Follow local radio, TV, official websites and social media, and Emergency Alerts. You may need to stay in for some hours. For a radiation emergency, GOV.UK Prepare says it could be one to two days.",
"If you need your regular medicine, UKHSA says to contact NHS 111 for advice rather than leaving the building.",
"If you think a chemical has got on you, GOV.UK Prepare says: remove yourself from the area, remove outer clothing (try not to pull it over your head), and remove the substance from your skin with a dry absorbent material.",
])+
'<h2 id="after">Afterwards</h2>\n'+ul([
"Only go home when the authorities say it is safe.",
"Restock your grab bag and replace any medicines you used.",
]),
[SRC_NRR,("GOV.UK Prepare: Get prepared for emergencies",P+"/get-prepared-for-emergencies/"),("GOV.UK Prepare: Advice for disabled persons and carers",P+"/get-prepared-for-emergencies/advice-for-disabled-persons-and-carers/"),("GOV.UK Prepare: Hazardous substance and radiation exposure",P+"/be-informed-about-hazards/hazardous-materials-incident/"),("UKHSA (GOV.UK): What to do in a chemical emergency","https://www.gov.uk/government/publications/chemical-emergencies-information-for-the-public/what-to-do-in-a-chemical-emergency"),("Ready Scotland: Make an emergency plan","https://ready.campaign.gov.scot/emergency-plan"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit"),("RSPCA: Floods and pets","https://www.rspca.org.uk/adviceandwelfare/seasonal/floods"),("GOV.UK: Personal flood plan","https://www.gov.uk/government/publications/personal-flood-plan/personal-flood-plan"),("GOV.UK: Emergency Alerts","https://www.gov.uk/alerts")],
"How to get ready to leave home quickly in the UK, pack a grab bag, plan for pets, and what to do if told to go in, stay in, tune in.")

# 2 Fire and CO
guide("fire-and-carbon-monoxide","Fire and carbon monoxide safety at home",
"Most home fires start by accident, and carbon monoxide can’t be seen or smelt. Working alarms and a simple escape plan protect everyone.",
'<div class="note call"><p><strong>If there is a fire: get out, stay out, call 999.</strong> Do not try to tackle it yourself. <strong>If you think a gas appliance is leaking carbon monoxide, call 0800 111 999</strong> (free, 24 hours) and go outside.</p></div>\n'+
ready("Get ready now",[
"<strong>Fit smoke alarms on every floor</strong> and test them at least once a month. GOV.UK Prepare says you are 11 times more likely to die in a fire if you have no working smoke alarms. In Scotland, the law on heat and smoke alarms changed in 2022.",
"<strong>Fit a carbon monoxide alarm</strong> that makes a loud sound. The NHS says to have one in each room with an appliance that burns gas, oil, coal or wood.",
"<strong>Get appliances serviced.</strong> The NHS says to have boilers, heaters and cookers serviced regularly by a qualified, registered engineer, and to keep chimneys and flues clean.",
"<strong>Plan and practise your escape route</strong> so everyone knows what to do. Keep exits clear and keep door and window keys where everyone can find them (GOV.UK Prepare).",
"<strong>Do a free home fire safety check.</strong> Use the <a href=\"https://www.ohfsc.co.uk/\">online home fire safety check</a> or contact your local fire service. In Northern Ireland, ask NIFRS for a free Home Fire Safety Check.",
"<strong>Charge safely.</strong> Follow the maker’s instructions for phones, laptops, e-bikes and e-scooters, use a compatible charger, and don’t charge them on your escape route (GOV.UK Prepare).",
"<strong>Keep heaters clear</strong> of curtains and furniture, and never use them to dry clothes. Use torches rather than candles in a power cut.",
"Teach children what the smoke alarm sounds like and how to “stop, drop and roll” (GOV.UK Prepare).",
],RI)+
'<h2 id="bedtime">A quick bedtime check</h2>\n<p>GOV.UK Prepare says you are more at risk from fire while asleep. Before bed:</p>\n'+ul([
"close inside doors",
"turn off and unplug appliances unless they are meant to stay on, like the freezer",
"check the cooker is off, and don’t leave the washing machine or dryer running",
"put candles and cigarettes out properly",
])+
'<h2 id="fire">If there is a fire</h2>\n'+ul([
"Get everyone out as soon as possible. Do not assume everyone has heard the alarm. Some children may not wake to it.",
"Don’t stop to investigate or pick up valuables. If there is smoke, keep low where the air is clearer.",
"Check doors before opening them. If a door is warm, don’t open it. Close doors behind you as you leave.",
"Call 999 once you are out, and alert neighbours if they are close by.",
"<strong>If you can’t get out:</strong> get everyone into one room, ideally with a window and a phone. Put bedding around the bottom of the door. Call 999, then open the window and shout “HELP FIRE”.",
"If clothes catch fire: stop, drop and roll, and smother the flames with a heavy coat or blanket.",
])+
'<h2 id="co">Carbon monoxide</h2>\n<p>The NHS says symptoms include a headache, dizziness, feeling sick, feeling weak, tiredness and confusion, chest or muscle pain, and shortness of breath. They may get better when you go outside. The HSE says warning signs include yellow or orange flames instead of blue, soot or staining around appliances, and pilot lights that keep going out.</p>\n'+ul([
"If you think there is carbon monoxide, stop using the appliance, go outside, and get medical advice. Don’t go back in until you have advice (NHS).",
"Call NHS 111 if you think you have symptoms. <strong>Call 999</strong> if someone is struggling to breathe, suddenly confused, unconscious, weak, or has chest or muscle pain. Do not drive yourself to A&amp;E.",
"Never use a barbecue or camping stove indoors, and never run engines in an enclosed space like a garage (NHS).",
])+
'<h2 id="after">After a fire</h2>\n'+ul([
"The fire service will tell you whether it is safe to go back in, and give you an incident number. The British Red Cross says you will need it for insurance.",
"Call your insurer as soon as you can. If you rent, tell your landlord. If you can’t stay at home and aren’t insured, contact your local council.",
"Check with a pharmacist before using any medicine that was exposed to heat.",
]),
[("GOV.UK Prepare: Fire in the home",P+"/be-informed-about-hazards/domestic-fire/"),("GOV.UK: Fire Kills","https://www.gov.uk/firekills"),("Online home fire safety check","https://www.ohfsc.co.uk/"),("Scottish Fire and Rescue Service: At home","https://www.firescotland.gov.uk/at-home/"),("nidirect: Fire safety and prevention","https://www.nidirect.gov.uk/articles/fire-safety-and-prevention"),("NHS: Carbon monoxide poisoning","https://www.nhs.uk/conditions/carbon-monoxide-poisoning/"),("HSE: Carbon monoxide awareness","https://www.hse.gov.uk/gas/domestic/co.htm"),("British Red Cross: After a house fire","https://www.redcross.org.uk/get-help/prepare-for-emergencies/after-house-fire")],
"Smoke alarms, carbon monoxide alarms, a fire escape plan and what to do if there is a fire or CO leak at home, from GOV.UK and the NHS.")

# 3 Phones and internet down
guide("phones-internet-down","Staying in touch when phones and the internet are down",
"Phone and internet outages are usually short and local. But storms and power cuts can sometimes take them out for days, so it helps to have a back-up plan.",
nrrbox("<p>The register’s worst case for <strong>“Simultaneous loss of all fixed and mobile forms of communication”</strong> (likelihood 3, 1–5%; impact 3, Moderate) imagines one region losing all connections, “with most fixed‑line connections remaining offline for several days due to a lack of power at the customer premises and damage to overhead cables.”</p><p>New risks in 2026 include <strong>“Digital resilience failure”</strong> (likelihood 4, 5–25%; impact 4, Significant), such as “a faulty software update that crashes critical servers”, based on the 2024 CrowdStrike outage.</p><p><strong>Severe space weather</strong> (likelihood 4, 5–25%; impact 4, Significant) could last “for 1‑2 weeks”, with “regional power disruptions, loss or disruption of Global Navigation Satellite Systems (for example, Global Positioning System (GPS)) and some telecommunications”. The steps on this page and in our <a href=\"power-cut.html\">power cut guide</a> help with all of these.</p>")+
ready("Get ready now",[
"<strong>Keep a battery or wind-up FM radio</strong> and spare batteries. GOV.UK Prepare says updates may be given on the radio during an outage.",
"<strong>Write important numbers on paper</strong>: family, neighbours, GP, utilities. Use our <a href=\"../plan.html\">household plan</a>.",
"<strong>Agree a meeting point</strong> with family in case you can’t reach each other. Choose somewhere easy to find and open to the public.",
"<strong>Keep a power bank charged</strong> for each phone.",
"<strong>Still on an old analogue landline?</strong> GOV.UK Prepare says the analogue network is being upgraded to digital and to contact your landline provider. West Yorkshire Prepared says the switchover is expected to finish by January 2027. Digital landlines need power to work.",
"<strong>Telecare and personal alarm users:</strong> call your landline provider. Digital Phone Switchover says the change could stop telecare alarms working. GOV.UK Prepare says if you are a vulnerable customer, such as a telecare user, your provider must give you a free back-up battery unit, so your landline works for at least an hour in a power cut.",
"<strong>Tell your provider</strong> if you need extra support. GOV.UK Prepare says this can mean priority fault repair and extra help during outages.",
"<strong>Check how medical devices behave offline.</strong> Ask the maker how a personal alarm or diabetes sensor would work if mobile or broadband is lost.",
"<strong>Download or print maps.</strong> GOV.UK Prepare says GPS may still work with no signal, but map apps need maps downloaded in advance.",
"<strong>Agree a back-up plan with anyone vulnerable</strong>, for example that you or a neighbour will visit in person if you can’t call.",
],RI)+
'<h2 id="during">During an outage</h2>\n'+ul([
"<strong>You can still call 999 from a mobile.</strong> GOV.UK Prepare says emergency calls automatically roam onto any available network, and the 999 system is designed to keep running in power cuts.",
"If your mobile network is down but your Wi-Fi works, try Wi-Fi Calling.",
"Use your phone sparingly to save battery. Messages may work when calls don’t. Moving a short distance can help, and public Wi-Fi may still work.",
"Check your provider’s status page or app. Ofcom says to report a fault to your provider if it isn’t listed, and tell them if you rely on the connection for telecare or health devices.",
"Check on neighbours, especially anyone who lives alone.",
])+
'<h2 id="after">Afterwards</h2>\n'+ul([
"Recharge power banks and replace radio batteries.",
"Ofcom says you may be entitled to compensation for a loss of service. Ask your provider.",
]),
[SRC_NRR,("GOV.UK Prepare: Phone and broadband outages",P+"/be-informed-about-hazards/phone-broadband-outages/"),("GOV.UK Prepare: Alerts",P+"/get-prepared-for-emergencies/alerts/"),("GOV.UK: Emergency Alerts","https://www.gov.uk/alerts"),("Digital Phone Switchover","https://digitalphoneswitchover.com/"),("Ofcom: Broadband and landline faults","https://www.ofcom.org.uk/phones-and-broadband/service-quality/broadband-landline-faults"),("West Yorkshire Prepared: Community Risk Register 2025 (PDF)","https://www.westyorkshireprepared.org.uk/wp-content/uploads/2025/10/3806-Community-Risk-Register-DIGITAL-FINAL-1.pdf"),("Met Office: Space weather","https://www.metoffice.gov.uk/weather/learn-about/space-weather")],
"How to stay in touch in the UK when mobile, landline and broadband are down, including the digital landline switchover, telecare and space weather.")

# 4 Cards and banking
guide("cash-and-banking","When cards and banking stop: cash and staying safe online",
"Card payments, banking apps and cash machines very rarely stop working, but when they do it can be for days. A little cash at home and good online security help.",
nrrbox("<p>The register’s worst case for <strong>“Technological failure at a systemically important retail bank”</strong> (likelihood 3, 1–5%; impact 3, Moderate) is critical technology out “for at least 2 days”, with customers “unable to view account balances, process payments, use online banking or withdraw cash from ATMs.” It says “The most significant impact would be felt by vulnerable customers with only a single bank account.”</p>")+
ready("Get ready now",[
"<strong>Keep a small amount of cash at home.</strong> West Yorkshire Prepared says to keep some “in case cash points and electronic payment systems stop working.” The British Red Cross suggests cash for essentials like food or fuel. Small notes and coins are easiest.",
"<strong>Secure your email account first</strong>, then your other accounts. GOV.UK Prepare says to use a passkey where you can, or a strong, unique password with 2-step verification.",
"<strong>Use a password manager</strong>, or your browser’s, to create and store strong passwords (GOV.UK Prepare).",
"<strong>Turn on automatic updates</strong> for your phone, computer and smart devices (GOV.UK Prepare).",
"<strong>Back up photos and files</strong>, and know how to restore them (GOV.UK Prepare).",
"<strong>Save these numbers:</strong> 159 to reach your bank safely, Report Fraud on 0300 123 2040 (Police Scotland: 101).",
],RI)+
'<h2 id="during">If payments stop working</h2>\n'+ul([
"Use your cash for essentials like food, medicine and fuel.",
"Follow updates from your bank and the news.",
"<strong>Watch out for scams.</strong> The register says a bank outage would bring “heightened fraud”. Ready Scotland warns criminals may take advantage of emergencies.",
"Check on anyone who may struggle, such as older neighbours who rely on one account.",
])+
'<h2 id="scams">Spotting and reporting scams</h2>\n'+ul([
"<strong>An unexpected call about money?</strong> Hang up and call <strong>159</strong>. Stop Scams UK says 159 connects you safely to your bank, covers more than 99% of UK current accounts, and cannot be spoofed.",
"Forward suspicious emails to <strong>report@phishing.gov.uk</strong> and suspicious texts to <strong>7726</strong> (NCSC). Don’t click links in them.",
"If you have lost money or been hacked, report it to <a href=\"https://www.reportfraud.police.uk/\">Report Fraud</a> or call 0300 123 2040 (England, Wales and Northern Ireland). In Scotland, call Police Scotland on 101. Tell your bank straight away.",
]),
[SRC_NRR,("GOV.UK Prepare: Cyber security",P+"/be-informed-about-hazards/cyber/"),("NCSC: Cyber security advice for you and your family","https://www.ncsc.gov.uk/section/advice-guidance/you-your-family"),("NCSC: Report a scam email","https://www.ncsc.gov.uk/collection/phishing-scams/report-scam-email"),("NCSC: Report a scam text","https://www.ncsc.gov.uk/collection/phishing-scams/report-scam-text-message"),("Stop Scams UK: 159","https://stopscamsuk.org.uk/159"),("Report Fraud","https://www.reportfraud.police.uk/"),("West Yorkshire Prepared: Community Risk Register 2025 (PDF)","https://www.westyorkshireprepared.org.uk/wp-content/uploads/2025/10/3806-Community-Risk-Register-DIGITAL-FINAL-1.pdf"),("British Red Cross: Prepare an emergency kit","https://www.redcross.org.uk/get-help/prepare-for-emergencies/prepare-an-emergency-kit"),("Ready Scotland: Make an emergency plan","https://ready.campaign.gov.scot/emergency-plan")],
"Why to keep some cash at home, how to secure your accounts, and how to spot and report scams if UK card payments or banking stop.")

# 5 Storms
guide("storms","Storms and high winds",
"Storms hit the UK most years, mainly in autumn and winter. Simple steps before a storm keep you safer and cut the damage.",
nrrbox("<p>The register rates <strong>Storms</strong> at likelihood 4 (5–25%) and impact 3 (Moderate). Its worst case is “storm force winds affecting multiple regions of the UK”, with “gusts in excess of 85 mph”. It says disruption to power, communications and transport “could last for 1‑4 days and for more than 5 days in remote rural locations.”</p>")+
ready("Get ready now",[
"<strong>Get weather warnings.</strong> Check the <a href=\"https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings\">Met Office warnings</a> or use the Met Office app, where you can set alerts for your area. GOV.UK Prepare says to pay extra attention when a storm is named.",
"<strong>Check your roof, chimney and gutters.</strong> The British Red Cross suggests checking for loose tiles, aerials and satellite dishes, having a professional check chimney stacks, and clearing gutters.",
"<strong>Check fences, gates and trees.</strong> Make sure fences and gates are in good condition, and deal with loose or overhanging branches (Red Cross).",
"<strong>Know who your power provider is</strong> and that you can call 105 in a power cut. See our <a href=\"power-cut.html\">power cut guide</a>.",
"<strong>Have a torch, radio and power bank ready</strong>, and a paper list of numbers.",
],RI)+
'<h2 id="forecast">When a storm is forecast</h2>\n'+ul([
"Secure or bring in loose things: ladders, trampolines, garden furniture, toys and bins (GOV.UK Prepare).",
"Close and fasten doors and windows, especially on the side facing the wind, and garage doors. Close and bolt the loft hatch.",
"Park cars in a garage, or away from buildings, trees, walls and fences.",
"If chimney stacks are tall or in poor condition, move beds away from the area directly below them.",
"Charge phones, power banks and back-up batteries for medical equipment.",
"Check whether schools are closing, and limit travel. Follow any ‘Do Not Travel’ advice.",
"Check on anyone who might need help.",
])+
'<h2 id="during">During the storm</h2>\n'+ul([
"Stay inside if you can. Keep away from windows. Open inside doors only as needed, and close them behind you.",
"If you must go out, don’t walk or shelter near buildings, walls, fences or trees. Use the door on the sheltered side.",
"Do not go out to repair damage while the storm is still going.",
"<strong>Keep well away from fallen power lines.</strong> GOV.UK Prepare says high-voltage electricity can jump gaps with no warning.",
"If you must drive, take care on bridges and high, open roads, and watch for side winds.",
])+
'<h2 id="after">After the storm</h2>\n'+ul([
"Don’t touch cables that have been blown down or are still hanging.",
"Don’t walk too close to walls, buildings and trees, as they may have been weakened.",
"Check on vulnerable neighbours and relatives and help them arrange repairs.",
"Storms can also cause flooding and water cuts. See our <a href=\"flooding.html\">flooding</a> and <a href=\"water-outage.html\">no water</a> guides.",
]),
[SRC_NRR,("GOV.UK Prepare: Storms",P+"/be-informed-about-hazards/storms/"),("Ready Scotland: Storms and high winds","https://ready.campaign.gov.scot/storms-wind"),("British Red Cross: Storms and thunderstorms","https://www.redcross.org.uk/get-help/prepare-for-emergencies/support-during-a-storm"),("Met Office: UK weather warnings","https://weather.metoffice.gov.uk/warnings-and-advice/uk-warnings")],
"How to prepare your home for storms and high winds in the UK, and what to do during and after, from GOV.UK Prepare and the Met Office.")

# 6 Illness at home
guide("illness-at-home","Illness at home: flu, norovirus and pandemics",
"Winter bugs are common, and most people get better at home. The same simple habits also help if a bigger outbreak or pandemic ever happens.",
nrrbox("<p>The register rates <strong>Pandemic</strong> at likelihood 4 (5–25%) and impact 5 (Catastrophic), one of its highest-scoring risks. Its worst case is “an unmitigated pandemic”, with a response stage “at least 9 months and potentially, significantly longer”. An outbreak of an emerging infectious disease is rated likelihood 4, impact 4 (Significant).</p>")+
ready("Get ready now",[
"<strong>Keep up to date with vaccines</strong>, including the flu vaccine if you are offered it. GOV.UK Prepare says vaccinations are the most effective way to prevent many infectious diseases.",
"<strong>Keep a small sick-day kit</strong>: paracetamol or ibuprofen, a thermometer, tissues, soap, and oral rehydration sachets (the NHS says a pharmacist may recommend these for diarrhoea and vomiting).",
"<strong>Keep enough of your regular medicines</strong> to last several days (GOV.UK Prepare).",
"<strong>Keep some easy food and drinks</strong> in the cupboard. See our <a href=\"food-storage.html\">food storage guide</a>.",
"<strong>Agree who could help</strong> with shopping, medicines or pets if your household is ill.",
"Take any unused antibiotics back to a pharmacy. GOV.UK Prepare says don’t save them for later or share them.",
],RI)+
'<h2 id="spread">Stop it spreading</h2>\n'+ul([
"Wash your hands with soap and water for at least 20 seconds, especially after the toilet and before preparing food. <strong>Hand gel does not kill norovirus</strong> (NHS).",
"Cover coughs and sneezes with a tissue, then bin it. Clean things people touch a lot, like door handles, taps and flush handles.",
"Let fresh air in.",
"If you are unwell, try to stay at home and avoid contact with others. With norovirus, the NHS says stay off school or work until you have not been sick or had diarrhoea for 2 days, and don’t visit hospitals or care homes.",
"Wash clothes and bedding with vomit or poo on them separately, on a 60°C wash.",
])+
'<h2 id="care">Looking after yourself at home</h2>\n'+ul([
"<strong>Flu:</strong> rest and sleep, drink plenty of water, and take paracetamol or ibuprofen if needed. Don’t give aspirin to under-16s. Antibiotics do not work for flu.",
"<strong>Norovirus:</strong> drink lots of fluids, in small sips if you feel sick. Avoid fruit juice and fizzy drinks. It usually gets better in 2 to 3 days.",
"<strong>Get help from NHS 111 or your GP</strong> if you are worried about a baby or child, are pregnant, have a long-term condition or weak immune system, or flu symptoms don’t improve after 7 days.",
"<strong>Call 999</strong> if someone has severe difficulty breathing or starts coughing up blood.",
])+
'<h2 id="outbreak">In a bigger outbreak</h2>\n'+ul([
"Follow official advice from GOV.UK and the NHS. Advice will depend on the illness.",
"Check on neighbours and relatives by phone, and offer to drop off shopping or medicine.",
"Shop normally. Our food storage guide helps you build a small store over time, so there’s no need to stock up in a hurry.",
]),
[SRC_NRR,("GOV.UK Prepare: Infectious disease outbreaks",P+"/be-informed-about-hazards/health-infectious-disease-outbreaks/"),("GOV.UK Prepare: Antimicrobial resistance",P+"/be-informed-about-hazards/health-antimicrobial-resistance/"),("NHS: Flu","https://www.nhs.uk/conditions/flu/"),("NHS: Norovirus","https://www.nhs.uk/conditions/norovirus/"),("nidirect: Public health emergencies","https://www.nidirect.gov.uk/information-and-services/advice-specific-emergencies/public-health-emergencies")],
"How to prevent and cope with flu, norovirus and other illness at home in the UK, and how to prepare for a bigger outbreak, from the NHS and GOV.UK.")

# 7 Hospital back-up plan
guide("hospital-backup-plan","If you’re suddenly in hospital: a back-up plan for carers",
"If you look after someone, or have children or pets who rely on you, think now about who would step in if you were suddenly ill or had an accident.",
ready("Get ready now",[
"<strong>Choose a back-up person</strong>, such as a relative, friend or neighbour, who could step in for a few hours while proper arrangements are made (NHS).",
"<strong>Make sure they can get in.</strong> The NHS says they should have door keys or know the code to a key safe, and know what care is needed.",
"<strong>Write care notes</strong> and leave them somewhere obvious. Carers UK suggests including: the person’s name and address, who to contact, their medicines and where they are kept, allergies, GP and pharmacy, any treatment, care services, continence products, mobility aids, and anything others need to know about behaviour.",
"<strong>Share the plan.</strong> Talk it through with the person you care for and your emergency contacts, and give them a copy or tell them where it is (Carers UK). Review it regularly.",
"<strong>Ask for a carer’s assessment.</strong> The NHS says to contact adult social services at your local council. It can cover someone taking over so you can have a break.",
"<strong>Find the council’s out-of-hours team.</strong> Carers UK says councils have an emergency duty team you can contact when the office is closed. In Northern Ireland, use your Health and Social Care Trust.",
"<strong>Make your information easy to find.</strong> If appropriate, GOV.UK Prepare suggests wearing medical alert tags or bracelets and adding medical information to your phone.",
"<strong>Include pets and children</strong> in the plan: who would feed and walk pets, or collect children from school.",
"Use the <a href=\"https://www.carersuk.org/help-and-advice/practical-support/planning-for-emergencies/\">Carers UK</a> planning guide to build your plan, and add your back-up person to our <a href=\"../plan.html\">household plan</a>.",
],RI)+
'<h2 id="during">If it happens</h2>\n'+ul([
"Tell hospital staff straight away that you are a carer and someone is relying on you. The NHS says you’ll be asked for an emergency contact when you are admitted.",
"Call your back-up person, or ask someone to call them for you.",
"If no one can help, call the council’s adult social services or emergency duty team. If anyone is at immediate risk, call 999 (Carers UK).",
"For health advice for yourself or the person you look after, call NHS 111.",
])+
'<h2 id="after">Afterwards</h2>\n'+ul([
"Update your plan with anything you learned.",
"Talk to the council about extra support, such as respite care, if you need it.",
"If you need to talk, Carers UK points to Samaritans, free on 116 123, at any time.",
]),
[("GOV.UK Prepare: Advice for disabled persons and carers",P+"/get-prepared-for-emergencies/advice-for-disabled-persons-and-carers/"),("NHS: Carers’ breaks and respite care","https://www.nhs.uk/social-care-and-support/support-and-benefits-for-carers/carer-breaks-and-respite-care/"),("NHS: Carer’s assessments","https://www.nhs.uk/social-care-and-support/support-and-benefits-for-carers/carer-assessments/"),("NHS: Going into hospital as a patient","https://www.nhs.uk/nhs-services/hospitals/going-into-hospital/going-into-hospital-as-a-patient/"),("Carers UK: Planning for emergencies","https://www.carersuk.org/help-and-advice/practical-support/planning-for-emergencies/")],
"A simple back-up plan for UK carers: who steps in, care notes, keys and council contacts if you are suddenly in hospital.")

# 8 Fuel
guide("fuel-and-heating-oil","Fuel shortages and heating oil",
"Fuel shortages are uncommon and usually short. Homes heated by oil, and people who rely on a car in rural areas, can prepare with a few simple habits.",
nrrbox("<p>The register’s worst case for <strong>“Insolvency affecting fuel supply”</strong> (likelihood 4, 5–25%; impact 1, Minor) is a fuel company failing, which “could cause regional disruption to the production and supply of refined fuels, impacting road transport, aviation and domestic heating fuel.” It says “Impacts would be greatest during winter months”, and that sudden “adaptive purchasing” (buying more than usual) “could result in temporary fuel shortages.”</p>")+
ready("Get ready now",[
"<strong>Check your heating oil level regularly</strong>, and don’t wait until it is nearly empty. Citizens Advice says keep at least a quarter of a tank while you wait for a delivery, or the system could be damaged.",
"<strong>Order early.</strong> Citizens Advice says oil is usually cheaper in summer and early autumn, and a delivery in a few weeks is usually cheaper than an urgent one.",
"<strong>Shop around.</strong> Citizens Advice suggests getting at least 3 quotes from members of UKIFDA, the fuel distributors’ trade body.",
"<strong>Think about an oil club</strong>, where neighbours order together. Your local council may know of one (Citizens Advice).",
"<strong>Aged 75 or over?</strong> Citizens Advice says your supplier should add you to the Cold Weather Priority scheme, but check you are on it with each supplier.",
"<strong>Check your tank</strong> for cracks, leaks or rust, keep the area around it clear for deliveries, and get your boiler serviced each year by an OFTEC-registered technician (UKIFDA).",
"<strong>Have a back-up for warmth</strong>: warm layers, blankets and hot water bottles. See our <a href=\"cold-weather.html\">cold weather guide</a>.",
],RI)+
'<h2 id="during">If there is a fuel shortage</h2>\n'+ul([
"<strong>Buy as you normally would.</strong> The register says buying more than usual can turn a small problem into a temporary shortage.",
"The government’s fuel plan allows limits on how much fuel you can buy per visit, and priority fuel for emergency services, so everyone can get some.",
"Never use a barbecue, camping stove or generator indoors for heat. See our <a href=\"fire-and-carbon-monoxide.html\">fire and carbon monoxide guide</a>.",
])+
'<h2 id="after">Afterwards</h2>\n'+ul([
"Top up as normal, rather than filling up in a rush.",
"If you are struggling with heating costs, Citizens Advice lists help for people who use oil, LPG, coal or wood.",
]),
[SRC_NRR,("GOV.UK: Summary of response tools in the National Emergency Plan for Fuel","https://www.gov.uk/government/publications/energy-emergency-plans-priority-fuel-allocation/summary-of-response-tools-in-the-national-emergency-plan-for-fuel"),("Citizens Advice: Help if you use oil, LPG, coal or wood","https://www.citizensadvice.org.uk/consumer/energy/energy-supply/get-help-paying-your-bills/help-with-bills-if-you-use-alternative-fuels/"),("UKIFDA: Winter campaign 2026-27","https://ukifda.org/ukifda-winter-campaign-2026-27/")],
"How UK households can prepare for fuel shortages and heating oil delays: tank levels, ordering early, oil clubs and the Cold Weather Priority scheme.")

# 9 Run Hide Tell
guide("run-hide-tell","Terrorism: Run, Hide, Tell",
"The chance of being caught up in a terrorist attack is low. Knowing three simple words could help keep you and others safe.",
nrrbox("<p>The register rates <strong>“Terrorist attacks in publicly accessible locations”</strong> at likelihood 5 (more than 25%) and impact 4 (Significant). For malicious risks, likelihood is measured over 2 years. GOV.UK Prepare says: “the chance of being caught up in a terrorist incident remains low”.</p>")+
'<div class="note call"><p><strong>RUN</strong> to a place of safety. <strong>HIDE</strong> if you can’t run: silence your phone and turn off vibrate. <strong>TELL</strong> the police by calling 999 when it is safe.</p></div>\n'+
ready("Get ready now",[
"<strong>Learn Run, Hide, Tell</strong> and talk about it with your family.",
"<strong>Notice where the exits are</strong> when you are in buildings and on public transport (British Red Cross).",
"<strong>Save the Anti-Terrorism Hotline: 0800 789 321.</strong> You can also report online at <a href=\"https://act.campaign.gov.uk/\">ACT</a>. In an emergency, always call 999.",
"<strong>Learn some first aid.</strong> See our <a href=\"first-aid.html\">first aid guide</a>.",
"<strong>Travelling abroad?</strong> GOV.UK Prepare says check the Foreign Office travel advice for the country first.",
],RI)+
'<h2 id="during">If you are caught up in an attack</h2>\n'+ul([
"<strong>Run</strong> if there is a safe route. Insist others come with you, but don’t let them slow you down. Leave your belongings. Don’t film the incident.",
"<strong>Hide</strong> if you can’t run. Find cover from gunfire behind solid walls. Stay quiet, silence your phone and turn off vibrate. Lock or barricade yourself in if you can, and stay away from the door.",
"<strong>Tell</strong> the police on 999 when it is safe. Say what is happening, where, where the attackers are, and describe them. If you can’t speak, listen to the call taker’s instructions.",
])+
'<h2 id="after">Afterwards</h2>\n'+ul([
"If you saw anything useful, tell the police.",
"You may be in shock without realising it. See a doctor (British Red Cross).",
"The government-funded Support Hub for victims and survivors of terrorism has a free 24-hour line: 0808 168 9111.",
]),
[SRC_NRR,("GOV.UK Prepare: Terrorism",P+"/be-informed-about-hazards/terrorism/"),("ProtectUK: Run Hide Tell","https://www.protectuk.police.uk/advice-and-guidance/response/run-hide-tell"),("ACT: Report suspicious activity","https://act.campaign.gov.uk/"),("British Red Cross: Terrorist attack","https://www.redcross.org.uk/get-help/prepare-for-emergencies/how-to-prepare-in-case-of-a-terrorist-attack")],
"Run, Hide, Tell: what to do if you are caught up in a terrorist attack in the UK, and how to report suspicious activity.")

open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"<url><loc>{u}</loc><lastmod>{CHECKED_ISO}</lastmod></url>\n" for u in dict.fromkeys(PAGES))+"</urlset>\n")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n")
print("sitemap",len(set(PAGES)))
