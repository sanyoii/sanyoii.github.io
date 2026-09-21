"""Capture local evidence; no external navigation or deployment."""
import json
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / sys.argv[1]
OUT.mkdir(exist_ok=True)
server = ThreadingHTTPServer(('127.0.0.1', 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
metrics = {}
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        names = ['index.html'] if sys.argv[1] == 'baseline' else ['index.html', 'btse-case.html', 'trend-support-case.html', 'asml-case.html', 'resume.html']
        for name in names:
            for width, height in [(390, 844), (1440, 900)]:
                for lang in (['en'] if name == 'resume.html' else ['en', 'zh']):
                    context = browser.new_context(viewport={'width': width, 'height': height}, reduced_motion='reduce')
                    context.add_init_script(f"localStorage.setItem('wl-lang', '{lang}')")
                    page = context.new_page()
                    page.goto(f'http://127.0.0.1:{server.server_port}/{name}', wait_until='networkidle')
                    key = f'{Path(name).stem}-{width}-{lang}'
                    if name == 'index.html':
                        metrics[key] = page.locator('#btse-evidence').bounding_box()['y']
                    page.screenshot(path=str(OUT / f'{key}.png'), full_page=True)
                    if sys.argv[1] != 'baseline':
                        page.screenshot(path=str(OUT / f'{key}-top.png'))
                        table = page.locator('.table-scroll:visible').first
                        if table.count():
                            table.scroll_into_view_if_needed()
                            page.screenshot(path=str(OUT / f'{key}-table.png'))
                            table.evaluate('(el) => el.scrollLeft = el.scrollWidth')
                            page.screenshot(path=str(OUT / f'{key}-table-end.png'))
                        page.locator('footer').scroll_into_view_if_needed()
                        page.screenshot(path=str(OUT / f'{key}-footer.png'))
                    context.close()
        browser.close()
finally:
    server.shutdown()
    server.server_close()
(OUT / 'metrics.json').write_text(json.dumps(metrics, indent=2), encoding='utf-8')
print(json.dumps(metrics))
