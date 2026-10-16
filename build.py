# Generates the static pages. Run: python3 build.py
import os
CHECKED="15 October 2026"
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
G=[("power-cut","Power cut"),("water-outage","No water (water outage)"),("gas-heating","No gas or heating"),("priority-services-register","Priority Services Register"),("grow-your-own","Grow some of your own food"),("rainwater","Collecting rainwater safely"),("first-aid","First aid at home")]
page("guides/index.html","Guides","<h1>Guides</h1><p class=\"lead\">Short, calm guides for when things stop working.</p><ul class=\"tick\">"+"".join(f'<li><a href="{s}.html">{t}</a></li>' for s,t in G)+f"</ul><p class=\"meta\">All guides last checked {CHECKED}.</p>","Short guides: power cut, water outage, gas and heating, Priority Services Register, growing food, rainwater and first aid.")

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

<h2>Water butts and sizes</h2>
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
{sources([("RHS: Collecting, storing and reusing water",RHSW),("RHS: Managing water in your garden","https://www.rhs.org.uk/gardening-for-the-environment/water"),("Drinking Water Inspectorate: Receiving a boil water notice","https://www.dwi.gov.uk/receiving-a-boil-water-notice/"),("Drinking Water Inspectorate: Protecting your private water supply (rainwater harvesting)","https://www.dwi.gov.uk/private-water-supplies/customers-receiving-pws/protecting-your-private-water-supply/"),("South East Water: Boil water and do not drink notices","https://www.southeastwater.co.uk/help/works-and-outages/our-promise-to-you-if-your-water-supply-is-interrupted/"),("UKHSA (GOV.UK): Mosquito control","https://www.gov.uk/government/publications/mosquito-control"),("NHS: Legionnaires’ disease","https://www.nhs.uk/conditions/legionnaires-disease/"),("Water Regs UK: Connecting mains water to other water sources","https://www.waterregsuk.co.uk/topics/all-faqs/can-mains-water-supplies-be-connected-to-installations-also-supplied-by-another-alternative-source-of-water/"),("Water Supply (Water Fittings) Regulations 1999 (legislation.gov.uk)","https://www.legislation.gov.uk/uksi/1999/1148/contents/made"),("GOV.UK Prepare: Water supply interruptions or outages",P+"/be-informed-about-hazards/water-supply-interruptions-or-outages/")])}
''',"How to collect rainwater safely in the UK: water butts, safe uses, why it is not drinking water, and keeping it separate from mains.")

page("guides/first-aid.html","First aid at home",f'''
<h1>First aid at home</h1>
<p class="meta">Last checked: <time datetime="2026-10-15">{CHECKED}</time></p>
<p class="lead">A simple first aid kit and a few basic steps can help while you wait for help, especially during a power cut or a cold snap. This page sums up the official advice and links to it in full.</p>
<div class="note call"><p><strong>This guide does not replace first aid training.</strong> It is a short summary of advice from the NHS, St John Ambulance and the British Red Cross. Always follow the full official page and the instructions of the 999 call handler. If someone is seriously ill or injured, call 999.</p></div>

<h2>Your home first aid kit</h2>
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
