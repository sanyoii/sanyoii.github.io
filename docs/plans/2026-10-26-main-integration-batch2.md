# 第二批主線整合：公開職涯主張

2026-10-26。基準 `d8ea990af77bd1d7fffa8a47ea6ba4c1ec5b3a57`；選取 `633b87f62d086e7a685d8730737d0f04e3040106` 的事實修正，依本機 PROFILE_CONTENT_SOURCE.md §3／§13 的使用者確認資料核對。原始公司報告不可取得；不宣稱獨立證實成效。

## 完成內容

- BTSE 中英文案例與公開履歷：30–50 Referral/Affiliate TestRail、約 20 Convert internal Wiki；Wallet 明確為使用而非推定撰寫。三項缺陷離職時仍 open。
- 首頁短指標移除無法完整保留條件的 CPU/RAM 數字；20pp 保留首月、SEG 退回 L2、缺資料及主管數據限定。
- `scripts/build_portfolio_pages.py` 從 Markdown 重建閱讀頁；trend-support-case.html 僅更新產生器來源 fingerprint，正文未變。
- 公開 PDF 沿用既有核准 Style C。為可重產，保存 `scripts/templates/public-resume-print.html`，來源為公司保留 commit `2a4b871e83227c42db340b952310c769bcfddb8e` 的 `resume_material/06-rendered-resumes-html-pdf/William-Lu-General-QA-Resume-Scannable-2026-10-16-Style-C.html`。本檔不含電話連結；未匯入其餘私人履歷素材。`.gitignore` 僅明列兩個公開產生器及兩個公開 HTML 來源，其他 scripts 仍排除，避免必要來源在交接時漏提交。
- 重產：`py -3 -B -X utf8 scripts/build_public_resume_pdf.py`，使用已安裝 Playwright Chromium、等待 fonts、print media、A4；封鎖遠端 HTTP 資源，不安裝套件。

## 本輪驗證

- 新增 `tests/test_claim_boundaries.py`，修前 3 項均因舊敘述失敗，修後通過。
- `py -3 -B -X utf8 scripts/build_portfolio_pages.py --check`：4 頁通過。
- `py -3 -B -X utf8 -m pytest -p no:cacheprovider tests/test_static.py tests/test_portfolio_pages.py tests/test_runtime.py tests/test_claim_boundaries.py -q --tb=short`：70 passed。使用既有主機 Chromium 快取；只連本機 HTTP 測試伺服器。
- pypdf：2 頁、約 595 × 842 pt A4；BTSE 數量／Wiki／Wallet使用／open、SEG-to-L2、20pp 限定通過，無私人電話。pypdfium2 逐頁渲染目視無明顯截字或重疊。
- Python requests 發出既有 dependency warning，未造成測試失敗；未因此修改依賴。

## 後續邊界

原 preservation 分支、候選審稿與歷史測試收據保留。這是本機驗證與主線推送工作，沒有重驗線上部署、真人手機、screen reader、LinkedIn／Cake、職缺或投遞狀態。CEX 本批只讀，不從技術 Pass 推導發布核准。
