# Portfolio 案例閱讀與求職入口：執行／驗收計畫

狀態：原本機實作完成，但使用者指出履歷版本、繁中文案與入口安排問題，內容驗收重新開啟。修訂草稿見 `docs/reviews/2026-09-21-portfolio-revision/REVIEW.md`，待確認後套用。原功能測試結果見 `test-records/2026-09-21-portfolio-case-reading/RESULT.md`；尚未 commit／push／發布。

## 1. 目標與設計

讓招募者從首頁直接閱讀 BTSE、Trend Micro incident／support、ASML 案例與公開 QA 履歷，減少跨到 GitHub 的步驟。維持 Senior QA／Product Quality 主定位，Technical Support 作為清楚的次要閱讀路徑。

沿用現有靜態 HTML／CSS／JavaScript、Python pytest 與 Playwright。三篇案例以現有雙語 Markdown 為唯一內容來源，在本機建置成靜態 HTML；履歷沿用現有英文公開 Markdown，不自行新增中文翻譯。GitHub 連結保留為來源入口。頁面載入不依賴外部 CDN、執行時 Markdown 下載或新增服務。

視覺沿用首頁與 DLP 的冷靜工程風格。只調整閱讀層級、入口與必要響應式問題，不重新品牌設計，不採 hyper-luxurious 定位。

## 2. 核准範圍與邊界

核准本計畫只授權下列本機實作、產生 HTML 與驗收；不包含 stage、commit、push、發布、修改求職平台或安裝新依賴。執行由主模型單一寫入並驗收，不要求另開 agent。

### 可修改與新增的檔案

| 檔案 | 責任 |
|---|---|
| `index.html` | 案例、Support、履歷入口與必要版面微調 |
| `BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md` | 原始內容；只有必要的標題／摘要／內部連結整理，不能改變事實 |
| `TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md` | 同上，明確呈現 incident／support 閱讀入口 |
| `ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md` | 同上，保留個人與團隊分工 |
| `PUBLIC_QA_PRODUCT_QUALITY_RESUME.md` | 英文公開履歷來源；僅調整必要的站內連結，不擴寫經歷 |
| `scripts/build_portfolio_pages.py` | 新增可重現的靜態頁面產生器及 `--check` 模式 |
| `scripts/templates/portfolio-page.html` | 新增共用版型 |
| `assets/portfolio-pages.css`、`assets/portfolio-pages.js` | 新頁面樣式與語言／導覽行為，不重構既有首頁與 DLP |
| `btse-case.html`、`trend-support-case.html`、`asml-case.html`、`resume.html` | 產生的頁面，不手動維護內容 |
| `tests/test_portfolio_pages.py` | 新增內容轉換、來源一致性與閱讀流程驗收 |
| `tests/test_static.py`、`tests/test_runtime.py` | 僅調整受入口變動影響的斷言，保留原有品質要求 |
| `test-records/2026-09-21-portfolio-case-reading/` | 本次基準、截圖、命令結果與驗收紀錄 |

既有 `dlp-case.html` 保留原流程並執行回歸驗收，本次不遷移其內容架構。

不碰 `.gitignore`、README、TESTPLAN、`test-status/`、既有未追蹤資料、私人履歷與申請包、其他專案、全域 Skill／設定。執行前重新確認工作區；上述可修改檔案若已有新修改，先保存與理解差異，不覆寫其他工作。

不新增 PDF、不替三個 Other experiments 部署 demo、不新增追蹤分析、不改求職主職稱。Other experiments 維持預設收合與現有公開程度標示。

## 3. 執行順序與階段出口

### A. 基準與來源核對

1. 記錄 `git status --short`、範圍內來源檔 SHA-256，保存將修改檔案的原始副本。
2. 執行既有三組網站測試，記錄既有失敗與環境限制，不將舊 PASS 當成此次基準。
3. 對照公開來源、`CLAIM_VERIFICATION_SHEET.md` 與 `PROFILE_CONTENT_SOURCE.md`；只讀私人來源，禁止把私人資料複製進網站。
4. 保存首頁英文／中文的 390×844 與 1440×900 基準畫面及首個案例入口位置。

出口：來源清楚、基準可比較。若事實衝突或必要能力不可用，先報告具體阻擋，不自行改主張或安裝依賴。

### B. BTSE 與共用靜態閱讀版型

1. 建立產生器與版型，先完成 `btse-case.html`。現有 Markdown 的中英段落、標題、清單、表格、強調、連結均須完整呈現。
2. 優先檢查環境是否已有適用的 Markdown renderer；不新增依賴。若以 Python 標準函式庫實作，明確限定三篇案例及履歷所需語法，遇到未支援結構即報錯，不能默默丟字或原樣洩出 Markdown 標記。
3. 所有摘要取自同一 Markdown，不在模板維護第二份事實文案。提供案例標題、摘要、段落導覽、來源與回首頁入口。
4. 新增轉換測試：表格、特殊字元與 HTML escaping、連結、雙語分段、缺少來源與未支援語法的反例。`--check` 檢查現有產物是否與來源／模板一致，不能改寫產物。

出口：BTSE 內容無遺漏、來源可追溯、可獨立開啟、切語言與返回可用。後續頁面沿用此版型，不複製一套產生邏輯。

### C. Support 入口與 Trend Micro 案例

1. 產生 `trend-support-case.html`，清楚區分診斷、恢復服務、workaround、hotfix 驗證與實際結案責任。
2. 首頁新增明確的 Technical Support／Incident RCA 案例入口；保留 DLP 原有卡片與連結，讓讀者能辨認兩者各自的重點。
3. 不以「also open to Senior Technical Support」擴大 hero 職稱，不新增缺乏證據的 support 成效。

出口：從首頁能直接找到並進入 Support 案例；DLP 原流程仍可用；QA 主定位保持清楚。

### D. ASML 與履歷

1. 產生 `asml-case.html`，首頁改連站內，保留 GitHub 來源。
2. 產生英文 `resume.html`；hero 與案例區現有履歷 CTA 指向站內，不新增重複按鈕。清楚標示英文履歷，避免呈現無效中文切換。
3. 保留 Taiwan、Fully Remote、4+ hours European overlap，不改成較弱的偏好表達。

出口：四個新增目的頁連結正確；履歷不含私人電話、附錄或未核准資料；職称、日期、學歷與公開來源一致。

### E. 響應式微調與整合驗收

先檢查實際畫面，只修正溢位、卡片入口不清楚、過大空白或遮擋等可觀察問題。若需要超出既有風格的大幅視覺改版，停止該部分並提出具體方案，不擴大本計畫。

出口：以下驗收矩陣通過，剩餘限制有明確紀錄。本機完成後交付 diff 與證據，等待另行發布指示。

## 4. 驗收矩陣

| 面向 | 必須通過的條件 |
|---|---|
| 內容完整性 | 各語言所有原始段落、表格列、數字、結果與限制皆保留；不得只靠特定關鍵字存在便宣稱完整 |
| 證據邊界 | BTSE 未解決事項不改寫為已修復；ASML 六位工程師與團隊實作分工保留；20 個百分點仍標明主管來源與缺少原始資料；CPU／memory 數字保留適用範圍與回憶來源 |
| 產物一致性 | 連續建置結果相同；`--check` 成功不寫檔；測試用暫存副本變更來源後，舊產物須被判定過期並回傳非零 |
| 導覽 | 首頁→每個案例／履歷→來源／返回案例區均可使用；站內連結無 404；舊 DLP 與錨點流程無回歸 |
| 語言 | 三篇案例英／繁中切換、刷新與跨頁保存符合現有 `wl-lang` 行為；文件 lang、標題同步；英文履歷不誤標為中文內容 |
| 響應式 | 首頁與三篇案例各跑英文／中文，履歷英文；320、390、768、1440px 下無整頁水平溢位、文字遮擋或不可操作按鈕；表格可局部橫捲但不得隱藏資料 |
| 手機入口 | 390×844 首頁保留可見主要 CTA；首個案例入口位置不劣於基準。若新增入口造成惡化，先調整卡片密度，不靠刪除必要證據解決 |
| 鍵盤與閱讀 | Tab 焦點可見、順序合理、無陷阱；語言按鈕與折疊可鍵盤操作；新頁面有單一 h1 與合理標題層級；200% zoom 可閱讀 |
| Runtime | 無未處理 pageerror；新頁面不發起外部資源請求；JavaScript 停用時仍能讀取英文主要內容與來源連結 |
| 視覺證據 | 保存桌面與手機的代表畫面並實際檢視，包含長表格、頁尾與雙語；不能只用 screenshot 檔案存在代替檢查 |

不宣稱真人招募轉換率提高、真手機驗證、screen reader 驗證或 WCAG 全面合規；這些沒有對應實測。瀏覽器 viewport 模擬與真人測試分開記錄。

## 5. 驗證命令與紀錄

在 `D:/Codex/Web3` 執行。以下建置器與新測試為本計畫預定新增，核准前不執行不存在的檔案。

```bash
# 實作前的既有基準
py -3 -m pytest tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py -q

# 實作後的產物與完整相關回歸
py -3 scripts/build_portfolio_pages.py
py -3 scripts/build_portfolio_pages.py --check
py -3 -m pytest tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py tests/test_portfolio_pages.py -q

# 僅檢查本次變動，不混入既有 Dashboard 差異
git diff --check -- index.html BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md PUBLIC_QA_PRODUCT_QUALITY_RESUME.md tests/test_static.py tests/test_runtime.py
```

正常命令期望 exit 0；刻意錯誤輸入由測試斷言非零。新檔另檢查 UTF-8、語法與產物一致性，不能因 `git diff --check` 不涵蓋未追蹤檔便省略。

Playwright 瀏覽器或 Python 套件若不可用，記錄缺少項目及影響；不把環境失敗列為功能 PASS，也不自動安裝。記錄實際執行命令、版本、exit code、通過／失敗數、截圖與人工目視結果於本次證據目錄。測試更新不得刪除品質斷言以製造 PASS。

## 6. 回復與完成交付

- 實作前保存範圍內原檔與雜湊。若需回復，只比對並還原本次造成的片段，保留其他 session／使用者修改；不使用 reset、checkout 或全目錄覆寫。
- 新增檔案需移除時，先確認檔案仍是本次產物且沒有後續修改；沒有必要不做清除。未發布的候選可以保留供審閱。
- 完成交付包含：實際修改清單、內容與來源一致性結果、整合測試結果、代表截圖、已知限制與本機預覽入口。
- 只有計畫核准才開始 A–E。Git 提交、push 與線上發布仍須另有明確授權；發布後才另驗 HTTP、來源／線上雜湊與實際入口，不能以本機 PASS 代替上線驗證。
