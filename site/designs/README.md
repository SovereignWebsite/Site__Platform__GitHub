# Five designs of github.platform.sovereignweb.site

Round 1 by design.c@SovereignWebsite.dinis (account C), 23 November 2026. The same words as the home page at dev 538378c and the same working access view: each design keeps the page's ids (#signin, #token, #forget, #status, #rate, #out, #detail) and loads the site's own /assets/gh.js. Checked against SovereignWebsite/Site__Agent__Design docs/guidelines.md and docs/rating.md. Unofficial, not made or endorsed by GitHub; none of the five copies GitHub's own look.

Each design carries a Content Security Policy that names only api.github.com, and says next to the form where the token goes (guidelines 1.3). Nothing loads from another host when the page opens.

## Round 2 (23 November 2026, 16:44 UTC)

Round 1's honest note asked for at least two designs rebuilt around the results. Done for two:
- **Key Ring** is now a workbench: the token form and its rules in a left rail, and "The ring: every way in" (the repository list and each access view) as the main area beside it.
- **Register** now makes the results the body of the book: the front page (the token rules and "Make an entry"), then "The register" with the repository list at full width.
In both, an empty-state line says where the results appear, and hides itself once they do; the tables keep whole words and scroll inside their own box. Tested with a mocked GitHub API (made-up repositories, in the test browser only, never published): results render, axe-core clean at every impact, no sideways scroll, light and dark, 390 and 1366 px.

## The five

1. **Key Ring.** A workbench: the token as a brass key tag in a rail, the ring of every way in (the results) as the main area.
2. **Strongroom** (dark first). A strongroom door: the rules for your token riveted on the plate, the access view opened inside.
3. **Register.** An access register: a title page, the token rules as numbered entries, the form as "Make an entry", and the register itself (the results) as the body.
4. **Pre-flight.** A checklist to run before you trust a repository: check how your token is kept, read your access, see what comes next.
5. **Brief.** Everything on one plain page.

## Rating (rating.md)

Checked locally at 320, 390 and 1366 px, light and dark: axe-core 4.10 finds nothing at any impact; the site's own .github/ci/axe.mjs, html-validate, share-check and quality pass; no sideways scroll; nothing from another host on load, and only api.github.com when the button is pressed (tested with a made-up token, which GitHub refused as expected; the results tables were not seen with a real token). Each is a 3 (candidate). Round 2 rebuilt designs 1 and 3 around the results (see above).

## Recommendation

**4, Pre-flight.** It puts the token's safety first, then the one action, which is the order a careful owner wants. Strongroom is second, for the most striking look.

## How to rebuild

`python3 site/designs/_build/build.py site` from the repository root.
