# QA 核心模板

這九份檔案是 QA Decision Desk 的 canonical authoring library。套用到 release 時，把填好的文件複製進該 repository，跟著 release version review；不要直接引用這裡的檔案，避免歷史 evidence 隨模板更新。

## Decision flow

```mermaid
flowchart LR
    REQUEST["00 Test Request"] --> RISK["01 Risk Assessment"]
    RISK --> SPEC["02 Test Spec + Design Decision"]
    SPEC --> SCENARIO["03 Scenario"]
    SCENARIO --> CASE["04 Test Case"]
    CASE --> RUN["05 Run Record"]
    RUN --> DEFECT["06 Defect Report"]
    RUN --> SUMMARY["07 Release Summary"]
    DEFECT --> SUMMARY
    SUMMARY --> STATUS["08 Dashboard Status"]
```

## Template index

| No. | Template | Use | Suggested repository copy |
|---|---|---|---|
| 00 | [QA Test Request](00-qa-test-request.md) | 鎖定 subject、scope 與 decision question | `docs/quality/<release>/quality-decision-brief.md` |
| 01 | [Quality Risk Assessment](01-quality-risk-assessment.md) | 決定風險與 target coverage | `docs/quality/<release>/risk-assessment.md` |
| 02 | [Test Spec](02-test-spec.md) | 定義 approach、test design decision、gates 與 evidence | `docs/quality/<release>/test-spec.md` |
| 03 | [Test Scenario](03-test-scenario.md) | 描述業務流程與正負向 coverage | `docs/quality/<release>/coverage-inventory.md` |
| 04 | [Test Case](04-test-case.md) | 保存可重現的 test procedure | `docs/quality/<release>/test-cases.md` |
| 05 | [Test Run Record](05-test-run-record.md) | Append-only 保存每次執行 | `test-records/<run-id>/run-record.md` |
| 06 | [Defect Report](06-defect-report.md) | 連結 failure、impact 與 verification | `docs/quality/<release>/defect-log.md` |
| 07 | [Release Quality Summary](07-release-quality-summary.md) | 形成 human-owned release recommendation | `docs/quality/<release>/release-quality-summary.md` |
| 08 | [Dashboard Status Contract](08-dashboard-status-contract.md) | 約束 `.test-dashboard/status.json` projection | `.test-dashboard/status.json` |

九份模板是 library，不代表每次 release 都要建立九份文件。依 `QA-Lite`、`QA-Standard`、`QA-High-Risk` 與 conditional triggers 決定所需組合；Test Run Record 與 Release Quality Summary 每次 release 都不能省略。

Test Design Decision 直接放在 02 Test Spec，**不新增第十個核心模板**。它保存這條可審查鏈：

```text
Risk → Failure mode → Method → Oracle → Execution evidence → Decision
```

選擇 Method 時同時考慮 risk、規格特徵與 observability／environment constraint。Expected result 優先引用 approved requirement、business rule、API／schema contract 或 reviewed domain decision；只有 current behavior 時標為 characterization evidence，無核准來源時誠實標 `Assumption`，來源衝突或需求未定義時標 `Unknown／needs-clarification`。

## Playbook advisory layer

### 填好之後怎麼驗證

QA-Lite 只維護三份 release-specific 記錄：**brief/design、run ledger、decision**。Requirement、Risk、Design、Case 使用穩定 ID；machine packet 引用這三份，不新增另一套審批真相。

依 [執行契約](../../docs/decision-workflow.md) 填入 `release-evidence.json`，執行 `npm run review:release -- <packet> --design-only` 檢查設計；實際測試 artifact 與人工 review 齊全後，才執行不含 `--design-only` 的 review 和 `npm run gate:release`。Template heading test 只驗模板，不能代替 filled-packet review。

未解決的必要 oracle、缺少 required case、過期 live/manual run、artifact 雜湊不符與已改變的審查 input 都不得變成 Ready。後續 Pass 追加到台帳；使用 `--previous` 核對不能被刪改的先前 attempts/events。

[`Playbooks/QA`](../../Playbooks/QA/README.md) 提供 requirement readiness、coverage analysis、regression selection、test data、API coverage、defect triage 與 RCA 的 reviewable workflow。Playbook 不是第十個核心模板，也不是 evidence source；reviewed findings 仍要落回上表的 release-specific artifacts。

Coverage Analysis 沿用 03 Test Scenario contract，把完整 Requirement／AC → Scenario → Case → Run matrix 寫到 `docs/quality/<release>/coverage-inventory.md`。07 Release Quality Summary 只保留 target vs actual、重要 gaps、residual risk 與 inventory link，不複製完整矩陣。

### Procedure examples (illustrative)

以下是文件品質的教學範例，預設 `Not Run`，不是產品測試結果。套用時記錄實際 repository、subject SHA、程序版本／hash 與執行環境；不把本頁更新回填成歷史 evidence。共用 setup／reset 引用固定版本，case 只列參數與操作差異；共用程序變更時，依引用找出受影響 cases，決定重跑範圍。

以下三例從本 repository 根目錄開始。共用準備：使用 Git Bash，執行下列命令建立獨立 evidence 目錄；保留這個 shell，後續 `$qa_evidence` 指向同一目錄。若命令失敗，停止並記錄阻礙，不繼續猜路徑。

```bash
qa_evidence=$(mktemp -d "${TMPDIR:-/tmp}/qa-procedure.XXXXXX") && printf '%s
' "$qa_evidence"
```

記下印出的目錄；notes 與輸出均保存在該目錄。這是暫存位置，正式使用時應依 05 Run Record 的 retention／hash 規則保留到 release evidence，不能只留下會消失的暫存連結。三例只讀取 repo 或執行本機 contract test；不需帳戶、網路或 reset，不刪除任何既有 evidence。

**Manual：檢查文件中的自我審查說明**

- 不足：只寫「確認模板正確」。
- 操作：①用文字編輯器開啟 `Templates/QA/04-test-case.md`。②找到 `## Review`。③閱讀該標題下、檢查清單之前的說明，確認是否要求揭露 self-review／role overlap，以及文件審查不能建立產品 `Pass`。④在 evidence 目錄建立 `manual-notes.md`，記錄檔案版本、日期、觀察到的文字與符合／不符合／無法判定。
- 教學驗收條件：兩項說明皆存在。此條件為本例的 `Assumption`，不是已核准產品需求；文件無法開啟則記錄阻礙，不能填 Pass。需要文字編輯器，不需 Node.js。

**Automated controlled test：執行既有模板結構檢查**

- 不足：只寫「跑測試並保留結果」。
- 前提：在相同 Git Bash 執行 `node --version`，確認符合 `package.json` 的 Node.js `>=22.13.0`；未安裝或版本不足就停止記錄阻礙。
- 操作：執行以下命令，保存完整 stdout／stderr 與原始 exit code；終端顯示的目錄是本次 artifact 位置。

```bash
node --test tests/template-contract.test.mjs > "$qa_evidence/template-contract.txt" 2>&1
qa_exit=$?
printf 'exit_code=%s
' "$qa_exit" >> "$qa_evidence/template-contract.txt"
cat "$qa_evidence/template-contract.txt"
```

- 判定：exit code `0`，且 runner 回報沒有 failed tests；非零則保留錯誤輸出，辨識測試 assertion failure 或執行環境阻礙。Oracle 為該版本 `tests/template-contract.test.mjs` 的 assertions，僅驗模板結構，不證明程序可執行或產品 Ready。不要拿目前實作反推產品需求。

**Exploratory charter：探索程序是否還需要讀者猜測**

- 不足：只寫「探索一下問題」。
- 操作：①開啟 `Templates/QA/04-test-case.md`，設定 10 分鐘計時。②依序閱讀 `Preconditions`、`Procedure`、`Cleanup／rollback`、`Review`。③針對每節問：套用者是否知道要填哪個入口、具體輸入、可觀察結果及來源？共用步驟是否能追到固定版本？等待結束與清理方式是否有交代？④在 evidence 目錄建立 `exploration-notes.md`，記錄檢查過的節、零個或多個疑點及未探索部分；不要把空白模板預留欄位本身當缺陷。
- 停止：四節皆檢查完或 10 分鐘到，以先到者為準。這是文件探索記錄，沒有「必須找到問題」或產品 Pass 的要求；探索尚未進行時保留 `Not Run`。

文件審查與實際走讀分開記錄。自我走讀要揭露角色重疊；未做走讀時，不把「另一位 tester 能重現」填成已驗證。Live 事件沒出現時保留 coverage gap；controlled test 通過不能替代缺少的 live observation。

## Shared rules

- 所有 evidence 都要綁定 repository、release、branch、full SHA、environment、scope、owner 與 timestamps。
- `Fail`、`Blocked`、retry 與後續 `Pass` 全部保留，不能覆寫 chronology。
- Product Test Status 和 Data Status 分開判定。
- `Ready` 需要 human-owned release assessment；測試全綠不會自動產生 Ready。
- 公開前執行 allowlist projection、secret／PII scan、link review 與 post-publish smoke。
