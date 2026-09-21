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

### 我處理哪些客戶問題

資安產品要保護資料，也不能妨礙客戶正常工作。升級失敗、驅動程式衝突或防護原則沒有正確套用，在不同環境可能出現不同症狀。我會先蒐集資料、設法重現，再確認原因。

在 Trend Micro 的 QA 與客戶技術支援工作中，我處理過大量客戶問題、P1 緊急案件與 hotfix 驗證，也在客戶正式環境執行外部 Beta 測試。我整理症狀與診斷資料，在可行時協助恢復環境，並提供工程團隊重現與驗證問題所需的資訊。

### 提早檢查 Chrome 更新對 DLP 的影響

Chrome 大、小版本更新，有時會讓 DLP 無法阻擋敏感檔案上傳。過去通常等到客戶回報，團隊才知道有相容性問題，再趕緊提供 hotfix。

我寫了 Python 程式，透過 Google 官方 API 檢查 Chrome Beta 與 Stable 版本。有新版本時，就觸發瀏覽器更新與敏感檔案上傳測試；如果 DLP 沒有擋下上傳，便寄信通知團隊。

`偵測 Chrome 新版本 → 更新瀏覽器 → 測試能否擋下敏感檔案上傳 → 失敗時寄信通知`

這讓團隊能在客戶回報前處理相容性問題，也減少每次 Chrome 更新時需要人工處理的工作。DLP QA 通常 4 人、最多 5 人，同時負責新功能 QA 與 SEG；這個案例發生時有 4 人。節省多少工時、提早找到多少缺陷，沒有保留量測資料。本文也不公開 API 網址細節或公司的專有實作。

### 改用網站清單，調整掃描範圍

原有的瀏覽器整合會把所有網站資料交給 DLP 掃描，客戶經常反映瀏覽變慢。團隊重構 DLP 時，我建議改用支援網站清單，不再預設掃描所有網站；這個設計後來由團隊採用並實作。

改版後只掃描支援的網站。文件會註明：不在清單上的網站不受支援。使用者可以先把網站加入設定檔試用；若仍無法運作，再回報技術支援，由團隊評估是否納入支援。自行加入網站，不代表防護一定有效。

**依我對當時 QA 效能測試報告的回憶，單獨改用網站清單後，CPU 與記憶體用量各比原先降低至少 10%。** 這是網站清單設計的比較結果，不是整個重構專案的合計成效。目前無法取得原始報告、基準值與測試環境資料，供他人獨立查證。

資源用量降低的同時，預設掃描範圍也縮小了。雖然有申請新增網站支援的流程，但不代表所有網站的防護範圍完全不變，也不能據此推算網頁載入速度改善多少。

### 讓轉交 SEG 的案件資料更完整

擔任 SEG Leader 時，我會先看案件描述、重現步驟與診斷資料。資料不足就退回 L2，清楚列出需要補什麼；資料完整的案件，再依處理優先順序、問題難度與工程師的工作量分派。

WFBS 技術支援團隊人員流動頻繁，新人常不熟悉案件處理。我建議把較簡略的 Survival Guide 改寫成 WFBS Guide Book，幫助新人認識產品並處理客戶問題。上線後，人員流動率沒有下降，但因資料不足被退回的案件比例逐月下降。

在 DLP 遇到類似問題時，我沿用這個經驗，提出按問題類型編排的圖文指南。先說明如何判斷問題類型，再逐步列出需要哪些資料、該怎麼蒐集。團隊也持續維護與更新指南。

**依當時主管提供的數據，DLP 指南上線第一個月，因資料不足被 SEG 退回 L2 補件的案件比例，下降 20 個百分點。** 這是退回比例的絕對變化，不是相對減少 20%，也不是處理時間縮短。目前無法取得基準、改善後比例、案件數與原始報表，供他人獨立查證。WFBS 的改善沒有保留量化數據；這個 DLP 數字也不適用於 Chrome 監測。

### 我怎麼排查問題

- 改動客戶電腦前，先看問題描述、重現步驟、日誌、記憶體傾印、系統資訊與環境變更紀錄。
- 環境允許時，在內部測試環境或客戶提供的虛擬機器重現問題。
- 使用 Windows Event Log、WinDbg、ProcMon、Process Explorer、效能資料、產品日誌與系統狀態，區分症狀和可能原因。
- 隔離測試的結果先視為假設，再用日誌、記憶體傾印、重現結果與元件狀態確認。
- 交付 hotfix 前，確認原本的問題是否解決，以及有沒有影響其他功能。客戶端部署與結案由技術支援團隊負責。
- 將反覆出現的問題納入回歸、系統、效能、升級與復原測試。

### 四個客戶案例

| 案例 | 客戶遇到的問題 | 我做的檢查與處理 | 處理結果 | 結果的限制 |
|---|---|---|---|---|
| WFBS 7.0 客戶問題與 SP1 | 發布後出現資源用量增加、速度變慢、停止回應與端點不穩定 | 我擔任日班案件負責人；缺資料就列出補件需求，可重現時整理日誌與記憶體傾印給工程團隊，再檢查 hotfix 與副作用。之後將問題納入 SP1 的 Scan、Messaging Security Agent、系統及效能測試 | 當時內部回報顯示，團隊處理並發布 SP1 後，支援需求下降；這是 QA、工程與技術支援團隊的共同成果 | 原始統計與紀錄已無法取得，不能將團隊處理量或支援需求下降全算成我的成果 |
| OfficeScan DLP P1 案件 | 同時執行兩套有 DLP 功能的產品時，防護原則失效，電腦也會當機 | 檢查原則與服務狀態，蒐集日誌、Windows 事件、完整記憶體傾印及處理程序資料，再用客戶提供的虛擬機器重現。驅動程式與處理程序攔截機制的資源競爭，可以解釋這兩種症狀 | 客戶接受一次只執行一套 DLP 產品，恢復正常操作；技術支援團隊結案後，未再收到相關案件 | 這是暫時解法，不是永久的相容性修正；沒有資料外洩的證據 |
| WFBS P1 升級案件 | 升級後，即時與手動掃描都沒有偵測到測試樣本 | 升級資料顯示檔案替換與清理失敗，造成元件版本混雜，必要處理程序也未正常執行。先完整移除再安裝，恢復預期偵測；之後重建客戶的升級流程，檢查 hotfix、完整功能與副作用 | hotfix 通過重建環境的測試；客戶端部署與結案由技術支援團隊處理 | 相同症狀可能來自其他原因，不能推論這個修正解決了所有掃描失敗的情況 |
| WFBS 7.0 外部 Beta | 在不同客戶的正式環境升級用戶端後，出現功能遺失、當機、停止回應或速度變慢 | 復原前先蒐集日誌、系統資訊、事件與記憶體傾印，再完整移除並重新安裝。每天將診斷資料交給產品團隊，後續版本則在下一個客戶環境檢查 | 現場資料幫助團隊修正後續版本，同時先讓客戶環境恢復可用 | 換到下一個客戶環境驗證，不等於在原本的電腦重測。正式版發布後仍有升級問題，Beta 並沒有消除這項風險 |

### 處理問題時的幾個原則

1. 復原前先保存資料。移除或重新安裝雖然可能恢復服務，也可能清掉分析原因所需的狀態。
2. 分開記錄「服務恢復」與「問題修好」。重新安裝或隔離衝突產品，不代表根本問題已經解決。
3. 重建客戶實際走過的流程。一般乾淨環境，不能取代造成問題的升級順序、軟體互動、原則設定或系統狀態。
4. 確認暫時措施是否有效。在 DLP 衝突案例中，加入排除清單只是延後當機，防護仍會失效，因此不能算修好。
5. 說清楚誰負責什麼。我整理資料、重現問題並驗證 hotfix；技術支援團隊負責客戶部署與結案，工程團隊負責修改程式。

### 可沿用的方法

- 列出轉交案件的必要資料：重現步驟、時間、產品日誌、Windows 事件、系統資訊、可取得的記憶體傾印，以及近期環境變更。
- 清理、回復升級前狀態、移除驅動程式或隔離產品前，先保存原始狀態。
- 記錄測試是在原環境、重建環境，還是另一個客戶環境執行。
- 除了原本的問題，也檢查是否影響服務、處理程序、驅動程式、防護原則、掃描與常用操作。
- 分別追蹤服務恢復、暫時解法、hotfix 驗證、客戶部署與永久修正。
- 將重複出現的問題納入回歸、升級、效能、復原與相容性測試。

### 資料來源與限制

- 內容來自我實際參與的工作與回憶。離職後，已無法取得前雇主的原始資料，供他人獨立查證。
- 案件退回比例下降 20 個百分點，來自當時主管提供的數據；CPU 與記憶體降幅，則來自我對 QA 效能報告的回憶。兩者是不同成果。
- 不公開客戶身分、地點、端點數量、精確升級流程、客戶環境中的第三方產品衝突細節，或繞過防護的操作方法。
- 各案例只能說明實際記錄的驗證範圍。我沒有宣稱曾發生資料外洩、修正適用所有情況，或做過未曾執行的原環境重測。修正、部署與結案仍依實際團隊分工說明。
