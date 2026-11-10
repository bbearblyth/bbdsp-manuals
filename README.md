# BB DSP Manuals

The online manual for BB DSP plug-ins, served by GitHub Pages from `docs/`.

- Words: `content.py` (one entry per plug-in: intro, quick start, controls, tips).
- Templates, colours and the per-plug-in animations: `build.py`.
- Styles: `docs/assets/site.css`.

Rebuild after editing:

    python3 build.py

Screenshots in `docs/img/` are the plug-ins' own offscreen test renders, converted to WebP.

Check phone layout in WebKit (what iPhone browsers use):

    swiftc -O tools/webkitshot.swift -o /tmp/webkitshot && /tmp/webkitshot "http://localhost:8765/index.html" out.png 390
