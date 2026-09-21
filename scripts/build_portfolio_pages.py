"""Build public reading pages from the existing public Markdown only.

Requires the existing markdown-it-py installation; never installs dependencies.
Run with --check to detect stale output without writing any files.
"""
import argparse
import hashlib
from html import escape
from importlib.metadata import version
from pathlib import Path
import re
from string import Template
import sys

try:
    from markdown_it import MarkdownIt
except ImportError:
    raise SystemExit('Missing markdown-it-py in this Python environment. Use the existing host environment; no packages were installed.')

ROOT = Path(__file__).resolve().parents[1]
SOURCE_BASE = 'https://github.com/sanyoii/sanyoii.github.io/blob/main/'
PAGES = (
    ('BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md', 'btse-case.html', 'BTSE｜CEX 產品品質案例'),
    ('TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md', 'trend-support-case.html', 'Trend Micro｜事件診斷與技術支援案例'),
    ('ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md', 'asml-case.html', 'ASML｜自動化與團隊帶領案例'),
    ('PUBLIC_QA_PRODUCT_QUALITY_RESUME.md', 'resume.html', None),
)
LINKS = {SOURCE_BASE + source: output for source, output, _ in PAGES}
LINKS['https://sanyoii.github.io/'] = 'index.html'


def parser():
    return MarkdownIt('commonmark', {'html': False, 'breaks': False}).enable('table')


def split_source(text, bilingual):
    lines = text.splitlines()
    if not lines or not lines[0].startswith('# '):
        raise ValueError('Source must start with one H1 title')
    title = lines[0][2:]
    body = '\n'.join(lines[1:]).strip()
    if not bilingual:
        return title, '', {'en': body}
    if body.count('## English\n') != 1 or body.count('## 繁體中文\n') != 1:
        raise ValueError('Expected exactly one English and one Traditional Chinese section')
    metadata, rest = body.split('## English\n')
    english, chinese = rest.split('## 繁體中文\n')
    if not english.strip() or not chinese.strip():
        raise ValueError('Both languages need content')
    return title, metadata.strip(), {'en': english.strip(), 'zh': chinese.strip()}


def render_markdown(text, lang, case=False, preserve_lines=False):
    # Footnotes/directives are not part of this renderer contract. Do not silently
    # flatten these future additions into text that looks like working Markdown.
    if re.search(r'^\s*(?:\[\^[^]]+\]:|:::|!\[)', text, re.M):
        raise ValueError('Unsupported footnote, directive or image in public source')
    md = parser()
    md.options['breaks'] = preserve_lines
    tokens = md.parse(text)
    toc = []
    count = 0
    for i, token in enumerate(tokens):
        if token.type in ('heading_open', 'heading_close'):
            level = int(token.tag[1:])
            if level < (3 if case else 2):
                raise ValueError('Unexpected heading level in source body')
            token.tag = f'h{level - 1 if case else level}'
            if token.type == 'heading_open':
                count += 1
                target = f'{lang}-section-{count}'
                token.attrSet('id', target)
                if token.tag == 'h2':
                    toc.append((target, tokens[i + 1].content))
        if token.children:
            for child in token.children:
                if child.type == 'link_open':
                    href = child.attrGet('href')
                    child.attrSet('href', LINKS.get(href, href))
        if token.type == 'th_open':
            token.attrSet('scope', 'col')
    rendered = md.renderer.render(tokens, md.options, {})
    label = 'Scrollable evidence table' if lang == 'en' else '可橫向捲動的案例表格'
    hint = 'Scroll horizontally to read all columns →' if lang == 'en' else '左右捲動，閱讀完整欄位 →'
    rendered = rendered.replace('<table>', f'<div class="table-evidence" data-scroll-hint="{hint}"><div class="table-scroll" role="region" tabindex="0" aria-label="{label}"><table>')
    rendered = rendered.replace('</table>', '</table></div></div>')
    return rendered, toc


def build_page(root, source, output, chinese_title):
    raw = (root / source).read_text(encoding='utf-8-sig')
    title, metadata, bodies = split_source(raw, chinese_title is not None)
    navs, articles = [], []
    for lang, body in bodies.items():
        html, toc = render_markdown(body, lang, case=chinese_title is not None)
        hidden = ' hidden' if lang == 'zh' else ''
        language = 'zh-Hant' if lang == 'zh' else 'en'
        links = ''.join(f'<li><a href="#{target}">{escape(label)}</a></li>' for target, label in toc)
        navs.append(f'<ol data-language="{lang}" lang="{language}"{hidden}>{links}</ol>')
        articles.append(f'<div class="source-body" data-source-body="{lang}" data-language="{lang}" lang="{language}"{hidden}>{html}</div>')
    meta_html = render_markdown(metadata, 'en', preserve_lines=True)[0] if metadata else ''
    if meta_html:
        meta_html = f'<div class="provenance" lang="en" data-source-meta>{meta_html}</div>'
    toggle = '<button id="langBtn" type="button" aria-label="切換為繁體中文">中文</button>' if chinese_title else '<span class="language-note">English resume</span>'
    template = (root / 'scripts/templates/portfolio-page.html').read_text(encoding='utf-8')
    # Dependency fingerprint includes shared assets and renderer version so a
    # --check also detects a stale build after layout/toolchain changes.
    digest = hashlib.sha256()
    for name in [source, 'scripts/build_portfolio_pages.py', 'scripts/templates/portfolio-page.html', 'assets/portfolio-pages.css', 'assets/portfolio-pages.js']:
        digest.update((root / name).read_text(encoding='utf-8-sig').encode('utf-8'))
    digest.update(version('markdown-it-py').encode())
    return Template(template).substitute(
        title=escape(title), title_zh=escape(chinese_title or title),
        kind='Case study' if chinese_title else 'Public QA resume',
        kind_zh='工作案例' if chinese_title else 'Public QA resume',
        bilingual='true' if chinese_title else 'false', toggle=toggle,
        provenance=meta_html, navigation='\n'.join(navs), content='\n'.join(articles),
        source=escape(SOURCE_BASE + source), digest=digest.hexdigest(),
    )


def main(argv=None):
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument('--check', action='store_true')
    args = cli.parse_args(argv)
    # Complete all renders first: a bad source cannot partially refresh output.
    try:
        pages = [(output, build_page(ROOT, source, output, zh)) for source, output, zh in PAGES]
    except (OSError, ValueError) as exc:
        print(f'Build failed: {exc}', file=sys.stderr)
        return 1
    stale = []
    for output, html in pages:
        path = ROOT / output
        data = html.encode('utf-8')
        if args.check:
            if not path.exists() or path.read_bytes() != data:
                stale.append(output)
        else:
            path.write_bytes(data)
    if stale:
        print('Stale or missing: ' + ', '.join(stale), file=sys.stderr)
        return 1
    print(f'{"Checked" if args.check else "Built"} {len(pages)} portfolio pages')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
