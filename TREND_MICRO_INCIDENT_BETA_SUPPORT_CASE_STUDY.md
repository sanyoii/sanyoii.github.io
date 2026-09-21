# Trend Micro Incident, Beta, and Support Case Study

> Period: May 2010–Jan 2023
> Roles: QA Engineer; Senior Customer Service Engineer; Senior QA Engineer & Senior Customer Service Engineer
> Public navigation: [Portfolio](https://sanyoii.github.io/) | [Public QA resume](https://github.com/sanyoii/sanyoii.github.io/blob/main/PUBLIC_QA_PRODUCT_QUALITY_RESUME.md)

> Source: Based on my direct work and recollection. Original employer records are no longer available for independent verification. Confidential details are omitted.

## English

### The product-quality problem

Endpoint security needs to protect data while allowing customers to keep working. A failed upgrade, a driver conflict, or an incomplete policy action can appear as different symptoms across endpoints. The first support report is therefore evidence, not yet the root cause.

Across Trend Micro QA and customer escalation roles, I worked on high-volume incidents, P1 support cases, hotfix validation, and an external beta in production environments. I gathered diagnostic information, helped restore the affected environment where possible, and gave Engineering the evidence needed to reproduce and test the problem.

### Proactive DLP checks after Chrome updates

Chrome major and minor releases sometimes broke the browser integration used to block sensitive-file uploads. We initially learned about failures from customer cases and then rushed compatibility hotfixes.

I wrote a Python program that checked Google's official API for Chrome Beta and Stable versions. On detecting a new version, the workflow triggered a browser update and a sensitive-file upload test. If DLP failed to block the upload, it emailed the team to flag the need for a correction.

`New Chrome version → browser update → DLP upload-blocking test → email alert on failure`

This helped the team address compatibility issues before customers discovered them and reduced manual effort around Chrome releases. DLP QA usually had four people and at most five, combining feature QA and SEG work; this case occurred with four. I do not have retained measurements of time saved or defects caught. The API endpoint and proprietary implementation are not reproduced here.

### Supported-site scanning: performance and scope

During a team-led DLP refactor, I proposed replacing scanning across all websites with a supported-site list. The team adopted the design. The previous browser integration sent website data through DLP scanning, and customers frequently reported slower browsing.

With the new design, scanning applied to supported sites. Documentation explicitly marked unlisted sites as unsupported. Users could add a site to a configuration file to try enabling support; if it did not work, they could open a Support case for the team to assess whether to support that site. Adding a site did not guarantee protection.

**Based on my recollection of the QA performance test report, switching this site-list design alone reduced CPU consumption and memory consumption by at least 10% each, relative to the previous design.** This was a comparison of the site-list design, not a combined result for the entire refactor. I proposed the design; the team adopted and implemented it.

The tradeoff was a narrower default scanning scope with a documented path for requesting additional site support. These resource reductions do not establish faster page loads by the same percentage or unchanged protection across all websites. The original report, baseline values, and test-environment details are not available for independent verification.

### Case information and support training

As SEG Leader, I checked each case for a clear problem description, reproduction steps, and required diagnostic information. I returned incomplete cases to L2 with specific collection requests. Complete cases were assigned by priority, complexity, and team workload.

Frequent WFBS Support staff changes left newcomers struggling to handle cases. I proposed replacing the rough Survival Guide with a practical WFBS Guide Book. After rollout, missing-information case returns declined month by month, even though staff turnover did not decline.

I applied that experience to DLP by initiating an illustrated diagnostic-data collection guide organized by issue type. It explained how to classify the problem, which evidence was needed, and how to collect it step by step. We continued maintaining and updating the material.

**In the first month after the DLP guide rolled out, the share of cases returned by SEG to L2 for missing information fell by 20 percentage points, according to figures shared by my manager at the time.** This is an absolute change in the case-return percentage, not a relative 20% reduction or a measure of resolution time. The baseline, final percentage, case count, and original report are not available for independent verification. The WFBS improvement remains qualitative; the DLP figure does not apply to WFBS or Chrome monitoring.

### How I handled incidents

- I checked the problem statement, reproduction steps, logs, dumps, system information, and environment history before changing the endpoint.
- I reproduced the failure locally or in a customer-provided VM when the available environment allowed it.
- I used Windows Event Log, WinDbg, ProcMon, Process Explorer, performance data, product logs, and system state to separate symptoms from likely causes.
- I treated isolation results as a working hypothesis until the logs, dumps, reproduction, and component state supported the same explanation.
- I verified the target behavior and side effects before a hotfix handoff. Support retained ownership of customer deployment and case closure.
- I carried recurring incident patterns into regression, system, performance, upgrade, and recovery coverage.

### Four cases

| Case | Failure signal | Evidence and action | Recorded outcome | Evidence boundary |
|---|---|---|---|---|
| WFBS 7.0 incident response and SP1 | Customers reported high resource use, slowdown, hangs, and endpoint instability after release | As the daytime Ticket Owner, I returned incomplete escalations with exact collection requests, reproduced issues when possible, packaged logs and dumps for Engineering, then tested hotfix targets and side effects. I later expanded Scan, Messaging Security Agent, system, and performance coverage for SP1 | Internal reporting indicated that support demand declined after the team response and SP1. This was a QA, Engineering, and Support team result | Original internal statistics and artifacts are inaccessible. I do not attribute team ticket volume or support reduction to myself |
| OfficeScan DLP P1 escalation | DLP policy enforcement failed and the endpoint crashed when two DLP-capable products operated together | I verified policy and service state, collected logs, Windows events, a full memory dump, and process data, then reproduced the conflict in a customer-provided VM. Driver and process-hook contention explained both symptoms | The customer accepted running one DLP product at a time. Operations resumed, Support closed the case, and no further related ticket was reported | This was an operational workaround, not a permanent compatibility fix. There was no evidence of a data breach |
| WFBS P1 upgrade escalation | Real-time and manual scans missed a test sample after an upgrade | Upgrade evidence showed failed file replacement and cleanup, leaving mixed-version components and missing processes. A clean removal and fresh install restored expected detection. I then rebuilt the customer upgrade path and tested the hotfix, full functions, and side effects | The hotfix passed the reconstructed customer path. Support handled customer deployment and closure | Similar symptoms could have other root causes. I do not claim that the hotfix resolved every scan failure or that I performed the customer rollout |
| WFBS 7.0 external beta | Production client upgrades produced missing functions, crashes, hangs, or slowdown across different environments | I collected logs, system information, events, and dumps before recovery, used clean removal and fresh installation to restore affected endpoints, and sent daily evidence packages to the product team. Later builds were checked in subsequent customer environments | Field evidence informed later builds and product fixes while customers regained usable environments | A subsequent environment is cross-environment validation, not a retest of the original endpoint. Upgrade failures still appeared after release, so the beta did not eliminate the risk |

### Quality decisions

1. Preserve evidence before recovery. An uninstall or clean installation can restore service and also erase the state needed for root-cause analysis.
2. Separate recovery from correction. A fresh install or product-isolation workaround can restore operations without proving that the underlying defect is fixed.
3. Test the customer's path. A generic clean environment does not replace the upgrade sequence, software interaction, policy state, or system condition that triggered the failure.
4. Reject partial mitigation as a fix. In the DLP case, whitelisting delayed the crash but enforcement still failed, so I did not classify it as resolution.
5. Keep ownership explicit. I prepared evidence, reproduced failures, validated hotfixes, and handed cases back. Support owned customer rollout and closure; Engineering owned code changes.

### Reusable incident and beta controls

- Define a minimum evidence package for escalation: reproduction steps, timestamps, product logs, Windows events, system information, dumps when available, and recent environment changes.
- Capture the original state before cleanup, upgrade rollback, driver removal, or product isolation.
- Record whether validation occurred in the original environment, a reconstructed environment, or a different customer environment.
- Verify both the target fix and side effects across services, processes, drivers, policy enforcement, scan behavior, and common user workflows.
- Track recovery, workaround, hotfix validation, customer deployment, and permanent correction as separate states.
- Convert repeated field failures into regression, upgrade, performance, recovery, and compatibility coverage.

### Evidence limits

- The proactive testing, support training, and four incident/beta cases come from direct work and my recollection. Former-employer records are no longer accessible.
- The 20-percentage-point case-return change comes from figures shared by my manager. CPU and memory reductions come from my recollection of the QA performance report and apply to a change in scanning scope. These are separate outcomes, and neither has been independently verified.
- Customer identities, locations, endpoint counts, exact upgrade paths, customer-specific third-party conflicts, and security-control bypass details are not disclosed.
- The case study does not claim a breach, a universal fix, sole ownership of team outcomes, or original-environment retesting where it did not occur.
- Product fixes, customer rollout, and case closure are attributed to the responsible Engineering and Support teams.

## 繁體中文

### 產品品質問題

端點防護除了要有效阻擋威脅，也不能妨礙客戶工作。升級失敗、驅動程式衝突或原則未正確套用，在不同環境可能呈現不同症狀；我會先蒐集資料、重現問題，再判斷原因。

我在 Trend Micro 的 QA 與客戶技術支援工作涵蓋大量客戶問題、P1 緊急案件、hotfix 驗證，以及客戶正式環境中的外部 Beta 測試。我負責整理症狀與診斷資料、在可行時協助恢復環境，並提供工程團隊可重現及驗證的問題資訊。

### Chrome 更新後的主動 DLP 驗證

Chrome 大、小版本更新有時會讓阻擋敏感檔案上傳的瀏覽器整合失效。團隊原先直到收到客戶案件，才得知相容性問題，接著緊急提供 hotfix。

我撰寫 Python 程式，從 Google 官方 API 取得 Chrome Beta 與 Stable 版本。偵測到新版本後，流程觸發瀏覽器更新及敏感檔案上傳測試；若 DLP 未能阻擋，就寄信通知團隊修正。

`偵測 Chrome 新版本 → 更新瀏覽器 → 驗證 DLP 上傳阻擋 → 失敗時寄信通知`

這讓團隊能在客戶回報前處理相容性問題，減少 Chrome 更新時的人工處理工作。DLP QA 通常 4 人、最多 5 人，同時負責新功能 QA 與 SEG 工作；這個案例發生時有 4 人。節省工時與提早發現的缺陷數沒有保留量測資料，本文也不公開 API 網址細節或公司專有實作。

### 支援網站清單：效能與掃描範圍

原有瀏覽器整合會將所有網站的資料交給 DLP 掃描，客戶經常反映瀏覽速度變慢。團隊決定重構 DLP 時，我提出改用支援網站清單，不再預設掃描所有網站，團隊採用並實作了這個設計。

改版後只針對支援網站掃描。文件明確將未列網站標為不支援，並說明使用者可先將網站加入設定檔嘗試；若仍無法作用，再向技術支援團隊回報，由團隊評估是否支援。加入設定檔不保證防護有效。

**依我對當時 QA 效能測試報告的回憶，單獨切換網站清單設計後，CPU 與記憶體消耗各相對於改善前降低至少 10%。** 這是網站清單設計的比較結果，不是整體重構的合併成效。原始報告、基準值與測試環境細節目前無法取得，未經獨立核實。

降低資源消耗的同時，預設掃描範圍也縮小了。這項設計提供了申請新增網站支援的流程，但不代表所有網站的防護範圍不變，也不能將資源消耗降幅解讀為網頁載入速度提升相同比例。

### 案件資料完整度與技術支援訓練

擔任 SEG Leader 時，我先檢查案件描述、重現步驟與必要診斷資料。資料不足就退回 L2，明確說明需要補哪些資訊；完整案件則依優先序、複雜度與成員手上的工作量分派。

WFBS 技術支援團隊的人員流動頻繁，新人常不熟悉案件處理。我提出將較粗略的 Survival Guide 重寫成 WFBS Guide Book，協助新人認識產品與處理客戶問題。上線後，人員流動率沒有下降，但案件因資料不足被退回的比例逐月下降。

在 DLP 遇到相似問題時，我運用 WFBS 的經驗，提出按問題類型編排的圖文診斷資料蒐集指南。先說明如何判斷問題類型，再逐步列出要收哪些資料、如何蒐集，團隊也持續維護及更新。

**依當時主管分享的數據，DLP 指南上線首月，案件因資料不足被 SEG 退回 L2 補件的比例下降 20 個百分點。** 這是退回比例的絕對變化，不是相對下降 20%，也不是案件處理時間。基準、改善後比例、案件數與原始報表目前無法取得，未經獨立核實。WFBS 的改善沒有保留量化數據；這個 DLP 數字也不適用於 Chrome 監測案例。

### 我怎麼處理客戶問題

- 改動客戶端點前，先檢查問題描述、重現步驟、日誌、記憶體傾印、系統資訊及環境變更紀錄。
- 環境允許時，在內部測試環境或客戶提供的虛擬機器重現問題。
- 使用 Windows Event Log、WinDbg、ProcMon、Process Explorer、效能資料、產品日誌與系統狀態，分辨症狀與可能原因。
- 隔離測試的結果先作為假設，再用日誌、記憶體傾印、重現結果及元件狀態交叉確認原因。
- 交付 hotfix 前，驗證目標問題與可能副作用；客戶端部署與結案由技術支援團隊負責。
- 將反覆出現的客戶問題納入回歸、系統、效能、升級及復原測試。

### 四個案例

| 案例 | 問題現象 | 證據與處理 | 已知結果 | 驗證限制 |
|---|---|---|---|---|
| WFBS 7.0 客戶問題處理與 SP1 | 發布後出現資源消耗增加、系統變慢、停止回應及端點不穩定 | 我擔任日班案件負責人；缺資料時明確要求補件，可重現時整理日誌與記憶體傾印給工程團隊，再驗證 hotfix 與副作用。後續將問題納入 SP1 的 Scan、Messaging Security Agent、系統及效能測試 | 當時內部回報顯示，團隊處理與 SP1 發布後，支援需求下降；這是 QA、工程及技術支援團隊的共同成果 | 原始統計與紀錄已無法取得，不能把團隊的案件處理量或支援需求下降全歸為個人成果 |
| OfficeScan DLP P1 案件 | 兩套具 DLP 功能的產品同時運作時，防護原則失效，端點也會當機 | 確認原則與服務狀態，蒐集日誌、Windows 事件、完整記憶體傾印及處理程序資料，再用客戶提供的虛擬機器重現。驅動程式與處理程序攔截機制的資源競爭能解釋兩種症狀 | 客戶接受一次只執行一套 DLP 產品，恢復日常操作；技術支援團隊結案後，未再收到相關案件 | 這是暫時處理方式，不是永久的相容性修正；沒有資料外洩的證據 |
| WFBS P1 升級案件 | 升級後，即時與手動掃描都未偵測到測試樣本 | 升級資料顯示檔案替換及清理失敗，造成元件版本混雜，必要處理程序也未正常運作。先完整移除再重新安裝，恢復預期偵測；之後重建客戶升級流程，驗證 hotfix、完整功能及副作用 | hotfix 通過重建環境中的測試；客戶端部署與結案由技術支援團隊處理 | 相同症狀可能有其他原因，這個結果不代表修正所有掃描失敗情況 |
| WFBS 7.0 外部 Beta | 不同客戶正式環境升級用戶端後，出現功能遺失、當機、停止回應或速度變慢 | 復原前先蒐集日誌、系統資訊、事件及記憶體傾印，再完整移除並重新安裝。每天將診斷資料交回產品團隊，後續版本則在下一個客戶環境檢查 | 現場資料協助後續版本修正，同時先恢復客戶環境的可用性 | 下一個客戶環境的驗證，不等於原端點複測。正式版發布後仍有升級問題，因此 Beta 並未消除這項風險 |

### 品質判斷

1. 復原前先保留證據。移除或重新安裝能恢復服務，也可能清掉分析根因所需的狀態。
2. 分開記錄服務復原與缺陷修正。重新安裝或隔離衝突產品，不代表底層問題已經修好。
3. 重建客戶實際操作流程。一般乾淨環境無法取代觸發問題的升級順序、軟體互動、原則設定或系統狀態。
4. 確認緩解措施是否真的解決問題。在 DLP 衝突案例中，加入排除清單只延後當機，防護仍會失效，因此不能判定為修復。
5. 清楚交接責任。我負責整理證據、重現及 hotfix 驗證；技術支援團隊負責客戶部署與結案，工程團隊負責程式修改。

### 可沿用的方法

- 定義轉交案件的必要資料：重現步驟、時間、產品日誌、Windows 事件、系統資訊、可取得的記憶體傾印及近期環境變更。
- 清理、還原升級、移除驅動程式或隔離產品前，先保存原始狀態。
- 記錄測試是在原環境、重建環境，或另一個客戶環境執行。
- 同時驗證目標問題與副作用，涵蓋服務、處理程序、驅動程式、原則執行、掃描行為及常用操作流程。
- 分別追蹤復原、暫時處理方式、hotfix 驗證、客戶部署與永久修正。
- 將重複出現的客戶問題納入回歸、升級、效能、復原及相容性測試。

### 資料來源與限制

- 案例來自我直接參與的工作與回憶，離職後已無法取得前雇主的原始資料供獨立核實。
- 20 個百分點的案件退回比例變化，來自主管分享的數據；CPU 與記憶體降幅則來自我對 QA 效能報告的回憶，兩者是不同成果。
- 不公開客戶身分、地點、端點數量、精確升級流程、客戶環境中的第三方產品衝突細節或繞過防護的操作。
- 驗證範圍以各案例記錄為準，沒有資料外洩、通用修復或未曾執行的原環境複測主張。團隊修正、部署與結案均保留實際分工。
