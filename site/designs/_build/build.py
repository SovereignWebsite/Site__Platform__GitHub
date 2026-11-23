#!/usr/bin/env python3
"""Five designs of github.platform.sovereignweb.site's home page. design.c@SovereignWebsite.dinis, round 1.
Same words and the same working access view: each design keeps the page's ids (#signin, #token, #forget,
#status, #rate, #out, #detail) and loads the site's own /assets/gh.js. Usage: build.py <site dir>"""
import os, sys, html

SITE = sys.argv[1]
OUT = os.path.join(SITE, "designs")
HOST = "https://github.platform.sovereignweb.site"
e = html.escape
H1 = "Your GitHub access, at a glance"
MARK = "github.platform.sovereignweb.site"
INTRO = ("See every repository you can reach, your role on each, and who else has access: people, teams, deploy keys, "
         "webhooks and rulesets. It only reads. An unofficial site, not made or endorsed by GitHub.")
STAYS = [
    "It is kept only in this tab's memory: reload or close the tab and it is gone. It is never stored, never logged and never sent anywhere but <code>api.github.com</code>, straight from your browser. This site has no server.",
    "The page only reads: it makes GET requests and nothing else, so it cannot change your repositories even with a token that could.",
    'Make a <a href="https://github.com/settings/personal-access-tokens/new">fine-grained token</a> with read-only access: Metadata, Administration (to see people, keys and rulesets) and Webhooks, on the repositories you choose. Give it a short expiry. An organisation may need to approve it.',
]
NEXT = [
    "Each repository now shows what stands out: public with you as admin, archived, a fork, no push for a year; and in its access view, a deploy key that can push, a webhook without HTTPS, no active ruleset.",
    "Signing in with GitHub instead of pasting a token. GitHub's login step does not allow calls from a web page, so it needs one small exchange step off the page; that waits for the owner's word.",
    'For the SovereignWebsite organisation, changes are proposed to <a href="https://github.com/SovereignWebsite/SovereignWebsite__Factory">SovereignWebsite__Factory</a>, which runs it as code; this site never applies them.',
]
SENT = "When you press the button, your token goes from this tab to api.github.com and nowhere else; this page names only that host in its security policy."
DESIGNS = [
    (1, "Key Ring", "Every way into your repositories is a key; the page is the ring that holds them, with your token as the one you bring."),
    (2, "Strongroom", "A strongroom, dark first: the rules for your token on the door, the access view inside."),
    (3, "Register", "An access register: who may enter, each column ruled, the rules for the token as its front page."),
    (4, "Pre-flight", "A pre-flight checklist: what stands out, step by step, before you trust a repository."),
    (5, "Brief", "Everything on one plain page, for reading fast or printing."),
]
FAMILY = [("https://sovereignwebsite.ai/", "Sovereign Website"), ("https://sovereignwebsite.org/", "Principles"),
          ("https://sovereignwebsite.site/", "Hosted"), ("https://hub.sovereignweb.site/", "Hub"),
          ("https://agents.sovereignweb.site/", "Agents"), ("https://vault.sovereignwebsite.site/", "Vault"),
          ("https://agenticcells.ai/", "AgentiCCells"), ("https://riskmandate.ai/", "RiskMandate"),
          ("https://newsroom.sgit.ai/", "Newsroom")]
CSP = ("default-src 'self'; connect-src 'self' https://api.github.com; img-src 'self'; "
       "style-src 'self' 'unsafe-inline'; script-src 'self'; base-uri 'none'; form-action 'self'")

BASE = """
*{box-sizing:border-box}
html{color-scheme:light dark;-webkit-text-size-adjust:100%}
body{margin:0;font:1.0625rem/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;background:var(--bg);color:var(--fg);overflow-wrap:break-word}
a{color:var(--link)}
:focus-visible{outline:3px solid var(--focus);outline-offset:2px}
.skip{position:absolute;left:-999px;top:.5rem;z-index:99;background:var(--bg);color:var(--fg);padding:.5rem .9rem;border:2px solid var(--focus)}
.skip:focus{left:1rem}
main *{min-width:0}
.chrome{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;justify-content:flex-end;position:relative;z-index:5;padding-top:.5rem}
.chrome details{position:relative}
.chrome summary{cursor:pointer;list-style:none;min-height:44px;display:inline-flex;align-items:center;padding:.35rem .8rem;border:1px solid var(--ctl);border-radius:999px;font-size:.9rem;background:var(--bg);color:var(--fg)}
.chrome summary::-webkit-details-marker{display:none}
.chrome summary::after{content:"";width:.45rem;height:.45rem;margin-left:.5rem;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:rotate(45deg) translateY(-2px)}
.chrome details[open] summary::after{transform:rotate(-135deg)}
.chrome ul{position:absolute;right:0;top:calc(100% + .35rem);margin:0;padding:.4rem;list-style:none;min-width:15rem;max-width:calc(100vw - 2rem);background:var(--bg);color:var(--fg);border:1px solid var(--ctl);border-radius:.6rem;box-shadow:0 .6rem 1.6rem rgba(0,0,0,.25)}
.chrome li a{display:block;padding:.55rem .7rem;border-radius:.4rem;color:var(--fg);text-decoration:none;font-size:.95rem}
.chrome li a:hover,.chrome li a:focus-visible{background:var(--hover)}
.chrome li a[aria-current]{font-weight:700;text-decoration:underline}
.chrome .gap{border-top:1px solid var(--ctl);margin-top:.3rem;padding-top:.3rem}
.chrome small{display:block;font-size:.85rem;color:var(--muted);font-weight:400}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.signin{display:grid;grid-template-columns:1fr auto auto;gap:.4rem .6rem;align-items:end;margin:1.25rem 0 .5rem}
.signin label{font-size:.9rem;color:var(--muted);grid-row:1}
.signin label[for=__none]{grid-column:2}
.signin input,.signin select,.signin button{font:inherit;font-size:1rem;padding:.55rem .7rem;border:1px solid var(--ctl);border-radius:6px;background:var(--field);color:var(--fg);min-height:44px}
.signin input{grid-column:1;grid-row:2}.signin select{grid-column:2;grid-row:2}
.signin button{grid-column:3;grid-row:2;background:var(--accent);color:var(--on-accent);border-color:var(--accent);font-weight:700;cursor:pointer}
@media (max-width:30rem){.signin{grid-template-columns:1fr auto}.signin button{grid-column:1/-1;grid-row:3}}
.status{font-weight:700;min-height:1.6em}
.note{font-size:.95rem;color:var(--muted)}
button.small,.out select{font:inherit;font-size:1rem;padding:.4rem .7rem;border:1px solid var(--ctl);border-radius:6px;background:var(--field);color:var(--link);font-weight:700;min-height:44px;cursor:pointer}
.out select{color:var(--fg);font-weight:400}
.out label{color:var(--muted)}
#forget{margin:.3rem 0}
.out h3{font-size:1.1rem;margin:1rem 0 .3rem}
.out table{border-collapse:collapse;width:100%;font-size:.95rem}
.out caption{text-align:left;font-weight:700;padding:.4rem 0}
.out th,.out td{text-align:left;vertical-align:top;padding:.45rem .6rem;border-bottom:1px solid var(--line);overflow-wrap:anywhere}
.out thead th{color:var(--muted);font-size:.9rem}
.scroll{overflow-x:auto;margin:1rem 0}
.out table{border-collapse:collapse;width:100%;font-size:.95rem}
.out caption{text-align:left;font-weight:700;padding:.4rem 0}
.out th,.out td{text-align:left;vertical-align:top;padding:.45rem .6rem;border-bottom:1px solid var(--line)}
.out thead th{color:var(--muted);font-size:.9rem}
.out th .sub{display:block;font-weight:400;color:var(--muted);font-size:.875rem}
.out tr.group th{background:var(--hover);font-size:.875rem;letter-spacing:.06em;text-transform:uppercase}
.out td.vals{white-space:pre-wrap;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;overflow-wrap:anywhere}
.out td.ok{color:var(--ok);font-weight:700;white-space:nowrap}
.out td.bad{color:var(--bad);font-weight:700}
.out td.num{text-align:right;font-variant-numeric:tabular-nums}
.sent{font-size:.9rem;color:var(--muted)}
footer{padding:2rem 0 3rem;font-size:.95rem}
footer nav{display:flex;flex-wrap:wrap;gap:.25rem 1.25rem}
footer nav a{min-height:44px;display:inline-flex;align-items:center}
@media print{.chrome,.skip,.signin,#forget{display:none}}
"""


def head(n, css):
    name, idea = (DESIGNS[n - 1][1], DESIGNS[n - 1][2]) if n else ("", "")
    title = f"{name}, design {n} of GitHub" if n else "Five designs, GitHub"
    desc = (f"Design {n} of github.platform.sovereignweb.site, {name}: {idea}" if n else
            "Five designs of github.platform.sovereignweb.site, the same access view in five ideas, side by side.")
    url = f"{HOST}/designs/{n}/" if n else f"{HOST}/designs/"
    img = f"{HOST}/assets/share/card-1200x630.jpg"
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="GitHub">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="GitHub">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{img}">
<link rel="canonical" href="{url}">
<style>{BASE}{css}</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def chrome(n):
    d = "".join(f'<li><a href="/designs/{i}/"{" aria-current=\"page\"" if i == n else ""}>{i}. {nm}<small>{idea}</small></a></li>' for i, nm, idea in DESIGNS)
    fam = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in FAMILY)
    return f"""<nav class="chrome" aria-label="Designs and the Sovereign Website family">
<details><summary>Choose a design</summary><ul>{d}<li class="gap"><a href="/designs/">All five, side by side</a></li><li><a href="/">The site as it is now</a></li></ul></details>
<details><summary>Sovereign Website</summary><ul><li><a href="/start/">Start here</a></li><li><a href="/agents/">Use with your AI</a></li><li><a href="/admin/">How this site was made</a></li><li class="gap"><a href="/policy/">How this site is governed</a></li>{fam}</ul></details>
</nav>"""


def own(cls="own"):
    return f'<nav class="{cls}" aria-label="This site"><a href="#signin">Read my access</a><a href="#token-rules">Your token stays with you</a><a href="/start/">Start here</a><a href="/agents/">Use with your AI</a></nav>'


def form(btn="Read my access"):
    return f"""<form id="signin" class="signin" autocomplete="off">
<label for="token">Your GitHub token (fine-grained, read-only)</label>
<input id="token" name="token" type="password" spellcheck="false" autocapitalize="off" required>
<button type="submit">{btn}</button>
</form>
<p class="sent">{SENT}</p>
<button id="forget" type="button" class="small" hidden>Forget the token</button>
<p id="status" class="status" role="status" aria-live="polite"></p>
<p id="rate" class="note"></p>
<div class="out"><div id="out"></div><div id="detail"></div></div>"""


def ul(items, cls="plain"):
    return f'<ul class="{cls}">' + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def footer():
    return f"""<footer>
<nav aria-label="About this site"><a href="/start/">Start here</a> <a href="/agents/">Use with your AI</a> <a href="/admin/">How this site was made</a> <a href="/policy/">How this site is governed</a></nav>
<p>A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Platform__GitHub">github.com/SovereignWebsite/Site__Platform__GitHub</a>.</p>
</footer>
<script src="/assets/gh.js" defer></script>
</body>
</html>
"""



# ---------------------------------------------------------------- 1. Key Ring
CSS1 = """
:root{--bg:#f7f4ee;--fg:#1d1b18;--muted:#57524a;--link:#7a3e12;--focus:#7a3e12;--ctl:#7d776c;--hover:#ece7dc;--field:#ffffff;--accent:#7a3e12;--on-accent:#ffffff;--line:#ddd6c8;--ok:#1d6b45;--bad:#a13a2a;--brass:#b07a2a;--tag:#fffdf8}
@media (prefers-color-scheme:dark){:root{--bg:#16140f;--fg:#efe9de;--muted:#c0b8a8;--link:#f0b27a;--focus:#f0b27a;--ctl:#8b8476;--hover:#24211b;--field:#1d1a15;--accent:#f0b27a;--on-accent:#1a0f06;--line:#3a352c;--ok:#86ddb3;--bad:#ff9b8a;--brass:#d9a85a;--tag:#1d1a15}}
.wrap{max-width:66rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:.5rem 1rem;padding:.5rem 0}
.brand{font-weight:800;font-size:1.2rem;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center;gap:.5rem}
.brand::before{content:"";width:1.4rem;height:1.4rem;border:4px solid var(--brass);border-radius:50%}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
.k{font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:1.5rem 0 .3rem}
h1{font-size:clamp(2.1rem,6vw,3.6rem);line-height:1.05;margin:0 0 1rem;letter-spacing:-.02em}
h2{font-size:clamp(1.45rem,3.4vw,2rem);margin:0 0 .4rem}
.lede{max-width:44rem;font-size:1.1rem}
.key{position:relative;background:var(--tag);border:2px solid var(--brass);border-radius:1.2rem 1.2rem 1.2rem 4rem;padding:1.25rem 1.25rem 1.25rem 2.5rem;margin:1.5rem 0}
.key::before{content:"";position:absolute;left:.9rem;top:1.25rem;width:.8rem;height:.8rem;border:3px solid var(--brass);border-radius:50%}
.tags{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,19rem),1fr));margin:2rem 0}
.tags section{background:var(--tag);border:1px solid var(--line);border-left:6px solid var(--brass);border-radius:.4rem 1rem 1rem .4rem;padding:1rem 1.2rem}
.plain{padding-left:1.1rem;margin:.4rem 0}.plain li{margin:.5rem 0}
footer{border-top:1px solid var(--line)}
"""


def d1():
    return head(1, CSS1) + f"""<div class="wrap">{chrome(1)}
<header class="mast"><a class="brand" href="/">GitHub</a>{own()}</header>
<main id="main"><p class="k">{MARK}</p><h1>{H1}</h1><p class="lede">{INTRO}</p>
<div class="key">{form()}</div>
<div class="tags"><section id="token-rules" aria-labelledby="h-st"><h2 id="h-st">Your token stays with you</h2>{ul(STAYS)}</section>
<section aria-labelledby="h-nx"><h2 id="h-nx">What comes next</h2>{ul(NEXT)}</section></div>
</main>
""" + footer().replace("</body>", "</div></body>")


# ---------------------------------------------------------------- 2. Strongroom (dark first, way out there)
CSS2 = """
:root{--bg:#0c0f12;--fg:#eef2f5;--muted:#b3bcc6;--link:#8fd3ff;--focus:#8fd3ff;--ctl:#7d8794;--hover:#18202a;--field:#121820;--accent:#8fd3ff;--on-accent:#06121a;--line:#26303c;--ok:#86ddb3;--bad:#ff9b8a;--steel:#1a222c;--rivet:#5d6b7a}
@media (prefers-color-scheme:light){:root{--bg:#eef1f4;--fg:#0e1318;--muted:#47525e;--link:#0b5394;--focus:#0b5394;--ctl:#6d7884;--hover:#dfe4ea;--field:#ffffff;--accent:#0b5394;--on-accent:#ffffff;--line:#c9d1da;--ok:#1d6b45;--bad:#a13a2a;--steel:#ffffff;--rivet:#9aa6b2}}
.wrap{max-width:76rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:.5rem 1rem;padding:.5rem 0}
.brand{font:800 1.1rem/1 ui-monospace,Menlo,Consolas,monospace;letter-spacing:.2em;text-transform:uppercase;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
.door{display:grid;gap:1.5rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,24rem),1fr));padding:clamp(1.5rem,4vw,3rem) 0;align-items:start}
.k{font:700 .85rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0}
h1{font-size:clamp(2.1rem,6vw,3.8rem);line-height:1.02;margin:.4rem 0 1rem;letter-spacing:-.02em}
h2{font-size:clamp(1.3rem,3vw,1.7rem);margin:0 0 .5rem}
.plate{background:var(--steel);border:1px solid var(--line);border-radius:1rem;padding:1.25rem;position:relative;box-shadow:inset 0 0 0 6px var(--bg),inset 0 0 0 7px var(--line)}
.plate::before,.plate::after{content:"";position:absolute;top:.7rem;width:.5rem;height:.5rem;border-radius:50%;background:var(--rivet)}
.plate::before{left:.7rem}.plate::after{right:.7rem}
.inside{background:var(--steel);border:1px solid var(--line);border-radius:1rem;padding:1.25rem;margin:0 0 2rem}
.plain{padding-left:1.1rem;margin:.4rem 0}.plain li{margin:.5rem 0}
footer{border-top:1px solid var(--line)}
"""


def d2():
    return head(2, CSS2) + f"""<div class="wrap">{chrome(2)}
<header class="mast"><a class="brand" href="/">GitHub</a>{own()}</header>
<main id="main">
<div class="door"><div><p class="k">{MARK}</p><h1>{H1}</h1><p>{INTRO}</p>
<section class="plate" id="token-rules" aria-labelledby="h-st"><h2 id="h-st">Your token stays with you</h2>{ul(STAYS)}</section></div>
<section class="plate" aria-labelledby="h-in"><h2 id="h-in">Open the view</h2>{form()}</section></div>
<section class="inside" aria-labelledby="h-nx"><h2 id="h-nx">What comes next</h2>{ul(NEXT)}</section>
</main>
""" + footer().replace("</body>", "</div></body>")


# ---------------------------------------------------------------- 3. Register
CSS3 = """
:root{--bg:#fbfaf6;--fg:#1b1a17;--muted:#56524a;--link:#1f4f7a;--focus:#1f4f7a;--ctl:#7f796e;--hover:#efece3;--field:#ffffff;--accent:#1f4f7a;--on-accent:#ffffff;--line:#d7d1c3;--ok:#1d6b45;--bad:#a13a2a;--rule:#b9b09d}
@media (prefers-color-scheme:dark){:root{--bg:#161512;--fg:#efece4;--muted:#c0baae;--link:#9cc8f0;--focus:#9cc8f0;--ctl:#8b8578;--hover:#24221d;--field:#1d1b17;--accent:#9cc8f0;--on-accent:#0b1420;--line:#3b3831;--ok:#86ddb3;--bad:#ff9b8a;--rule:#5a5446}}
.wrap{max-width:64rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:.5rem 1rem;padding:.5rem 0;border-bottom:3px double var(--rule)}
.brand{font:700 1.25rem Georgia,"Iowan Old Style","Times New Roman",serif;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
h1,h2{font-family:Georgia,"Iowan Old Style","Times New Roman",serif}
.title{text-align:center;padding:clamp(1.5rem,5vw,3rem) 0 1rem;border-bottom:1px solid var(--rule)}
.k{font:600 .85rem ui-monospace,Menlo,Consolas,monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0}
h1{font-size:clamp(2.1rem,6vw,3.4rem);line-height:1.08;margin:.6rem auto 1rem;max-width:20ch}
.title p{max-width:42rem;margin:0 auto}
.leaf{display:grid;gap:2rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,22rem),1fr));padding:2rem 0;border-bottom:1px solid var(--rule)}
h2{font-size:1.45rem;margin:0 0 .4rem}
.plain{list-style:none;padding:0;margin:0;counter-reset:n}
.plain li{counter-increment:n;padding:.55rem 0 .55rem 2.2rem;position:relative;border-bottom:1px solid var(--line)}
.plain li::before{content:counter(n,decimal-leading-zero);position:absolute;left:0;font:700 .9rem ui-monospace,Menlo,Consolas,monospace;color:var(--muted)}
.entry{padding:2rem 0}
footer{border-top:3px double var(--rule)}
"""


def d3():
    return head(3, CSS3) + f"""<div class="wrap">{chrome(3)}
<header class="mast"><a class="brand" href="/">GitHub</a>{own()}</header>
<main id="main">
<div class="title"><p class="k">The access register · {MARK}</p><h1>{H1}</h1><p>{INTRO}</p></div>
<div class="leaf"><section id="token-rules" aria-labelledby="h-st"><h2 id="h-st">Your token stays with you</h2>{ul(STAYS)}</section>
<section aria-labelledby="h-en"><h2 id="h-en">Make an entry</h2>{form()}</section></div>
<section class="entry" aria-labelledby="h-nx"><h2 id="h-nx">What comes next</h2>{ul(NEXT)}</section>
</main>
""" + footer().replace("</body>", "</div></body>")


# ---------------------------------------------------------------- 4. Pre-flight
CSS4 = """
:root{--bg:#f2f5f2;--fg:#111a14;--muted:#46524a;--link:#14663f;--focus:#14663f;--ctl:#6f7b73;--hover:#e1e8e2;--field:#ffffff;--accent:#14663f;--on-accent:#ffffff;--line:#cfd9d1;--ok:#14663f;--bad:#a13a2a;--card:#ffffff;--amber:#7a4e00}
@media (prefers-color-scheme:dark){:root{--bg:#0d120f;--fg:#e9f0eb;--muted:#b0bdb4;--link:#86ddb3;--focus:#86ddb3;--ctl:#7b877f;--hover:#18211b;--field:#131a15;--accent:#86ddb3;--on-accent:#08140d;--line:#29342c;--ok:#86ddb3;--bad:#ff9b8a;--card:#131a15;--amber:#ffcf6e}}
.wrap{max-width:72rem;margin:0 auto;padding:0 1rem}
.mast{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:.5rem 1rem;padding:.5rem 0}
.brand{font-weight:800;font-size:1.2rem;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:.25rem 1rem;font-size:.95rem}.own a{color:var(--fg);min-height:44px;display:inline-flex;align-items:center}
.k{font-size:.85rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin:1.5rem 0 .3rem}
h1{font-size:clamp(2.1rem,6vw,3.6rem);line-height:1.05;margin:0 0 1rem;letter-spacing:-.02em}
h2{font-size:clamp(1.3rem,3vw,1.7rem);margin:0 0 .5rem}
.lede{max-width:44rem;font-size:1.1rem}
.list{list-style:none;margin:1.5rem 0;padding:0;display:grid;gap:1rem;counter-reset:c}
.list>li{counter-increment:c;background:var(--card);border:1px solid var(--line);border-radius:.8rem;padding:1.1rem 1.2rem 1.1rem 4rem;position:relative}
.list>li::before{content:counter(c);position:absolute;left:1rem;top:1rem;width:2.2rem;height:2.2rem;border:3px solid var(--accent);border-radius:.4rem;display:grid;place-items:center;font-weight:800;color:var(--accent)}
.plain{padding-left:1.1rem;margin:.4rem 0}.plain li{margin:.5rem 0}
footer{border-top:1px solid var(--line)}
"""


def d4():
    return head(4, CSS4) + f"""<div class="wrap">{chrome(4)}
<header class="mast"><a class="brand" href="/">GitHub</a>{own()}</header>
<main id="main"><p class="k">Pre-flight · {MARK}</p><h1>{H1}</h1><p class="lede">{INTRO}</p>
<ol class="list">
<li id="token-rules"><h2>Check how your token is kept</h2>{ul(STAYS)}</li>
<li><h2>Read your access</h2>{form()}</li>
<li><h2>What comes next</h2>{ul(NEXT)}</li>
</ol>
</main>
""" + footer().replace("</body>", "</div></body>")


# ---------------------------------------------------------------- 5. Brief
CSS5 = """
:root{--bg:#ffffff;--fg:#111111;--muted:#4a4a4a;--link:#0b4f8a;--focus:#0b4f8a;--ctl:#767676;--hover:#f0f0f0;--field:#ffffff;--accent:#0b4f8a;--on-accent:#ffffff;--line:#d6d6d6;--ok:#1d6b45;--bad:#a13a2a}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--fg:#f1f1f1;--muted:#bdbdbd;--link:#8cc4ff;--focus:#8cc4ff;--ctl:#8a8a8a;--hover:#222;--field:#1a1a1a;--accent:#8cc4ff;--on-accent:#0b0b0b;--line:#333;--ok:#86ddb3;--bad:#ff9b8a}}
.wrap{max-width:42rem;margin:0 auto;padding:0 1rem}
.brand{font:700 1.1rem Georgia,"Times New Roman",serif;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.own{display:flex;flex-wrap:wrap;gap:0 1rem;font-size:.95rem}.own a{min-height:44px;display:inline-flex;align-items:center}
h1{font:700 clamp(2rem,6vw,2.6rem)/1.15 Georgia,serif;margin:1.25rem 0 .75rem}
h2{font:700 1.45rem Georgia,serif;margin:2rem 0 .4rem;padding-top:1rem;border-top:1px solid var(--line)}
.plain{padding-left:1.2rem}.plain li{margin:.4rem 0}
footer{border-top:1px solid var(--line);margin-top:2rem}
"""


def d5():
    return head(5, CSS5) + f"""<div class="wrap">{chrome(5)}
<header><a class="brand" href="/">GitHub</a>{own()}</header>
<main id="main"><p>{MARK}</p><h1>{H1}</h1><p>{INTRO}</p>{form()}
<h2 id="token-rules">Your token stays with you</h2>{ul(STAYS)}
<h2>What comes next</h2>{ul(NEXT)}</main>
""" + footer().replace("</body>", "</div></body>")


CSSI = """
:root{--bg:#f6f5f2;--fg:#151515;--muted:#4f4c47;--link:#7a3e12;--focus:#7a3e12;--ctl:#77736c;--hover:#e9e6df;--card:#fff;--line:#dcd8cf;--field:#fff;--accent:#7a3e12;--on-accent:#fff;--ok:#1d6b45;--bad:#a13a2a}
@media (prefers-color-scheme:dark){:root{--bg:#121212;--fg:#efede8;--muted:#bdb9b1;--link:#f0b27a;--focus:#f0b27a;--ctl:#85817a;--hover:#222;--card:#1c1c1c;--line:#333;--field:#1a1a1a;--accent:#f0b27a;--on-accent:#1a0f06;--ok:#86ddb3;--bad:#ff9b8a}}
.wrap{max-width:76rem;margin:0 auto;padding:0 1rem}
.brand{font-weight:800;color:var(--fg);text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
h1{font:700 clamp(2rem,5.5vw,3rem)/1.1 Georgia,serif;margin:1rem 0 .75rem}
.cards{list-style:none;margin:1.5rem 0 3rem;padding:0;display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fit,minmax(min(100%,20rem),1fr))}
.cards li{background:var(--card);border:1px solid var(--line);border-radius:.6rem;overflow:hidden}
.cards img{display:block;max-width:100%;height:auto;aspect-ratio:16/10;object-fit:cover;object-position:top;width:100%;border-bottom:1px solid var(--line)}
.cards .b{padding:1rem}.cards h2{font-size:1.2rem;margin:0 0 .3rem}.cards p{margin:.3rem 0}
footer{border-top:1px solid var(--line)}
"""


def index(rec):
    cards = "".join(f'<li><img src="/designs/{i}/shot-1366.webp" alt="Design {i}, {nm}, at desktop width" width="1366" height="854" loading="lazy"><div class="b"><h2><a href="/designs/{i}/">{i}. {nm}</a></h2><p>{idea}</p>{"<p><strong>Recommended by the designer.</strong></p>" if i == rec else ""}</div></li>' for i, nm, idea in DESIGNS)
    f = footer().replace('<script src="/assets/gh.js" defer></script>\n', "")
    return head(0, CSSI) + f"""<div class="wrap">{chrome(0)}
<header><a class="brand" href="/">GitHub</a></header>
<main id="main"><h1>Five designs of this site</h1>
<p>The same access view and the same words, in five ideas. Each one works: paste a read-only token and press the button. The owner picks one; the keeper makes it the site.</p>
<ul class="cards">{cards}</ul></main>
""" + f.replace("</body>", "</div></body>")


if __name__ == "__main__":
    for i, f in {1: d1, 2: d2, 3: d3, 4: d4, 5: d5}.items():
        os.makedirs(f"{OUT}/{i}", exist_ok=True)
        open(f"{OUT}/{i}/index.html", "w").write(f())
    open(f"{OUT}/index.html", "w").write(index(int(os.environ.get("RECOMMEND", "4"))))
    print("built", OUT)
