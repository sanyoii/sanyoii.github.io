# Portfolio 站內閱讀驗收

> 後續修正：使用者確認本輪公開履歷仍沿用舊技能分類，另指出繁中文案與連結配置問題。以下 56 項 PASS 僅證明當時指定來源的轉換與功能，不能證明履歷已同步最新核准版本，也不能代替中文與資訊安排驗收。修訂草稿見 `docs/reviews/2026-09-21-portfolio-revision/REVIEW.md`；目前尚待確認後套用。

日期：2026-09-21。範圍：已核准計畫的本機實作與驗收。未 stage、commit、push 或發布。

## 實作結果

- 新增 `btse-case.html`、`trend-support-case.html`、`asml-case.html`、`resume.html`；前三頁雙語，履歷維持英文。
- 首頁既有案例與履歷 CTA 改指向站內；Trend incident 的文字連結改成明確的 Technical Support／Incident RCA 入口，附診斷、恢復與 hotfix 驗證說明。
- QA 主定位、remote 條件、DLP 原有卡片及 Other experiments 預設收合保留。
- 共用 Python 產生器從公開 Markdown 產生靜態 HTML；模板、CSS、JavaScript 與 renderer 版本納入建置指紋。`--check` 不寫檔。
- 原始三篇案例與公開履歷 Markdown 均未修改，與基準 SHA-256 相同；既有 DLP 頁面也相同。轉換只處理展示結構與站內連結。
- 手機目錄預設收合，桌面展開；原始來源說明置於正文之後，完整各語言證據限制仍在正文。長表格局部橫捲且提示不隨表格移走。

## 實際驗證

主機環境：Python 3.14，pytest 9.1.1、Playwright 1.58.0、markdown-it-py 4.2.0，皆為既有安裝。本次未安裝依賴。沙箱 Python 看不到這些 user-site 套件，改用主機既有環境完成驗收。

| 命令／檢查 | 結果 |
|---|---|
| `py -3 -X utf8 -m pytest tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py -q`（基準） | exit 0；25 passed，26.33 秒 |
| `py -3 -X utf8 scripts/build_portfolio_pages.py` | exit 0；Built 4 portfolio pages |
| `py -3 -X utf8 scripts/build_portfolio_pages.py --check` | exit 0；Checked 4 portfolio pages |
| `py -3 -X utf8 -m pytest -p no:cacheprovider tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py tests/test_portfolio_pages.py -q`（最後版本） | exit 0；56 passed，40.98 秒 |
| `py -3 -X utf8 test-records/2026-09-21-portfolio-case-reading/capture.py after` | exit 0；70 張最終截圖 |
| `git diff --check -- index.html tests/test_static.py tests/test_runtime.py` | exit 0；無 whitespace error |
| 11 個實作／測試檔 UTF-8 解碼與 SHA-256 | 成功；見 `final-hashes.json` |

56 項包含完整來源文字比對（所有段落與表格資料）、四頁×四種寬度（320／390／768／1440）、雙語切換／刷新／返回、站內目的頁與錨點、外部資源請求與 pageerror、英文履歷不覆寫中文偏好、鍵盤基本操作、CSS 200% zoom、停用 JavaScript 的英文閱讀，以及既有首頁／DLP 回歸。

反例涵蓋未支援 footnote／directive／image 語法、缺少來源、暫存副本的來源變更；確認失敗時非零且不覆寫既有產物。HTML markup 與不安全連結也有 escaping／拒絕檢查。

基準與最後版本的首頁 BTSE 入口位置相同（document y，CSS px）：

| 畫面 | 改前 | 改後 |
|---|---:|---:|
| 390×844 英文 | 903.609375 | 903.609375 |
| 390×844 中文 | 801.328125 | 801.328125 |
| 1440×900 英文 | 765.796875 | 765.796875 |
| 1440×900 中文 | 717.609375 | 717.609375 |

390×844 主要 CTA 在首屏；並未宣稱英文 BTSE 卡片本身已移進首屏。

## 目視驗收與限制

已實際檢视代表畫面：BTSE 手機英文首屏、中文長表格右端、Trend 桌面英文案例、ASML 手機中文證據限制與頁尾、英文履歷手機首屏。初版目錄過長與表格提示被捲走已修正，最終截圖重新擷取並檢视；新頁面配色對齊現有首頁／DLP。

`after/` 保留所有畫面；代表檔名：
- `btse-case-390-en-top.png`
- `btse-case-390-zh-table-end.png`
- `trend-support-case-1440-en-top.png`
- `asml-case-390-zh-footer.png`
- `resume-390-en-top.png`

限制：使用 Chromium 與模擬 viewport；沒有真手機、screen reader、Firefox／Safari、真人招募者或轉換率驗證。200% 為 CSS zoom smoke check，不是完整作業系統／瀏覽器縮放驗收。未宣稱完整 WCAG 合規。長表格在小螢幕仍需橫向捲動。

環境既有 requests 套件版本警告未影響測試；基準 pytest cache 無法寫入，最後測試停用 cache，不修改權限或套件。Git 有 LF→CRLF 提示，檔案未因此重新格式化。

## 證據與回復

- `before/`：8 個基準檔副本；`baseline-hashes.json`：原始雜湊；`baseline-status.txt`：原有工作區狀態。
- `baseline/metrics.json`、`after/metrics.json`：首頁位置比較。
- `final-hashes.json`：本次 11 個實作／測試檔雜湊。
- 不變來源與 DLP 雜湊已讀回核對；原有 Dashboard、README、TESTPLAN、`.gitignore` 及其他修改未納入本次編輯。
- 回復時只還原本次片段，先核對是否有後續修改；不使用 reset／checkout／全目錄覆寫。

重建使用已安裝 markdown-it-py 的主機 Python。線上尚未更新，這份驗收不構成發布證據；Git 與發布需要另行明確授權。
