import pathlib, re
SRC = pathlib.Path(__file__).parent / "src"
OUT = pathlib.Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

PHONE = "480.750.2999"
TEL = "tel:+14807502999"

NAV = [("about", "about.html", "About"), ("services", "services.html", "Services"),
       ("who", "who-we-help.html", "Who We Help"), ("process", "process.html", "Our Process"),
       ("resources", "resources.html", "Resources"), ("contact", "contact.html", "Contact")]

LOGO = '<img class="logo-img" src="drs-logo.png" width="600" height="408" alt="Diamond Retirement Strategies">'

def header(active):
    cur = ' aria-current="page"'
    links = "\n      ".join(
        f'<a href="{h}"{cur if k == active else ""}>{t}</a>' for k, h, t in NAV)
    return f'''<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="index.html" aria-label="Diamond Retirement Strategies home">
      {LOGO}
    </a>
    <button class="menu-btn" id="menuBtn" aria-controls="siteNav" aria-expanded="false" aria-label="Open menu"><span></span></button>
    <nav class="nav" id="siteNav" data-open="false" aria-label="Main">
      {links}
      <a class="btn btn-ink" href="contact.html">Book a consultation</a>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer>
  <div class="wrap foot-grid">
    <div class="foot-brand">
      <span class="logo-plate"><img class="logo-img" src="drs-logo.png" width="600" height="408" alt="Diamond Retirement Strategies"></span>
      <p>Retirement income planning for individuals, couples and families in Phoenix and across the Valley.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul><li><a href="about.html">About us</a></li><li><a href="services.html">Services</a></li><li><a href="who-we-help.html">Who we help</a></li><li><a href="process.html">Our process</a></li><li><a href="resources.html">Resources &amp; FAQ</a></li></ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul><li><a href="contact.html">Book a consultation</a></li><li>Phone {PHONE}</li><li>Fax 480.636.7734</li><li>Phoenix, AZ · Valley-wide</li></ul>
    </div>
    <div>
      <h4>Follow</h4>
      <ul><li><a href="https://www.facebook.com/Diamond-Retirement-Strategies-104124224723516/" target="_blank" rel="noopener">Facebook</a></li><li><a href="https://www.linkedin.com/in/michele-diamond-5115a460" target="_blank" rel="noopener">LinkedIn</a></li><li><a href="https://drsestateplan.com" target="_blank" rel="noopener">DRS Estate Planning</a></li></ul>
    </div>
  </div>
  <div class="wrap legal">
    <p>Licensed Insurance Professional. Life insurance and annuities can be used in a variety of retirement planning strategies. Guarantees are backed by the financial strength and claims-paying ability of the issuing insurance company.</p>
    <p>This material has been prepared for informational purposes only. It is not intended to provide, and should not be relied upon for, accounting, legal, tax or investment advice. Diamond Retirement Strategies is not affiliated with or endorsed by the Social Security Administration, Medicare or any government agency.</p>
    <p>© 2026 Diamond Retirement Strategies</p>
  </div>
</footer>'''

CTA_STRIP = f'''<section class="band cta" aria-label="Book a consultation">
  <div class="wrap strip">
    <div>
      <p class="eyebrow">Let's begin</p>
      <h2>Ready for a clear look at your retirement income?</h2>
      <p>Book a no-cost, no-obligation review with our team. Most first meetings take about an hour.</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-gem" href="contact.html">Book a consultation</a>
      <a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a>
    </div>
  </div>
</section>'''

GEM_LINE = '''<svg class="gem-line" viewBox="0 0 200 170" aria-hidden="true"><g fill="none" stroke="rgba(220,220,245,.55)" stroke-width="1"><path d="M45 10h110l40 45L100 165 5 55z"/><path d="M5 55h190M45 10l20 45 35-45 35 45 20-45M65 55l35 110 35-110"/></g></svg>'''

def page_hero(crumb, h1, lede):
    return f'''<section class="page-hero">
  {GEM_LINE}
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></p>
    <h1>{h1}</h1>
    <p>{lede}</p>
  </div>
</section>'''

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&family=Open+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="site.css">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="favicon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">'''

import shutil
for _f in ['drs-logo.png','favicon-32.png','favicon-192.png','apple-touch-icon.png','favicon.ico']:
    shutil.copy(pathlib.Path(__file__).parent/'assets'/_f, OUT/_f)

PAGES = [
    # file, <title>, nav key, body, cta strip?
    ("index.html", "Diamond Retirement Strategies", None, "home.html", False),
    ("about.html", "About Us · Diamond Retirement Strategies", "about", "about.html", True),
    ("services.html", "Services · Diamond Retirement Strategies", "services", "services.html", True),
    ("who-we-help.html", "Who We Help · Diamond Retirement Strategies", "who", "who.html", True),
    ("process.html", "Our Process · Diamond Retirement Strategies", "process", "process.html", True),
    ("resources.html", "Resources & FAQ · Diamond Retirement Strategies", "resources", "resources.html", True),
    ("contact.html", "Contact · Diamond Retirement Strategies", "contact", "contact.html", False),
]

def render_body(text):
    # {{hero|crumb|h1|lede}} macro
    def rep(m):
        crumb, h1, lede = m.group(1).split("||")
        return page_hero(crumb.strip(), h1.strip(), lede.strip())
    text = re.sub(r"\{\{hero\|(.*?)\}\}", rep, text, flags=re.S)
    return text.replace("{{PHONE}}", PHONE).replace("{{TEL}}", TEL)

(OUT / "site.css").write_text((SRC / "base.css").read_text() + (SRC / "extra.css").read_text() + (SRC / "vfx.css").read_text())
(OUT / "site.js").write_text((SRC / "site.js").read_text() + "\n" + (SRC / "vfx.js").read_text())

for fname, title, key, body, strip in PAGES:
    main = render_body((SRC / "pages" / body).read_text())
    inner = f'''{header(key)}
<main id="top">
{main}
{CTA_STRIP if strip else ""}
</main>
{FOOTER}
<script src="site.js"></script>'''
    head = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n'
    if fname == "index.html":
        html = head + inner  # published page: skeleton added at publish
    else:
        html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
</head>
<body>
{inner}
</body>
</html>'''
    (OUT / fname).write_text(html)
    print("built", fname, len(html))
