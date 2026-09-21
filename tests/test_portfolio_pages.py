"""Source fidelity and reader journeys for the generated public pages."""
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlparse

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('portfolio_build', ROOT / 'scripts/build_portfolio_pages.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def normalized(text):
    return re.sub(r'\s+', '', text)


def plain(html):
    parser = Text()
    parser.feed(html)
    return normalized(''.join(parser.parts))


@pytest.mark.parametrize('source,output,zh', build.PAGES)
def test_every_source_block_is_preserved(browser, site_url, source, output, zh):
    title, metadata, bodies = build.split_source((ROOT / source).read_text(encoding='utf-8'), zh is not None)
    page = browser.new_page()
    page.goto(f'{site_url}/{output}')
    assert page.locator('h1').count() == 1
    assert page.locator('h1').inner_text() == title
    # Compare ALL rendered text, including every table cell, to an unmodified
    # Markdown render. Not a keyword-only claim check.
    for lang, body in bodies.items():
        expected = plain(build.parser().render(body))
        actual = page.locator(f'[data-source-body="{lang}"]').text_content()
        assert normalized(actual) == expected
    if metadata:
        assert normalized(page.locator('[data-source-meta]').text_content()) == plain(build.parser().render(metadata))
    assert page.locator(f'.source-link[href="{build.SOURCE_BASE}{source}"]').count() == 1
    page.close()


def test_renderer_preserves_structure_and_escapes_markup():
    html, toc = build.render_markdown('## Heading\n\nA **bold** & `code` [link](https://example.com). <script>alert(1)</script>\n\n| A | B |\n|---|---|\n| One | Two |\n\n1. First\n2. Second', 'en')
    assert '<strong>bold</strong>' in html
    assert '<code>code</code>' in html
    assert '&lt;script&gt;' in html and '<script>' not in html
    assert '<th scope="col">A</th>' in html
    assert '<td>Two</td>' in html and '<ol>' in html
    assert toc == [('en-section-1', 'Heading')]
    unsafe, _ = build.render_markdown('[bad](javascript:alert(1))', 'en')
    assert 'href="javascript:' not in unsafe


@pytest.mark.parametrize('width', [320, 390, 1440])
@pytest.mark.parametrize('output', ['btse-case.html', 'asml-case.html', 'trend-support-case.html'])
def test_metadata_fields_and_navigation_do_not_run_together(browser, site_url, width, output):
    page = browser.new_page(viewport={'width': width, 'height': 900})
    page.goto(f'{site_url}/{output}')
    lines = page.locator('[data-source-meta]').inner_text().splitlines()
    assert any(line.startswith('Period:') for line in lines)
    assert any(line.startswith(('Role:', 'Roles:')) for line in lines)
    assert any(line.startswith('Public navigation:') for line in lines)
    for link in page.locator('[data-source-meta] a').all():
        assert link.evaluate('(el) => el.getClientRects().length') == 1
    assert page.evaluate('document.documentElement.scrollWidth <= window.innerWidth')
    page.close()


@pytest.mark.parametrize('bad', ['[^note]: Hidden footnote', ':::note', '![image](asset.png)'])
def test_unsupported_source_fails_explicitly(bad):
    with pytest.raises(ValueError):
        build.render_markdown(bad, 'en')


def test_check_detects_source_drift_and_never_writes(tmp_path, monkeypatch):
    names = [p[0] for p in build.PAGES] + ['scripts/build_portfolio_pages.py', 'scripts/templates/portfolio-page.html', 'assets/portfolio-pages.css', 'assets/portfolio-pages.js']
    for name in names:
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    monkeypatch.setattr(build, 'ROOT', tmp_path)
    assert build.main([]) == 0
    before = {p[1]: (tmp_path / p[1]).read_bytes() for p in build.PAGES}
    mtimes = {p[1]: (tmp_path / p[1]).stat().st_mtime_ns for p in build.PAGES}
    assert build.main(['--check']) == 0
    assert mtimes == {p[1]: (tmp_path / p[1]).stat().st_mtime_ns for p in build.PAGES}
    assert build.main([]) == 0
    assert before == {p[1]: (tmp_path / p[1]).read_bytes() for p in build.PAGES}
    # Git checkouts may use CRLF; semantic inputs and build fingerprints stay stable.
    for name in names:
        path = tmp_path / name
        path.write_bytes(path.read_text(encoding='utf-8').replace('\n', '\r\n').encode('utf-8'))
    assert build.main(['--check']) == 0
    source = tmp_path / build.PAGES[0][0]
    source.write_text(source.read_text(encoding='utf-8') + '\nAdditional source paragraph.\n', encoding='utf-8')
    assert build.main(['--check']) == 1
    assert before == {p[1]: (tmp_path / p[1]).read_bytes() for p in build.PAGES}
    source.unlink()
    assert build.main([]) == 1
    assert before == {p[1]: (tmp_path / p[1]).read_bytes() for p in build.PAGES}


@pytest.mark.parametrize('source,output,zh', build.PAGES)
@pytest.mark.parametrize('width', [320, 390, 768, 1440])
def test_reading_layout_language_links_and_no_external_requests(browser, site_url, source, output, zh, width):
    context = browser.new_context(viewport={'width': width, 'height': 900})
    page = context.new_page()
    errors, requests = [], []
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.on('request', lambda request: requests.append(request.url))
    assert page.goto(f'{site_url}/{output}').ok
    for language in (['en', 'zh-Hant'] if zh else ['en']):
        assert page.locator('html').get_attribute('lang') == language
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
        assert page.locator('h1').is_visible()
        if page.locator('.contents').get_attribute('open') is None:
            page.locator('.contents summary').click()
        links = page.locator('.contents ol:visible a')
        links.last.click()
        target = links.last.get_attribute('href')
        assert page.locator(target).is_visible()
        if language == 'en' and zh:
            page.locator('#langBtn').click()
            page.reload()
            assert page.title().startswith(zh)
    assert errors == []
    assert all(urlparse(url).netloc == urlparse(site_url).netloc for url in requests)
    # Verify every local anchor/destination, without contacting third parties.
    for href in page.locator('a[href]').evaluate_all('(els) => els.map(el => el.getAttribute("href"))'):
        parsed = urlparse(href)
        if parsed.scheme:
            continue
        if not parsed.path:
            assert page.locator(f'[id="{parsed.fragment}"]').count() == 1
        else:
            assert context.request.get(f'{site_url}/{parsed.path}').ok
    page.locator('footer a[href="index.html#evidence"]').click()
    assert page.locator('#evidence').is_visible()
    assert page.locator('html').get_attribute('lang') == ('zh-Hant' if zh else 'en')
    context.close()


def test_home_destinations_and_mobile_baseline(browser, site_url):
    baseline = json.loads((ROOT / 'test-records/2026-09-21-portfolio-case-reading/baseline/metrics.json').read_text())
    context = browser.new_context(viewport={'width': 390, 'height': 844}, reduced_motion='reduce')
    page = context.new_page()
    page.goto(site_url)
    for lang in ['en', 'zh']:
        assert page.locator('#btse-evidence').bounding_box()['y'] <= baseline[f'index-390-{lang}'] + 1
        cta = page.locator('.ctas').bounding_box()
        assert cta['y'] + cta['height'] <= 844
        assert not page.locator('.experiments').get_attribute('open')
        if lang == 'en':
            page.locator('#langBtn').click()
    for selector, dest in [('#btse-evidence', 'btse-case.html'), ('#incident-evidence', 'trend-support-case.html'), ('#asml-evidence', 'asml-case.html'), ('.ctas a[href="resume.html"]', 'resume.html')]:
        page.goto(site_url)
        page.locator(selector).click()
        assert page.url.endswith(dest)
        page.locator('footer a[href="index.html#evidence"]').click()
        assert page.locator('html').get_attribute('lang') == 'zh-Hant'
    page.set_viewport_size({'width': 320, 'height': 900})
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    context.close()


@pytest.mark.parametrize('output', [p[1] for p in build.PAGES])
def test_keyboard_zoom_and_javascript_disabled(browser, site_url, output):
    context = browser.new_context(viewport={'width': 1280, 'height': 900})
    page = context.new_page()
    page.goto(f'{site_url}/{output}')
    page.keyboard.press('Tab')
    assert page.locator('.skip-link').evaluate('(el) => el === document.activeElement')
    assert page.locator('.skip-link').evaluate('(el) => getComputedStyle(el).outlineStyle') != 'none'
    page.keyboard.press('Enter')
    # CSS zoom is an explicit 200% layout smoke check, not a real-device claim.
    page.evaluate("document.body.style.zoom = '2'")
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    button = page.locator('#langBtn')
    if button.count():
        button.focus()
        page.keyboard.press('Enter')
        assert page.locator('html').get_attribute('lang') == 'zh-Hant'
    context.close()
    nojs = browser.new_context(java_script_enabled=False)
    page = nojs.new_page()
    assert page.goto(f'{site_url}/{output}').ok
    assert page.locator('[data-source-body="en"]').is_visible()
    assert page.locator('.source-link').is_visible()
    nojs.close()


def test_english_resume_does_not_overwrite_chinese_preference(browser, site_url):
    context = browser.new_context()
    context.add_init_script("localStorage.setItem('wl-lang', 'zh')")
    page = context.new_page()
    page.goto(f'{site_url}/resume.html')
    assert page.locator('html').get_attribute('lang') == 'en'
    assert page.locator('#langBtn').count() == 0
    assert page.evaluate("localStorage.getItem('wl-lang')") == 'zh'
    context.close()
