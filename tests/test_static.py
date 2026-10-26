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
    for filename in ("index.html", "404.html", "dlp-case.html"):
        html = (repo_root / filename).read_text(encoding="utf-8")

        assert html.count("data-en=") == html.count("data-zh="), f"Unpaired data-en/data-zh in {filename}"
        assert html.count("data-alt-en=") == html.count("data-alt-zh="), f"Unpaired data-alt-en/data-alt-zh in {filename}"


def test_personal_phone_number_is_not_published(repo_root):
    for filename in (
        "index.html",
        "404.html",
        "dlp-case.html",
        "resume.html",
        "btse-case.html",
        "trend-support-case.html",
        "asml-case.html",
    ):
        html = (repo_root / filename).read_text(encoding="utf-8")
        assert "0922" not in html, f"{filename} contains a mobile-number fragment"
        assert "+886" not in html, f"{filename} contains a country-code fragment"
        assert "922 596 190" not in html, f"{filename} contains a phone-number fragment"


def test_index_has_one_primary_heading_and_standards_doctype(repo_root):
    html = (repo_root / "index.html").read_text(encoding="utf-8")
    parser = HeadingCounter()
    parser.feed(html)

    assert html.lower().startswith("<!doctype html>")
    assert parser.h1_count == 1


def test_external_urls_are_allowlisted(repo_root):
    unexpected = []
    for filename in (
        "index.html",
        "404.html",
        "dlp-case.html",
        "resume.html",
        "btse-case.html",
        "trend-support-case.html",
        "asml-case.html",
    ):
        html = (repo_root / filename).read_text(encoding="utf-8")
        urls = re.findall(r"https?://[^\"'\s<>]+", html)
        unexpected.extend(
            f"{filename}: {url}"
            for url in urls
            if not (
                url.startswith("https://sanyoii.github.io/")
                or url.startswith("https://www.linkedin.com/")
                or url.startswith("https://github.com/sanyoii")
                or url == "http://www.w3.org/2000/svg"
            )
        )
    assert unexpected == []


def test_portfolio_publishes_only_canonical_claim_wording(repo_root):
    html = (repo_root / "index.html").read_text(encoding="utf-8")

    assert "critical defects" not in html
    assert "重大邏輯錯誤" not in html
    assert ">TypeScript</span>" not in html
    assert "high-severity defects" in html
    assert "高嚴重度缺陷" in html


def test_bilingual_readmes_switch_and_stay_off_the_site(repo_root):
    english = (repo_root / "README.md").read_text(encoding="utf-8")
    chinese = (repo_root / "README.zh-TW.md").read_text(encoding="utf-8")
    workflow = (repo_root / ".github/workflows/pages.yml").read_text(encoding="utf-8")

    assert english.startswith("**English** | [繁體中文](README.zh-TW.md)\n")
    assert chinese.startswith("[English](README.md) | **繁體中文**\n")
    assert "--exclude '/README.md'" in workflow
    assert "--exclude '/README.zh-TW.md'" in workflow
    assert (repo_root / "index.html").is_file()
    assert (repo_root / ".nojekyll").is_file()
    assert "sanyoii@gmail.com" in (repo_root / "index.html").read_text(encoding="utf-8")
    for banned in ("D:/", "D:\\", "docs/reviews", "（台灣說法待確認）", "複測", "出場", "優先級"):
        assert banned not in chinese


def test_contact_links_use_short_labels_and_preserve_destinations(repo_root):
    html = (repo_root / "index.html").read_text(encoding="utf-8")

    assert '<span class="reach-text">LinkedIn</span>' in html
    assert '<span class="reach-text">GitHub</span>' in html
    assert 'href="https://www.linkedin.com/in/williamlu5405"' in html
    assert 'href="https://github.com/sanyoii"' in html


def test_day20_public_evidence_is_cross_linked(repo_root):
    base = "https://github.com/sanyoii/sanyoii.github.io/blob/main/"
    public_resume = "PUBLIC_QA_PRODUCT_QUALITY_RESUME.md"
    case_studies = (
        "BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md",
        "TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md",
        "ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md",
    )
    html = (repo_root / "index.html").read_text(encoding="utf-8")

    assert 'id="evidence"' in html
    assert 'href="resume.html"' in html
    pages = ('btse-case.html', 'trend-support-case.html', 'asml-case.html')
    for filename, page in zip(case_studies, pages):
        assert f'href="{page}"' in html
        assert f'{base}{filename}' in (repo_root / page).read_text(encoding='utf-8')
    assert f'{base}{public_resume}' in (repo_root / 'resume.html').read_text(encoding='utf-8')

    resume = (repo_root / public_resume).read_text(encoding="utf-8")
    assert "https://sanyoii.github.io/" in resume
    assert f'{base}{public_resume}' not in resume
    assert "independent verification" in resume
    assert "Local release candidate" not in resume
    for filename in case_studies:
        assert f'{base}{filename}' in resume
        case_study = (repo_root / filename).read_text(encoding="utf-8")
        assert "https://sanyoii.github.io/" in case_study
        assert f'{base}{public_resume}' in case_study
        assert "independent verification" in case_study
        assert "Local only" not in case_study
        assert "Do not publish or link" not in case_study


def test_public_resume_excludes_private_application_content(repo_root):
    resume = (repo_root / "PUBLIC_QA_PRODUCT_QUALITY_RESUME.md").read_text(
        encoding="utf-8"
    )

    assert "+886" not in resume
    assert "0922" not in resume
    assert "922 596 190" not in resume
    assert "Private Day 13 Appendix" not in resume
    assert "private role-specific source" not in resume


def test_role_paths_and_work_evidence_are_reachable(repo_root):
    html = (repo_root / "index.html").read_text(encoding="utf-8")
    for anchor in ("btse-evidence", "support-evidence", "asml-evidence", "cex-lab"):
        assert f'id="{anchor}"' in html
    assert 'href="#evidence"' in html
    for case in ('btse-case.html', 'trend-support-case.html', 'asml-case.html', 'dlp-case.html'):
        assert f'href="{case}"' in html
        assert (repo_root / case).is_file()
    assert 'href="assets/William-Lu-Public-QA-Resume.pdf"' in html
    assert (repo_root / "assets/William-Lu-Public-QA-Resume.pdf").is_file()
    assert 'href="test-status/"' in html
    assert (repo_root / "test-status/index.html").is_file()
    assert 'href="https://github.com/sanyoii/cex-market-data-quality-lab"' in html
    assert 'href="https://github.com/sanyoii/cex-market-data-quality-lab/actions"' in html
    # Non-QA experiments live off the homepage; their assets stay in the repo.
    for off_home in ("hd-decode", "Codex Skill Dashboard", "jobsmith"):
        assert off_home not in html
    assert "my work at Binance" not in html
