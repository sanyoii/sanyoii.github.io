# Portfolio 中英文文案檢視

日期：2026-09-21。目的：招聘讀者能讀懂貢獻與結果，英文自然，中文採台灣常用說法。AI 味是語氣判斷，無法據此判定作者或保證所有讀者觀感。

## 範圍與本次修改

完整檢視 index.html、dlp-case.html、404.html、PUBLIC_QA_PRODUCT_QUALITY_RESUME.md、BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md、ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md、TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md。包含 HTML 語言切換文字、預設文字與非切換文字。

公開履歷目前只有英文，不宣稱已檢查不存在的中文版本。本輪不含私人履歷變體、STAR／claim sheet、README、其他專案連結目的地、test-status 產生的 Dashboard，也不是整個 Web3 repo 的全文審閱。

依使用者已採用建議，僅修改首頁主張；以下其他項目是待採用的審閱建議，尚未整批改稿。

EN: I identify product risks early and turn technical findings into better product quality and more effective ways of working.

ZH: 我提早辨識產品風險，將技術分析轉化為產品品質與團隊工作方式的改善。

## 結論

英文主體清楚，但有抽象套語、過度保證及過多內部審核術語。中文首頁與新 DLP 頁較完整，三份長案例仍有大量一般英文詞嵌在中文句子裡，應逐段重寫。不能將目前全套文案評為已完成台灣中文潤稿。

## 第一優先：語意與主張

1. index.html JobSmith：`so it cannot quietly fabricate experience` 把 keyword limits 寫成防止捏造的保證；`ATS-safe PDFs` 也容易暗示適用所有 ATS。建議：`My contributions include PDF export, ATS compatibility checks, resume-parsing checks, and limits on inferred keywords. Generated content still needs review.`／「我加入 PDF 匯出、ATS 相容性檢查、履歷解析檢查與關鍵字推導上限；產生的內容仍需人工核對。」中文原句的「避免」與英文絕對保證強度不同。
2. index.html 頁尾：`Designed, written, tested, and shipped as one dependency-free file.` 已與多頁網站、圖片及獨立測試檔不符，中文「測試與發布都收在一個檔案」也不準確。建議刪除這句技術宣傳，保留姓名與聯絡連結即可。
3. index.html hd-decode：`Most personality readings ... you forget by the next day` 是無依據概括，中文還把 personality readings 換成命理解讀。`someone ... can still finish it` 也未有讀者驗證。改述設計：`A personal project that presents Human Design readings as a visual report, with plain-language explanations and expandable terminology.`／「這是我的人類圖報告專案，以視覺化版面呈現解讀，先用白話說明，再讓讀者展開查看術語。」
4. index.html `Low-tech` 不等於「低維護」，後者是成本主張。建議 `A dashboard for reviewing test results and evidence`／「集中查看測試結果與證據的儀表板」。
5. index.html PASS 段中文多出「幾天後」時間判斷。建議 `A passing result needs a tested version, a clear scope, and supporting evidence.`／「測試通過的結果，需要對應的版本、明確的測試範圍與佐證資料。」
6. 履歷與案例頂端 Day 17／18／19／20、Frozen、blocked metrics、user-attested 等是內部編輯語彙。保留期間、職責、一次清楚的來源說明；編輯進度和排除舊主張的理由留在私人紀錄。不要刪掉數據旁的重要口徑。

## 第二優先：自然語氣與台灣用語

| 現文 | 建議 | 理由 |
|---|---|---|
| My work sits at the intersection of… | My experience spans crypto exchange testing, security incident investigation, and test automation.／我的經驗涵蓋加密貨幣交易所測試、資安事件調查與測試自動化。 | 用工作內容取代抽象定位套語 |
| 無人值守測試 | 不需全程人工操作的測試 | 台灣招聘讀者較自然；案例內仍保留異常需人工處理 |
| 人員汰換率 | 人員流動率 | turnover 不必然指公司淘汰員工 |
| 成員負載 | 成員手上的工作量 | 人員分派用語較自然；CPU 負載仍可保留 |
| 資金劃轉 | 帳戶間資金移轉 | 若原產品 UI 固定用「劃轉」，引用 UI 時可保留 |
| 升級案件的進件品質 | 轉交 SEG 的案件資料完整度 | 避免與軟體升級混淆，也更接近實際指標 |
| 接入流程 | 串接至流程／納入流程 | 本文語境較自然 |
| 網站覆蓋 | 網站支援範圍／防護範圍 | 依原意選用，不能視作同義詞一律取代 |
| 向 Support 開 case | 向技術支援團隊回報 | 面向外部招聘讀者較直接 |
| 高量 incident | 大量客戶問題／大量事件處理 | 避免直譯，依實際工作範圍選詞 |

保留產品名、工具名與有辨識價值的術語：DLP、SEG、L2、API、SQL、WinDbg、TestComplete、Bamboo、Jira、HMI。一般字應改中文：engineer→工程師、review→檢查／審查、handoff→交接、blocker→阻礙、workflow→流程、test case→測試案例、source control→版本控制。產品模組名稱保留原名；不要把所有英文術語機械翻譯。

## 第三優先：文件語氣與結構

- ASML 中文最需要逐段改寫。例如首段可改為：「不同時區的 ASML 工程師共用 HMI eP5 測試環境。每次測試都要啟動模擬器、載入對應功能的 Recipe、執行操作，再清理環境。耗時較長的案例需要工程師持續操作；若環境未完整重置，也會影響下一位使用者。」Recipe 保留產品語境。
- BTSE 中文方法段可改為：「先畫出使用者操作流程，以正常輸入建立對照，再測試邊界值與異常輸入。使用試算表比對預期與實際結果。」產品名稱與測試範圍另保留，不縮成泛稱而失去專業資訊。
- Trend Micro 中文問題段可改為：「端點防護除了要有效阻擋威脅，也不能妨礙客戶工作。升級失敗、驅動程式衝突或原則未正確套用，在不同環境可能呈現不同症狀；我會先蒐集資料、重現問題，再判斷原因。」
- DLP `The performance result belongs to a narrower scanning scope` 搭配不自然。可改 `These resource savings came with a narrower default scanning scope.`／「降低資源消耗的同時，預設掃描範圍也縮小了。」
- DLP 第一人稱與 `recalled by the author` 混用。可統一為 `The figures are based on my recollection of the QA performance report; the original report is unavailable.`／「數據依我對當時 QA 效能報告的回憶整理，目前無法提供原始報告。」與原有「單獨切換設計」說明一起保留。
- 履歷 `issue-type-based DLP diagnostic-data collection guide` 名詞過密。改 `Proposed a DLP troubleshooting guide organized by issue type, with step-by-step instructions for collecting diagnostic data.`
- 履歷 `expanded high-impact feature coverage through broader Test Cases and scope` 過度抽象。可依既有 Trend Micro 案例具體寫 `Expanded scan, system, and performance tests using patterns from customer incidents.`
- TOI 對外可寫 training sessions and technical handover／操作訓練與技術交接，不猜縮寫全名。若保留，首次說明用途。
- `Attendance did not prove adoption` 的界線值得保留，但不必在每段重複。可在成果處寫：「約 20–30 人參加操作說明；其中可確認約 2–3 人曾獨立執行，並提出修改需求。」其餘使用情形仍列未知。
- `The case separates…`、`Read the decisions… together` 是描述文件如何編排，首頁可直接說自己的工作。個人與團隊貢獻在案例內交代一次即可。
- 404 的 `or it never was` 不自然，中文「也可能從來沒有這一頁」可刪。改 `The page may have moved, or the address may be incorrect.`／「頁面可能已移動，或網址輸入有誤。」

## 必須保留的事實界線

- DLP 補件退回比例下降 20 個百分點：指南上線首月、依主管分享數據；不是相對 20%、處理時間或 WFBS 指標。
- CPU／記憶體各相對降低至少 10%：只切換網站清單設計的 QA 比較；未列網站明確不支援，原報告未核實。
- Python 監測由本人撰寫；網站清單由本人提案、團隊採用實作。
- ASML 原架構由客戶提供，六位工程師完成多數程式，異常路徑仍需要人工。
- BTSE 的三個問題未有完成修復或避免財損證據，不能為了更有力而改成已解決。

## 本次驗證

`py -3 -m pytest tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py -q -p no:cacheprovider`：exit 0，25 passed in 14.13s。`git diff --check -- index.html`：exit 0，Git 提示 LF／CRLF 轉換警告。

測試確認首頁新文案未破壞既有版面與語言切換，不證明文案毫無 AI 味，也不是新一輪真人易讀性測試。未 commit、push 或發布。
