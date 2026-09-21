# BTSE CEX Product Quality Case Study

> Period: Sep 2024–Nov 2024
> Role: Senior QA Engineer, Nogle／BTSE
> Public navigation: [Portfolio](https://sanyoii.github.io/) | [Public QA resume](https://github.com/sanyoii/sanyoii.github.io/blob/main/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md)

> Source: Based on my direct work and recollection. Original employer records are no longer available for independent verification. Confidential details are omitted.

## English

### The product-quality problem

A centralized crypto exchange moves value through connected Wallet, trading, commission, and conversion flows. A defect can start in one screen and affect a balance, order, fee, or payout somewhere else. I tested those connections at BTSE across Wallet, Referral and Affiliate, Spot, Futures, Convert, fees, funding, liquidation, and KYC.

During my three months at BTSE, I found three significant logic issues in trading, referral commission, and conversion flows that could affect amount calculations, and escalated them to the relevant teams for priority handling. The original reports stayed in BTSE's internal systems. I did not retain proprietary copies after leaving the company.

### How I tested the flows

I started with product behavior, then checked the data path behind it.

- I mapped the user flow and tested normal values before moving to boundary and negative cases.
- I compared behavior across assets, browsers, entry points, and connected product flows.
- I used Browser DevTools for E2E Web API and WebSocket inspection.
- I used TestRail for Wallet, Referral and Affiliate, and Convert cases.
- I used SQL through TablePlus to validate Wallet balances, collateral details, fund transfers, order and trade history, fees, and settlement data.
- I built spreadsheet calculations to compare expected and observed results. For fees, funding, and liquidation, I used BTSE's published formulas. For commissions, I confirmed the expected allocation with my QA mentor.

These checks used browser network records and API data. I did not directly inspect server logs at BTSE.

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

- Define accepted boundaries for each input and provide consistent, actionable error responses across the UI and API.
- Test values on both sides of each boundary, then repeat them across assets and connected flows.
- Reconcile total commission allocation across hierarchy levels and activity patterns.
- Compare order, position, currency, fee, and settlement state before and after each transaction.
- Cover order states from pending or open through filled, canceled, rejected, and triggered outcomes.
- Keep KYC state testing separate from AML screening and compliance ownership.

### Evidence limits

- The three findings are based on my direct work and recollection. Original employer records are no longer accessible.
- The case study does not disclose exact thresholds, internal account topology, transaction values, customer data, identifiers, or response content.
- It does not claim a fix, production outage, avoided loss, or validated financial impact.
- BTSE work did not include Postman, Swagger, direct server-log analysis, AML screening, smart-contract testing, or chain-node operation.
- Current public BTSE formulas cannot prove which formula version was in use during Sep–Nov 2024.

## 繁體中文

### 我負責哪些測試

交易所的錢包、交易、佣金與兌換功能彼此相連。一個地方出錯，可能影響其他功能的餘額、訂單、手續費或佣金分配。我在 BTSE 負責 Wallet、Referral／Affiliate、Spot、Futures、Convert、手續費、資金費用、強制平倉與 KYC 測試，也會檢查這些功能之間的資料是否一致。

三個月任職期間，我在交易、推薦佣金與兌換流程找到 3 個可能影響金額計算的重大邏輯問題，並提報團隊優先處理。原始報告保存在 BTSE 內部系統；離職後，我沒有保留公司的專有資料。

### 我怎麼測

我先從使用者操作確認功能是否正常，再往下檢查相關資料。

- 先整理操作流程，用正常輸入建立對照，再測邊界值與異常輸入。
- 換不同資產、瀏覽器和操作入口，比對相連功能的結果。
- 用瀏覽器開發者工具檢查端到端 Web API 與 WebSocket 通訊。
- 用 TestRail 管理 Wallet、Referral／Affiliate 與 Convert 的測試案例。
- 透過 TablePlus 執行 SQL，核對錢包餘額、抵押品、帳戶間轉帳、掛單與成交紀錄、手續費及結算資料。
- 用試算表比對預期與實際金額。手續費、資金費用與強制平倉依 BTSE 當時的公開公式計算；佣金分配則先向指導我的資深 QA 確認。

這些檢查使用瀏覽器網路紀錄與 API 資料。我在 BTSE 沒有直接查看或分析伺服器日誌。

### 三個問題與處理結果

| 功能 | 發現的問題 | 我怎麼確認 | 可能影響 | 當時的處理結果 |
|---|---|---|---|---|
| Futures／Spot | 輸入邊界值後，價格結果不一致，或畫面無法顯示可用結果 | 用正常輸入對照，再換不同資產、三種瀏覽器，並檢查 API 回應 | 相同的邊界處理問題可能影響不只一個交易介面 | QA 與工程團隊確認問題；當時以版本發布為優先，問題尚未結案 |
| Referral／Affiliate | 在層級較深、交易活躍的代理關係中，佣金超過預期分配 | 建立多帳號測試模型、產生交易，取得後台結果後再用試算表核對 | 原本較少出現的情況，可能隨代理交易增加而擴大 | 管理團隊將問題排在版本發布之後；我離職時仍未結案，最後的 TestRail 審查也還沒完成 |
| Convert | 從不同入口操作、換不同資產組合，輸入邊界值後都無法取得可用結果 | 重開瀏覽器、測試三種瀏覽器、更換來源與目標資產，並檢查 Convert API 回應 | 其他依賴同一兌換服務的功能也可能受影響 | 工程團隊確認問題，當時仍未結案；沒有服務中斷或修復完成的證據 |

### 我如何判斷問題

我會先確認問題影響哪些功能，再判斷處理的優先順序。

1. 先查影響範圍，再判斷嚴重度。換產品、資產或入口都能穩定重現的問題，值得進一步追查。
2. 用預期金額與實際結果核對，讓團隊能檢查佣金、手續費、資金費用與強制平倉的計算差異。
3. 分清楚觀察結果與推測。當時能證明缺陷及受影響的功能，不能證明曾經中斷服務、已經修復，或避免了多少損失。
4. 把測試模型、重現步驟與測試範圍寫進內部 Wiki 和 TestRail，供團隊後續使用。

### 可用在其他交易所的測試方法

以下是我會沿用的測試方法，不代表 BTSE 已經採用或完成修正。

- 為各種輸入定義可接受範圍，確認介面與 API 的錯誤回應一致，而且能讓使用者知道如何處理。
- 測試邊界兩側的值，再換不同資產與相連功能重測。
- 在不同代理層級與交易條件下，核對佣金分配總額。
- 比對交易前後的訂單、倉位、幣別、手續費與結算狀態。
- 檢查訂單的待處理、掛單、成交、取消、拒絕與觸發等狀態。
- 把 KYC 狀態測試與洗錢防制篩查、法遵責任分開。

### 資料來源與限制

- 這三個案例來自我實際參與的工作與回憶。離職後，已無法取得前雇主的原始紀錄，供他人獨立查證。
- 不公開精確門檻、內部帳號結構、交易金額、客戶資料、識別碼或 API 回應內容。
- 沒有證據能證明問題已修好、曾造成正式環境服務中斷，或避免了多少財務損失。
- 這段經驗不包含 Postman、Swagger、伺服器日誌分析、洗錢防制篩查、智能合約測試或區塊鏈節點操作。
- 目前的公開公式，無法證明 2024 年 9–11 月實際使用的是哪一版公式。
