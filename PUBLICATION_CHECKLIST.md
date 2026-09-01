# Day 16 / Day 20 — Portfolio Controlled Release Checklist

> Status: `Day 20 Website Production PASS · LinkedIn / platforms pending`
> Audit date: 2026-09-01 (Asia/Taipei)
> Scope: `index.html`、三份 case studies、公開 Resume、`404.html`、`assets/og-card.png`、GitHub Pages production 與 release／rollback path
> Canonical content source: `PROFILE_CONTENT_SOURCE.md` (`Frozen v1.2`)
> Production URL: `https://sanyoii.github.io/`
> Boundary: Day 16 與 Day 20 網站均已完成授權部署與 production verification；LinkedIn／其他平台仍未修改，也未送出表單。

## 1. Release decision

**Decision: `DAY 20 WEBSITE PRODUCTION PASS / PROFILE UPDATES PENDING`**

Day 16 audit 發現的兩個 content blockers 已在 local candidate 修正：

1. Hero 已改為 canonical `high-severity defects`／`高嚴重度缺陷`。
2. 未取得 verified evidence 的 `TypeScript` badge 已移除。

Day 16 已在取得當次授權後完成部署，最後驗證的 production commit 為 `7870505`。Day 20 website content commit `07247a6` 已將三份 case studies、公開 Resume 與網站互相連結；隔離 worktree 的完整 Portfolio suite 與 staged-diff gate 均通過。

2026-09-01 已取得 Day 20 網站發布授權。非 force push 將 `main` 從 `7870505` 前進到 `07247a6`；GitHub Pages run `33520661052` 在 `1m 39s` 後成功。fresh production verification 已確認 `#evidence`、四份公開文件、桌面／手機、EN／繁中、3 張作品圖片與空 console。LinkedIn／其他 live profiles 不在本次授權範圍。

### Status legend

| Status | Definition |
|---|---|
| `Pass` | 2026-09-01 有 fresh evidence，且符合本清單 requirement |
| `Fail` | 已確認違反 requirement；publication blocker |
| `Blocked` | 受環境或權限阻擋，無法完成驗證 |
| `Unknown` | 沒有足夠 fresh evidence；不得推定為 Pass |
| `N/A` | 不屬於本次 scope，並記錄原因 |

網站發布 required items 已全為 `Pass`，因此 Day 20 website 標為 `Production PASS`；LinkedIn 與選定平台更新仍是 Day 20 的獨立未完成項目。

## 2. Candidate and evidence identity

| Item | Evidence | Status |
|---|---|---|
| Release worktree | Base `7870505`；branch `codex/day20-controlled-release`；isolated path `.worktrees/day20-controlled-release-20260901` | `Pass` |
| Day 20 staged scope | `index.html`、`tests/test_static.py`、三份 case studies、公開 Resume、此 checklist，共 7 files | `Pass` |
| Published content source | GitHub `main` content commit = `07247a6984e0b56b132bfacfb6bd849a78546111`；non-force push range `7870505..07247a6` | `Pass` |
| Day 20 Pages deployment | GitHub Actions run `33520661052`，head `07247a6`，conclusion `success`，duration `1m 39s` | `Pass` |
| Last verified Day 16 production | Last-fetched `refs/remotes/origin/main` = `7870505`；Pages content run `33413123839` and docs run `33413694716` concluded `success` | `Pass` |
| RiskQA release gate | `RiskQADemoSite` public `main` = `481ee31`；evidence state `Unknown/Stale`，`expiresAt=2026-09-07T23:56:31+08:00`；`npm test`、`npm run lint`、`npm run build` 均通過 | `Pass` |
| Original repository scope | 原始 dirty working tree 保留；發布只在隔離 worktree 操作，未清理、stash 或覆寫其他變更 | `Pass` |

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
| C-09 | 三份 case studies 與公開 Resume 維持 evidence limits 並有雙向 cross-links | Static tests＋文件 inspection | `Pass` | 公開 Resume 不含私人電話或 application-only appendix；四份文件均連回 Portfolio |

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
| L-02 | External URL 僅使用 allowlist | `tests/test_static.py::test_external_urls_are_allowlisted` | `Pass` | GitHub、LinkedIn、production assets only；LinkedIn／GitHub 顯示文字保留完整 `https://` |
| L-03 | LinkedIn contact link 可到達指定 profile | Production direct navigation | `Pass` | Final URL `https://www.linkedin.com/in/williamlu5405/`；title `William Lu \| LinkedIn` |
| L-04 | GitHub contact link可到達指定 profile | Production direct navigation | `Pass` | Final URL `https://github.com/sanyoii`；title `sanyoii · GitHub` |
| L-05 | Email link schema 正確 | DOM inspection | `Pass` | `mailto:sanyoii@gmail.com`；未實際寄信 |
| L-06 | Portfolio images 在 production 載入成功 | Production lazy-load scroll＋DOM image state | `Pass` | 3 張 work images 均 `complete=true`，尺寸為 1440×900、2560×1720、1440×900 |
| L-07 | Day 20 Evidence section 暴露三份 case studies 與公開 Resume | Production DOM＋公開 GitHub main 檔案清單 | `Pass` | 4 個 GitHub `blob/main` URLs 均有 accessible link name、`target=_blank` 與 `rel=noopener`；四個檔名都公開可見 |

## 6. Production rendering and responsive behavior

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| P-01 | Production document 完整載入並使用 standards mode | Production DOM inspection | `Pass` | `readyState=complete`、`CSS1Compat`、1 個 `h1` |
| P-02 | Desktop rendering 無缺圖或 console error | Production 1440×900 target viewport＋DOM／console inspection | `Pass` | Browser 實際回報 1441×900；3 images loaded；console `[]` |
| P-03 | 375／768／1440 widths 無 horizontal overflow | Fresh automated suite＋production desktop／mobile DOM | `Pass` | automated widths 全通過；production 1441 desktop 與 391 mobile 均無 horizontal overflow |
| P-04 | 390×844 mobile Hero 不與 language toggle 重疊，CTA 在 viewport budget 內 | Production mobile geometry inspection | `Pass` | EN CTA bottom `788.81 < 844`；ZH CTA bottom `668.43 < 844`；toggle overlap = false |
| P-05 | EN／ZH Hero fold budget 均符合 test contract | Fresh local browser suite | `Pass` | 1366×768、1440×900、390×844、375×812 均通過 |
| P-06 | 404 page 不被索引且能回首頁 | Fresh local browser suite | `Pass` | `noindex`＋home link |
| P-07 | Day 20 Evidence cards 在 desktop／mobile 不重疊或水平溢出 | Codex in-app Browser，1440×900 target 與 390×844 target | `Pass` | Desktop 2×2；mobile 單欄；out-of-viewport = 0，overlap count = 0 |

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
| R-03 | Browser runtime suite | `./.venv/Scripts/python.exe -m pytest tests/ -q` | `Pass` | Day 20 release candidate fresh run：`21 passed in 10.64s` |
| R-04 | Day 20 production Browser gate | Codex in-app Browser on `https://sanyoii.github.io/?day20=07247a6` | `Pass` | EN／繁中切換同步 title、`html lang` 與 accessible toggle name；3 images complete；console `[]` |

## 8. Rollback readiness

| ID | Requirement | Method／evidence | Status | Notes |
|---|---|---|---|---|
| RB-01 | 可識別目前網站內容的 production recovery point | GitHub main／Actions evidence | `Pass` | content commit `07247a6`；successful Pages run `33520661052` |
| RB-02 | Rollback 不改寫 Git history | Procedure review | `Pass` | 使用 `git revert <bad-commit>`，禁止 `reset --hard`／force-push |
| RB-03 | Rollback 後重新通過 deployment 與 production gate | Procedure documented below | `Pass` | 必須等待 Pages success，再重跑本清單 required checks |
| RB-04 | 實際 production rollback drill | 本次沒有刻意製造 production failure | `N/A` | 不把未執行的 rollback 說成已驗證 |

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
- [x] Day 16 最終 release candidate：`19 passed`。
- [x] 重新檢查 content diff，沒有新增未核准 claims。
- [x] Day 20 網站發布已取得當次明確授權，並已建立隔離 worktree。
- [x] Day 20 完整 suite：`21 passed in 10.64s`。
- [x] Day 20 staged-diff gate：精確 7 files，沒有 missing／extra，`git diff --cached --check` 通過。
- [x] Day 20 content commit `07247a6` 已 non-force push；Pages run `33520661052` 成功；fresh production verification 通過。
- [ ] LinkedIn 與選定平台更新；不在本次網站發布授權範圍。

## 10. Execution notes

- 第一次從 repository root 執行未限定路徑的 `pytest`，誤收進 nested `cex-market-data-quality-lab` tests，因該 project dependencies／import path 不屬於 Portfolio environment 而 collection failed。這不是 Portfolio test result。
- 限定正確 scope `tests/` 後，sandbox 內 Chromium 因 `spawn EPERM` 無法啟動；獲准在 sandbox 外執行相同 command 後，初次 audit 為 `17 passed`，blocker remediation 加入 regression test 後為 `18 passed`，Day 16 contact URL 顯示 regression test 後最終為 `19 passed`。
- `wmux browser` 當次無法連線，因此依 project fallback rule 使用 Codex in-app browser 完成 production read-only inspection。
- Production full-page screenshot 在 capture stitching 中出現重複區塊；DOM count 複核為 3 個 Proof cards、4 個 Work cards、1 個 Education heading、1 個 Contact line，故判定為 screenshot artifact，不是 production DOM duplication。
- Blocker remediation 採 test-first：新增 canonical claim wording regression test，修正前 `1 failed`，修改 Hero wording 並移除 `TypeScript` badge 後 targeted test 與完整 suite 均通過。
- Day 20 先新增 cross-link／public-resume regression tests，實作前為 `2 failed, 5 passed`；保留 Day 16 contact URL 顯示 regression test 後，targeted static tests 為 `8 passed`，完整 suite 為 `21 passed in 10.64s`。
- Day 20 Browser 的 full-page capture 因長頁面與進場動畫再次出現 stitching 重影；單一 viewport、DOM counts、card rectangles 與 overlap calculation 均正常，因此不視為頁面 duplication。
- Day 20 external read-only precheck：GitHub public commit history 顯示 `main` 最新 commit `7870505`、checks `2 / 2`；production DOM 沒有 `#evidence`，0 console warning／error，確認 Day 20 candidate 尚未發布。
- Day 20 content commit `07247a6` 已以非 force `HEAD:main` push；Pages run `33520661052` 成功。production 1440×900 target 與 390×844 target 均無 overflow／Evidence card overlap，EN／繁中、4 個公開文件、3 張圖片與 console gate 全部通過。
- `raw.githubusercontent.com` 被 Browser client policy 以 `ERR_BLOCKED_BY_CLIENT` 擋下；未將此誤判為 source 404，改以 4 個 `blob/main` 頁面 title 與公開 repository main 檔案清單交叉確認。
