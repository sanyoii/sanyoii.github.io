# ASML Automation and Leadership Case Study

> Period: May 2023–Apr 2024
> Role: Project Leader / Senior Automation Test Engineer, Zealogics／ASML engagement
> Scope: HMI eP5 modules iCDU, MM Flow, and ADEL; fully remote distributed team
> Public navigation: [Portfolio](https://sanyoii.github.io/) | [Public QA resume](https://github.com/sanyoii/sanyoii.github.io/blob/main/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md)

> Source: Based on my direct work and recollection. Original employer records are no longer available for independent verification. Confidential details are omitted.

## English

### The delivery problem

ASML engineers in different time zones shared complex HMI eP5 test environments. A test run required Simulator startup, function-specific Recipe loading, manual operation, and cleanup. Long-running cases kept an engineer at the environment. An incomplete reset could also prevent the next engineer from starting.

I led six Zealogics Automation Engineers in the ASML-side STA team. ASML supplied the base TestComplete automation architecture. I improved its configurability and cross-product use, designed the setup-to-cleanup lifecycle, planned reusable modules, and coordinated delivery across iCDU, MM Flow, and ADEL. I implemented some test cases; the six engineers completed most coding.

### Architecture and test strategy

I included the environment lifecycle in the automation architecture.

- The workflow covered Simulator startup, initialization, retrieval of current test files and test cases, environment setup, Recipe loading, execution, status reporting, cleanup, and reset.
- Engineers could trigger the normal path from a `.bat` file or Bamboo, then review the TestComplete or Bamboo result.
- The normal path ran unattended from setup through reset. A Bamboo connection failure still required an engineer to check the environment and connection state.
- I reviewed test cases before assignment. I grouped repeated behavior into reusable modules, then divided implementation work among the six engineers.
- I assessed whether each test case supported full automation. When it did not, I proposed partial automation to remove repeatable manual work while keeping the required human step visible.
- Bitbucket held source code. Bamboo and TestComplete handled CI test orchestration and result review. The team also used Python, VS Code, Jira, and Confluence.

### Delivery and team leadership

I planned the technical work and tracked progress, risks, and requests for help across teams.

- Daily syncs surfaced environment blockers, dependencies, and work that needed help from another ASML function owner.
- I represented STA in management and weekly status meetings. Jira filters and JQL supported ticket and test case status reviews, but the original queries and counts are no longer available.
- I used one-on-ones for blockers, support, and direct performance feedback. Annual formal evaluations went to my direct manager; the later approval chain is unknown.
- I reviewed the delivery scope, assigned tasks and test cases, discussed implementation details with the engineers, and tracked risk, schedule, tickets, and handoff.
- I created Jira and Confluence material for test cases, Test System Design, work records, operation guidance, and newcomer onboarding. I cannot confirm whether the onboarding material remained in use after my engagement.

### Training and feedback

I provided training, live demonstrations, operating instructions, and technical documentation to client engineers across functions. Approximately 20–30 people attended.

I can confirm that approximately 2–3 engineers ran the automation independently after training and submitted change requests. I do not know how many of the other attendees used it. The team discussed informal feedback in daily syncs or Communicator and tracked formal requests in Jira. I completed what the schedule allowed; ASML inherited the open requests after the engagement ended.

### Handoff during the budget change

ASML reduced its software-outsourcing budget, and STA lost funding. I documented the six engineers' capabilities, arranged work handoffs, and worked with my direct manager on reassignment. All six moved to other ASML teams or projects. Engineering leadership and HR made the final placement decisions.


### Recorded outcome

- Engineers could start the normal workflow through a batch file or Bamboo and review one result after unattended setup, execution, cleanup, and reset.
- The workflow reduced repeated manual setup, operation, and cleanup work. It also gave users a consistent reset path for shared environments.
- Reusable modules and pre-assignment review reduced duplicate implementation across the three HMI eP5 modules.
- Independent use and Jira feedback provided limited adoption evidence. Session attendance alone was not counted as adoption.
- ASML received the technical material, open Jira requests, and team handoffs when the engagement ended.

### Quality and leadership decisions

1. Include the environment lifecycle in the architecture. Automation that leaves setup or reset to memory can still block the next user.
2. Choose full or partial automation case by case. A visible manual boundary is safer than claiming unattended execution for a step that still needs judgment.
3. Separate architecture ownership from coding volume. I designed and coordinated the improvements; six engineers implemented most code.
4. Separate attendance from use. Training attendance shows who took part. Independent runs and modification requests show stronger adoption evidence.
5. Keep exception and ownership boundaries explicit. Connection failures required manual investigation, and ASML leadership and HR owned final staffing decisions.

### Reusable controls

- Model setup, data retrieval, execution, reporting, cleanup, and reset as one stateful workflow.
- Add health checks for environment availability, connection state, required files, services, and final reset state.
- Review test cases before assignment and extract reusable modules before parallel implementation begins.
- Record whether a test case is fully automated, partially automated, or manual, including the reason and human handoff point.
- Track delivery status, environment blockers, feedback, and open requests in one reviewable ticket flow.
- Keep training attendance, independent use, feedback, and long-term adoption as separate measures.
- Prepare technical documentation, capability records, and open-work ownership before a team transition.

### Evidence limits

- This case is based on my direct work and recollection. Original project records are no longer accessible.
- Setup-time, cost, and coverage improvements are described without percentages because the source measurements are unavailable.
- The case study does not claim that I created ASML's base architecture, implemented the full system alone, automated every test case, prevented downtime, or delivered zero-failure automation.
- Bitbucket use is limited to source control. No Git workflow, branch strategy, pull-request ownership, Bamboo integration detail, or separate reporting tool is claimed.
- Individual performance details, Jira queries, ticket counts, and post-departure use of onboarding material remain private or unknown.

## 繁體中文

### 交付問題

不同時區的 ASML 工程師共用 HMI eP5 測試環境。每次測試都要啟動模擬器、載入對應功能的 Recipe、執行操作，再清理環境。耗時較長的案例需要工程師持續操作；若環境未完整重置，也會影響下一位使用者。

我在 ASML 的 STA 團隊帶領 6 位 Zealogics 自動化測試工程師。ASML 提供既有 TestComplete 架構；我改善設定彈性與跨產品使用方式，設計從環境設定到清理重置的流程、規劃共用模組，並協調 iCDU、MM Flow 與 ADEL 三個模組的交付。我實作部分測試案例，多數程式由 6 位工程師完成。

### 架構與測試策略

我將測試前後的環境準備與清理一併納入自動化設計。

- 流程涵蓋啟動模擬器、初始化、取得最新測試檔案與案例、設定環境、載入 Recipe、執行測試、回報狀態、清理及重置。
- 工程師可透過 `.bat` 檔或 Bamboo 啟動正常流程，最後在 TestComplete 或 Bamboo 查看結果。
- 正常流程從環境設定到重置都不需全程人工操作；若 Bamboo 連線失敗，仍需工程師檢查環境與連線狀態。
- 我先審查測試案例，將重複行為整理成共用模組，再分派給 6 位工程師實作。
- 逐一判斷案例是否適合全自動化；不適合時，改採部分自動化，減少重複操作並保留必要的人工作業。
- Bitbucket 用於版本控制；Bamboo 與 TestComplete 負責 CI 測試流程與結果檢視。團隊也使用 Python、VS Code、Jira 及 Confluence。

### 交付與團隊帶領

我負責技術規劃，也追蹤進度、風險與需要跨團隊協助的工作。

- 每日會議用來確認環境問題、工作相依性，以及需要其他 ASML 功能負責人協助的事項。
- 我代表 STA 參加管理與每週進度會議，使用 Jira 篩選器及 JQL 檢視工作單與測試案例狀態。
- 透過一對一會談了解困難、提供支援及績效回饋；年度正式考核交給直屬主管，後續核定流程不在我的確認範圍內。
- 我確認交付範圍、分派工作與測試案例、和工程師討論實作細節，並追蹤風險、時程、工作單與交接。
- 我在 Jira 和 Confluence 整理測試案例、測試系統設計、工作紀錄、操作說明與新人教材。離開專案後，無法確認教材是否持續使用。

### 操作訓練與使用回饋

我為客戶端不同職能的工程師提供操作訓練、現場示範及技術文件，約有 20–30 人參加。

其中可確認約 2–3 位工程師曾在訓練後獨立執行自動化測試，並提出修改需求；其餘參與者的使用情形未知。非正式回饋在每日會議或 Communicator 討論，正式需求則進 Jira 追蹤。我在時程內完成能處理的項目，專案結束後由 ASML 接手未完成需求。

### 預算調整時的交接

ASML 削減軟體委外預算後，STA 失去經費。我整理 6 位工程師的能力與工作內容、安排交接，並和直屬主管協調轉任。最後 6 位工程師都轉到其他 ASML 團隊或專案；最終人事安排由工程主管與人資決定。

### 已知結果

- 工程師可透過批次檔或 Bamboo 啟動正常流程，待環境設定、測試執行、清理與重置完成後查看結果。
- 流程減少重複的環境設定、操作與清理，也讓共用環境有一致的重置方式。
- 共用模組與分派前審查，減少三個 HMI eP5 模組的重複實作。
- 獨立執行與 Jira 修改需求提供了部分實際使用證據；參加訓練的人數不視為使用人數。
- 專案結束時，ASML 接收技術資料、未完成的 Jira 需求及團隊交接資料。

### 品質與管理判斷

1. 將環境準備與重置納入架構，避免依賴人工記憶而影響下一位使用者。
2. 逐案選擇全自動化或部分自動化，明確保留需要人工判斷的步驟。
3. 分清楚設計與實作分工：我負責改善設計及協調，多數程式由工程師完成。
4. 以獨立操作與修改需求觀察實際使用情況，不以參加訓練人數代替。
5. 保留例外處理與決策權責：連線失敗需人工檢查，人事安排由 ASML 工程主管及人資決定。

### 可沿用的方法

- 將環境設定、資料取得、測試執行、結果回報、清理與重置規劃為一套有明確狀態的流程。
- 檢查環境是否可用、連線狀態、必要檔案與服務，以及最後是否完成重置。
- 分派工作前先審查案例、整理共用模組，再由工程師分工實作。
- 記錄每個案例採全自動化、部分自動化或手動測試的理由，以及人工接手的位置。
- 用工作單追蹤交付進度、環境問題、回饋及未完成需求。
- 分別記錄訓練參與、獨立操作、使用回饋與長期使用情形。
- 團隊調整前備妥技術文件、人員能力資料及未完成工作的接手安排。

### 資料來源與限制

- 本案例依我直接參與的工作與回憶整理。離開專案後，已無法取得原始紀錄供獨立核實。
- 沒有可核實的環境設定時間、成本或測試涵蓋率改善比例；成果維持定性描述。
- ASML 提供原始架構，團隊完成多數程式，並非所有案例都能全自動執行。本文沒有零故障或避免停機的量測結果。
- 工具描述限於實際使用範圍，未提供 Git 分支策略、PR 管理、Bamboo 整合細節或其他報表工具的證據。
- 個人績效資料不公開；原始 Jira 查詢、工作單數量及離開專案後的教材使用情況無法確認。
