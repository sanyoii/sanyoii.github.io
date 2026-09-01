# BTSE CEX Product Quality Case Study

> Status: `Day 17 Complete v1 / Public 2026-09-01`
> Period: Sep 2024–Nov 2024
> Role: Senior QA Engineer, Nogle／BTSE
> Evidence: `User-attested / confidential internal sources inaccessible / not independently document-verifiable`
> Public boundary: This file uses sanitized product-flow categories. It omits internal thresholds, account structures, transaction data, response bodies, identifiers, and implementation details.
> Public navigation: [Portfolio](https://sanyoii.github.io/) | [Public QA resume](https://github.com/sanyoii/sanyoii.github.io/blob/main/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md)

## English

### The product-quality problem

A centralized crypto exchange moves value through connected Wallet, trading, commission, and conversion flows. A defect can start in one screen and affect a balance, order, fee, or payout somewhere else. I tested those connections at BTSE across Wallet, Referral and Affiliate, Spot, Futures, Convert, fees, funding, liquidation, and KYC.

During my three-month role, I found three significant logic issues in trading, referral commission, and conversion flows that could affect amount calculations, and escalated them to the relevant teams for priority handling. The original reports stayed in BTSE's internal systems. I did not retain proprietary copies after leaving the company.

### How I tested the flows

I started with product behavior, then checked the data path behind it.

- I mapped the user flow and tested normal values before moving to boundary and negative cases.
- I compared behavior across assets, browsers, entry points, and connected product flows.
- I used Browser DevTools for E2E Web API and WebSocket inspection.
- I used TestRail for Wallet, Referral and Affiliate, and Convert cases.
- I used SQL through TablePlus to validate Wallet balances, collateral details, fund transfers, order and trade history, fees, and settlement data.
- I built spreadsheet calculations to compare expected and observed results. For fees, funding, and liquidation, I used BTSE's published formulas. For commissions, I confirmed the expected allocation with my QA mentor.

I kept Browser network and API inspection separate from log analysis. I did not perform direct server-log analysis at BTSE.

### Three risk findings

| Product flow | Failure signal | Validation approach | Product-quality risk | Recorded outcome |
|---|---|---|---|---|
| Futures and Spot | Boundary inputs produced inconsistent pricing or left the UI without a usable result | Reproduced with normal controls, multiple assets, three browsers, and API-response inspection | A shared boundary-handling weakness could affect more than one trading surface | QA and Engineering accepted the issue; it remained open while the team focused on release work |
| Referral and Affiliate | Commission values exceeded the expected allocation under a deeper, active account hierarchy | Built a multi-account model, generated trades, collected admin results, and compared them with spreadsheet calculations | A low-frequency path could become material as affiliate activity grew | Management kept it behind release work; the issue remained open and the final TestRail review did not finish before my employment ended |
| Convert | Boundary inputs left the UI without a usable result across different entry points and asset pairs | Restarted the browser, tested three browsers, changed source and target assets, and inspected the Convert API response | A Convert failure could affect other product flows that depended on the same service | Engineering accepted the issue; it remained open, with no outage or fix evidence |

### Product-quality decisions

I assessed each finding by product risk and affected scope.

1. I checked scope before severity. A reproducible result across products, assets, or entry points carried more weight than one failed screen.
2. I used expected-versus-observed comparisons for financial logic. The comparison made commission, fee, funding, and liquidation errors reviewable.
3. I separated evidence from impact. I could show the defect and the affected flow. I had no evidence for an outage, a completed fix, or a prevented loss, so I did not claim them.
4. I documented the test model. The internal Wiki and TestRail records gave the team reproduction steps, coverage, and a starting point for future testing.

### Reusable test controls

The following controls describe the test approach I would carry into another CEX. They do not describe confirmed BTSE remediation.

- Define accepted boundaries for each input and return one usable error contract across UI and API layers.
- Test values on both sides of each boundary, then repeat them across assets and connected flows.
- Reconcile total commission allocation across hierarchy levels and activity patterns.
- Compare order, position, currency, fee, and settlement state before and after each transaction.
- Cover order states from pending or open through filled, canceled, rejected, and triggered outcomes.
- Keep KYC state testing separate from AML screening and compliance ownership.

### Evidence limits

- The three findings come from direct work and user-attested memory. Former-employer records are no longer accessible.
- The case study does not disclose exact thresholds, internal account topology, transaction values, customer data, identifiers, or response content.
- It does not claim a fix, production outage, avoided loss, or validated financial impact.
- BTSE work did not include Postman, Swagger, direct server-log analysis, AML screening, smart-contract testing, or chain-node operation.
- Current public BTSE formulas cannot prove which formula version was in use during Sep–Nov 2024.

## 繁體中文

### 產品品質問題

中心化加密貨幣交易所會把 Wallet、交易、佣金與兌換流程串在一起。一個畫面的錯誤，可能影響另一個流程的餘額、訂單、手續費或分潤。我在 BTSE 測試 Wallet、Referral／Affiliate、Spot、Futures、Convert、fee、funding、liquidation 與 KYC，也檢查這些流程之間的連動。

在三個月任職期間，我在交易、推薦佣金和兌換流程中，發現 3 個可能影響金額計算的重大邏輯問題，並提報給相關團隊優先處理。原始報告留在 BTSE 內部系統；離職後我沒有保留任何公司資料。

### 我怎麼測

我先確認產品行為，再檢查後面的資料路徑。

- 先畫出 user flow，以正常值建立對照，再測 boundary 與 negative cases。
- 跨資產、Browser、入口與相連產品流程比對結果。
- 使用 Browser DevTools 檢查 E2E Web API 與 WebSocket。
- 使用 TestRail 管理 Wallet、Referral／Affiliate 與 Convert cases。
- 透過 TablePlus 執行 SQL，驗證 Wallet 餘額、抵押品明細、資金劃轉、掛單與成交、手續費及結算資料。
- 使用 spreadsheet calculation 比對 expected／observed results。Fee、funding 與 liquidation 依 BTSE 當時公開公式計算；commission 的 expected allocation 則與 Senior QA Mentor 確認。

Browser network／API inspection 與 log analysis 是不同證據。在 BTSE 任職期間，我沒有直接查看或分析 server logs。

### 三個風險案例

| 產品流程 | 失敗訊號 | 驗證方式 | 產品品質風險 | 已知結果 |
|---|---|---|---|---|
| Futures／Spot | Boundary input 造成價格結果不一致，或 UI 沒有可用結果 | 用正常值對照，跨多種資產、三種 Browser 與 API response 重現 | 相同的 boundary-handling 弱點可能影響不只一個交易介面 | QA 與 Engineering 確認是 issue；團隊先處理 Weekly Release，issue 維持 open |
| Referral／Affiliate | 在較深且交易活躍的代理關係中，commission 超過 expected allocation | 建立多帳號測試模型、產生交易、取得後台結果，再用 spreadsheet 比對 | 低發生率情境可能隨 affiliate 活動增加而擴大 | Management 將它排在 release work 之後；issue 維持 open，employment 結束前未完成 final TestRail review |
| Convert | Boundary input 在不同入口與 asset pairs 中都讓 UI 沒有可用結果 | 重開 Browser、跨三種 Browser、更換來源／目標資產並檢查 Convert API response | Convert service 的失敗可能影響依賴它的其他產品流程 | Engineering 確認是 issue；issue 維持 open，沒有 outage 或 fix evidence |

### 品質判斷

我依產品風險與影響範圍判斷每個 finding 的價值。

1. 先確認影響範圍，再判斷 severity。能跨產品、資產或入口穩定重現的問題，比單一畫面失敗更值得追。
2. 金融邏輯用 expected／observed comparison。commission、fee、funding 與 liquidation 的差異才能被 review。
3. 把 evidence 與 impact 分開。我能證明 defect 與受影響流程；沒有 outage、fix 或 avoided loss 的證據，就不寫成成果。
4. 留下可重用的 test model。內部 Wiki 與 TestRail 記錄讓團隊取得 reproduce steps、coverage 與後續測試起點。

### 可重用的測試控制

以下是我會帶到其他 CEX 的測試方法，不代表 BTSE 已採用或完成 remediation。

- 為每個 input 定義可接受 boundary，讓 UI 與 API 回傳一致且可處理的 error contract。
- 測試 boundary 兩側的值，再跨資產與相連流程重跑。
- 在不同代理層級與活動條件下，核對 total commission allocation。
- 比對每筆交易前後的 order、position、currency、fee 與 settlement state。
- 覆蓋 pending／open、filled、canceled、rejected 與 triggered 等 order states。
- 把 KYC state testing 與 AML screening／compliance ownership 分開。

### 證據限制

- 三個 finding 來自本人直接參與及回憶確認；離職後已無法存取前雇主資料。
- 本文不揭露精確 thresholds、內部帳號結構、交易數值、客戶資料、識別碼或 response 內容。
- 本文不聲稱 issue 已修正、曾造成 production outage、避免損失或有已驗證的財務影響。
- BTSE 經驗不包含 Postman、Swagger、direct server-log analysis、AML screening、smart-contract testing 或 chain-node operation。
- 現行公開公式不能證明 Sep–Nov 2024 使用的 historical formula version。
