# Diamond Retirement Strategies — website

Website for Diamond Retirement Strategies (Phoenix, AZ). Hosted on GitHub Pages, which builds the blog automatically with Jekyll — no software to install.

## Pages
`index.html` (Home) · `about.html` · `services.html` · `who-we-help.html` · `process.html` · `resources.html` · `blog.html` · `contact.html`

Blog posts live in `_posts/` as simple Markdown files. **To publish a post, see [BLOG-GUIDE.md](BLOG-GUIDE.md).**

## Publish with GitHub Pages
1. Repo **Settings → Pages**.
2. Source: **Deploy from a branch** → Branch `main`, folder `/ (root)` → Save.
3. After a minute the site is live at `https://spanglerdeluxe.github.io/DiamondRetirementStrategies/`.
4. Custom domain (e.g. `www.drstrategies.org`): enter it under **Settings → Pages → Custom domain**, then point the domain's DNS `CNAME` record to `spanglerdeluxe.github.io`.

## Before going live
- The two consultation forms are design-only. Connect them to a form service (e.g. Formspree) by adding an `action` and removing the demo handler in `site.js`.
- Have compliance review all copy (including blog posts) and add the current approval code to the footer.
- Confirm office hours, client commitments and bios.

## How it's built
- `_layouts/default.html` and `_layouts/post.html` — header, footer and article template used by the blog.
- `.pages.yml` — settings for the Pages CMS editor (app.pagescms.org).
- `_source/` — the design sources. Running `python3 _source/build.py` regenerates the pages into `_source/deploy`.
