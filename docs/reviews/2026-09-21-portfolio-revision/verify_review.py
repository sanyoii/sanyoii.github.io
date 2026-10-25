"""Check only the draft and its source relationship; not production acceptance."""
from collections import Counter
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import re
import shutil
import tempfile
from threading import Thread

from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location('draft', HERE / 'build_review.py')
draft = importlib.util.module_from_spec(spec)
spec.loader.exec_module(draft)
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


draft.snapshot()
check('Root website and source snapshots unchanged', True)
resume = (HERE / 'candidate-sources/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md').read_text(encoding='utf-8')
skill_source = draft.read('PROFILE_CONTENT_SOURCE.md').split('### Work evidence — current bilingual skill map')[1].split('Additional confirmed tools')[0]
expected_skills = []
for line in skill_source.splitlines():
    if line.startswith('| ') and not line.startswith('| English'):
        cells = [x.strip() for x in line.strip('|').split('|')]
        expected_skills.append((cells[0], cells[2]))
check('All seven skill categories match the current source', draft.source_resume_skills(resume) == expected_skills)
check('CI tools only in the correct skill category', all(('Jenkins' not in body and 'Bamboo' not in body) for category, body in expected_skills if category != 'Automation & CI'))
check('No private phone or appendix imported', not any(x in resume for x in ['+886', '0922', 'Private Day 13 Appendix']))
check('Metric attribution retained', all(x.lower() in resume.lower() for x in ['20 percentage points', 'figures shared by my manager', 'Based on my recollection', 'at least 10%', 'unlisted', 'independent verification']))
check('Latest work responsibilities retained', all(x in resume for x in ['SEG Leader and QA Leader', 'Tracked work and defects in Jira', 'Designed test specifications, cases, and test data', 'internal beta scope', 'six engineers completed most implementation coding']))
qa = draft.read('application-packets/2026-09-21-profile-sync/qa-source.md')
career = qa.split('### PROFESSIONAL EXPERIENCE')[1].split('### EDUCATION')[0]
for heading in re.findall(r'^#### (.+)$', career, re.M):
    check('Formal role retained: ' + heading, '### ' + heading in resume)
for date in re.findall(r'^\w{3} \d{4}–(?:\w{3} \d{4}|Present)', career, re.M):
    check('Employment date retained: ' + date, date in resume)

number_diffs = {}
for source in ['BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md', 'ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md', 'TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md']:
    old = draft.read(source)
    new = (HERE / 'candidate-sources' / source).read_text(encoding='utf-8')
    check('English source unchanged: ' + source, old.split('## 繁體中文')[0] == new.split('## 繁體中文')[0])
    old_zh, new_zh = old.split('## 繁體中文')[1], new.split('## 繁體中文')[1]
    numbers = lambda s: Counter(re.findall(r'\d+(?:[.––-]\d+)?%?', s))
    if numbers(old_zh) != numbers(new_zh):
        number_diffs[source] = {'before': dict(numbers(old_zh)), 'after': dict(numbers(new_zh))}
    check('Table rows retained: ' + source, sum(l.startswith('|') for l in old_zh.splitlines()) == sum(l.startswith('|') for l in new_zh.splitlines()))
    check('Evidence section retained: ' + source, '### 資料來源與限制' in new_zh and '獨立查證' in new_zh)
check('No changed numeric tokens in long-case Chinese', not number_diffs)

# Negative check in a temporary directory, never alter the reviewed sources.
with tempfile.TemporaryDirectory(prefix='portfolio-source-review-') as tmp:
    temp_root = Path(tmp)
    for name in draft.INPUTS:
        dest = temp_root / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, dest)
    changed = temp_root / 'PROFILE_CONTENT_SOURCE.md'
    changed.write_bytes(changed.read_bytes() + b'\nChanged for negative check\n')
    actual_root = draft.ROOT
    draft.ROOT = temp_root
    try:
        draft.snapshot()
    except ValueError as exc:
        check('Changed authoritative source requires review', 'REVIEW_REQUIRED' in str(exc))
    else:
        raise AssertionError('Source drift was silently accepted')
    finally:
        draft.ROOT = actual_root

class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass

server = ThreadingHTTPServer(('127.0.0.1', 0), partial(Quiet, directory=str(ROOT)))
Thread(target=server.serve_forever, daemon=True).start()
prefix = f'http://127.0.0.1:{server.server_port}/docs/reviews/2026-09-21-portfolio-revision/preview/'
shots = HERE / 'screenshots'
shots.mkdir(exist_ok=True)
try:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for width, height in [(390, 844), (1440, 900)]:
            context = browser.new_context(viewport={'width': width, 'height': height}, reduced_motion='reduce')
            page = context.new_page()
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            check(f'Home HTTP {width}', page.goto(prefix + 'index.html', wait_until='networkidle').ok)
            check(f'Chinese home {width}', page.locator('html').get_attribute('lang') == 'zh-Hant')
            check(f'Home overflow {width}', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
            check(f'Three topic groups {width}', page.locator('.review-case').count() == 3)
            check(f'No duplicate resume entry {width}', page.locator('a[href="resume.html"]').count() == 1)
            check(f'No old summary strip {width}', page.locator('.experience-strip').count() == 0)
            check(f'No loose support row {width}', page.locator('.full-notes').count() == 0)
            page.screenshot(path=str(shots / f'home-{width}.png'), full_page=True)
            page.screenshot(path=str(shots / f'home-{width}-top.png'))
            page.locator('#evidence').scroll_into_view_if_needed()
            page.screenshot(path=str(shots / f'cases-{width}.png'))
            for filename in ['resume.html','btse-case.html','asml-case.html','trend-support-case.html','dlp-case.html']:
                check(f'{filename} HTTP {width}', page.goto(prefix + filename, wait_until='networkidle').ok)
                check(f'{filename} overflow {width}', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
                check(f'{filename} title {width}', page.locator('h1').is_visible())
                page.screenshot(path=str(shots / f'{Path(filename).stem}-{width}.png'), full_page=True)
            check(f'No pageerror {width}', not errors)
            context.close()
        for width in [390, 1440]:
            context = browser.new_context(viewport={'width': width, 'height': 900})
            page = context.new_page()
            errors = []
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(prefix + 'index.html')
            for lang in ['en', 'zh-Hant']:
                for filename in ['btse-case.html', 'asml-case.html', 'trend-support-case.html', 'dlp-case.html']:
                    page.goto(prefix + 'index.html')
                    if page.locator('html').get_attribute('lang') != lang:
                        page.locator('#langBtn').click()
                    page.reload()
                    check(f'Home keeps {lang} after reload {width} {filename}', page.locator('html').get_attribute('lang') == lang)
                    page.locator(f'.review-cases a[href="{filename}"]').click()
                    check(f'Case inherits {lang} {width} {filename}', page.locator('html').get_attribute('lang') == lang)
                    if filename != 'dlp-case.html':
                        selected = 'en' if lang == 'en' else 'zh'
                        other = 'zh' if selected == 'en' else 'en'
                        check(f'Correct body visible {lang} {width} {filename}', page.locator(f'[data-source-body="{selected}"]').is_visible() and not page.locator(f'[data-source-body="{other}"]').is_visible())
                    else:
                        check(f'DLP heading text {lang} {width}', page.locator('h1').inner_text() == page.locator('h1').get_attribute('data-en' if lang == 'en' else 'data-zh'))
                    page.reload()
                    check(f'Case reload keeps {lang} {width} {filename}', page.locator('html').get_attribute('lang') == lang)
                    page.locator('footer a[href="index.html#evidence"]').click()
                    check(f'Return keeps {lang} {width} {filename}', page.locator('html').get_attribute('lang') == lang)
            page.goto(prefix + 'btse-case.html')
            page.locator('#langBtn').click()
            switched = page.locator('html').get_attribute('lang')
            page.locator('footer a[href="index.html#evidence"]').click()
            check(f'Case toggle is preserved on return {width}', page.locator('html').get_attribute('lang') == switched)
            page.screenshot(path=str(shots / f'language-return-{width}.png'))
            page.locator('.review-cases a[href="btse-case.html"]').click()
            page.screenshot(path=str(shots / f'btse-english-{width}.png'))
            check(f'Language journeys have no pageerror {width}', not errors)
            context.close()
        browser.close()
finally:
    server.shutdown()
    server.server_close()
(HERE / 'verification.json').write_text(json.dumps({'checks_passed': len(checks), 'checks': checks, 'numeric_diffs': number_diffs, 'limits': ['Draft-only checks; not production acceptance', 'Human approval pending', 'No real-device or screen-reader test']}, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'{len(checks)} draft checks passed; source text and visual quality still require review.')
