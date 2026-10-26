"""Guard user-confirmed claim boundaries, not an obsolete candidate snapshot."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_btse_case_separates_authored_cases_from_wallet_usage():
    text = (ROOT / 'BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md').read_text(encoding='utf-8')
    assert 'used TestRail for Wallet cases' in text
    assert 'Convert test cases and study scenarios in the internal Wiki' in text
    assert '並使用 TestRail 執行 Wallet 測試案例' in text
    assert '內部 Wiki' in text
    assert 'TestRail for Wallet, Referral and Affiliate, and Convert' not in text


def test_resume_preserves_case_ownership_and_unresolved_outcome():
    text = (ROOT / 'PUBLIC_QA_PRODUCT_QUALITY_RESUME.md').read_text(encoding='utf-8')
    assert 'used TestRail for Wallet cases' in text
    assert 'remained open when I left' in text
    assert 'first-month SEG-to-L2 missing-info returns' in text
    assert 'manager-shared figures' in text
    assert not re.search(r'Authored[^\n]*, Wallet test cases', text)


def test_home_short_metric_keeps_scope_and_return_direction():
    text = (ROOT / 'index.html').read_text(encoding='utf-8')
    assert 'first-month SEG-to-L2 missing-info returns' in text
    assert 'SEG 因缺件退回 L2' in text
    assert '(manager-reported)' in text
    assert 'CPU/RAM' not in text
    assert '≥10% DLP CPU/RAM Cut' not in text
