import pathlib, re
SRC = pathlib.Path(__file__).parent / "src"
OUT = pathlib.Path(__file__).parent / "out"
OUT.mkdir(exist_ok=True)

PHONE = "480.750.2999"
TEL = "tel:+14807502999"

NAV = [("about", "about.html", "About"), ("services", "services.html", "Services"),
       ("who", "who-we-help.html", "Who We Help"), ("process", "process.html", "Our Process"),
       ("resources", "resources.html", "Resources"), ("blog", "blog.html", "Blog"),
       ("contact", "contact.html", "Contact")]

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
      <ul><li><a href="about.html">About us</a></li><li><a href="services.html">Services</a></li><li><a href="who-we-help.html">Who we help</a></li><li><a href="process.html">Our process</a></li><li><a href="resources.html">Resources &amp; FAQ</a></li><li><a href="blog.html">Blog</a></li></ul>
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

GEM_LINE = '<span class="gem-line" aria-hidden="true"><img src="drs-mark.png" alt="" width="760" height="578"></span>'

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
ASSETS = pathlib.Path(__file__).parent.parent/'assets'
if not ASSETS.exists(): ASSETS = pathlib.Path(__file__).parent/'assets'
for _f in ['drs-mark.png','drs-logo.png','favicon-32.png','favicon-192.png','apple-touch-icon.png','favicon.ico']:
    shutil.copy(ASSETS/_f, OUT/_f)

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

(OUT / "site.css").write_text((SRC / "base.css").read_text() + (SRC / "extra.css").read_text() + (SRC / "vfx.css").read_text() + (SRC / "blog.css").read_text())
(OUT / "site.js").write_text((SRC / "site.js").read_text() + "\n" + (SRC / "vfx.js").read_text())

import datetime, markdown, yaml, html as _html

SKELETON_STYLE = '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}html{scrollbar-gutter:stable}.brand .logo-img{height:72px;width:auto}</style>'
DESC = "Diamond Retirement Strategies helps individuals, couples and families in Phoenix, AZ plan dependable retirement income: rollovers, annuities, Medicare, long-term care and life insurance."

def inner(key, main, strip):
    return f'''{header(key)}
<main id="top">
{main}
{CTA_STRIP if strip else ""}
</main>
{FOOTER}
<script src="site.js"></script>'''

def full_doc(title, body, desc=DESC):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="claude:viewport-fit-sides" content="cover">
{FONTS}
{SKELETON_STYLE}
</head>
<body>
{body}
</body>
</html>
'''

# ---------------- Blog data ----------------
CAT_ICON = GEM_LINE.replace('class="gem-line"', 'class="thumb-mark"')

def load_posts():
    posts = []
    for f in sorted((SRC / "posts").glob("*.md")):
        raw = f.read_text()
        _, fm, body = raw.split("---", 2)
        meta = yaml.safe_load(fm)
        slug = f.stem[11:]
        d = meta["date"] if isinstance(meta["date"], datetime.date) else datetime.date.fromisoformat(str(meta["date"]))
        words = len(re.findall(r"\w+", body))
        posts.append(dict(meta, slug=slug, file=f.name, date=d, body=body.strip(),
                          html=markdown.markdown(body, extensions=["extra", "sane_lists"]),
                          url=f"blog-{slug}.html", mins=words // 200 + 1))
    return sorted(posts, key=lambda p: p["date"], reverse=True)

def fmt(d): return d.strftime("%B ") + str(d.day) + d.strftime(", %Y")

def thumb(cat, image=None):
    if image:
        return f'<div class="post-thumb"><img src="{image}" alt="" loading="lazy"></div>'
    return f'<div class="post-thumb" aria-hidden="true">{CAT_ICON}<span class="cat">{_html.escape(cat)}</span></div>'

def card(p, featured=False):
    return f'''<a class="post-card{' featured' if featured else ''}" href="{p['url']}" data-cat="{_html.escape(p['category'])}">
        {thumb(p['category'], p.get('image'))}
        <div class="body">
          <p class="meta">{_html.escape(p['category'])} · <time datetime="{p['date'].isoformat()}">{fmt(p['date'])}</time></p>
          <h3>{_html.escape(p['title'])}</h3>
          <p>{_html.escape(p['excerpt'])}</p>
          <span class="go">Read article →</span>
        </div>
      </a>'''

BLOG_HERO = page_hero("Blog", "Insights for a <em>confident</em> retirement.",
                      "Plain-English articles on retirement income, Social Security, Medicare and more from the team at Diamond Retirement Strategies.")

def blog_index(cards_html, filters_html):
    return f'''{BLOG_HERO}
<section class="band" aria-label="Articles">
  <div class="wrap">
    <div class="filters" role="group" aria-label="Filter by topic">{filters_html}</div>
    <div class="post-grid">
      {cards_html}
    </div>
    <p class="empty" id="noPosts" hidden>No articles in this topic yet.</p>
  </div>
</section>'''

ASIDE = f'''<aside class="post-aside">
        <div class="card">
          <p class="tag">Have a question?</p>
          <h3>Talk it through with us</h3>
          <p>Every situation is different. A free consultation shows how this applies to you.</p>
          <a class="btn btn-ink" href="contact.html">Book a consultation</a>
          <p>Or call <strong>{PHONE}</strong></p>
        </div>
        <a class="back" href="blog.html">← All articles</a>
      </aside>'''

POST_DISCLAIMER = '<p class="post-disclaimer">This article is for general information only and is not tax, legal or investment advice. Rules and limits change; please talk with a qualified professional about your own situation.</p>'

def post_main(title, cat, date_iso, date_txt, mins, author, cover, body, more):
    return f'''<section class="page-hero">
  {GEM_LINE}
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="blog.html">Blog</a><span aria-hidden="true">/</span><span>{cat}</span></p>
    <h1>{title}</h1>
    <p class="post-meta"><span><time datetime="{date_iso}">{date_txt}</time></span><span>{mins} min read</span><span>{author}</span></p>
  </div>
</section>
<section class="band" aria-label="Article">
  <div class="wrap post-layout">
    <article>
      {cover}
      <div class="article">
{body}
      </div>
      {POST_DISCLAIMER}
    </article>
    {ASIDE}
  </div>
</section>
<section class="band band-alt" aria-labelledby="moreTitle">
  <div class="wrap">
    <div class="sec-row"><div class="sec-head"><p class="eyebrow">Keep reading</p><h2 id="moreTitle">More from the blog</h2></div><a class="textlink" href="blog.html">All articles →</a></div>
    <div class="post-grid" style="margin-top:40px">
      {more}
    </div>
  </div>
</section>'''

# ---------------- Preview build (claude.ai artifact) ----------------
posts = load_posts()
cats = []
for p in posts:
    if p["category"] not in cats: cats.append(p["category"])
filters = '<button type="button" data-filter="all" aria-pressed="true">All topics</button>' + "".join(
    f'<button type="button" data-filter="{_html.escape(c)}" aria-pressed="false">{_html.escape(c)}</button>' for c in cats)
blog_main = blog_index("\n      ".join(card(p, i == 0) for i, p in enumerate(posts)), filters)

GENERATED = {}  # fname -> (title, key, main, strip, desc)
for fname, title, key, body, strip in PAGES:
    GENERATED[fname] = (title, key, render_body((SRC / "pages" / body).read_text()), strip, DESC)
GENERATED["blog.html"] = ("Blog · Diamond Retirement Strategies", "blog", blog_main, True, "Articles on retirement income, Social Security, Medicare and more from Diamond Retirement Strategies.")
for p in posts:
    more = "\n      ".join(card(q) for q in posts if q is not p)[:]
    cover = f'<figure class="post-cover"><img src="{p["image"]}" alt=""></figure>' if p.get("image") else ""
    main = post_main(_html.escape(p["title"]), _html.escape(p["category"]), p["date"].isoformat(), fmt(p["date"]),
                     p["mins"], _html.escape(p.get("author", "Diamond Retirement Strategies")), cover, p["html"], more)
    GENERATED[p["url"]] = (f'{p["title"]} · Diamond Retirement Strategies', "blog", main, False, _html.escape(p["excerpt"]))

for fname, (title, key, main, strip, desc) in GENERATED.items():
    body = inner(key, main, strip)
    if fname == "index.html":
        html = f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{FONTS}\n<style>html{{scrollbar-gutter:stable}}.brand .logo-img{{height:72px;width:auto}}</style>\n' + body
    else:
        html = full_doc(_html.escape(title, quote=False), body, desc)
    (OUT / fname).write_text(html)
print("preview pages:", len(GENERATED))

# ---------------- Deploy build (GitHub Pages + Jekyll) ----------------
DEPLOY = pathlib.Path(__file__).parent / "deploy"
if DEPLOY.exists(): shutil.rmtree(DEPLOY)
DEPLOY.mkdir()
for f in ["site.css", "site.js", "drs-mark.png", "drs-logo.png", "favicon-32.png", "favicon-192.png", "apple-touch-icon.png", "favicon.ico"]:
    shutil.copy(OUT / f, DEPLOY / f)
for fname, (title, key, main, strip, desc) in GENERATED.items():
    if fname.startswith("blog"): continue  # blog pages are generated by Jekyll
    (DEPLOY / fname).write_text(full_doc(_html.escape(title, quote=False), inner(key, main, strip), desc).replace('<meta name="claude:viewport-fit-sides" content="cover">\n', ''))

# _posts
(DEPLOY / "_posts").mkdir()
for p in posts:
    shutil.copy(SRC / "posts" / p["file"], DEPLOY / "_posts" / p["file"])
(DEPLOY / "assets" / "blog").mkdir(parents=True)
(DEPLOY / "assets" / "blog" / ".gitkeep").write_text("")

# Jekyll config
(DEPLOY / "_config.yml").write_text(f'''title: Diamond Retirement Strategies
description: "{DESC}"
permalink: /blog-:title:output_ext
markdown: kramdown
timezone: America/Phoenix
exclude:
  - README.md
  - BLOG-GUIDE.md
  - _source
defaults:
  - scope:
      path: ""
      type: posts
    values:
      layout: post
      author: Diamond Retirement Strategies
''')

LIQ_THUMB = ('{% if post.image %}<div class="post-thumb"><img src="{{ post.image }}" alt="" loading="lazy"></div>'
             '{% else %}<div class="post-thumb" aria-hidden="true">' + CAT_ICON + '<span class="cat">{{ post.category }}</span></div>{% endif %}')
LIQ_CARD = ('<a class="post-card{% if forloop.first and featured %} featured{% endif %}" href="{{ post.url | remove_first: \'/\' }}" data-cat="{{ post.category }}">'
            + LIQ_THUMB +
            '<div class="body"><p class="meta">{{ post.category }} · <time datetime="{{ post.date | date: \'%Y-%m-%d\' }}">{{ post.date | date: "%B %-d, %Y" }}</time></p>'
            '<h3>{{ post.title }}</h3><p>{{ post.excerpt | strip_html | strip }}</p><span class="go">Read article →</span></div></a>')

layouts = DEPLOY / "_layouts"; layouts.mkdir()
default = full_doc("{% if page.title %}{{ page.title }} · {% endif %}Diamond Retirement Strategies",
                   inner("blog", "{{ content }}", False).replace("</main>", "{% if page.cta %}" + CTA_STRIP + "{% endif %}\n</main>"),
                   "{% if page.excerpt %}{{ page.excerpt | strip_html | strip | truncate: 160 }}{% else %}{{ site.description }}{% endif %}"
                   ).replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
(layouts / "default.html").write_text(default)
liquid_more = ('{% assign featured = false %}{% assign shown = 0 %}{% for post in site.posts %}{% if post.url != page.url and shown < 3 %}'
               + LIQ_CARD + '{% assign shown = shown | plus: 1 %}{% endif %}{% endfor %}')
post_layout = "---\nlayout: default\n---\n" + post_main(
    "{{ page.title }}", "{{ page.category }}", "{{ page.date | date: '%Y-%m-%d' }}", '{{ page.date | date: "%B %-d, %Y" }}',
    "{{ content | number_of_words | divided_by: 200 | plus: 1 }}", "{{ page.author }}",
    '{% if page.image %}<figure class="post-cover"><img src="{{ page.image }}" alt=""></figure>{% endif %}',
    "{{ content }}", liquid_more)
(layouts / "post.html").write_text(post_layout)

liquid_filters = ('<button type="button" data-filter="all" aria-pressed="true">All topics</button>'
                  '{% assign cats = site.posts | map: "category" | uniq %}{% for c in cats %}'
                  '<button type="button" data-filter="{{ c }}" aria-pressed="false">{{ c }}</button>{% endfor %}')
liquid_cards = '{% assign featured = true %}{% for post in site.posts %}' + LIQ_CARD + '{% endfor %}'
(DEPLOY / "blog.html").write_text("---\nlayout: default\ntitle: Blog\ncta: true\n---\n" + blog_index(liquid_cards, liquid_filters))

# Pages CMS (friendly editor at app.pagescms.org)
(DEPLOY / ".pages.yml").write_text('''media:
  input: assets/blog
  output: assets/blog
content:
  - name: posts
    label: Blog posts
    type: collection
    path: _posts
    filename: "{year}-{month}-{day}-{primary}.md"
    view:
      fields: [ title, category, date ]
      default:
        sort: date
        order: desc
    fields:
      - name: title
        label: Title
        type: string
        required: true
      - name: date
        label: Publish date
        type: date
        required: true
      - name: category
        label: Topic
        type: select
        required: true
        options:
          values: [ "Retirement Income", "Social Security", "Medicare", "Rollovers", "Long-Term Care", "Life Insurance & Legacy", "Taxes", "Firm News" ]
      - name: excerpt
        label: Summary (shown on the blog page, 1–2 sentences)
        type: text
        required: true
      - name: image
        label: Cover image (optional)
        type: image
      - name: author
        label: Author
        type: string
        default: Diamond Retirement Strategies
      - name: body
        label: Article
        type: rich-text
''')
shutil.copytree(SRC.parent / "deploy_extra", DEPLOY, dirs_exist_ok=True) if (SRC.parent / "deploy_extra").exists() else None
# keep sources for future edits
srcdir = DEPLOY / "_source"; srcdir.mkdir()
shutil.copytree(SRC, srcdir / "src"); shutil.copy(__file__, srcdir / "build.py")
shutil.copytree(ASSETS, srcdir / "assets", ignore=shutil.ignore_patterns("ARE-6794*"))
print("deploy files:", sum(1 for _ in DEPLOY.rglob("*") if _.is_file()))
