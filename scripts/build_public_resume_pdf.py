"""Render the approved public Style C print sources (Senior QA and QA Lead); never install dependencies."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]

# (source, output) paths relative to ROOT. Senior QA first.
BUILDS = (
    ('scripts/templates/public-resume-print.html',
     'assets/William-Lu-Public-QA-Resume.pdf'),
    ('scripts/templates/public-resume-print-qa-lead.html',
     'assets/William-Lu-QA-Lead-Resume.pdf'),
)


def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        for source_rel, output_rel in BUILDS:
            source = ROOT / source_rel
            output = ROOT / output_rel
            if 'tel:' in source.read_text(encoding='utf-8').lower():
                raise ValueError('Public print source must not contain a phone link')
            page = browser.new_page()
            # The approved source is self-contained. No remote fonts or images.
            page.route('http://**/*', lambda route: route.abort())
            page.route('https://**/*', lambda route: route.abort())
            page.goto(source.as_uri())
            page.evaluate('document.fonts.ready')
            page.emulate_media(media='print')
            page.pdf(path=str(output), format='A4', print_background=True,
                     prefer_css_page_size=True, display_header_footer=False)
            page.close()
            print(f'Built {output_rel}')
        browser.close()


if __name__ == '__main__':
    main()
