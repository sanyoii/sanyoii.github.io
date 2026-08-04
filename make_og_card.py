"""Regenerate assets/og-card.png from index.html.

Every string on the card is read out of the live DOM, so the card cannot drift from the
site: change a headline or a job title and rerun this. The layout is card-specific
(1200x630 needs its own composition), but the palette and font stack are taken from the
page's own :root tokens.

    C:/Python314/python.exe make_og_card.py           # write assets/og-card.png
    C:/Python314/python.exe make_og_card.py --check   # render beside it and compare
"""

import html
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = Path(__file__).parent
INDEX = BASE / "index.html"
TARGET = BASE / "assets" / "og-card.png"
CHECK = "--check" in sys.argv
out = TARGET.with_name("og-card.check.png") if CHECK else TARGET

SCRAPE = """
() => {
  const text = (sel) => {
    const node = document.querySelector(sel);
    if (!node) throw new Error('missing element: ' + sel);
    return node.textContent.trim().replace(/\\s+/g, ' ');
  };
  // the card's supporting paragraph is the Web3 impact section intro
  const lede = document.querySelector('#impact .sec-sub');
  const stats = [...document.querySelectorAll('.stats > *')].map((cell) => ({
    n: cell.querySelector('.stat-n').textContent.trim(),
    l: cell.querySelector('.stat-l').textContent.trim(),
  }));
  const tokens = getComputedStyle(document.documentElement);
  return {
    eyebrow: text('.eyebrow'),
    name: text('h1'),
    role: text('.role'),
    tagline: text('.tagline'),
    lede: lede ? lede.textContent.trim().replace(/\\s+/g, ' ') : '',
    stats,
    bg: tokens.getPropertyValue('--bg').trim(),
    ink: tokens.getPropertyValue('--ink').trim(),
    dim: tokens.getPropertyValue('--ink-dim').trim(),
    faint: tokens.getPropertyValue('--ink-faint').trim(),
    rule: tokens.getPropertyValue('--rule').trim(),
    accent: tokens.getPropertyValue('--accent').trim(),
    sans: tokens.getPropertyValue('--sans').trim(),
    display: tokens.getPropertyValue('--display').trim(),
    mono: tokens.getPropertyValue('--mono').trim(),
  };
}
"""


def card_html(d: dict) -> str:
    esc = {k: html.escape(v) if isinstance(v, str) else v for k, v in d.items()}
    stats = "".join(
        f'<div class="stat"><span class="n">{html.escape(s["n"])}</span>'
        f'<span class="l">{html.escape(s["l"])}</span></div>'
        for s in d["stats"]
    )
    return f"""<!doctype html><meta charset="utf-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{ width: 1200px; height: 630px; overflow: hidden; }}
  body {{
    background: {esc['bg']}; color: {esc['ink']}; font-family: {d['sans']};
    padding: 52px 84px 40px; display: flex; flex-direction: column; align-items: flex-start;
    -webkit-font-smoothing: antialiased;
  }}
  .eyebrow {{ font-family: {d['mono']}; font-size: 15px; letter-spacing: 3.4px;
             text-transform: uppercase; color: {esc['faint']}; }}
  h1 {{ font-family: {d['display']}; font-size: 78px; font-weight: 500; letter-spacing: -2.5px;
       line-height: 1.02; margin: 20px 0 10px; }}
  .role {{ font-size: 25px; font-weight: 500; color: {esc['dim']}; }}
  .tagline {{ font-family: {d['display']}; font-size: 39px; font-weight: 400; line-height: 1.2;
             margin-top: 22px; max-width: 940px; }}
  .rule {{ width: 62px; height: 3px; background: {esc['accent']}; margin: 28px 0 0;
          flex: none; }}
  .lede {{ font-size: 19px; line-height: 1.62; color: {esc['dim']};
          margin-top: 26px; max-width: 900px; }}
  .stats {{ width: 100%; margin-top: auto; padding-top: 24px;
           border-top: 1px solid {esc['rule']};
           display: grid; grid-template-columns: repeat(4, 1fr); gap: 26px; }}
  .n {{ display: block; font-size: 38px; font-weight: 300; color: {esc['accent']};
       letter-spacing: -0.5px; }}
  .l {{ display: block; font-size: 15px; color: {esc['faint']}; margin-top: 5px; }}
</style>
<p class="eyebrow">{esc['eyebrow']}</p>
<h1>{esc['name']}</h1>
<p class="role">{esc['role']}</p>
<p class="tagline">{esc['tagline']}</p>
<div class="rule"></div>
{'<p class="lede">' + esc['lede'] + '</p>' if d['lede'] else ''}
<div class="stats">{stats}</div>
"""


with sync_playwright() as play:
    browser = play.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    page.goto(INDEX.resolve().as_uri())
    page.wait_for_load_state("networkidle")
    data = page.evaluate(SCRAPE)
    page.close()

    draft = BASE / "_og-card-source.html"
    draft.write_text(card_html(data), encoding="utf-8")
    card = browser.new_page(
        viewport={"width": 1200, "height": 630}, device_scale_factor=1
    )
    card.goto(draft.as_uri())
    card.wait_for_load_state("networkidle")
    overflow = card.evaluate("() => document.body.scrollHeight - 630")
    card.screenshot(path=str(out))
    browser.close()
    draft.unlink(missing_ok=True)

print(f"role    : {data['role']}")
print(f"stats   : {', '.join(s['n'] for s in data['stats'])}")
print(f"lede    : {'yes' if data['lede'] else 'MISSING — check the .lede selector'}")
print(f"overflow: {overflow}px" + ("  <-- content is cut off" if overflow > 0 else ""))
print(f"written : {out.name}")

if CHECK and TARGET.is_file():
    print("identical to committed card:", TARGET.read_bytes() == out.read_bytes())
