import re
from html.parser import HTMLParser


class HeadingCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        if tag.lower() == "h1":
            self.h1_count += 1


def test_bilingual_text_and_alt_attributes_are_paired(repo_root):
    html = (repo_root / "index.html").read_text(encoding="utf-8")

    assert html.count("data-en=") == html.count("data-zh=")
    assert html.count("data-alt-en=") == html.count("data-alt-zh=")


def test_personal_phone_number_is_not_published(repo_root):
    for filename in ("index.html", "404.html"):
        html = (repo_root / filename).read_text(encoding="utf-8")
        assert "0922" not in html, f"{filename} contains a mobile-number fragment"
        assert "+886" not in html, f"{filename} contains a country-code fragment"


def test_index_has_one_primary_heading_and_standards_doctype(repo_root):
    html = (repo_root / "index.html").read_text(encoding="utf-8")
    parser = HeadingCounter()
    parser.feed(html)

    assert html.lower().startswith("<!doctype html>")
    assert parser.h1_count == 1


def test_external_urls_are_allowlisted(repo_root):
    unexpected = []
    for filename in ("index.html", "404.html"):
        html = (repo_root / filename).read_text(encoding="utf-8")
        urls = re.findall(r"https?://[^\"'\s<>]+", html)
        unexpected.extend(
            f"{filename}: {url}"
            for url in urls
            if not (
                url.startswith("https://sanyoii.github.io/")
                or url.startswith("https://www.linkedin.com/")
                or url == "http://www.w3.org/2000/svg"
            )
        )
    assert unexpected == []
