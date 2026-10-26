"""Render the approved public Style C print source; never install dependencies."""
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def main():
    source = ROOT / 'scripts/templates/public-resume-print.html'
    output = ROOT / 'assets/William-Lu-Public-QA-Resume.pdf'
    if 'tel:' in source.read_text(encoding='utf-8').lower():
        raise ValueError('Public print source must not contain a phone link')
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        # The approved source is self-contained. No remote fonts or images.
        page.route('http://**/*', lambda route: route.abort())
        page.route('https://**/*', lambda route: route.abort())
        page.goto(source.as_uri())
        page.evaluate('document.fonts.ready')
        page.emulate_media(media='print')
        page.pdf(path=str(output), format='A4', print_background=True,
                 prefer_css_page_size=True, display_header_footer=False)
        browser.close()
    print('Built assets/William-Lu-Public-QA-Resume.pdf')


if __name__ == '__main__':
    main()
