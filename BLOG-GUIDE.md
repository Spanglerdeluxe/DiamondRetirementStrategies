# How to post on the Diamond Retirement Strategies blog

You can publish a new article in about five minutes, without touching any code. The site rebuilds itself about a minute after you save.

There are two ways to do it. **Option A is the easiest** and the one we recommend for Michele and Carrie.

---

## Option A — Pages CMS (a simple editor, like Word)

**One-time setup (2 minutes)**

1. Go to **https://app.pagescms.org** and click **Sign in with GitHub**.
2. Approve access to the `DiamondRetirementStrategies` repository.
3. Open the project. You'll see **Blog posts** in the left menu.

**To write a new post**

1. Click **Blog posts → Add an entry**.
2. Fill in the form:
   - **Title** – the headline.
   - **Publish date** – today's date (or the date you want shown).
   - **Topic** – pick one (Medicare, Social Security, etc.). Topics become the filter buttons on the blog page.
   - **Summary** – 1–2 sentences shown on the blog page under the title.
   - **Cover image** – optional. Upload a photo; if you skip it, a navy diamond graphic is used.
   - **Article** – write the post. Use the toolbar for headings, bold, lists and links.
3. Click **Save**. That's it — the post appears on the site in about a minute.

**To edit or delete a post:** open it from the Blog posts list, make changes and Save, or use the ⋯ menu to delete.

---

## Option B — Directly on GitHub

1. Open the repository on github.com and go into the **`_posts`** folder.
2. Click **Add file → Create new file**.
3. Name the file with the date first, then the title in lowercase with dashes:
   `2026-11-03-your-post-title.md`
4. Paste this at the top and fill it in:

```
---
title: "Your Post Title"
date: 2026-11-03
category: Medicare
excerpt: "One or two sentences that appear on the blog page."
---

Write the article here.

## A section heading

Normal paragraphs are just text. Use **bold** for emphasis,
- dashes for bullet lists,
and [link text](contact.html) for links.
```

5. Click **Commit changes**. The post goes live in about a minute.

---

## Tips

- **Topics:** use one of these so the filters stay tidy: Retirement Income, Social Security, Medicare, Rollovers, Long-Term Care, Life Insurance & Legacy, Taxes, Firm News.
- **Future dates:** a post with a date in the future won't appear until that date.
- **Compliance:** get each article approved before you publish, and keep the approval code in your records. Every post automatically shows a short "not tax, legal or investment advice" note at the bottom.
- **Links to book a meeting:** link to `contact.html` to send readers to the consultation form.
