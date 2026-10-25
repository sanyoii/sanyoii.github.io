# 履歷與求職資料修正補強計畫及檢查表

日期：2026-09-21
狀態：計畫與檢查表完成；尚未執行本輪修正。

## 目標、做法與完成定義

依本次交叉審查逐項修正正式來源、雙語母稿、QA／Technical Support 履歷、平台替換稿與 PDF，消除分類混雜、雙語落差、來源歸屬不清及局部更新造成的版本差異。

沿用 Markdown 正式來源、現有 Python／ReportLab build.py、pypdf／PyMuPDF 驗證工具，以及使用者指定的 Sumsub L3 黑白版型。內容先完成，再生成 PDF；不新增套件或更換整套產生方式。主執行者為唯一寫入者與驗收負責人，不啟用 subagent。

本輪完成必須同時符合：修正矩陣 R01–R09 全數有結果；保護條件 G01–G08 通過；完成第一次逐項驗收及第二次成品反向檢查；每項結果附本輪檔案位置或檢查證據。舊 PASS 不算新證據，Blocked／未驗證不算完成。

平台實際發布仍屬原六階段計畫的第 5 階段。本計畫完成的是可供同步的一致版本，不以本機稿完成冒稱已上線。

## 範圍與責任

修改範圍：

- PROFILE_CONTENT_SOURCE.md：正式中英文內容及技能來源。
- BILINGUAL_MASTER_RESUME.md：中英文母稿。
- WEB3_QA_PRODUCT_QUALITY_RESUME.md、WEB3_TECHNICAL_SUPPORT_RESUME.md：Application Resume 與必要版本註記；保留私人附錄。
- LINKEDIN_PROFILE_UPDATE_PACK.md、JOB_PLATFORM_PROFILE_DRAFTS.md：當前替換稿；歷史發布收據保留。
- application-packets/2026-09-21-profile-sync/：profile-change-set.md、qa-source.md、support-source.md、build.py、verify.py、兩份 PDF、逐頁圖、驗收紀錄及雜湊。
- PLATFORM_PROFILE_MATRIX.md、PROJECT_MEMORY.md：完成後只同步本批次狀態。
- 新增本批次 correction-review.md，作為本計畫 R／G 項目的唯一執行驗收表；不另建求職 tracker。

僅作證據讀取：CLAIM_VERIFICATION_SHEET.md、STAR_STORY_BANK.md、MASTER_CAREER_TIMELINE.md、相關公開案例、使用者提供的兩份 DOCX／XLSX 與 Sumsub PDF 參考。若发现實質事實衝突，停止該主張，不自行改寫證據。

禁止修改：原始 Office 文件、已投遞歷史 PDF、公開網站與公開履歷、AGENTS.md、全域記憶／設定、無關 dirty 內容、test-status、平台薪資／隱私／通知／語言程度、正式職稱與日期。此計畫不包含 Git stage／commit／push、刪檔、投遞、聯絡或人才庫重送。

## 審查發現 → 修正 → 驗收矩陣

| ID / 優先序 | 發現與精確修改範圍 | 修正要求 | 完成證據與判定 |
|---|---|---|---|
| R01 / P1 | 雙語母稿 English CORE SKILLS 與中文核心技能不同步；正式來源與 QA 新技能需一致 | 建立同一份已確認技能對照；補齐 Load、Stress、Compatibility、資安產品功能驗證、RAT／FAST／TOFT 的來源註記及設計／審查／Beta 責任。中英文語意相同，不要求逐字翻譯；角色短稿可選材 | 列出中英對照及母稿位置，逐項核對；不能只搜到單字就判定正確 |
| R02 / P1 | 平台替換稿缺最新 Skills 與 Trend Micro QA Engineer 2010–2013 更新項目 | 在三平台相關草稿及 profile-change-set.md 增加技能候選／對應欄位與 WFBS 經歷新文；中文 Cake 與英文版本對齊。若無獨立技能欄，指定可承載內容的既有段落，不假設平台具備欄位 | 每項有平台、欄位、舊存稿或 Unknown、新文、語言、字元數、來源；區分「草稿已備妥」與「欄位存在性未讀回」 |
| R03 / P1 | DLP 英文效能敘述及自訂網站支援流程不如中文精確 | 各來源／QA履歷／平台稿中，明確說是當時 QA 效能測試結果、單獨網站清單設計比較、CPU 與記憶體各相對至少降低 10%。自訂加入失效後經 Support 回報，由團隊評估是否支援；保留未列網站不支援及本人提案／團隊實作 | 全部使用此數據的位置逐段核對；私人來源保留使用者回憶、原始報告不在手，對外不暗示已獨立核實 |
| R04 / P2 | QA 技能表的 Test Planning & Design 混入 RAT／FAST／TOFT；Performance & Security 混合不同分類 | 規劃列只保留風險、規格／案例／資料設計與審查；驗收及功能測試承接 RAT／FAST／TOFT；效能列保留 Performance／Load／Stress；資安產品功能驗證放入適切的功能範圍或 Trend 經歷。不要為列齊而過度增加列數 | 每個項目可說明所在分類；無 UAT、滲透測試、Soak／Scalability 或其他未證實延伸；實際 PDF 表格可讀 |
| R05 / P2 | Support 摘要偏職責、獎項與工具，新價值不突出 | 改為簡潔呈現複雜問題診斷、案件資料完整度與工程交接改善；獎項留在經歷。20 個百分點完整口徑留在 DLP 經歷，不壓成無上下文數字 | 摘要與經歷有分工；不寫成 12+ 年 Web3／L3、不保證數據成果可泛化；與 QA 摘要明確區分 |
| R06 / P2 | 中文母稿與 Cake 稿中英混寫、無人值守、升級處理等用語不夠自然 | 普通敘述改為台灣用語；如「正常流程不需人工介入」「根因分析」「客戶問題診斷」「提報並轉交處理」。工具、產品、API／SDK 等必要名稱保留英文；逐句依語境處理，不全檔機械替換 | 讀完整段落檢查自然度與中英意義；同一成果無責任、數據、語氣強度差異 |
| R07 / P2 | Trend Micro 經歷把自動化、診斷工具、環境堆在同一條；與技能區重複 | 技能表保留檢索用途；經歷將工具放回其實際工作情境。刪除無額外資訊的重複列舉，但保留重要已確認工具在至少一個合適位置 | 修正前後工具對照；Python／Selenium／Robot Framework／TMSTAF／Jenkins／GitHub 與診斷工具等不被誤刪、誤歸公司或新增熟練度 |
| R08 / P2 | 粗體依固定字串套用，QA／Support 同義內容強調不一致；缺件字樣被孤立加粗 | 以來源中的明確重點標記或單一可審核的呈現規則設定強調，避免偶然命中字串。兩份皆突出相同層級的角色、行動與成果；數字連同指標，正文維持正常字重 | PDF span 確認分類／關鍵片段用 Bold，正文用 Regular；四頁目視確認強調不零碎、不整段全粗、不丟來源條件。移除不再使用的舊字串替換規則 |
| R09 / P2 | Jira 被放進診斷；上一則把 Jira／Confluence／Bitbucket／GitHub 混為一列的建議也需修正 | Quality Leadership／Delivery 與 Diagnostics 分開。Jira／Confluence 表達追蹤與協作，Bitbucket／GitHub 表達版本控制與程式碼協作；優先回到有據的工作情境，不為四個工具硬增一列。QA、Support、母稿皆核對 | 無把工具當領導能力／診斷能力的分類；Jenkins／GitHub 屬 Trend、Bamboo／Bitbucket 屬 ASML 的既有歸屬保持正確 |

## 必須保留的事實與範圍檢查表

- [ ] G01：20 個百分點＝DLP 指南首月、SEG 因缺件退回 L2 的案件比例、主管分享；不得改成相對20%、bug rate、時間或CSAT。
- [ ] G02：CPU／記憶體各至少10%相對降幅；單項網站清單設計比較、QA測試來源、未支援網站與團隊實作的限制完整。
- [ ] G03：ASML 帶領6位工程師；既有架構、多數程式由團隊完成、正常流程與人工例外仍清楚；不新增成本／覆蓋率成果。
- [ ] G04：職稱、日期、學歷、聯絡資料及私人附錄不變；家庭照護不新增私密細節。DLP／WFBS最新人數定案不被舊資料覆蓋。
- [ ] G05：BTSE 只稱找到並提報3個高嚴重度缺陷；不聲稱已修復、避免財損或公開內部細節。
- [ ] G06：不把ML、BDD、FET、Volume、UAT、滲透測試等來源線索直接升格為已驗證專長；RAT／FAST／TOFT文章只解釋術語。
- [ ] G07：Google Chrome監測Python為本人撰寫；不推論所有工作流程元件由本人獨立開發，不新增攔截率／工時／事故數。
- [ ] G08：來源與發布狀態分離；本機完成不等於外部已存檔、ATS已驗證或招募成效提升；原有dirty內容、歷史檔與外部設定保持不動。

## 執行順序與驗收

### T1 — 唯讀基線與備份

1. 讀回本計畫矩陣對應檔案、當下有效 instructions；重查 branch、status、相關差異。讀取 ignored 來源。
2. 在本批次新建 before-consistency-correction/，只備份本輪要改的檔案、build／verify、兩份 PDF，記錄 SHA-256。已存在則建立新時間戳子目錄，不覆寫。
3. 在 correction-review.md 建立 R01–R09、G01–G08 執行列，初始均為 Pending，含「修改位置／第一次驗收／第二次驗收／證據／未解事項」欄位。
4. 原始DOCX／XLSX以已留存雜湊確認是否改變；變更時重讀相關資料，不沿用舊解讀。

基線命令（Git Bash，cwd=D:/Codex/Web3）：

```bash
git branch --show-current
git status --short
git diff --name-only
```

预期 exit 0，記錄真實結果；不 pull／reset／stash。備份讀回與雜湊一致後才能修改。

### T2 — 正式來源與雙語母稿

依 R01、R03、R06、R07、R09 修正 PROFILE_CONTENT_SOURCE.md 與 BILINGUAL_MASTER_RESUME.md。先核對下一個未使用版本，再更新版本／日期，保留舊收據，驗收前標 Draft。

先完成中英對照與來源／責任確認，再讓下游縮寫；不以複製同一長段落作為同步。遇到實質衝突只停止相關主張，其餘獨立工作繼續。

### T3 — 兩份履歷及平台稿

1. QA：依 R04、R07、R09 重整技能分類，維持產品品質／測試設計／實作證據。
2. Support：依 R05 改摘要；依 R07、R09 整理工具與交接描述；不硬塞完整 QA 類別。
3. 依 R02、R03、R06 同步 LinkedIn、Cake、web3.career 適用段落及精確替換表。Skills候選清單與實際平台欄位對應分開；未讀回者標 Unknown。
4. 角色PDF来源快照只從 Application Resume 擷取，排除私人附錄。

驗收：檔案逐段對照 R01–R07／R09；完整主張可追到正式來源。每個新平台段落都有確切文案及本地字元數。標示「草稿可供線上比對」，不標「已可無條件直接發布」。

### T4 — 字重、PDF與驗證程式

1. 實作 R08，沿用黑白Letter版型與現有閱讀尺寸。來源若加入強調標記，匯出與驗證必須正確解析，PDF不得殘留Markdown符號；平台純文字稿不得帶入不支援標記。
2. verify.py 既有snapshot／職稱／日期／附錄／數據檢查繼續保留；增加實際字重與必要技能存在性检查。只為合理的呈現標記正規化，不放寬事實斷言取得綠燈。
3. 重新產生兩份PDF及逐頁圖，保存全新文字與連結檢查、頁數及hash；先去除重複文字調整篇幅，不以縮小字體強壓兩頁。

```bash
py -3 -X utf8 application-packets/2026-09-21-profile-sync/build.py
py -3 -X utf8 application-packets/2026-09-21-profile-sync/verify.py
git diff --check
```

預期皆 exit 0；两份PDF目標各2頁。git diff --check無法涵蓋ignored內容，必須另看備份差異与讀回。PDF逐頁以PyMuPDF渲染後直接目視，確認表格、字重、連結、分頁、標題與正文；文字檢查不代替視覺驗收。不使用固定PACKETS舊驗證器冒充本批次驗收。

### T5 — 第一次逐項驗收

主執行者依 R01–R09、G01–G08 順序打開實際來源與成品。每列只有四種結果：Pass／Fail／Blocked／Not applicable；N/A須說明原因且不得用來略過原始修正項。附對應位置、命令exit、當輪產物或檢視紀錄。任何Fail必須修正後重驗受影響項目。

### T6 — 第二次 double check（成品反向核對）

重新從最終成品出發，不只重看編輯差異或第一次打勾結果：

1. QA PDF → qa-source → QA Markdown → 正式來源：核對分類、數據、責任及實際粗體。
2. Support PDF → support-source → Support Markdown：核對角色定位、摘要／經歷分工及相同成果的強調一致性。
3. 英文母稿 ↔ 中文母稿：逐項核對技能與對應成果，防止只更新其中一語。
4. 各平台替換表 → 平台原稿 → 正式來源：核對2010–2013經歷、技能候選、效能敘述與台灣中文用語均已覆蓋。
5. 原始審查矩陣 → 全部成品：逐列回答「修在哪裡、怎麼證明、還缺什麼」。不得只給「全部完成」一句。
6. 第二輪若有修改，重跑受影響驗證、重產圖片及hash；不得引用修改前PASS。最終才將當前版本標為本機驗收完成。

此為主執行者的第二輪檢查，不冒稱獨立第三方審查。最終回報必須列出R01–R09的結果，以及任何未完成的G項／外部驗證缺口。

### T7 — 狀態與交接

更新本批次 verification.md、PLATFORM_PROFILE_MATRIX.md、PROJECT_MEMORY.md，指向 correction-review.md 與最終來源／PDF。清楚保留：外部平台尚未讀回／發布、既有HUB同步受阻等未解事項，不擅自變更其他工作狀態。本輪不修改AI公司HUB或外部平台；原六階段計畫後續續接時依既有授權及當下能力處理。

## 回復、授權與停止條件

- 本輪只寫計畫；計畫核准後執行上列本機修正。已核准原平台同步的欄位不需重複取得同一授權，但本計畫新增的線上修改項目要先交付具體差異並核對授權範圍，不自行擴大。
- 不依賴未來瀏覽器可用來完成本機工作。瀏覽器不可用時交付可讀回比對的草稿，外部狀態維持Blocked。
- 回復以before-consistency-correction中的單檔／精確段落為依據；先確認沒有使用者同時修改，不整個worktree還原。歷史PDF與原始材料保留。
- 數據、職稱、個人／團隊責任出現衝突，停止相關主張；不能用縮寫掩蓋衝突。
- 工具失敗記錄精確錯誤；有安全替代方案則使用，無法驗證則標Blocked，不沿用舊PASS。沒有新增安裝、權限修改或Git發布的授權。

## 計畫本身的覆蓋核對（不是實作完成表）

- [x] 六項主要審查發現：R01–R06。
- [x] 工具／成果重複及粗體一致性：R07–R08。
- [x] Jira問題及上一輪混合工具分類的修正：R09。
- [x] 數據、ownership、職涯事實與未證實專長限制：G01–G08。
- [x] 修改位置、來源、驗收方法、回復與外部邊界明列。
- [x] 完成後逐項查核及第二次反向double check：T5–T6。
- [x] 現有dirty worktree保留；不以計畫寫入冒稱已修完履歷。

執行結果尚未填寫。開始執行時建立 correction-review.md，不將上述計畫覆蓋勾選複製成實作PASS。
