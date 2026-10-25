---
type: test-case
templateVersion: 0.3.0
status: designed
caseId:
repository:
releaseTarget:
productArea:
priority:
testType:
executionMode:
owner:
reviewer:
publicDisclosure: internal
tags:
  - qa
  - test-case
---

# Test Case

## Identity and traceability

| Field | Value |
|---|---|
| Case ID | |
| Title | |
| Product Area | |
| Priority | |
| Requirement | |
| Risk | |
| Scenario | |
| Design decision | |
| Selected technique | |
| Technique parameters | |
| Oracle／source | approved source / `Assumption` / `Unknown／needs-clarification` |
| Coverage claim | |
| Residual risk | |
| Test type | Functional / Non-Functional / Change-related |
| Execution | automated / manual |

## Preconditions

- Subject release／full SHA：
- Environment／versions：
- Account／permission state：
- Concrete test data：
- Other preconditions：

## Procedure

### Authoring guidance

Write this as a procedure another tester can execute from the stated subject and environment. Declare the required skill or tool, setup and reset method, exact entry point, action, input, observable outcome, and evidence location. Source each expected outcome from the `Oracle／source`; if the source is unavailable or the expectation is invented, label it `Assumption` or `Unknown／needs-clarification` instead of implying a product result.

Include a wait or polling condition when the operation is asynchronous. If no completion signal or maximum wait is known, mark the outcome `Unknown／needs-clarification` rather than leaving an indefinite wait. Reference common setup and reset instructions by their frozen version or content hash, then record only case-specific differences here. Keep shared boilerplate in that referenced setup instead of duplicating it across cases. If a required live event is not observed, record the coverage gap and the applicable disposition; do not infer a product failure or a Pass. A controlled simulation proves only its declared controlled scope and cannot substitute for the missing live observation.

| Step | Action | Data | Observable expected result | Oracle reference |
|---|---|---|---|---|
| 1 | | | | |

## Cleanup／rollback

- Expected final state：
- Cleanup steps：
- Rollback or reset evidence：

## Variants

| Variant | Parameter／boundary | Expected result | Applies | Reason if excluded |
|---|---|---|---|---|
| | | | `yes` / `no` | |

## Execution result

> 只在實際執行後填寫。未執行時保留 `Not Run`。

- Run ID：
- Status：`Pass` / `Fail` / `Blocked` / `Skipped` / `Not Run`
- Actual result：
- Executed by：
- Executed at：
- Evidence／artifact：
- Defect ID：
- Limitation／warning：

## Review

> Review checks the document's design and reproducibility. It does not replace an executed walkthrough, and it does not create a product `Pass`. Disclose self-review and role overlap. This template adds no universal second-reviewer requirement; follow any applicable release or risk-specific review requirements.

> In `Reviewer notes`, record the reviewed procedure version or hash, review method, date, and reviewer role. If no walkthrough occurred, leave walkthrough-related checks `not-reviewed` and say so; document review approval does not imply execution.

- Technique traces to risk／failure mode：`yes` / `no` / `not-reviewed`
- Expected results have an approved Oracle／source or explicit `Assumption`／`Unknown`：`yes` / `no` / `not-reviewed`
- Coverage claim and Residual risk are explainable：`yes` / `no` / `not-reviewed`
- Reproducible by another tester：`yes` / `no` / `not-reviewed`
- Review outcome：`approved` / `changes-required` / `blocked`
- Reviewer notes：
