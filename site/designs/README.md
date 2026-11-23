# Five designs of github.platform.sovereignweb.site

Round 1 by design.c@SovereignWebsite.dinis (account C), 23 November 2026. The same words as the home page at dev 538378c and the same working access view: each design keeps the page's ids (#signin, #token, #forget, #status, #rate, #out, #detail) and loads the site's own /assets/gh.js. Checked against SovereignWebsite/Site__Agent__Design docs/guidelines.md and docs/rating.md. Unofficial, not made or endorsed by GitHub; none of the five copies GitHub's own look.

Each design carries a Content Security Policy that names only api.github.com, and says next to the form where the token goes (guidelines 1.3). Nothing loads from another host when the page opens.

## The five

1. **Key Ring.** Every way into your repositories is a key: the form is a brass key tag, the rules and next steps hang as tags.
2. **Strongroom** (dark first). A strongroom door: the rules for your token riveted on the plate, the access view opened inside.
3. **Register.** An access register: a title page, the token rules as numbered entries, the form as "Make an entry".
4. **Pre-flight.** A checklist to run before you trust a repository: check how your token is kept, read your access, see what comes next.
5. **Brief.** Everything on one plain page.

## Rating (rating.md)

Checked locally at 320, 390 and 1366 px, light and dark: axe-core 4.10 finds nothing at any impact; the site's own .github/ci/axe.mjs, html-validate, share-check and quality pass; no sideways scroll; nothing from another host on load, and only api.github.com when the button is pressed (tested with a made-up token, which GitHub refused as expected; the results tables were not seen with a real token). Each is a 3 (candidate). Honest note for round 2: designs 1, 3 and 4 share one column structure; at least two should rebuild the page around the results (the repository list and the flags) once they can be seen with a real read-only token.

## Recommendation

**4, Pre-flight.** It puts the token's safety first, then the one action, which is the order a careful owner wants. Strongroom is second, for the most striking look.

## How to rebuild

`python3 site/designs/_build/build.py site` from the repository root.
