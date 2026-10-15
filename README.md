# Diamond Retirement Strategies — website

Static website for Diamond Retirement Strategies (Phoenix, AZ). Plain HTML/CSS/JS — no build step needed to host it.

## Pages
`index.html` (Home) · `about.html` · `services.html` · `who-we-help.html` · `process.html` · `resources.html` · `contact.html`

Shared files: `site.css`, `site.js`, `drs-logo.png`, favicons.

## Publish with GitHub Pages
1. Repo **Settings → Pages**.
2. Source: **Deploy from a branch** → Branch `main`, folder `/ (root)` → Save.
3. After a minute the site is live at `https://spanglerdeluxe.github.io/DiamondRetirementStrategies/`.
4. Custom domain (e.g. `www.drstrategies.org`): enter it under **Settings → Pages → Custom domain**, then point the domain's DNS `CNAME` record to `spanglerdeluxe.github.io`.

## Before going live
- The two consultation forms are design-only. Connect them to a form service (e.g. Formspree, Basin, Netlify Forms) by adding an `action` and removing the demo handler in `site.js`.
- Have compliance review all copy and add the current approval code to the footer.
- Confirm office hours, client commitments and bios.

## Editing
Edit the HTML files directly, or edit the sources in `_source/src` and run `python3 _source/build.py` (outputs to `_source/out`).
