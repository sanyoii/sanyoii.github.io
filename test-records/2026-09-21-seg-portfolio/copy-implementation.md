# 中英文潤稿完成紀錄

日期：2026-09-21。依 bilingual-copy-review.md 的建議修訂七份公開內容；本機版本，未 commit、push 或發布。

## 修改

- index.html：保留已採用的首頁主張；移除單一檔案宣傳，收斂 JobSmith 的保證及 hd-decode 的概括；修正 Low-tech／低維護、PASS 時間落差與台灣用語。
- dlp-case.html：統一第一人稱、改善自然度、將轉交案件與軟體升級區分，保留支援範圍與數據來源。
- 404.html：簡化中英文錯誤說明。
- 三份完整案例：逐段改寫中文，保留工具、模組名稱、職責、日期、結果與限制；英文刪減套語及重複說明。
- PUBLIC_QA_PRODUCT_QUALITY_RESUME.md：簡化冗長名詞、具體描述工作、保留來源限制；仍為英文履歷。
- 公開文件移除 Day／Frozen 等編輯狀態；舊內容及歷史發布註記完整保存在 before-copy-edit/，不代表本次已發布。
- tests/test_static.py：兩處固定發布日期斷言改為來源限制檢查；原連結與隱私檢查保留。
- HUB 僅更新 Web3 狀態欄。

## 事實核對

DLP 首月退回比例下降20個百分點及主管來源保留；CPU／記憶體各相對降低至少10%、單獨切換設計、未列網站不支援及原報告無法核實保留。ASML 6位工程師、20–30位訓練參與者、2–3位已知獨立使用者、人工例外與人事決策分工保留。BTSE問題未結案、無已修復或避免財損證據保留。

## 最新驗證

- `py -3 -m pytest tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py -q -p no:cacheprovider`：exit 0，**25 passed in 13.61s**。
- `py -3 -X utf8 test-records/2026-09-21-seg-portfolio/check-copy.py`：exit 0。首頁與DLP頁 × 中英文 × 390／1440px共八種畫面無橫向溢出，切換文字與語言屬性一致，HTML英文預設內容一致。
- `git diff --check -- index.html 404.html tests/test_static.py`：exit 0。
- 截圖為 `copy-*.png`；曾檢視桌機英文與手機中文合成預覽。最後JobSmith一句及履歷training用詞微調後，八張截圖與文字檢查已重新產生。
- 最終檔案 SHA-256：copy-final-sha256.txt。

初測因固定舊發布日期的斷言出現1 failed／24 passed，更新相應檢查後全數通過。Python requests 版本相容性警告與Git LF／CRLF提示仍存在，未造成測試失敗。

## 限制

文案自然度是編輯判斷，不是AI來源偵測結論。未進行真人閱讀測試、screen reader、真手機或線上部署驗證。私人求職來源、其他履歷變體、連出專案與test-status產生檔未修改；既有dirty worktree保留。
