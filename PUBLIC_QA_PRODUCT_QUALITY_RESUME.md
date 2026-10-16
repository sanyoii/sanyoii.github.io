# William Lu

> Role: Senior QA Engineer | Software Quality Assurance, Test Automation & Root-Cause Analysis

Taiwan | UTC+8 | Open to Fully Remote | [sanyoii@gmail.com](mailto:sanyoii@gmail.com)

[Portfolio](https://sanyoii.github.io/) | [LinkedIn](https://www.linkedin.com/in/williamlu5405) | [GitHub](https://github.com/sanyoii) | [Download 2-Page PDF Resume](https://sanyoii.github.io/assets/William-Lu-Public-QA-Resume.pdf)

## Professional summary

Senior QA Engineer and QA/Support Leader with **12+ years in software quality assurance and escalation engineering** (plus 4 years in embedded firmware) across **Enterprise Security & DLP (Trend Micro)**, **Semiconductor Automation (Zealogics / ASML)**, and **FinTech / Crypto Exchange (BTSE)**. Proven track record of catching high-severity financial logic defects before release, leading remote automation teams, designing unattended CI test lifecycles, and resolving complex customer production incidents through deep root-cause analysis (RCA). Two-time **Yearly Best SEG Engineer (2019, 2021)**.

## Career highlights

- **12+ Yrs QA · 2× Best SEG Engineer:** 12+ years in QA & escalation leadership (+4 yrs firmware); named Trend Micro Yearly Best SEG Engineer in **2019 & 2021**.
- **3 High-Severity Financial Logic Bugs @BTSE:** Escalated before release across Futures margin/price-band checks, Spot fee calculations, and Convert pricing, alongside **50+ structured TestRail cases**.
- **Led 6 Remote Automation Engineers @ASML:** Directed HMI eP5 automation delivery (`iCDU`, `MM Flow`, `ADEL`) and built **unattended TestComplete + Bamboo CI** execution.
- **-10% CPU/RAM & -20pp Escalation Returns @Trend Micro:** Proposed DLP supported-site scanning (**≥10% CPU/RAM reduction**) and authored a diagnostic guide cutting L2 missing-evidence returns by **20 percentage points**.

## Core skills

### Test Strategy & QA Leadership

Risk-based Testing, Test Specifications & Test Data Design, Test Reviews, QA Leadership, Beta Planning, Automation Feasibility Assessment, Reusable-Module Planning, Release Sign-off & Shift Handover

### Functional, System & Performance Testing

Manual & Exploratory Testing, Functional & Regression Testing, Boundary / Negative / FET (Force-Error Test); RAT (Release Acceptance Test), FAST (Functional Acceptance Simple Test), TOFT (Task-Oriented Function Test); System & Compatibility Testing, Cross-browser (Chrome, Edge, Firefox), Performance, Load, Stress & Long-Running Memory-Leak Tracking (`PerfMon`)

### Automation, API, WebSocket & Data Validation

Python, Selenium, Robot Framework, TMSTAF, TestComplete, Jenkins, Atlassian Bamboo; E2E Web API Validation, WebSocket Event Inspection, Browser DevTools, SQL (`TablePlus`), Excel Financial Reconciliation

### Troubleshooting, RCA & Environments

Defect Triage, Customer Escalation Reproduction, Incident RCA, Hotfix Validation, Log and Dump Analysis (`WinDbg`, `ProcMon`, `Process Explorer`, `Windows Event Log`); TestRail, Jira (Filters / JQL), Confluence, GitHub, Bitbucket; VMware, VirtualBox, Hyper-V, Windows Server, Microsoft Azure

### 2025–Present Practice & Product Domains

Python, `pytest`, `Playwright`, `GitHub Actions`; Enterprise Endpoint Security & DLP SDK; Exchange Workflows (Wallet, Spot, Futures, Convert, Referral/Affiliate, Fees, Funding, Liquidation, KYC)

## Professional experience

### Independent QA Engineering & Family Caregiving

Feb 2025–Present | Taiwan (UTC+8)

- Family caregiving career break while maintaining active QA engineering practice through public Python, `pytest`, `Playwright`, and `GitHub Actions` verification suites for real-time market data and bilingual web quality.

### Nogle (BTSE) | Senior QA Engineer

Sep 2024–Nov 2024 | Taipei, Taiwan | On-site · [Full Case Study](https://github.com/sanyoii/sanyoii.github.io/blob/main/BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md)

- **End-to-End Exchange Quality:** Owned functional, financial-logic, and regression verification across **Wallet, Spot, Futures, Convert, and Referral/Affiliate** workflows on Web and mobile apps, validating UI state, REST APIs, and **WebSocket** events (`order book`, `ticker`, `trade history`, `liquidation`, `position updates`, `ADL`) via Browser DevTools, `TablePlus` SQL, and independent Excel models.
- **High-Severity Financial Defect Discovery:** Identified and escalated **three high-severity financial-logic defects** prior to production release:
  1. *Futures Sub-Account Isolation:* Main-account balance was erroneously counted during sub-account margin checks, enabling unbacked leverage exposure.
  2. *Futures Price-Band Bypass & Referral Tier Boundary:* Post-placement order price edits bypassed the ±2% mark-price protection check, and boundary checks uncovered a referral rebate tier miscalculation (`> 10,000 USDT` vs. `>= 10,000 USDT`).
  3. *Convert Quote & Fee Regression:* Identified an inverted base/quote conversion rate and split-order fee-waiver state loss through DevTools payload inspection and Excel verification.
- **Test Asset & Handover Standardization:** Authored **50+ structured TestRail cases** across happy, boundary, negative, and permission paths; built an environment matrix (`dev` / `staging` / `pre-prod`), test-account inventory, and cross-shift handover checklist.

### Zealogics / ASML | Project Leader / Senior Automation Test Engineer

May 2023–Apr 2024 | Fully Remote · [Full Case Study](https://github.com/sanyoii/sanyoii.github.io/blob/main/ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md)

- **Remote Team & Delivery Leadership:** Led **six Automation Engineers** in a fully remote ASML engagement covering HMI eP5 modules (`iCDU`, `MM Flow`, `ADEL`), managing weekly progress via custom Jira Filters/JQL, code/test reviews, annual performance evaluations, and client TOI/live demos.
- **Unattended CI Lifecycle Design:** Architected the end-to-end test execution flow (Simulator startup, initialization, Recipe loading, execution, reporting, cleanup, and environment reset) within the existing TestComplete architecture—enabling **unattended normal-path execution** via `.bat` and Atlassian Bamboo triggers (while isolating connection failures for manual investigation).
- **Modular Reuse & Feasibility:** Assessed manual test cases for full vs. partial automation, planned shared modules prior to assignment to eliminate duplicate coding, authored Test System Design docs in Confluence, and contributed direct test implementation alongside the team.

### Trend Micro | Senior QA Engineer & Senior Customer Service Engineer

Jul 2014–Jan 2023 | Taipei, Taiwan | On-site · [Incident & Beta Case Study](https://github.com/sanyoii/sanyoii.github.io/blob/main/TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md) · [DLP Compatibility & Perf. Case Study](https://sanyoii.github.io/dlp-case.html)

- **QA & SEG Leadership:** Served as **QA Leader and Service Engineer Group (SEG) Leader** for the Data Loss Prevention (DLP) SDK and enterprise security products (`OfficeScan`, `WFBS-SVC`, `IMSVA`), bridging system/performance QA with global customer-escalation RCA and hotfix validation.
- **Proactive Chrome Compatibility Automation:** Built Python monitoring via Google APIs (`googleapis.com`) to detect Chrome Beta and Stable releases, trigger browser updates and sensitive-file upload tests, and send email alerts when DLP failed to block an upload—catching browser breaks before customer reports.
- **Performance Optimization (-10% CPU/RAM):** Proposed **supported-site scanning**, adopted and implemented by the team during a DLP refactor; based on my recollection of the QA performance test report, **CPU and memory usage each fell by at least 10%** relative to the previous design.
- **Support Diagnostic Standardization (-20pp Returns):** Initiated an issue-type-based DLP diagnostic guide; in its first month, **the share of cases SEG returned to L2 for missing information fell by 20 percentage points** according to figures shared by my manager.
- **Deep Escalation RCA & Recognition:** Automated regression suites (Python, Selenium, Robot Framework, TMSTAF, Jenkins) and reproduced complex customer crashes/leaks across VMware, VirtualBox, Hyper-V, and Azure labs using `WinDbg`, `ProcMon`, and `Process Explorer`; named **Yearly Best SEG Engineer in 2019 and 2021**.

### Trend Micro | Senior Customer Service Engineer

Jun 2013–Jul 2014 | Taipei, Taiwan | On-site

- Served as SEG Leader and final escalation point for critical WFBS Advanced incidents across APAC, Europe, and the US; led dump/upgrade-log RCA, reconstructed customer-upgrade-path hotfix validation, and proposed the WFBS Guide Book to reduce missing-info case returns.

### Trend Micro | QA Engineer

May 2010–Jun 2013 | Taipei, Taiwan | On-site

- Owned module, system, and long-running performance testing (Python + Windows Performance Monitor) for Worry-Free Business Security Advanced (`6.0 SP1–7.0 SP1`); served as **Internal & External Beta Owner**, leading on-site production beta deployments and field diagnostics across Europe.

### Tatung | Firmware Engineer

Apr 2006–Apr 2010 | Taipei, Taiwan | On-site

- Developed and validated embedded C firmware for European/US LCD TVs (from-scratch OSD UI and A/V hardware calibration) and Java control systems for smart meters, supporting stable mass-production releases and a GE OEM engagement.

## Selected case studies

- [BTSE CEX Product Quality](https://github.com/sanyoii/sanyoii.github.io/blob/main/BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md): trading, referral commission, and conversion cases, with test methods and known outcomes.
- [Trend Micro Incident, Beta, and Support](https://github.com/sanyoii/sanyoii.github.io/blob/main/TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md): proactive Chrome regression checks, SEG intake improvement, incident RCA, and external beta work.
- [Trend Micro DLP Compatibility & Performance](https://sanyoii.github.io/dlp-case.html): proactive Chrome compatibility guard, supported-site scanning optimization, and L2 diagnostic guide rollout.
- [ASML Automation and Leadership](https://github.com/sanyoii/sanyoii.github.io/blob/main/ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md): test workflow design, leadership of six automation engineers, training, and technical handover.

The case studies describe my direct work without confidential customer or implementation details. Original employer records are no longer available for independent verification. The DLP case-return change comes from figures shared by my manager; resource reductions come from my recollection of the QA performance report. Baseline values and original reports are unavailable.

## Selected portfolio

- [QA Portfolio & Risk-Based QA Decision Desk](https://sanyoii.github.io/): bilingual work and employment evidence with static, runtime, responsive, and accessibility smoke checks.
- [Public repository](https://github.com/sanyoii/sanyoii.github.io): source, tests, and publication evidence.
- [CEX Market Data Quality Lab](https://github.com/sanyoii/cex-market-data-quality-lab): Python/pytest checks for REST snapshots, WebSocket sequencing, and order-book invariants. Public market data only; no accounts, orders, or funds. The repository records tested revisions and limitations.

## Education

### MS, Information Engineering & Computer Science

Feng Chia University, Taiwan | 2003–2005

### BS, Information Engineering & Computer Science

Feng Chia University, Taiwan | 1998–2003

## Remote availability

Based in Taiwan (UTC+8). Seeking Fully Remote roles with at least four hours of European business-hour overlap (`09:00–24:00` Taiwan time) and up to 25% travel. Languages: Mandarin Chinese (Native), English (Professional working proficiency). Weekend, holiday, shift, and on-call coverage require role-level confirmation.
