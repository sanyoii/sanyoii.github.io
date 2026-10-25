from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

root=Path(__file__).resolve().parents[2]
out=Path(__file__).parent
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
    browser=p.chromium.launch()
    for width in [390,1440]:
        for lang in ['en','zh']:
            context=browser.new_context(viewport={'width':width,'height':900})
            page=context.new_page()
            page.goto(f'http://127.0.0.1:{server.server_port}',wait_until='networkidle')
            if lang=='zh': page.locator('#langBtn').click()
            for filename in ['index.html','dlp-case.html']:
                page.goto(f'http://127.0.0.1:{server.server_port}/{filename}',wait_until='networkidle')
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
                for node in page.locator('[data-en]').all():
                    assert node.text_content()==node.get_attribute('data-'+lang)
                page.screenshot(path=str(out/f'copy-{filename[:-5]}-{width}-{lang}.png'),full_page=True)
            context.close()
    browser.close()
server.shutdown()
for filename in ['index.html','dlp-case.html']:
    soup=BeautifulSoup((root/filename).read_text(encoding='utf-8'),'html.parser')
    for node in soup.select('[data-en]'):
        assert node.get_text()==node['data-en'], (filename,node.get_text())
        assert node.get('data-zh')
for filename in ['ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md','BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md','TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md']:
    s=(root/filename).read_text(encoding='utf-8')
    assert s.count('## English')==1 and s.count('## 繁體中文')==1
    assert 'Day 1' not in s and 'user-attested' not in s
    assert '資料來源與限制' in s
print('Eight browser views: no overflow; bilingual text and English fallback match. Three bilingual Markdown case sections verified.')
