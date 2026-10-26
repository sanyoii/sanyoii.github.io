"""How I lead QA matrix: published facts only, both languages, no extra figures."""
from pathlib import Path
import re

import pytest

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / 'how-i-lead-qa.html'

FORBIDDEN = (
    '-25%',
    '−25%',
    '–25%',
    '-30%',
    '−30%',
    '–30%',
    '-40%',
    '−40%',
    '–40%',
    '100+',
    '100 +',
    'CPU/RAM',
    'CPU / RAM',
    'at least 10%',
    '至少 10%',
    '降低至少 10%',
    '10% lower',
    '20–30',
    '20-30',
    '20~30',
    '2–3',
    '2-3',
    '2~3',
    '-25% calls',
    '-25% cost',
    '25% cost',
    'docs/reviews',
    'D:/',
    'D:\\',
    '/workspace',
    'PROFILE_CONTENT',
    'Service Engineer Group',
)


def language_block(html, lang):
    match = re.search(
        rf'<div class="source-body" data-language="{lang}".*?</div>\s*(?=<div class="source-body"|</article>)',
        html,
        re.S,
    )
    assert match, lang
    return match.group(0)


def test_how_i_lead_page_exists_and_homepage_points_at_it(repo_root):
    assert PAGE.is_file()
    html = PAGE.read_text(encoding='utf-8')
    home = (repo_root / 'index.html').read_text(encoding='utf-8')
    assert html.lower().startswith('<!doctype html>')
    assert html.count('<h1') == 1
    assert 'href="how-i-lead-qa.html"' in home
    assert 'class="lb-read" href="how-i-lead-qa.html"' in home
    assert 'class="lb-read" href="asml-case.html"' not in home
    assert 'href="how-i-lead-qa.html" data-en="How I lead QA"' in home
    for target in (
        'asml-case.html#en-section-2',
        'asml-case.html#en-section-3',
        'asml-case.html#en-section-5',
        'asml-case.html#zh-section-2',
        'asml-case.html#zh-section-3',
        'asml-case.html#zh-section-5',
        'trend-support-case.html#en-section-4',
        'trend-support-case.html#zh-section-4',
        'dlp-case.html#intake',
    ):
        assert f'href="{target}"' in html
    asml = (repo_root / 'asml-case.html').read_text(encoding='utf-8')
    trend = (repo_root / 'trend-support-case.html').read_text(encoding='utf-8')
    dlp = (repo_root / 'dlp-case.html').read_text(encoding='utf-8')
    for anchor in ('en-section-2', 'en-section-3', 'en-section-5', 'zh-section-2', 'zh-section-3', 'zh-section-5'):
        assert f'id="{anchor}"' in asml
    assert 'id="en-section-4"' in trend and 'id="zh-section-4"' in trend
    assert 'id="intake"' in dlp


def test_how_i_lead_page_has_no_forbidden_figures_or_local_records():
    text = PAGE.read_text(encoding='utf-8')
    found = [item for item in FORBIDDEN if item in text]
    assert found == []
    assert 'QA and support engineering' in text
    assert 'QA 與技術支援工程' in text
    assert 'manager-reported' in text
    assert '主管提供數據' in text
    assert 'self-reported' in text
    assert '本人自述' in text


def test_seg_is_expanded_on_first_use_in_each_language():
    html = PAGE.read_text(encoding='utf-8')
    english = language_block(html, 'en')
    chinese = language_block(html, 'zh')
    assert english.count('SEG (Service Engineering Group)') == 1
    assert chinese.count('SEG（Service Engineering Group）') == 1
    assert english[english.find('SEG'):].startswith('SEG (Service Engineering Group)')
    assert chinese[chinese.find('SEG'):].startswith('SEG（Service Engineering Group）')
    assert 'SEG (Service Engineering Group)' not in chinese
    assert 'SEG（Service Engineering Group）' not in english


@pytest.mark.parametrize('width', [390, 1280])
@pytest.mark.parametrize('lang', ['en', 'zh'])
def test_how_i_lead_matrix_stacks_on_mobile_and_grids_on_desktop(browser, site_url, width, lang):
    context = browser.new_context(viewport={'width': width, 'height': 900})
    page = context.new_page()
    page.goto(f'{site_url}/how-i-lead-qa.html', wait_until='networkidle')
    if lang == 'zh':
        page.locator('#langBtn').click()
        assert page.locator('h1').inner_text() == '我怎麼帶 QA 團隊'
    else:
        assert page.locator('h1').inner_text() == 'How I lead QA'
    assert page.evaluate('document.documentElement.scrollWidth <= document.documentElement.clientWidth')
    visible = page.locator('[data-language]:visible')
    people = visible.locator('[data-row="people"]')
    asml = people.locator('[data-org="asml"]').bounding_box()
    trend = people.locator('[data-org="trend"]').bounding_box()
    assert asml and trend
    if width == 390:
        assert not visible.locator('.matrix-head').is_visible()
        assert trend['y'] >= asml['y'] + asml['height'] - 1
        assert visible.locator('[data-org="asml"] h3').first.is_visible()
    else:
        assert visible.locator('.matrix-head').is_visible()
        assert abs(asml['y'] - trend['y']) < 2
        assert trend['x'] > asml['x'] + asml['width'] - 1
    context.close()
