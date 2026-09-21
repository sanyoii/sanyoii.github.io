import pytest


@pytest.mark.parametrize("width", [375, 768, 1440])
def test_dlp_case_navigation_language_and_layout(browser, site_url, width):
    context = browser.new_context(viewport={"width": width, "height": 900})
    page = context.new_page()
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)))
    page.goto(site_url)
    page.locator('a[href="dlp-case.html"]').click()
    assert page.url.endswith("/dlp-case.html")
    for language in ["en", "zh-Hant"]:
        assert page.locator("html").get_attribute("lang") == language
        assert page.evaluate("document.documentElement.scrollWidth <= innerWidth")
        assert page.locator("h1").is_visible()
        assert page.locator("#intake .source").inner_text()
        page.locator("details summary").click()
        assert page.locator(".detail-list").is_visible()
        page.locator("details summary").click()
        if language == "en":
            page.locator("#langBtn").click()
            page.reload()
    page.locator('footer a[href="index.html#evidence"]').click()
    assert page.locator("html").get_attribute("lang") == "zh-Hant"
    assert page.locator("#evidence").is_visible()
    assert errors == []
    context.close()
