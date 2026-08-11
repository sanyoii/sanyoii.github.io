# Pytest Environment and Regression Test Record

## Execution metadata

| Field | Value |
|---|---|
| Record ID | TR_20260810_PYTEST_001 |
| Date / timezone | 2026-08-10 / Asia/Taipei |
| Repository | `D:\Codex\Web3` |
| Branch | `main` |
| Revision under test | `24f68e97230a4f4224be4ce3cdf25761cf6cf814` plus current uncommitted test-environment documentation changes |
| Runtime | Windows, Python 3.12.13, pytest 9.1.1, Playwright 1.58.0, Chromium headless shell 1208 |
| Final command | `.\.venv\Scripts\python.exe -m pytest tests\ -v --junitxml=test-records\2026-08-10-pytest-results.xml` |
| Final result | **Pass — 17 passed, 1 warning, exit code 0, 125.57 seconds** |
| Result artifact | `test-records\2026-08-10-pytest-results.xml` |

## Test scenarios

| Scenario ID | Title / Description | Traceability | Path | E2E intent |
|---|---|---|---|---|
| TS_ENV_001 | 驗證 Web3 portfolio 測試環境當依 pinned requirements 建置時，可獨立且可重複執行 pytest 與 Playwright | User request: install pytest and preserve repeatable test evidence; `tests/requirements.txt` | Happy Path: compatible Python and native packages install successfully. Negative Path: detect an incompatible native `greenlet` binary before running browser tests. | From clean virtual environment setup through dependency import and test collection. |
| TS_REG_001 | 驗證 Web3 portfolio 當完整 regression suite 執行時，靜態與 Chromium runtime quality gates 皆產生可追蹤結果 | `TESTPLAN.md`; automated requirements 1–12 | Happy Path: all 17 checks pass. Negative Path: browser launch is blocked or a product assertion fails, and the run remains recorded rather than omitted. | From local HTTP serving and browser launch through responsive, bilingual, privacy, structure, network, motion, and 404 checks. |

Scenarios intentionally describe business and validation paths only. Concrete inputs and actions are kept in the test cases below.

## Test types

| Test Type | Applied scope |
|---|---|
| Smoke Test | Confirm Python, pytest, Playwright, and native dependencies can load before the full run. |
| Integration Test | Validate Python, pytest fixtures, Playwright, local HTTP server, and Chromium work together. |
| System Test | Exercise the portfolio as a complete locally served website. |
| Regression Test | Re-run existing static and runtime checks after environment/documentation changes. |
| Usability Test | Automated viewport overflow, fold-budget, language-toggle, and reduced-motion checks. |
| Security / Privacy Test | Reject unexpected external requests and publication of known personal phone fragments. |

Unit, UAT, Performance/Load, and Stress tests were not executed because they are outside this run's defined scope.

## Test cases

### TC_ENV_001 — Install the pinned test environment

**Basic identification and management**

- Test Case ID: `TC_ENV_001`
- Title / Summary: Verify that the repository-local Python environment installs pinned pytest and Playwright dependencies.
- Module / Component: Test infrastructure / Python virtual environment
- Priority: High
- Test Type: Smoke Test

**Environment and pre-conditions**

- Pre-conditions: Repository is available at `D:\Codex\Web3`; Python 3.12.13 can create `.venv`; `tests\requirements.txt` exists.
- Test Data: `pytest==9.1.1`, `playwright==1.58.0`.

**Test steps**

1. Create `.venv` with Python 3.12.13.
2. Run `.\.venv\Scripts\python.exe -m pip install --requirement tests\requirements.txt`.
3. Run `.\.venv\Scripts\python.exe -m pytest --version`.
4. Import Playwright and verify the active Python executable.

**Result criteria**

- Expected Result: Installation exits with code 0; pytest reports 9.1.1; Playwright imports from `.venv`.
- Actual Result: Installation exited 0; pytest reported 9.1.1; Playwright import succeeded under Python 3.12.13.
- Status / Result: Pass

**Traceability and follow-up**

- Requirements Traceability: `TS_ENV_001`; user request dated 2026-08-10.
- Post-conditions / Attachments: `.venv` remains repository-local and is excluded by `.gitignore`; pinned inputs remain in `tests\requirements.txt`.

### TC_ENV_002 — Detect and repair an incompatible native dependency

**Basic identification and management**

- Test Case ID: `TC_ENV_002`
- Title / Summary: Verify that test collection exposes a Python ABI mismatch and succeeds after reinstalling the matching native package.
- Module / Component: Test infrastructure / Playwright dependency chain
- Priority: High
- Test Type: Smoke Test, Integration Test

**Environment and pre-conditions**

- Pre-conditions: `.venv` exists and dependencies were installed.
- Test Data: Initial file `_greenlet.cp314-win_amd64.pyd`; active runtime Python 3.12.13; corrected package `greenlet==3.5.4` for CPython 3.12.

**Test steps**

1. Run `.\.venv\Scripts\python.exe -m pytest tests\ -v`.
2. Capture the collection error and inspect the installed native binary tag.
3. Reinstall with `.\.venv\Scripts\python.exe -m pip install --force-reinstall --no-cache-dir greenlet==3.5.4`.
4. Verify that `_greenlet.cp312-win_amd64.pyd` loads and Playwright imports.
5. Re-run test collection as part of the full suite.

**Result criteria**

- Expected Result: ABI mismatch is visible; compatible binary is installed; subsequent collection finds all 17 tests.
- Actual Result: First run failed with `ModuleNotFoundError: No module named 'greenlet._greenlet'`. The CPython 3.14 binary was replaced by `_greenlet.cp312-win_amd64.pyd`; Playwright then imported and 17 tests collected.
- Status / Result: Pass after environment correction; initial failure retained in this record.

**Traceability and follow-up**

- Requirements Traceability: `TS_ENV_001`.
- Post-conditions / Attachments: Compatible native dependency remains inside `.venv`; no application source was changed to hide the failure.

### TC_RUN_001 — Execute the full suite inside the restricted sandbox

**Basic identification and management**

- Test Case ID: `TC_RUN_001`
- Title / Summary: Verify that restricted execution records browser-launch limitations without misreporting a product failure.
- Module / Component: Test runner / sandbox boundary
- Priority: High
- Test Type: Regression Test, System Test

**Environment and pre-conditions**

- Pre-conditions: All 17 tests collect; Chromium headless shell exists.
- Test Data: `tests\test_static.py`, `tests\test_runtime.py`; Chromium executable under the user Playwright cache.

**Test steps**

1. Run `.\.venv\Scripts\python.exe -m pytest tests\ -v` in the restricted sandbox.
2. Record the static-test results.
3. Record the browser fixture setup errors and their shared cause.

**Result criteria**

- Expected Result: Static tests run; any sandbox restriction is explicitly classified and preserved.
- Actual Result: 4 static tests passed; 13 runtime tests errored during fixture setup with `BrowserType.launch: spawn EPERM`.
- Status / Result: Blocked for runtime coverage; static subset Pass.

**Traceability and follow-up**

- Requirements Traceability: `TS_REG_001`.
- Post-conditions / Attachments: The restriction was resolved by rerunning the identical suite outside the sandbox in `TC_RUN_002`; no failed evidence was deleted.

### TC_RUN_002 — Execute the complete regression suite with browser permission

**Basic identification and management**

- Test Case ID: `TC_RUN_002`
- Title / Summary: Verify that the complete static and Chromium runtime regression suite passes and produces machine-readable evidence.
- Module / Component: Portfolio / automated QA suite
- Priority: High
- Test Type: Integration Test, System Test, Regression Test, Usability Test, Security / Privacy Test

**Environment and pre-conditions**

- Pre-conditions: `TC_ENV_001` and `TC_ENV_002` pass; Playwright Chromium can launch outside the restricted sandbox.
- Test Data: 17 parametrized and standalone checks defined under `tests\`; viewports 375, 768, 1440, 1366x768, 1440x900, 390x844, and 375x812.

**Test steps**

1. Run `.\.venv\Scripts\python.exe -m pytest tests\ -v --junitxml=test-records\2026-08-10-pytest-results.xml` with browser-launch permission.
2. Wait for browser teardown and the final pytest exit code.
3. Confirm the JUnit XML artifact exists and contains the complete run.
4. Record every warning and the final totals.

**Result criteria**

- Expected Result: All 17 tests pass, exit code is 0, and JUnit XML is generated.
- Actual Result: 17 passed, exit code 0, duration 125.57 seconds. One `PytestCacheWarning` reported that `.pytest_cache` could not be created due to Windows access denial; it did not affect the tests or JUnit result.
- Status / Result: Pass

**Traceability and follow-up**

- Requirements Traceability: `TS_REG_001`; `TESTPLAN.md` automated requirements 1–12.
- Post-conditions / Attachments: `test-records\2026-08-10-pytest-results.xml`. Cache warning remains disclosed and may reduce incremental-run caching only.

## Execution chronology

1. Initial collection: Fail — incompatible CPython 3.14 `greenlet` native binary in the Python 3.12 environment.
2. Dependency correction: Pass — compatible CPython 3.12 binary installed and Playwright imported.
3. Restricted full run: Blocked — 4 passed, 13 browser fixture errors caused by sandbox `spawn EPERM`.
4. Permitted full run: Pass — 17 passed, 1 cache warning, exit code 0; JUnit evidence generated.

No failed or blocked run has been replaced by the successful result; each is retained above for reproducibility and diagnosis.
