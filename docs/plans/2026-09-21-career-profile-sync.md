# LinkedIn、Cake 與投遞履歷同步執行計畫

日期：2026-09-21
狀態：計畫完成，尚未執行。使用者本輪要求寫計畫；不把本文件當作平台寫入或新一輪 Git 發布授權。

## 目標與做法

讓正式內容來源、QA／Technical Support 投遞履歷、LinkedIn、Cake 與主要求職平台使用一致的職涯事實；依受眾調整篇幅與順序，不把同一篇文案複製到所有平台。中文採自然台灣用語，英文具體簡潔，保留技術關鍵字。

沿用 Markdown 來源、既有 Python／ReportLab 履歷工具、現有平台帳號與欄位。順序為：

現況讀回 → 來源版本更新 → 兩份主履歷與平台草稿 → PDF驗收 → 核准欄位發布 → 儲存後讀回。

單一主執行者負責寫入及驗收；本計畫不啟用 subagent。Cake 上傳障礙獨立處理，不阻擋其他文案準備。若近期已有指定職缺，優先完成該職缺需要的履歷，不為同步低優先平台延誤投遞。

## 已知起點與限制

- Portfolio 最終推送紀錄為 `5c635361b616b1c9e530b431b4f0852fa370cbe1`；25項合併後測試通過是先前證據，Pages與線上頁面仍需新驗證。
- 原工作目錄 main 記錄停在 `3684475`，有其他 dirty 變更；不直接 pull、reset、stash、清理或覆寫。執行前重新核對。
- `PROFILE_CONTENT_SOURCE.md` 標頭是 Frozen v1.2，但內文說明該收據為歷史版本；新SEG／DLP成果已在私人事實資料及公開案例，尚未完整同步兩份主履歷。
- LinkedIn與web3.career最後保存的發布紀錄為9/1；Cake為9/7。本計畫不將歷史PASS視為目前平台狀態。
- Cake 9/7紀錄：線上履歷已改，附件當時仍為2024舊PDF，新檔上傳遇到Not allowed；需先讀回，不能假設目前仍故障。
- Cake舊build.py有固定日期、固定輸出與額外文字替換，包含SEG全名替換。不得直接重跑並覆寫舊產物，也不得沿用未重新核對的縮寫展開。

## 範圍與檔案責任

| 類別 | 負責檔案／欄位 | 處理方式 |
|---|---|---|
| 事實與版本 | PROFILE_CONTENT_SOURCE.md、CLAIM_VERIFICATION_SHEET.md、STAR_STORY_BANK.md、BILINGUAL_MASTER_RESUME.md | 先讀取比對；新成果已有則引用，不重複建立。必要時修訂正式來源及雙語母稿，保留舊版本收據 |
| 兩份主履歷 | WEB3_QA_PRODUCT_QUALITY_RESUME.md、WEB3_TECHNICAL_SUPPORT_RESUME.md | 只更新Application Resume及必要來源註記；私人附錄不得出現在輸出 |
| 平台草稿 | LINKEDIN_PROFILE_UPDATE_PACK.md、JOB_PLATFORM_PROFILE_DRAFTS.md | 更新可貼上的精確文案與變更欄位；舊發布紀錄保留日期，不改寫成新PASS |
| Cake新產物 | application-packets/2026-09-21-profile-sync/ | 存放profile-change-set.md、QA／Support來源快照、build.py、新PDF、驗證紀錄與截圖；如執行跨日，以實際開始日建立新批次 |
| 完成狀態 | PLATFORM_PROFILE_MATRIX.md；本批次verification.md | 區分draft、saved、read-back verified、blocked；不另建求職tracker |
| 後續同步 | PROJECT_MEMORY.md、AI-一人公司/HUB.md | 只在完成後記必要現況；保持本次授權範圍。HUB縮整若仍被拒絕則列缺口，不反覆整檔覆寫 |

禁止順便修改：AGENTS.md、全域設定、瀏覽器權限、薪資／語言程度／隱私設定、正式職稱日期、其他專案、test-status產生檔及無關dirty內容。不改投遞狀態、不新投遞、不寄訊息、不重送人才庫表單。

## 階段1：唯讀盤點與來源核對

責任：主執行者；只產生本批次盤點紀錄。

1. 在D:/Codex/Web3執行並記錄：
   - `git branch --show-current`
   - `git status --short`
   - `git diff --name-only`
   - `git ls-remote origin refs/heads/main`
2. 讀取當下有效AGENTS.md、PROJECT_MEMORY.md、MASTER_CAREER_TIMELINE.md，以及上述事實來源。ignored檔照樣讀回，不以Git未列出判定不存在。
3. 使用當下可用的官方瀏覽器操作能力，唯讀查看LinkedIn About／Experience／Featured；Cake個人檔案／公開線上履歷／精選附件。記錄實際文字、連結、附件名稱、公開或登入狀態及時間。
4. 新DLP頁、首頁與公開履歷連結需確認能開啟、內容符合本批次版本；部署未驗證前，不把新DLP URL寫成已可供招聘者使用。
5. 若有平台語言分頁，確認實際存在的版本再處理，不推定已有中文LinkedIn頁面。

驗收：每個目標欄位有「目前內容／目標變更／證據來源／可見性／驗證時間」。登入或讀取受阻只標Blocked；可繼續本地草稿，不猜平台現況。

停止條件：職稱、日期、數據或個人／團隊歸屬出現實質衝突時，停止該主張的下游使用；其餘獨立工作可繼續。

## 階段2：正式成果來源更新

責任：主執行者；PROFILE_CONTENT_SOURCE.md為下游文案入口，claim sheet保存事實判定。

1. 建立三項新成果的中英短句與長句：Chrome監測、支援網站清單、DLP診斷指南。沿用已確認故事，不增列未證實數據。
2. 明確註記來源為使用者直接參與／回憶、主管分享數據或回憶中的QA報告，不冒稱已看過原始公司報表。
3. 保留v1.2歷史收據；建立下一個未使用的版本號、修訂日期及來源對照。全項檢查完成前標為草稿，不先宣稱Frozen／PASS。
4. 區分「舊而未支持的20%主張」與「新確認的20個百分點」，不能用整批刪除所有百分比的舊規則處理。
5. 更新母稿中對應段落；未受影響的職稱、日期、學歷、工作型態及個人資料不變。

必保條件：
- DLP指南：上線首月、因資料不足被SEG退回L2的案件比例、下降20個百分點、主管分享；非相對20%、處理時間或WFBS數據。
- 效能：CPU與記憶體各相對降低至少10%；單獨切換網站清單設計、QA比較、未列網站明確不支援。本人提案，團隊實作。
- Chrome：本人撰寫Python監測Beta／Stable；更新、上傳測試、失敗通知流程；沒有工時或提早攔截數的量化主張。
- ASML：6位工程師、多數程式由團隊完成、既有架構、例外需人工；BTSE未結案問題不改寫成已修復或避免財損。

驗收：逐項對照來源，短版也保留會改變主張意義的條件。正式技能清單仍保留已確認工具，不因潤稿刪掉必要專業資訊。

## 階段3：兩份主履歷與平台文案

1. QA／Product Quality版：BTSE金融邏輯與Chrome主動驗證優先；依篇幅安排效能設計與ASML自動化。
2. Technical Support版：SEG診斷、案件分派、指南與20個百分點優先；補充Chrome主動驗證及跨團隊合作。
3. QA Lead職缺使用既有事實重排ASML規劃、分工、程式審查與驗收；不把正式職稱改成未擔任的管理職。
4. LinkedIn：Headline原則保留Senior QA主定位；About用短段落呈現價值，Experience放具體行動與成果；Featured依已驗證可用連結更新介紹，不無故刪掉舊項目。
5. Cake：分別列出個人檔案、線上履歷、PDF附件的變更，沿用已採用的版面；中文完整書寫，產品和工具名稱保留。
6. web3.career：Bio濃縮代表成果，Experience同步；保留其他欄位與設定。
7. Talent Collective：先確認既有資料能否編輯。無明確更新方式則維持原提交，列待辦，不重新送表單。
8. Sumsub等特定公司履歷只在近期要使用時另對照當下JD；不把QA版直接當L3 Support版。

驗收：profile-change-set.md逐欄提供舊文、新文、使用語言、字元數、事實來源。限制以當下編輯器為準，不把9/1的字元上限當新驗證。履歷不得帶入私人附錄或不必要個人資料；不把12+年QA經驗寫成12+年Web3。

## 階段4：產生與驗收PDF

1. 先讀取已安裝的適用PDF／履歷skill及既有產生器；重用scripts/generate_ats_pdfs.py的build_pdf能力，以本批次獨立build.py輸出新檔。不直接執行會批次覆寫舊檔的入口。
2. 新build.py只讀本批次來源快照，分別輸出QA與Technical Support版本；不植入舊Sumsub、SailPoint或其他公司限定內容。
3. 檢查舊Cake版的肖像、聯絡欄及版面需要；網站版與ATS附件可有不同排版，但事實一致。英文主履歷不強塞雙語成一份附件。
4. PDF逐頁渲染及目視檢查：無裁切、重疊、孤立標題或空白頁；文字可擷取，閱讀順序、連結及數據正確。兩頁為目標，不以過小字體硬壓。
5. 核對scripts/validate_application_packets.py的PACKETS與新檔是否匹配；它使用固定清單，不宣稱可直接驗證任意新PDF。適用時以`--output-dir`指向本批次；不適用則使用PDF解析與視覺驗收，不為了綠燈修改歷史測試期待。

執行時命令：`py -3 -X utf8 application-packets/2026-09-21-profile-sync/build.py`；預期exit 0，來源快照與兩份PDF存在且非空。build.py須先在本階段建立並檢視，現在尚不存在。驗證紀錄需保存實際命令、exit code、頁數、截圖及SHA-256，不提前填PASS。

## 階段5：具體變更核准與平台同步

發布前交付：逐欄替換表、兩份PDF、來源限制與尚未解決事項。核對使用者屆時授權；已明確批准的同一批欄位不重問。本輪寫計畫與先前Portfolio commit/push不等於任意平台存檔、上傳或再次提交申請的授權。

在相應外部動作獲授權後：
1. 若Cake仍展示舊附件，優先上傳已驗收的新QA PDF並替換精選選擇；不先刪除舊檔。若上傳受阻，記錄精確錯誤，停止該步，不自行變更瀏覽器權限；繼續其他已授權欄位。
2. 更新LinkedIn About、Trend Micro／ASML相關Experience及必要Featured介紹；保存後立即讀回。保留既有隱私與通知偏好。
3. 更新Cake個人檔案與線上履歷；分別核對，不能用其中一項成功代替其他項。
4. 更新web3.career的核准欄位；人才庫僅走既有資料更新途徑。

驗收：登入狀態確認已存檔；可公開內容再從未登入狀態核對。重新開啟或下載精選PDF，確認是本批次內容，不只看檔名或上傳成功提示。平台重新壓縮PDF造成hash不同時，比對頁數、文字及畫面，不直接判失敗。

## 階段6：收尾與交接

- PLATFORM_PROFILE_MATRIX.md按實際結果更新URL、日期、版本與狀態；區分草稿完成、已存檔、公開讀回、上傳受阻。
- 完成報告列出已改欄位、未改欄位、附件狀態、可用連結及驗證限制；不把平台文案改好等同ATS一定可解析、能被搜尋或能提高回覆率。
- 將已確認版本與後續事項同步PROJECT_MEMORY.md；HUB僅縮整Web3四欄至600字內，不覆寫其他主線。
- 不把過往投遞改成重新投遞；不因本輪產物變更職缺tracker的submitted／closed狀態。
- 不自動commit／push。來源與附件含私人資料，發布前依當次明確授權逐檔確認。

## 回復策略與停止條件

- 編輯前保存允許範圍內的原文、檔案hash及畫面；舊履歷與驗證紀錄保留。
- 本地變更以精確差異回復，不用git reset或覆蓋整個工作樹。
- 外部誤存時只恢復本批次改過的欄位與原附件選擇；碰到其他人同時修改先停止，不覆蓋。
- 權限不足、無登入、附件能力受阻：交付可貼文案／可用PDF及具體缺口；不繞過平台限制。
- 任何新數據、職稱或敏感公開範圍無法確定，停止相關欄位，保留其餘可獨立完成工作。

## 本輪完成定義

本輪只交付此執行計畫並核對可用來源／工具；後續實作依上述階段進行。第一個安全動作是唯讀讀回LinkedIn與Cake目前內容，並建立本批次變更對照，不是直接改平台。
