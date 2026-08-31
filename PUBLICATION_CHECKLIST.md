# Day 16 — Portfolio Publication Checklist

> Status: `Complete v1 / Production PASS`
> Audit date: 2026-09-01 (Asia/Taipei)
> Scope: `index.html`、`404.html`、`assets/og-card.png`、GitHub Pages production 與 release／rollback path
> Canonical content source: `PROFILE_CONTENT_SOURCE.md` (`Frozen v1.2`)
> Production URL: `https://sanyoii.github.io/`
> Day 16 boundary: 本次完成 local audit、content remediation、regression test、授權部署與 production verification；未修改 live profiles、未送出表單。

## 1. Release decision

**Decision: `PRODUCTION PASS`**

Day 16 audit 發現的兩個 content blockers 已在 local candidate 修正：

1. Hero 已改為 canonical `high-severity defects`／`高嚴重度缺陷`。
2. 未取得 verified evidence 的 `TypeScript` badge 已移除。

Local Portfolio suite fresh result 為 `19 passed`，且新增 regression tests 防止 canonical wording、unsupported badge 與 contact URL 顯示回歸。經使用者明確授權後，Portfolio commits `62adfc6`、`0915582` 與 RiskQA freshness commit `481ee31` 已推送；GitHub Pages run `33413123839` 成功部署，production read-only verification 通過。

### Status legend

| Status | Definition |
|---|---|
| `Pass` | 2026-08-31 有 fresh evidence，且符合本清單 requirement |
| `Fail` | 已確認違反 requirement；publication blocker |
| `Blocked` | 受環境或權限阻擋，無法完成驗證 |
| `Unknown` | 沒有足夠 fresh evidence；不得推定為 Pass |
| `N/A` | 不屬於本次 scope，並記錄原因 |

Local required items 全為 `Pass` 時，local candidate 才能標為 `PASS`。Production 已完成授權部署與 fresh live verification，因此本清單解除 `HOLD`。

## 2. Candidate and evidence identity

| Item | Evidence | Status |
|---|---|---|
| Local source | Release worktree `HEAD` = `0915582f63a1858c3e1d4a8c3c3693cad4361ac3` | `Pass` |
| Remote source | GitHub `main` = `0915582f63a1858c3e1d4a8c3c3693cad4361ac3` | `Pass` |
| Local／remote content boundary | Release worktree 與 remote main 指向同一 content commit；`404.html` 未變更 | `Pass` |
| Latest Pages deployment | GitHub Actions run `33413123839`，head `0915582`，conclusion `success` | `Pass` |
| Local repository scope | 隔離 release worktree 僅含兩個 Portfolio fixes 與本清單；原始 dirty worktree 未納入 commit | `Pass` |

## 3. Content consistency and claim boundary

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| C-01 | Name、Primary role、location 與 positioning 對齊 canonical source | 比對 `PROFILE_CONTENT_SOURCE.md` §§2–4 與 Hero | `Pass` | William Lu、Senior QA、Web3／Crypto、Taiwan UTC+8 一致 |
| C-02 | BTSE、ASML、Trend Micro 的職稱、數字、attribution 與 chronology 不超出核准範圍 | 比對 canonical bullet bank 與 `index.html` Proof／Timeline | `Pass` | 3 個 high-severity defects、6 位 engineers、2 次 internal awards、12+ years 均有對應 source |
| C-03 | Degree wording 與日期對齊 reconciled source | 比對 MS／BS 欄位與 `Education` section | `Pass` | MS 2003–2005；BS 1998–2003 |
| C-04 | 不把 high-severity defects 升級成 critical | `index.html` Hero availability text＋regression test | `Pass` | Local EN／ZH 已改為 `high-severity defects`／`高嚴重度缺陷` |
| C-05 | Work evidence 與 Portfolio evidence 明確分區 | Proof／Timeline／Capabilities 與 `Systems I build` 為獨立 sections | `Pass` | Portfolio tooling 未寫成 prior-employment use |
| C-06 | Skills／technology badges 不得包含 canonical source 明列的 unsupported claim | `TypeScript` badge scan＋regression test | `Pass` | Local candidate 已移除 `TypeScript` badge |
| C-07 | Career break 不公開 health、relationship 或其他 private details | Timeline 只寫 caregiving 與 self-directed study | `Pass` | 未暴露被禁止的 private details |
| C-08 | CTA 與 contact wording 符合目前 QA／Product Quality／Technical Support routing | Hero CTA 與 contact section inspection | `Pass` | 沒有導向 excluded Customer Success／general PM positioning |

## 4. SEO and social preview

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| S-01 | Default title 與 canonical website short title 一致 | HTML head＋production runtime | `Pass` | `William Lu — Senior QA Engineer \| Web3 & Crypto` |
| S-02 | Meta description、`og:title`、`og:description`、`og:type`、`og:url`、`og:image` 與 Twitter card 存在 | Static inspection | `Pass` | Production URL 與 absolute OG image URL 正確 |
| S-03 | OG image 可載入且尺寸正確 | Production direct image inspection | `Pass` | `1200 × 630`，loaded successfully |
| S-04 | EN／ZH runtime title、description 與 `html lang` 同步 | Production language toggle inspection＋automated runtime test | `Pass` | EN `lang=en`；ZH `lang=zh-Hant` |
| S-05 | Social crawler locale boundary 明確 | Static OG tags inspection | `Pass` | 單一 URL 採 English canonical OG；JS 切換不改 OG tags，不宣稱 localized social cards |

## 5. Links and assets

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| L-01 | Internal anchors 有對應 target | Static test＋DOM inspection | `Pass` | `#main`、`#top`、`#impact`、`#work`、`#capabilities`、`#contact` 均存在 |
| L-02 | External URL 僅使用 allowlist | `tests/test_static.py::test_external_urls_are_allowlisted` | `Pass` | GitHub、LinkedIn、production assets only；LinkedIn／GitHub 顯示文字含完整 `https://` |
| L-03 | LinkedIn contact link 可到達指定 profile | Production direct navigation | `Pass` | Final URL `https://www.linkedin.com/in/williamlu5405/`；title `William Lu \| LinkedIn` |
| L-04 | GitHub contact link可到達指定 profile | Production direct navigation | `Pass` | Final URL `https://github.com/sanyoii`；title `sanyoii · GitHub` |
| L-05 | Email link schema 正確 | DOM inspection | `Pass` | `mailto:sanyoii@gmail.com`；未實際寄信 |
| L-06 | Portfolio images 在 production 載入成功 | Full-page production rendering＋DOM image state | `Pass` | 3 張 work images 均 complete，`naturalWidth > 0` |

## 6. Production rendering and responsive behavior

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| P-01 | Production document 完整載入並使用 standards mode | Production DOM inspection | `Pass` | `readyState=complete`、`CSS1Compat`、1 個 `h1` |
| P-02 | Desktop rendering 無缺圖或 console error | 1280×720 production full-page visual inspection＋console log check | `Pass` | 0 broken images、0 console errors |
| P-03 | 375／768／1440 widths 無 horizontal overflow | Fresh local browser suite | `Pass` | 3 個 widths 均通過 |
| P-04 | 375×812 mobile Hero 不與 language toggle 重疊，CTA 在 viewport budget 內 | Fresh local browser suite＋production 375×812 inspection | `Pass` | Production `scrollWidth=360`、viewport width `375`、CTA bottom約 `708 < 813` |
| P-05 | EN／ZH Hero fold budget 均符合 test contract | Fresh local browser suite | `Pass` | 1366×768、1440×900、390×844、375×812 均通過 |
| P-06 | 404 page 不被索引且能回首頁 | Fresh local browser suite | `Pass` | `noindex`＋home link |

## 7. Accessibility and runtime

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| A-01 | Bilingual text 與 image alt attributes 成對 | Fresh static tests | `Pass` | `data-en`／`data-zh` 與 `data-alt-en`／`data-alt-zh` counts paired |
| A-02 | Document semantics 有 doctype、單一 `h1` 與 skip link | Static test＋source inspection | `Pass` | Skip link target = `#main` |
| A-03 | Language toggle 有 accessible name 並同步 `html lang` | Source＋production runtime inspection | `Pass` | `aria-label` 隨語言更新 |
| A-04 | Reduced-motion 不隱藏 `.fade` content | Fresh runtime test | `Pass` | 所有受測元素 opacity ≥ 0.9 |
| A-05 | Contact SVG 不進入 accessibility tree | Source inspection | `Pass` | `aria-hidden=true`、`focusable=false` |
| A-06 | Full WCAG 2.1 AA、screen reader 與 color-contrast certification | 本次未執行完整 conformance audit | `N/A` | 本清單只證明 smoke checks；不得宣稱 WCAG conformance |
| R-01 | 首頁不產生 external runtime requests | Fresh runtime test | `Pass` | Dependency-free runtime contract 通過 |
| R-02 | Language choice 更新內容、metadata 並在 reload 後保留 | Fresh runtime test | `Pass` | `wl-lang` persistence 通過 automated test |
| R-03 | Browser runtime suite | `./.venv/Scripts/python.exe -m pytest tests/ -q` | `Pass` | 最終 release candidate fresh run：`19 passed` |

## 8. Rollback readiness

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| RB-01 | 可識別目前 production recovery point | GitHub API／Actions evidence | `Pass` | Remote main `0915582`；successful Pages run `33413123839` |
| RB-02 | Rollback 不改寫 Git history | Procedure review | `Pass` | 使用 `git revert <bad-commit>`，禁止 `reset --hard`／force-push |
| RB-03 | Rollback 後重新通過 deployment 與 production gate | Procedure documented below | `Pass` | 必須等待 Pages success，再重跑本清單 required checks |
| RB-04 | 實際 production rollback drill | 本次未故意製造 production failure | `N/A` | 不把未執行的 rollback 說成已驗證 |

### Rollback procedure

1. 先確認 production failure、bad commit 與最後一個 known-good Pages run。
2. 取得當次明確 deploy 授權後，以 `git revert <bad-commit>` 建立可追溯的復原 commit；不得 force-push 或 rewrite history。
3. Push 前跑 `./.venv/Scripts/python.exe -m pytest tests/ -q`。
4. Push 後等待 GitHub Pages workflow 完成，確認 run conclusion = `success`。
5. 重新驗證 production title／description、EN／ZH 切換、desktop／mobile、links、images、console errors 與 404 behavior。
6. 將 recovery commit、workflow run URL、production check date 與結果記回本文件或當次 test record。

## 9. Required remediation before `PASS`

- [x] 將 Hero EN `critical defects` 改為 canonical `high-severity defects`。
- [x] 將 Hero ZH `重大邏輯錯誤` 改為 canonical `高嚴重度缺陷`。
- [x] 從 Portfolio 移除沒有 verified evidence 的 `TypeScript` badge。
- [x] 修正後重跑 `./.venv/Scripts/python.exe -m pytest tests/ -q`：`19 passed`。
- [x] 重新檢查 content diff，沒有新增未核准 claims。
- [x] 取得當次明確授權後完成 commit／push／deploy；run `33413123839` 成功。
- [x] Production 驗證 EN／ZH、1440／390 widths、contact URLs、3 張 lazy images 與 console：全部通過。

## 10. Execution notes

- 第一次從 repository root 執行未限定路徑的 `pytest`，誤收進 nested `cex-market-data-quality-lab` tests，因該 project dependencies／import path 不屬於 Portfolio environment 而 collection failed。這不是 Portfolio test result。
- 限定正確 scope `tests/` 後，sandbox 內 Chromium 因 `spawn EPERM` 無法啟動；獲准在 sandbox 外執行相同 command 後，初次 audit 為 `17 passed`，canonical claim regression 後為 `18 passed`，contact URL display regression 後最終為 `19 passed`。
- `wmux browser` 當次無法連線，因此依 project fallback rule 使用 Codex in-app browser 完成 production read-only inspection。
- Production full-page screenshot 在 capture stitching 中出現重複區塊；DOM count 複核為 3 個 Proof cards、4 個 Work cards、1 個 Education heading、1 個 Contact line，故判定為 screenshot artifact，不是 production DOM duplication。
- Blocker remediation 採 test-first：新增 canonical claim wording regression test，修正前 `1 failed`，修改 Hero wording 並移除 `TypeScript` badge 後 targeted test 與完整 suite 均通過。
- Contact URL display 亦採 test-first：新增完整 `https://` 顯示測試後先得到 `1 failed`，修正 LinkedIn／GitHub 顯示文字後 targeted 與完整 suite 均通過。
- Production run `33413123839` 對 head `0915582` 完成 build 與 deploy；in-app browser fresh verification 為 desktop/mobile 無 overflow、EN/ZH 正確、3 張 lazy images `complete=true` 且 `naturalWidth>0`、console 0 error/warn。
