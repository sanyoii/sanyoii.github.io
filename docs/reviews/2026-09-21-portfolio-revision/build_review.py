"""Build a review-only portfolio. Does not write website/source files at repo root."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
import hashlib
import importlib.util
import json
import re
import sys
from string import Template

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE / 'preview'
CANDIDATES = HERE / 'candidate-sources'
INPUTS = ['PROFILE_CONTENT_SOURCE.md', 'application-packets/2026-09-21-profile-sync/qa-source.md',
          'CLAIM_VERIFICATION_SHEET.md', 'PUBLIC_QA_PRODUCT_QUALITY_RESUME.md', 'index.html', 'dlp-case.html',
          'BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md', 'ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md',
          'TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md']
SNAPSHOT = HERE / 'source-snapshot.json'
spec = importlib.util.spec_from_file_location('portfolio_builder', ROOT / 'scripts/build_portfolio_pages.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def read(name):
    return (ROOT / name).read_text(encoding='utf-8')


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(text.encode('utf-8'))


def snapshot():
    hashes = {n: hashlib.sha256((ROOT / n).read_bytes()).hexdigest() for n in INPUTS}
    if not SNAPSHOT.exists():
        raise ValueError('Missing reviewed source snapshot; do not automatically accept current source versions.')
    approved = json.loads(SNAPSHOT.read_text(encoding='utf-8'))['source_sha256']
    changed = [n for n in INPUTS if hashes[n] != approved.get(n)]
    if changed:
        raise ValueError('REVIEW_REQUIRED: source changed: ' + ', '.join(changed))


def public_resume():
    original = read('PUBLIC_QA_PRODUCT_QUALITY_RESUME.md')
    qa = read('application-packets/2026-09-21-profile-sync/qa-source.md')
    summary = qa.split('### PROFESSIONAL SUMMARY\n')[1].split('### CORE SKILLS\n')[0].strip().replace('**', '')
    table = read('PROFILE_CONTENT_SOURCE.md').split('### Work evidence — current bilingual skill map')[1].split('Additional confirmed tools')[0]
    skills = []
    for line in table.splitlines():
        if line.startswith('| ') and not line.startswith('| English'):
            cells = [x.strip() for x in line.strip('|').split('|')]
            skills.append(f'### {cells[0]}\n\n{cells[2]}')
    assert len(skills) == 7
    career = qa.split('### PROFESSIONAL EXPERIENCE\n')[1].split('### EDUCATION\n')[0].strip()
    career = career.replace('#### ', '### ').replace('**', '')
    career = career.replace('QA performance tests comparing this design change alone showed CPU and memory use each fell by at least 10% relative to the previous design.',
        'Based on my recollection of the QA performance test report, this design change alone reduced CPU and memory use by at least 10% each relative to the previous design.')
    # Keep the public header and case/evidence limits. Never import the private
    # application header (phone) or application-only fields into this candidate.
    result = original.split('## Professional summary')[0] + '## Professional summary\n\n' + summary
    result += '\n\n## Core skills\n\n' + '\n\n'.join(skills)
    result += '\n\n## Professional experience\n\n' + career
    result += '\n\n## Selected case studies' + original.split('## Selected case studies')[1]
    assert '+886' not in result and '0922' not in result and 'Private Day' not in result
    return result


def replace_copy(html, filename):
    mapping = json.loads((HERE / filename).read_text(encoding='utf-8'))
    for old in mapping:
        if old not in html:
            raise ValueError('Copy source no longer matches: ' + old[:50])
    return re.sub(r'data-zh="([^\"]*)"', lambda m: 'data-zh="' + escape(mapping.get(m[1], m[1]), quote=True) + '"', html)


def source_resume_skills(resume):
    block = resume.split('## Core skills\n')[1].split('## Professional experience\n')[0]
    return [(heading, body.strip()) for heading, body in re.findall(r'### ([^\n]+)\n+(.+?)(?=\n### |\Z)', block, re.S)]


def draft_shell(title, body, lang='zh-Hant'):
    return f'''<!doctype html><html lang="{lang}"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{escape(title)}</title><link rel="stylesheet" href="../../../../assets/portfolio-pages.css"><body><main><header class="reading-header"><p>內容與版面草稿｜尚未套用到網站</p><h1>{escape(title)}</h1><a href="index.html">返回首頁草稿</a></header><article>{body}</article><footer><a href="index.html#evidence">返回工作案例</a><a href="resume.html">查看英文履歷</a></footer></main></body></html>'''


def bilingual_case(source, candidate, title_zh):
    title, metadata, bodies = builder.split_source(candidate, True)
    navigation, content = [], []
    for lang, body in bodies.items():
        rendered, toc = builder.render_markdown(body, lang, case=True)
        hidden = ' hidden' if lang == 'zh' else ''
        language = 'zh-Hant' if lang == 'zh' else 'en'
        links = ''.join(f'<li><a href="#{target}">{escape(label)}</a></li>' for target, label in toc)
        navigation.append(f'<ol data-language="{lang}" lang="{language}"{hidden}>{links}</ol>')
        content.append(f'<div class="source-body" data-source-body="{lang}" data-language="{lang}" lang="{language}"{hidden}>{rendered}</div>')
    metadata_html, _ = builder.render_markdown(metadata, 'en', preserve_lines=True)
    html = Template(read('scripts/templates/portfolio-page.html')).substitute(
        title=escape(title), title_zh=escape(title_zh), kind='Case study', kind_zh='工作案例',
        bilingual='true', toggle='<button id="langBtn" type="button" aria-label="切換為繁體中文">中文</button>',
        provenance=f'<div class="provenance" lang="en" data-source-meta>{metadata_html}</div>',
        navigation='\n'.join(navigation), content='\n'.join(content),
        source=escape(builder.SOURCE_BASE + source), digest=hashlib.sha256(candidate.encode('utf-8')).hexdigest())
    html = html.replace('href="assets/', 'href="../../../../assets/').replace('src="assets/', 'src="../../../../assets/')
    html = html.replace('<body>', '<body><p style="padding:12px 24px" data-en="Content and layout draft — not applied to the website" data-zh="內容與版面草稿｜尚未套用到網站">Content and layout draft — not applied to the website</p>', 1)
    return html


def candidate_pages():
    resume = public_resume()
    write(CANDIDATES / 'PUBLIC_QA_PRODUCT_QUALITY_RESUME.md', resume)
    body, _ = builder.render_markdown(resume.split('\n', 1)[1], 'en')
    write(OUT / 'resume.html', draft_shell('William Lu — QA Resume', body, 'en'))
    for source, output, title, zh in [
        ('BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md', 'btse-case.html', '交易、佣金與兌換測試', 'btse.zh-TW.md'),
        ('ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md', 'asml-case.html', '自動化測試規劃與團隊帶領', 'asml.zh-TW.md'),
        ('TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md', 'trend-support-case.html', '客戶問題排查與產品改善', 'trend-support.zh-TW.md')]:
        original = read(source)
        chinese = (HERE / zh).read_text(encoding='utf-8')
        candidate = original.split('## 繁體中文')[0] + chinese
        write(CANDIDATES / source, candidate)
        write(OUT / output, bilingual_case(source, candidate, title))


def home_page():
    html = replace_copy(read('index.html'), 'home-copy.json')
    html = html.replace('I identify product risks early and turn technical findings into better product quality and more effective ways of working.', 'I have 12+ years across software QA and customer engineering, including crypto exchange testing, security-product troubleshooting, and automation team leadership.')
    html = html.replace('Taiwan · Fully Remote · 4+ hours of European overlap. 12+ years across QA and customer engineering.', 'Based in Taiwan, seeking fully remote roles with 4+ hours of European business-hour overlap on weekdays.')
    html = html.replace('Read resume ↗', 'Read resume')
    html = html.replace('Hiring for a Web3 QA role? Contact me to discuss your product and testing needs.', 'Hiring for QA or technical support? Get in touch.')
    html = re.sub(r'\s*<a class="btn btn-ghost" href="#contact".*?</a>', '', html)
    html = re.sub(r'<div class="experience-strip">.*?</div>', '', html, flags=re.S)
    html = re.sub(r'<p class="resume-entry fade">.*?</p>', '', html, flags=re.S)
    start = html.index('      <div class="evidence-grid">')
    end = html.index('\n    </div>\n  </section>', start)
    html = html[:start] + '''      <div class="review-cases">
        <article class="review-case" id="btse-evidence">
          <div><p class="case-company">BTSE</p><h3 data-en="Trading, commissions, and conversion" data-zh="交易、佣金與兌換測試">Trading, commissions, and conversion</h3></div>
          <div><p data-en="I found and reported three high-severity defects through boundary testing and financial checks. The case records my methods and what remained unresolved." data-zh="我透過邊界測試與金額核對，找出並回報 3 個高嚴重度缺陷。案例說明測試方法，以及離職時仍未解決的問題。">I found and reported three high-severity defects through boundary testing and financial checks. The case records my methods and what remained unresolved.</p><a href="btse-case.html" data-en="Read BTSE case" data-zh="閱讀 BTSE 案例">Read BTSE case</a></div>
        </article>
        <article class="review-case" id="asml-evidence">
          <div><p class="case-company">ASML / Zealogics</p><h3 data-en="Automation planning and team leadership" data-zh="自動化測試規劃與團隊帶領">Automation planning and team leadership</h3></div>
          <div><p data-en="I led six engineers and planned the workflow within the existing TestComplete architecture. The team implemented most of the code; connection failures still required manual investigation." data-zh="我帶領 6 位工程師，沿用既有 TestComplete 架構規劃測試流程。多數程式由團隊完成，連線失敗等例外仍需人工檢查。">I led six engineers and planned the workflow within the existing TestComplete architecture. The team implemented most of the code; connection failures still required manual investigation.</p><a href="asml-case.html" data-en="Read ASML case" data-zh="閱讀 ASML 案例">Read ASML case</a></div>
        </article>
        <article class="review-case" id="support-evidence">
          <div><p class="case-company">Trend Micro</p><h3 data-en="Customer troubleshooting and product improvement" data-zh="客戶問題排查與產品改善">Customer troubleshooting and product improvement</h3></div>
          <div><p data-en="My work covered reproducing incidents, diagnosing causes, validating hotfixes, and improving proactive tests and diagnostic guides. These two cases cover the different parts." data-zh="我重現客戶問題、分析原因並驗證 hotfix，也透過主動測試與診斷指南改善問題處理。以下兩篇分別說明這些工作。">My work covered reproducing incidents, diagnosing causes, validating hotfixes, and improving proactive tests and diagnostic guides. These two cases cover the different parts.</p><div class="review-links"><a href="trend-support-case.html" data-en="Incident and support case" data-zh="客戶事件處理案例">Incident and support case</a><a href="dlp-case.html" data-en="DLP compatibility and performance" data-zh="DLP 相容性與效能案例">DLP compatibility and performance</a></div></div>
        </article>
      </div>''' + html[end:]
    html = html.replace('依職位查看 CEX 產品品質、自動化領導或技術支援案例。每個案例都說明我負責的部分與結果。', '這些案例說明我負責的工作、處理方法與結果，也保留尚未解決的問題和資料限制。')
    # This existing tag has no support in the current verified skill map. Keep
    # the concern explicit in the review rather than repeating it as a claim.
    html = re.sub(r'\s*<span class="tag" data-en="API Security" data-zh="API 安全">API Security</span>', '', html)
    html = html.replace('src="assets/', 'src="../../../../assets/').replace('href="test-status/"', 'href="../../../../test-status/"')
    # Use Chinese only for the first review visit, never overwrite a saved choice.
    html = html.replace('<script>document.documentElement', '<script>try { if (localStorage.getItem("wl-lang") === null) localStorage.setItem("wl-lang", "zh"); } catch(e) {}</script>\n<script>document.documentElement', 1)
    styles = '''<style>
    .review-banner { background:#233c36;color:#edf1ed;padding:10px 24px;font-size:13px; }
    .review-banner a { color:inherit; }
    .review-case { display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:36px;padding:28px 0;border-top:1px solid var(--rule); }
    .review-case h3 { font-size:24px;line-height:1.4;margin:8px 0 0; }
    .review-case p { font-size:15px;line-height:1.8; }
    .review-case a { display:inline-flex;align-items:center;min-height:44px;color:var(--accent-strong);text-underline-offset:5px;font-size:14px; }
    .review-links { display:flex;flex-wrap:wrap;gap:8px 24px; }
    .review-case a:focus-visible { outline:2px solid var(--accent);outline-offset:4px; }
    @media(max-width:760px) { .review-case { grid-template-columns:1fr;gap:12px;padding:24px 0; } .review-case h3 { font-size:22px; } }
    </style>'''
    html = html.replace('</head>', styles + '</head>')
    html = html.replace('<body>', '<body><div class="review-banner">內容與版面草稿，尚未套用網站。<a href="../REVIEW.md">查看變更與驗收說明</a></div>', 1)
    write(OUT / 'index.html', html)


def dlp_page():
    html = replace_copy(read('dlp-case.html'), 'dlp-copy.json')
    html = html.replace('https://github.com/sanyoii/sanyoii.github.io/blob/main/TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md', 'trend-support-case.html')
    html = html.replace('https://github.com/sanyoii/sanyoii.github.io/blob/main/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md', 'resume.html')
    html = html.replace('William Lu — DLP 產品決策案例', 'William Lu — Chrome 相容性與 DLP 效能改善')
    html = html.replace('Chrome 相容性監測、支援網站掃描與 SEG 進件品質改善。', 'Chrome 相容性測試、DLP 掃描範圍調整，以及客戶案件診斷指南。')
    # Uniform case navigation: cases/language at top; cases/resume at bottom.
    html = re.sub(r'<div class="nav-links">.*?</div>', '<div class="nav-links"><a href="index.html#evidence" data-en="All cases" data-zh="工作案例">All cases</a></div>', html, flags=re.S)
    html = re.sub(r'<a href="index.html#contact" data-en="Contact" data-zh="聯絡">Contact</a>', '', html)
    html = html.replace('<body>', '<body><p style="padding:12px 24px">內容草稿｜尚未套用網站</p>', 1)
    # This page owns an existing language switcher; its saved setting comes from the draft home.
    write(OUT / 'dlp-case.html', html)


def main():
    snapshot()
    if '--check-sources' in sys.argv:
        print('Source snapshot matches; content approval remains pending.')
        return
    candidate_pages()
    home_page()
    dlp_page()
    print('Built review-only pages and candidate Markdown; root website unchanged.')


if __name__ == '__main__':
    main()
