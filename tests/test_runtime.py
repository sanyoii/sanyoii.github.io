from urllib.parse import urlparse

import pytest


def open_page(browser, site_url, viewport, **context_options):
    context = browser.new_context(viewport=viewport, **context_options)
    page = context.new_page()
    page.goto(site_url, wait_until="networkidle")
    return context, page


def bottom_of(page, selector):
    return page.locator(selector).evaluate(
        "(element) => element.getBoundingClientRect().bottom"
    )


def assert_above_fold(page, selector):
    assert bottom_of(page, selector) <= page.evaluate("window.innerHeight")


def test_home_page_makes_no_external_network_requests(browser, site_url):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    site_origin = urlparse(site_url).netloc
    external_requests = []

    def record_external_request(request):
        parsed = urlparse(request.url)
        if parsed.scheme in {"http", "https"} and parsed.netloc != site_origin:
            external_requests.append(request.url)

    page.on("request", record_external_request)
    page.goto(site_url, wait_until="networkidle")

    assert external_requests == []
    context.close()


def test_home_page_renders_in_standards_mode(browser, site_url):
    context, page = open_page(browser, site_url, {"width": 1440, "height": 900})

    assert page.evaluate("document.compatMode") == "CSS1Compat"
    context.close()


@pytest.mark.parametrize("width", [375, 768, 1440])
def test_home_page_has_no_horizontal_overflow(browser, site_url, width):
    context, page = open_page(browser, site_url, {"width": width, "height": 900})

    dimensions = page.evaluate(
        "() => ({"
        "scrollWidth: document.documentElement.scrollWidth,"
        "clientWidth: document.documentElement.clientWidth"
        "})"
    )
    assert dimensions["scrollWidth"] == dimensions["clientWidth"]
    context.close()


def test_language_choice_updates_metadata_and_survives_reload(browser, site_url):
    context, page = open_page(browser, site_url, {"width": 1440, "height": 900})

    page.locator("#langBtn").click()

    assert page.locator("html").get_attribute("lang") == "zh-Hant"
    assert page.title() == "William Lu — 資深 QA 工程師｜Web3 與加密產品"
    assert page.locator('meta[name="description"]').get_attribute("content") == (
        "資深 QA 工程師，具 BTSE 中心化加密貨幣交易所測試經驗；"
        "在 Trend Micro 近 13 年經歷中，工作涵蓋資安產品 QA、事件 RCA 與客戶工程。"
    )
    image_alts = page.locator("img[data-alt-zh]").evaluate_all(
        "(images) => images.map((image) => ({"
        "alt: image.alt,"
        "expected: image.getAttribute('data-alt-zh')"
        "}))"
    )
    assert image_alts
    assert all(item["alt"] == item["expected"] for item in image_alts)

    page.reload(wait_until="networkidle")
    assert page.locator("html").get_attribute("lang") == "zh-Hant"
    assert page.evaluate("localStorage.getItem('wl-lang')") == "zh"
    context.close()


@pytest.mark.parametrize(
    ("width", "height"),
    [(1366, 768), (1440, 900), (390, 844), (375, 812)],
)
def test_hero_content_respects_viewport_fold_budget(
    browser, site_url, width, height
):
    context, page = open_page(
        browser,
        site_url,
        {"width": width, "height": height},
        reduced_motion="reduce",
    )

    if (width, height) == (375, 812):
        assert_above_fold(page, ".avail")
    else:
        assert_above_fold(page, ".ctas")

    page.locator("#langBtn").click()
    assert_above_fold(page, ".ctas")
    if (width, height) == (375, 812):
        assert_above_fold(page, ".avail")
    context.close()


def test_mobile_eyebrow_does_not_overlap_language_toggle(browser, site_url):
    context, page = open_page(browser, site_url, {"width": 375, "height": 812})
    eyebrow = page.locator(".eyebrow").bounding_box()
    language_toggle = page.locator(".lang").bounding_box()

    assert eyebrow is not None
    assert language_toggle is not None
    overlaps = not (
        eyebrow["x"] + eyebrow["width"] <= language_toggle["x"]
        or language_toggle["x"] + language_toggle["width"] <= eyebrow["x"]
        or eyebrow["y"] + eyebrow["height"] <= language_toggle["y"]
        or language_toggle["y"] + language_toggle["height"] <= eyebrow["y"]
    )
    assert not overlaps
    context.close()


def test_reduced_motion_keeps_fade_content_visible(browser, site_url):
    context, page = open_page(
        browser,
        site_url,
        {"width": 1440, "height": 900},
        reduced_motion="reduce",
    )
    opacities = page.locator(".fade").evaluate_all(
        "(elements) => elements.map("
        "(element) => Number(getComputedStyle(element).opacity)"
        ")"
    )

    assert opacities
    assert min(opacities) >= 0.9
    context.close()


def test_404_page_is_noindexed_and_links_home(browser, site_url):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    response = page.goto(f"{site_url}/404.html", wait_until="networkidle")

    assert response is not None and response.ok
    robots = page.locator('meta[name="robots"]').get_attribute("content")
    assert robots is not None and "noindex" in robots.lower()
    assert page.locator('a[href="/"]').count() >= 1
    context.close()
