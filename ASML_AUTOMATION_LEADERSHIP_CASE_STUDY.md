# ASML Automation and Leadership Case Study

> Status: `Day 19 Complete v1 / Public 2026-09-01`
> Period: May 2023–Apr 2024
> Role: Project Leader / Senior Automation Test Engineer, Zealogics／ASML engagement
> Scope: HMI eP5 modules iCDU, MM Flow, and ADEL; fully remote distributed team
> Evidence: `User-attested / original internal sources inaccessible / not independently document-verifiable`
> Public boundary: This file uses sanitized workflow and team information. It omits internal Test Cases, environment data, Jira queries, delivery metrics, performance ratings, and individual team-member details.
> Public navigation: [Portfolio](https://sanyoii.github.io/) | [Public QA resume](https://github.com/sanyoii/sanyoii.github.io/blob/main/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md)

## English

### The delivery problem

ASML engineers in different time zones shared complex HMI eP5 test environments. A test run required Simulator startup, function-specific Recipe loading, manual operation, and cleanup. Long-running cases kept an engineer at the environment. An incomplete reset could also prevent the next engineer from starting.

I led six Zealogics Automation Engineers in the ASML-side STA team. ASML supplied the base TestComplete automation architecture. I improved its configurability and cross-product use, designed the setup-to-cleanup lifecycle, planned reusable modules, and coordinated delivery across iCDU, MM Flow, and ADEL. I implemented some Test Cases; the six engineers completed most coding.

### Architecture and test strategy

I included the environment lifecycle in the automation architecture.

- The workflow covered Simulator startup, initialization, retrieval of current test files and Test Cases, environment setup, Recipe loading, execution, status reporting, cleanup, and reset.
- Engineers could trigger the normal path from a `.bat` file or Bamboo, then review the TestComplete or Bamboo result.
- The normal path ran unattended from setup through reset. A Bamboo connection failure still required an engineer to check the environment and connection state.
- I reviewed Test Cases before assignment. I grouped repeated behavior into reusable modules, then divided implementation work among the six engineers.
- I assessed whether each Test Case supported full automation. When it did not, I proposed partial automation to remove repeatable manual work while keeping the required human step visible.
- Bitbucket held source code. Bamboo and TestComplete handled CI test orchestration and result review. The team also used Python, VS Code, Jira, and Confluence.

### Delivery and team leadership

I combined technical planning with visible delivery controls.

- Daily syncs surfaced environment blockers, dependencies, and work that needed help from another ASML function owner.
- I represented STA in management and weekly status meetings. Jira filters and JQL supported ticket and Test Case status reviews, but the original queries and counts are no longer available.
- I used one-on-ones for blockers, support, and direct performance feedback. Annual formal evaluations went to my direct manager; the later approval chain is unknown.
- I reviewed the delivery scope, assigned tasks and Test Cases, discussed implementation details with the engineers, and tracked risk, schedule, tickets, and handoff.
- I created Jira and Confluence material for Test Cases, Test System Design, work records, operation guidance, and newcomer onboarding. I cannot confirm whether the onboarding material remained in use after my engagement.

### Enablement and feedback

I delivered TOI, live demos, operation guidance, and technical documentation to cross-functional client-side engineers. Approximately 20–30 people attended those sessions. Attendance did not prove adoption.

I can identify approximately 2–3 engineers who used the automation independently because they ran it after the sessions and submitted modification requests. The team discussed informal feedback in daily syncs or Communicator and tracked formal requests in Jira. I completed what the schedule allowed; ASML inherited the open requests after the engagement ended.

### Handoff during the budget change

ASML reduced its software-outsourcing budget, and STA lost funding. I documented the six engineers' capabilities, arranged work handoffs, and worked with my direct manager on reassignment. All six moved to other ASML teams or projects. Engineering leadership and HR made the final placement decisions.

My leadership contribution was preparing capability evidence and coordinating the transition. ASML controlled the budget, and its Engineering leadership and HR made the final staffing decisions.

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
4. Separate attendance from use. TOI participation shows reach. Independent runs and modification requests show stronger adoption evidence.
5. Keep exception and ownership boundaries explicit. Connection failures required manual investigation, and ASML leadership and HR owned final staffing decisions.

### Reusable controls

- Model setup, data retrieval, execution, reporting, cleanup, and reset as one stateful workflow.
- Add health checks for environment availability, connection state, required files, services, and final reset state.
- Review Test Cases before assignment and extract reusable modules before parallel implementation begins.
- Record whether a Test Case is fully automated, partially automated, or manual, including the reason and human handoff point.
- Track delivery status, environment blockers, feedback, and open requests in one reviewable ticket flow.
- Keep TOI attendance, independent use, feedback, and long-term adoption as separate measures.
- Prepare technical documentation, capability records, and open-work ownership before a team transition.

### Evidence limits

- The case comes from direct work and user-attested memory. Former-project records are no longer accessible.
- The old setup-time, operating-cost, and coverage percentages are excluded because the source data is unavailable.
- The case study does not claim that I created ASML's base architecture, implemented the full system alone, automated every Test Case, prevented downtime, or delivered zero-failure automation.
- Approximately 20–30 people attended TOI or demos; I can identify approximately 2–3 independent users. The remaining attendees' usage is unknown.
- Bitbucket use is limited to source control. No Git workflow, branch strategy, pull-request ownership, Bamboo integration detail, or separate reporting tool is claimed.
- Individual performance details, Jira queries, ticket counts, and post-departure use of onboarding material remain private or unknown.

## 繁體中文

### 交付問題

不同時區的 ASML engineers 共用複雜的 HMI eP5 test environments。一次測試包含 Simulator 啟動、function-specific Recipe loading、manual operation 與 cleanup。長時間 Test Case 需要 engineer 持續操作；reset 沒做完整，也可能讓下一位 engineer 無法開始。

我在 ASML-side STA team 帶領 6 位 Zealogics Automation Engineers。Base TestComplete automation architecture 由 ASML 提供；我改善 configurability 與 cross-product use，設計 setup-to-cleanup lifecycle、規劃 reusable modules，並協調 iCDU、MM Flow 與 ADEL 的交付。我實作部分 Test Cases，多數 coding 由 6 位 engineers 完成。

### Architecture 與 test strategy

我把 environment lifecycle 納入 automation architecture。

- Workflow 涵蓋 Simulator startup、initialization、取得現行 test files／Test Cases、environment setup、Recipe loading、execution、status reporting、cleanup 與 reset。
- Engineers 可從 `.bat` 或 Bamboo trigger 啟動 normal path，最後查看 TestComplete／Bamboo result。
- Normal path 可從 setup 到 reset unattended 執行；Bamboo connection failure 仍需要 engineer 檢查 environment 與 connection state。
- 分派前先 review Test Cases，把重複行為規劃成 reusable modules，再交由 6 位 engineers 分工實作。
- 每個 Test Case 都先判斷是否適合 full automation；不適合時提出 partial automation，移除可重複的 manual work，並保留必要的人工作業點。
- Bitbucket 用於 source control；Bamboo 與 TestComplete 用於 CI test orchestration／result review。團隊也使用 Python、VS Code、Jira 與 Confluence。

### Delivery 與 team leadership

我把 technical planning 與可檢查的 delivery control 放在一起。

- Daily sync 用來處理 environment blocker、dependency，以及需要其他 ASML function owner 協助的工作。
- 我代表 STA 參加 management／weekly status meetings。Jira Filters 與 JQL 用於 review ticket／Test Case status，但原始 queries 與數字已無法取得。
- One-on-one 用於確認 blocker、提供支援與直接回饋。Annual formal evaluation 交給 direct manager；後續 approval chain 為 `Unknown`。
- 我 review delivery scope、分派 tasks／Test Cases、和 engineers 討論 implementation details，並追蹤 risk、schedule、tickets 與 handoff。
- 我在 Jira／Confluence 整理 Test Cases、Test System Design、work records、operation guidance 與 newcomer onboarding material。離職後是否持續使用 onboarding material 為 `Unknown`。

### Enablement 與 feedback

我對 cross-functional client-side engineers 執行 TOI、live demo，並提供 operation／technical documentation。約 20–30 人參加；attendance 不等於 adoption。

目前可確認約 2–3 位 engineers 能獨立執行，因為他們在 session 後實際使用 automation 並提出 modification requests。非正式 feedback 在 daily sync／Communicator 討論，正式 requests 進 Jira 追蹤。我在時程內完成可處理項目；engagement 結束後，open requests 由 ASML 接手。

### 預算變更時的 handoff

ASML 削減 software-outsourcing budget，STA 失去預算。我整理 6 位 engineers 的能力、安排工作交接，並和 direct manager 協調 reassignment。6 位 engineers 最後都轉到其他 ASML teams／projects；final placement 由 Engineering leadership 與 HR 決定。

我的 leadership contribution 是準備 capability evidence 並協調 transition。預算由 ASML 控制，final staffing decision 由 Engineering leadership／HR 負責。

### 已知結果

- Engineers 可透過 batch file／Bamboo 啟動 normal workflow，在 unattended setup、execution、cleanup 與 reset 後查看統一結果。
- Workflow 減少重複的 manual setup、operation 與 cleanup，也提供 shared environments 一致的 reset path。
- Reusable modules 與分派前 review 減少三個 HMI eP5 modules 的重複 implementation。
- Independent use 與 Jira feedback 提供有限 adoption evidence；session attendance 不計為 adoption。
- Engagement 結束時，ASML 接收 technical material、open Jira requests 與 team handoffs。

### 品質與 leadership 判斷

1. Architecture 要包含 environment lifecycle。Setup／reset 若依賴記憶，automation 仍可能阻擋下一位使用者。
2. 逐案選擇 full／partial automation。保留明確 manual boundary，比把仍需判斷的步驟寫成 unattended execution 更可靠。
3. Architecture ownership 與 coding volume 分開。我負責設計及協調改善；多數 code 由 6 位 engineers 完成。
4. Attendance 與實際使用分開。TOI participation 代表接觸範圍；independent runs／modification requests 才是較強的 adoption evidence。
5. Exception 與 ownership boundary 寫清楚。Connection failure 需要人工排查；final staffing decision 由 ASML leadership／HR 負責。

### 可重用的 controls

- 把 setup、data retrieval、execution、reporting、cleanup 與 reset 建模成一個 stateful workflow。
- 為 environment availability、connection state、required files／services 與 final reset state 建立 health checks。
- 分工前先 review Test Cases，parallel implementation 前先抽出 reusable modules。
- 標示 Test Case 是 fully automated、partially automated 或 manual，並記錄原因與 human handoff point。
- 用可 review 的 ticket flow 追蹤 delivery status、environment blockers、feedback 與 open requests。
- 把 TOI attendance、independent use、feedback 與 long-term adoption 分開衡量。
- Team transition 前整理 technical documentation、capability records 與 open-work ownership。

### 證據限制

- 本案例來自本人直接參與及回憶確認；離開 engagement 後已無法存取原始 project records。
- 舊有 setup-time、operating-cost 與 coverage percentages 因 source data 無法取得，本文不使用。
- 本文不聲稱我建立 ASML base architecture、獨自完成整套系統、automated every Test Case、prevented downtime 或交付 zero-failure automation。
- 約 20–30 人參加 TOI／demo；目前可確認約 2–3 人能獨立使用，其餘 attendees 的 usage 為 `Unknown`。
- Bitbucket claim 限於 source control；本文不延伸 Git workflow、branch strategy、pull-request ownership、Bamboo integration details 或 separate reporting tool。
- 個人 performance details、Jira queries、ticket counts 與離職後 onboarding material 使用狀態維持 private／Unknown。
