#!/usr/bin/env python3
"""Builds the BB DSP manual site into docs/ (served by GitHub Pages).

    python3 build.py

Words live in content.py; this file holds the page templates, the house-style
colour maths and the small text-free animations shown on each page.
"""
import html, os, re
from content import PLUGINS, KINDS

OUT = os.path.join (os.path.dirname (os.path.abspath (__file__)), "docs")

# --- House colours -----------------------------------------------------------
FRAME, CHARCOAL, CARD, LCD = "#B3B3B3", "#4D4D4D", "#FBFAF6", "#232019"

def rgb (h):  h = h.lstrip ("#"); return [int (h[i:i+2], 16) / 255 for i in (0, 2, 4)]
def hexs (c): return "#" + "".join (f"{round (max (0, min (1, v)) * 255):02X}" for v in c)
def lum (c):
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = map (f, c); return 0.2126 * r + 0.7152 * g + 0.0722 * b
def contrast (a, b):
    la, lb = sorted ((lum (a), lum (b)), reverse=True); return (la + 0.05) / (lb + 0.05)
def mix (a, b, t): return [x + (y - x) * t for x, y in zip (a, b)]

def readable_on (accent, bg, toward, need=4.5):
    """Nudges an accent towards `toward` until it reads on `bg` (like LookAndFeelTE::onLcd)."""
    a, b, d = rgb (accent), rgb (bg), rgb (toward)
    for i in range (0, 101):
        c = mix (a, d, i / 100)
        if contrast (c, b) >= need: return hexs (c)
    return hexs (d)

def accent_vars (accent):
    a = rgb (accent)
    ink = readable_on (accent, CARD, "#1E1C18")            # accent as text on the cream card
    lcd = readable_on (accent, LCD, "#FFFFFF", 5.0)         # accent as digits in a dark well
    on  = "#1E1C18" if contrast (a, rgb ("#1E1C18")) > contrast (a, rgb (CARD)) else CARD
    soft = hexs (mix (a, rgb (CARD), 0.86))
    return f"--accent:{accent};--accent-ink:{ink};--accent-lcd:{lcd};--accent-on:{on};--accent-soft:{soft};"

# --- Titles keep their lowercase i -------------------------------------------
def title (name, cls="t"):
    """BDRmono has no lowercase, so each 'i' is drawn by CSS (stem, flag, foot, diamond dot)."""
    inner = "".join (LI if ch == "i" else html.escape (ch) for ch in name)
    return f'<span class="{cls}"><span class="sr">{html.escape (name)}</span><span aria-hidden="true">{inner}</span></span>'

# An inline SVG sits on the text baseline, sized in em to one BDRmono cell.
# Measured from the face: advance .678em, cap height .80em, stroke .15em.
LI = ('<svg class="li" viewBox="0 0 68 80"><path d="M3 24h30v41h17v15H1V65h17V39H3z"/>'
      '<path d="M25.5 0l8 8-8 8-8-8z"/></svg>')

def labelise (text):
    """Control names in content.py write plugin names with a lowercase i too."""
    return re.sub (r"\b[A-Zi]*i[A-Zi]*\b", lambda m: title (m.group (0)) if re.search ("[A-Z]", m.group (0)) else m.group (0), text)

# --- The BB DSP mark -----------------------------------------------------------
LOGO = """<svg class="logo" viewBox="280 185 1390 1410" role="img" aria-label="BB DSP">
<g fill="#B3B3B3">
<polygon points="697,472 971,200 1253,476 1156,573 971,397 796,571"/>
<polygon points="697,472 971,200 1253,476 1156,573 971,397 796,571" transform="rotate(90 973 891)"/>
<polygon points="697,472 971,200 1253,476 1156,573 971,397 796,571" transform="rotate(180 973 891)"/>
<polygon points="697,472 971,200 1253,476 1156,573 971,397 796,571" transform="rotate(270 973 891)"/>
</g>
<g fill="#4D4D4D" fill-rule="evenodd">
<path d="M959,493 L657,799 L748,890 L656,985 L958,1290 Z M863,725 L791,799 L862,869 Z M861,913 L790,985 L862,1058 Z"/>
<path d="M959,493 L657,799 L748,890 L656,985 L958,1290 Z M863,725 L791,799 L862,869 Z M861,913 L790,985 L862,1058 Z" transform="translate(1951 0) scale(-1 1)"/>
</g>
<circle class="m m1" cx="674" cy="587" r="42" fill="#E8352A"/>
<line class="m m2" x1="1236" y1="560" x2="1306" y2="628" stroke="#3B80C4" stroke-width="26"/>
<rect class="m m3" x="551" y="832" width="122" height="122" fill="#EB712F" transform="rotate(45 612 893)"/>
<rect class="m m4" x="1279" y="828" width="122" height="122" fill="#62D1B5" transform="rotate(45 1340 889)"/>
<line class="m m5" x1="646" y1="1152" x2="714" y2="1220" stroke="#F4C443" stroke-width="26"/>
<circle class="m m6" cx="1270" cy="1192" r="42" fill="#7DD23F"/>
</svg>"""

def mark (size=18):
    return (f'<svg class="mk" width="{size}" height="{size}" viewBox="0 0 20 20" aria-hidden="true">'
            f'<rect x="5" y="5" width="10" height="10" transform="rotate(45 10 10)" fill="var(--accent)"/></svg>')

# --- Text-free animations, one per plugin --------------------------------------
# Each shows what the effect does, through shape, size, position and the accent.
A, G, C = "var(--accent)", FRAME, CHARCOAL
def svg (body): return f'<svg class="motion" viewBox="0 0 240 240" aria-hidden="true">{body}</svg>'

MOTIONS = {
"pipe": svg (f"""
<line x1="20" y1="120" x2="220" y2="120" stroke="{G}" stroke-width="4"/>
<rect x="60" y="100" width="40" height="40" fill="none" stroke="{G}" stroke-width="3"/>
<rect x="140" y="100" width="40" height="40" fill="none" stroke="{G}" stroke-width="3" transform="rotate(45 160 120)"/>
<g><rect x="-10" y="-10" width="20" height="20" fill="{C}">
<animate attributeName="fill" values="{C};{C};var(--accent);var(--accent);{C}" keyTimes="0;.25;.32;.75;1" dur="4s" repeatCount="indefinite"/>
<animateTransform attributeName="transform" type="rotate" values="0;0;45;45;90" keyTimes="0;.62;.68;.95;1" dur="4s" repeatCount="indefinite"/></rect>
<animateTransform attributeName="transform" type="translate" values="20 120;220 120" dur="4s" repeatCount="indefinite"/></g>"""),
"prism": svg (f"""
<g opacity=".9">{''.join (f'''<g><rect x="-22" y="-22" width="44" height="44" transform="rotate(45)" fill="{col}"/>
<animateTransform attributeName="transform" type="translate" values="120 120;{x} {y};{x} {y};120 120" keyTimes="0;.35;.7;1" dur="5s" repeatCount="indefinite"/></g>'''
 for col, x, y in (("#E8352A", 60, 150), ("#F4C443", 120, 80), ("#3B80C4", 180, 150)))}</g>
<rect x="98" y="98" width="44" height="44" transform="rotate(45 120 120)" fill="{C}">
<animate attributeName="opacity" values="1;0;0;1" keyTimes="0;.3;.75;1" dur="5s" repeatCount="indefinite"/></rect>"""),
"borealis": svg ("".join (
    f'<rect x="{18 + i * 26}" y="40" width="14" height="160" fill="{col}" opacity=".15">'
    f'<animate attributeName="opacity" values=".12;.9;.12" dur="{2.2 + (i * 7 % 5) * .55}s" begin="{i * .37}s" repeatCount="indefinite"/></rect>'
    for i, col in enumerate (("#D9342B", "#EC6A2C", "#F2A93B", "#E8D44A", "#6CC24A", "#3BB3A0", "#3B80C4", "#5F5069")))),
"quiver": svg (f"""
<line x1="30" y1="110" x2="210" y2="110" stroke="{G}" stroke-width="3" stroke-dasharray="8 8"/>
<rect x="80" y="110" width="80" height="90" fill="{C}"/>
<rect x="80" y="60" width="80" height="50" fill="var(--accent)" style="transform-origin:120px 110px;animation:jelly 0.5s ease-in-out infinite alternate"/>"""),
"reverie": svg (f"""
<rect x="70" y="70" width="100" height="100" fill="none" stroke="{G}" stroke-width="3"/>
<rect x="70" y="70" width="100" height="100" fill="var(--accent)" style="transform-origin:120px 120px;animation:spin 6s linear infinite">
<animate attributeName="rx" values="0;50;0" dur="6s" repeatCount="indefinite"/></rect>"""),
"blip": svg (f"""
<rect x="20" y="160" width="200" height="4" fill="{G}"/>
<rect x="20" y="100" width="40" height="40" fill="var(--accent)" style="animation:stutter 2.4s steps(1) infinite"/>
{''.join (f'<rect x="{x}" y="176" width="10" height="10" transform="rotate(45 {x+5} 181)" fill="{G}"/>' for x in range (25, 220, 25))}"""),
"ionise": svg (f"""
<rect x="70" y="70" width="100" height="100" fill="none" stroke="{G}" stroke-width="3" transform="rotate(45 120 120)"/>
<rect x="85" y="85" width="70" height="70" fill="{C}" transform="rotate(45 120 120)">
<animate attributeName="fill" values="{C};var(--accent);var(--accent);{C};var(--accent);{C};{C}" keyTimes="0;.08;.3;.34;.4;.46;1" dur="1.6s" calcMode="discrete" repeatCount="indefinite"/></rect>"""),
"ripple": svg (f"""
<g style="animation:bob 3.2s ease-in-out infinite"><rect x="90" y="78" width="60" height="60" fill="var(--accent)"/>
<rect x="90" y="122" width="60" height="16" fill="{G}"/></g>
{''.join (f'<circle cx="{x}" cy="132" r="3" fill="{C}"><animate attributeName="cy" values="132;{126 if i%2 else 138};132" dur="2.4s" begin="{i*.15}s" repeatCount="indefinite"/></circle>' for i, x in enumerate (range (16, 236, 14)))}"""),
"inhale": svg (f"""
<rect x="60" y="60" width="120" height="120" fill="var(--accent)" style="transform-origin:120px 120px;animation:breathe 3s ease-in infinite">
<animate attributeName="rx" values="60;60;0;0" keyTimes="0;.1;.85;1" dur="3s" repeatCount="indefinite"/></rect>
<rect x="95" y="95" width="50" height="50" fill="{C}" style="transform-origin:120px 120px;animation:punch 3s infinite"/>"""),
"interlude": svg (f"""
<line x1="20" y1="170" x2="220" y2="170" stroke="{G}" stroke-width="3"/>
<rect x="30" y="110" width="70" height="60" fill="{C}" style="animation:phrase 4s infinite"/>
<rect x="140" y="110" width="70" height="60" fill="{C}" style="animation:phrase 4s 2s infinite"/>
<circle cx="120" cy="120" r="40" fill="var(--accent)" style="transform-origin:120px 140px;animation:gap 4s infinite"/>"""),
"twirl": svg (f"""
<rect x="40" y="100" width="40" height="40" fill="none" stroke="{G}" stroke-width="3"/>
<g style="animation:sway 2.6s ease-in-out infinite alternate"><rect x="130" y="95" width="50" height="50" fill="var(--accent)" style="transform-origin:155px 120px;animation:spin 2.6s linear infinite"/></g>"""),
"hiraeth": svg (f"""
<g style="transform-origin:120px 120px;animation:breathe 5s ease-out infinite"><rect x="70" y="70" width="100" height="100" fill="none" stroke="{G}" stroke-width="3" transform="rotate(45 120 120)"/></g>
<rect x="90" y="90" width="60" height="60" fill="var(--accent)" transform="rotate(45 120 120)">
<animate attributeName="opacity" values=".2;1;1;.2" keyTimes="0;.4;.7;1" dur="5s" repeatCount="indefinite"/></rect>
{''.join (f'<rect x="{117 + 70*dx}" y="{117 + 70*dy}" width="6" height="6" fill="var(--accent)"><animate attributeName="opacity" values="0;0;1;0" keyTimes="0;.6;.8;1" dur="5s" repeatCount="indefinite"/></rect>' for dx, dy in ((1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)))}"""),
}

# --- Page shell ------------------------------------------------------------------
def nav (active):
    items = [("index.html", "PLUG-INS", "home"), ("getting-started.html", "GETTING STARTED", "start")]
    links = "".join (f'<a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{title (t)}</a>' for h, t, k in items)
    return f"""<header class="top"><div class="wrap top-in">
<a class="brand" href="index.html">{LOGO}<span><b>BB DSP</b><small>DIGITAL SONIC PLAYGROUND</small></span></a>
<nav>{links}</nav></div></header>"""

def page (fname, title_text, body, active="", style="", desc=""):
    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape (title_text)}</title>
<meta name="description" content="{html.escape (desc)}">
<link rel="icon" href="assets/mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head><body style="{style}">
{nav (active)}
<main>{body}</main>
<footer class="foot"><div class="wrap">{mark (14)}<span>BB DSP · Digital Sonic Playground</span><span class="sp"></span><span>AU · VST3 · Standalone · macOS</span></div></footer>
<script src="assets/site.js"></script>
</body></html>"""
    with open (os.path.join (OUT, fname), "w") as f: f.write (doc)

def lcd (value, wide=False):
    return f'<span class="lcd{" w" if wide else ""}">{html.escape (value)}</span>'

# --- Home ----------------------------------------------------------------------
def build_home():
    cards = []
    for p in PLUGINS:
        img = p["images"][0][0]
        cards.append (f"""<a class="pcard" href="{p['slug']}.html" data-kind="{p['kind']}" style="{accent_vars (p['accent'])}">
<div class="pcard-h">{mark()}{title (p['name'])}<span class="chip">{KINDS[p['kind']]}</span></div>
<div class="pcard-img{' dark' if p.get('dark') else ''}"><img src="img/{p['slug']}/{img}" alt="{html.escape (p['name'])} interface" loading="lazy"></div>
<p>{html.escape (p['tagline'])}</p></a>""")
    kinds = [("all", "ALL")] + [(k, v) for k, v in KINDS.items()]
    seg = "".join (f'<button type="button" data-filter="{k}"{" class=\"on\"" if k == "all" else ""}>{v}</button>' for k, v in kinds)
    body = f"""
<section class="hero wrap">
<div class="hero-txt">
<p class="eyebrow">{mark()}<span>USER MANUALS</span></p>
<h1>Sound you can <em>see</em>.</h1>
<p class="lede">BB DSP makes audio and MIDI plug-ins for macOS. Every one is built around a single moving shape that shows what is happening to your sound right now. These pages explain what each control does, how to set each plug-in up in your DAW, and a few ways to get started.</p>
<p class="cta"><a class="btn" href="#plugins">BROWSE THE PLUG-INS</a><a class="btn ghost" href="getting-started.html">GETTING STARTED</a></p>
</div>
<div class="hero-logo">{LOGO}</div>
</section>
<section class="wrap" id="plugins">
<div class="bar"><h2 class="sec">{mark()}<span>{"PLUG-INS"}</span><span class="count">{len (PLUGINS):02d}</span></h2>
<div class="seg" role="group" aria-label="Filter by type">{seg}</div></div>
<div class="grid">{''.join (cards)}</div>
</section>"""
    page ("index.html", "BB DSP Manuals", body, "home",
          desc="User manuals for BB DSP audio and MIDI plug-ins.")

# --- Getting started -------------------------------------------------------------
def build_start():
    st = accent_vars ("#F26419")
    rows = [
        ("KNOB", "drag", "Drag up or down to turn. The flip counter beside it shows the value."),
        ("COUNTER", "click", "Click the digits to type an exact value, then press Return."),
        ("DROPDOWN", "click", "Click the dark box to pick from a list."),
        ("SWITCH", "click", "Segmented switches light the chosen option in the plug-in's colour."),
        ("ON", "click", "Turns the plug-in or card on. Off passes the sound through untouched."),
        ("MIN", "click", "Folds a card down to just its animation."),
        ("PRESET", "click", "Header menu of factory sounds (on plug-ins that have them)."),
        ("OPTIONS", "click", "Swaps the main page for the set-and-forget settings."),
    ]
    tbl = "".join (f'<div class="row"><div class="rn">{title (n)}</div><div class="rv">{lcd (v.upper())}</div><div class="rd">{html.escape (d)}</div></div>' for n, v, d in rows)
    places = [
        ("AUDIO FX", "Insert in an Audio FX slot on any audio or instrument track.", "QUiVER, REVERiE, BLiP, iONiSE, RiPPLE, iNHALE, iNTERLUDE, TWiRL, HiRAETH"),
        ("INSTRUMENT", "Load as the track's software instrument.", "BOREALiS"),
        ("MIDI FX", "Insert in the MIDI FX slot above the instrument. Its CC output reaches the instrument on the same track only.", "PiPELiNE"),
        ("MIDI-CONTROLLED FX", "In Logic, load in a Software Instrument track's INSTRUMENT slot under AU MIDI-controlled Effects, then pick the audio source in the plug-in header's Side Chain menu.", "PRiSM"),
    ]
    pl = "".join (f'<div class="place"><h3>{title (k)}</h3><p>{html.escape (t)}</p><p class="who">{labelise (html.escape (w))}</p></div>' for k, t, w in places)
    body = f"""
<section class="wrap doc">
<p class="eyebrow">{mark()}<span>GETTING STARTED</span></p>
<h1 class="ph">Set up once, then play.</h1>
<p class="lede">Every BB DSP plug-in shares the same controls, the same colours and the same layout, so once you know one, you know them all.</p>

<h2 class="sec">{mark()}<span>INSTALLING</span></h2>
<div class="card"><p>Each plug-in comes as an <b>AU</b> component, a <b>VST3</b> and a <b>Standalone</b> app. Copy them to:</p>
<div class="paths"><div>{lcd ("AU", True)}<code>~/Library/Audio/Plug-Ins/Components/</code></div>
<div>{lcd ("VST3", True)}<code>~/Library/Audio/Plug-Ins/VST3/</code></div>
<div>{lcd ("APP", True)}<code>/Applications/</code></div></div>
<p>Then restart your DAW so it rescans. In Logic Pro, new plug-ins appear under <b>Audio Units → BB DSP</b>. If one is missing, open the Plug-in Manager and choose <b>Reset &amp; Rescan Selection</b>.</p></div>

<h2 class="sec">{mark()}<span>WHERE EACH ONE GOES</span></h2>
<div class="places">{pl}</div>

<h2 class="sec">{mark()}<span>THE CONTROLS</span></h2>
<div class="card table">{tbl}</div>

<h2 class="sec">{mark()}<span>READING THE COLOURS</span></h2>
<div class="card colours">
<div><span class="sw" style="background:{FRAME}"></span><p><b>Frame grey</b> is structure: tracks, guides, outlines and thresholds.</p></div>
<div><span class="sw" style="background:{CHARCOAL}"></span><p><b>Charcoal</b> is a shape at rest: nothing is happening to the sound.</p></div>
<div><span class="sw" style="background:var(--accent)"></span><p><b>The plug-in's own colour</b> means active right now. If you see it move, the effect is working.</p></div>
<div><span class="sw" style="background:{LCD}"></span><p><b>Dark wells</b> hold values: counters and dropdowns.</p></div>
</div>

<h2 class="sec">{mark()}<span>TEMPO AND TIMING</span></h2>
<div class="card"><p>Anything rhythmic (sync rates, bar-length loops, sequencers) locks to the host's tempo <i>and</i> its position in the bar, so it lands in the same place every time you press play. Plug-ins that need to look ahead (iNTERLUDE, HiRAETH) report their latency so your DAW lines everything up. iNHALE is the one exception: it delays by whole bars, and tells you how far to move your region.</p></div>
</section>"""
    page ("getting-started.html", "Getting Started · BB DSP Manuals", body, "start", st,
          "How to install BB DSP plug-ins and use their shared controls.")

# --- A plugin's manual -------------------------------------------------------------
def build_plugin (p, prev, nxt):
    st = accent_vars (p["accent"])
    if p.get ("spectrum"):
        st += "--accent-grad:linear-gradient(90deg,#D9342B,#F2A93B,#6CC24A,#3B80C4,#5F5069);"
    toc = [("overview", "OVERVIEW"), ("quick", "QUICK START"), ("how", "HOW IT WORKS"), ("controls", "CONTROLS"), ("tips", "TIPS"), ("specs", "SPECS")]
    toc_html = "".join (f'<a href="#{i}">{title (t)}</a>' for i, t in toc)
    groups = []
    for gname, rows in p["groups"]:
        r = []
        for n, rng, dflt, d in rows:
            well = f'<div class="rv">{lcd (dflt)}</div>' if dflt not in ("-", "") else '<div class="rv"></div>'
            rng_html = f'<span class="rng">{html.escape (rng)}</span>' if rng not in ("-", "") else ""
            r.append (f'<div class="row"><div class="rn">{labelise (html.escape (n))}{rng_html}</div>{well}<div class="rd">{html.escape (d)}</div></div>')
        groups.append (f'<h3 class="grp">{labelise (html.escape (gname))}</h3><div class="card table">{"".join (r)}</div>')
    imgs = p["images"]
    gallery = "".join (f'<figure><div class="shot{" dark" if p.get("dark") else ""}"><img src="img/{p["slug"]}/{f}" alt="{html.escape (c)}" loading="lazy"></div><figcaption>{html.escape (c)}</figcaption></figure>' for f, c in imgs[1:])
    quick = "".join (f'<li><span class="n">{i:02d}</span><span>{labelise (html.escape (s))}</span></li>' for i, s in enumerate (p["quick"], 1))
    how = "".join (f'<div class="how"><h3>{mark (12)}{html.escape (h)}</h3><p>{labelise (html.escape (t))}</p></div>' for h, t in p["how"])
    tips = "".join (f'<li>{labelise (html.escape (t))}</li>' for t in p["tips"])
    specs = "".join (f'<div><dt>{html.escape (k.upper())}</dt><dd>{html.escape (v)}</dd></div>' for k, v in p["specs"])
    body = f"""
<section class="phero wrap">
<div class="phero-txt">
<p class="eyebrow">{mark()}<span>{KINDS[p['kind']]}</span></p>
<h1 class="pname{' grad' if p.get('spectrum') else ''}">{title (p['name'])}</h1>
<p class="lede">{html.escape (p['tagline'])}</p>
<p class="chips"><span class="chip">AU</span><span class="chip">VST3</span><span class="chip">STANDALONE</span></p>
</div>
<div class="phero-motion">{MOTIONS[p['motion']]}</div>
</section>
<section class="wrap"><figure class="main-shot"><div class="shot{' dark' if p.get('dark') else ''}"><img src="img/{p['slug']}/{imgs[0][0]}" alt="{html.escape (imgs[0][1])}"></div><figcaption>{html.escape (imgs[0][1])}</figcaption></figure></section>
<div class="wrap layout">
<aside class="toc"><div>{toc_html}</div></aside>
<article class="doc">
<h2 class="sec" id="overview">{mark()}<span>OVERVIEW</span></h2>
<div class="prose">{''.join (f'<p>{labelise (html.escape (x))}</p>' for x in p['intro'])}</div>
{f'<div class="gallery">{gallery}</div>' if gallery else ''}
<h2 class="sec" id="quick">{mark()}<span>QUICK START</span></h2>
<ol class="steps">{quick}</ol>
<h2 class="sec" id="how">{mark()}<span>HOW IT WORKS</span></h2>
<div class="hows">{how}</div>
<h2 class="sec" id="controls">{mark()}<span>CONTROLS</span></h2>
<p class="hint">Values in the dark wells are the defaults.</p>
{''.join (groups)}
<h2 class="sec" id="tips">{mark()}<span>TIPS</span></h2>
<ul class="tips">{tips}</ul>
<h2 class="sec" id="specs">{mark()}<span>SPECS</span></h2>
<dl class="specs card">{specs}</dl>
<nav class="pn">
<a href="{prev['slug']}.html" style="{accent_vars (prev['accent'])}"><small>PREVIOUS</small>{title (prev['name'])}</a>
<a href="{nxt['slug']}.html" class="nx" style="{accent_vars (nxt['accent'])}"><small>NEXT</small>{title (nxt['name'])}</a>
</nav>
</article></div>"""
    page (f"{p['slug']}.html", f"{p['name']} Manual · BB DSP", body, "", st, p["tagline"])

def main():
    os.makedirs (os.path.join (OUT, "assets"), exist_ok=True)
    with open (os.path.join (OUT, "assets", "mark.svg"), "w") as f:
        f.write ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><rect x="4" y="4" width="12" height="12" transform="rotate(45 10 10)" fill="#4D4D4D"/><rect x="7.5" y="7.5" width="5" height="5" transform="rotate(45 10 10)" fill="#F26419"/></svg>')
    build_home(); build_start()
    for i, p in enumerate (PLUGINS):
        build_plugin (p, PLUGINS[i - 1], PLUGINS[(i + 1) % len (PLUGINS)])
    open (os.path.join (OUT, ".nojekyll"), "w").close()
    print ("built", len (PLUGINS) + 2, "pages into", OUT)

if __name__ == "__main__":
    main()
