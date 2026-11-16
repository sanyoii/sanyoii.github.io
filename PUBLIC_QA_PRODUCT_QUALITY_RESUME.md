# William Lu

> Role: Senior QA Engineer | Software Quality Assurance, Test Automation & Root-Cause Analysis

Taiwan | UTC+8 | Fully Remote · Flexible Hours (Americas, EMEA, APAC) | [sanyoii@gmail.com](mailto:sanyoii@gmail.com)

[Portfolio](https://sanyoii.github.io/) | [LinkedIn](https://www.linkedin.com/in/williamlu5405) | [GitHub](https://github.com/sanyoii) | [Download 2-Page PDF Resume](https://sanyoii.github.io/assets/William-Lu-Public-QA-Resume.pdf)

## Professional summary

Senior QA Engineer who has worked across three industries: **Enterprise Security & Data Loss Prevention (DLP) (Trend Micro, nearly 13 years in QA and sustaining engineering)**, **Semiconductor Automation (Zealogics / ASML)**, and **FinTech / Crypto Exchange (BTSE)**, plus 4 years earlier in embedded firmware. Traced customer-site issues to root cause and carried recurring patterns into regression coverage; designed an unattended normal-path test execution lifecycle within the existing TestComplete architecture; and led six remote automation engineers at ASML. Two-time recipient of Trend Micro's **internal Yearly Best SEG (Sustain Engineering Group) Engineer** recognition (2019, 2021).

## Career highlights

- **Led 6 Remote Automation Engineers @ASML:** designed the **unattended normal-path execution lifecycle** within the existing TestComplete architecture via Atlassian Bamboo.
- **-20pp Escalation Returns @Trend Micro (manager-reported):** Initiated a diagnostic guide cutting first-month SEG-to-L2 missing-info returns by **20 percentage points** (per manager-shared figures; L2 = Level 2 support).
- **3 High-Severity Financial Logic Defects @BTSE:** Reproduced, documented, and escalated across trading (Futures/Spot), referral commission, and conversion flows.
- **2× Internal Best SEG Engineer @Trend Micro:** Received Trend Micro's **internal Yearly Best SEG Engineer** recognition in **2019 & 2021**.

## Core skills

### Test Strategy & QA Leadership

Risk-based Testing, Test Specifications & Test Data Design, Test Reviews, QA Leadership, Beta Planning, Automation Feasibility Assessment, Reusable-Module Planning, Technical Handover (TOI) & Onboarding Documentation

### Functional, System & Performance Testing

Manual & Exploratory Testing, Functional & Regression Testing, Boundary / Negative / FET (Force-Error Test); RAT (Release Acceptance Test), FAST (Functional Acceptance Simple Test), TOFT (Task-Oriented Function Test); System & Compatibility Testing, Cross-browser (Chrome, Edge, Firefox), Performance, Load, Stress & Long-Running Memory-Leak Tracking (`PerfMon`)

### Automation, API, WebSocket & Data Validation

Selenium, Robot Framework, TestComplete, TMSTAF, Jenkins, Atlassian Bamboo, Python (test scripting); E2E Web API Validation, WebSocket Event Inspection, Browser DevTools, SQL (`TablePlus`), Excel Financial Reconciliation

### Root-Cause Analysis, Troubleshooting & Environments

Defect Triage, Customer-Site Issue Reproduction, Incident RCA, Hotfix Validation, Log and Dump Analysis (`WinDbg`, `ProcMon`, `Process Explorer`, `Windows Event Log`); TestRail, Jira (Filters / JQL), Confluence, GitHub, Bitbucket; VMware, VirtualBox, Hyper-V, Windows Server, Microsoft Azure

### Personal Practice (2025–Present)

Python (test scripting), `pytest`, `Playwright`, `GitHub Actions`

### Product Domains

Enterprise Endpoint Security & DLP SDK; Exchange Workflows (Wallet, Spot, Futures, Convert, Referral/Affiliate, Fees, Funding, Liquidation, KYC)

## Professional experience

### Career Break | Family Caregiving

Feb 2025–Present | Taiwan (UTC+8)

- Career break for family caregiving while maintaining hands-on QA engineering practice through personal Python, `pytest`, `Playwright`, and `GitHub Actions` verification projects for public market data and bilingual web quality.

### Nogle (BTSE) | Senior QA Engineer

Sep 2024–Nov 2024 | Taipei, Taiwan | On-site · [Full Case Study](https://sanyoii.github.io/btse-case.html)

- **End-to-End Exchange Quality:** Executed manual, exploratory, functional, boundary, negative, and regression testing across **Wallet (deposit, withdrawal, blockchain confirmation), Referral/Affiliate, Spot, Futures, Convert, maker/taker fees, funding rate calculation/settlement, liquidation/partial liquidation, and Individual/Corporate KYC** on Web workflows across **Chrome, Edge, and Firefox**, validating UI state, REST APIs, **WebSocket** events (`executionReport`, `orderUpdate`, `outboundAccountPosition`, `positionUpdate`, `Balance Update`) via Browser DevTools, `TablePlus` SQL, and spreadsheet formula models.
- **High-Severity Financial Defect Discovery:** Reproduced, documented, and escalated **three high-severity financial-logic defects** for engineering prioritization across trading (Futures/Spot), referral commission, and conversion flows.
- **Test Case Design & Onboarding Documentation:** Authored **30–50 Referral/Affiliate test cases in TestRail** (first review completed before departure) and **~20 Convert test cases and study scenarios in the internal Wiki**; used TestRail for Wallet cases and wrote newcomer onboarding study notes and defect investigation pages in the internal Wiki.

All three defects were acknowledged and escalated for priority handling, and remained open when I left.

### Zealogics / ASML | Project Leader / Senior Automation Test Engineer

May 2023–Apr 2024 | Fully Remote · [Full Case Study](https://sanyoii.github.io/asml-case.html)

- **Remote Team Leadership:** Led **six Automation Engineers** in a fully remote ASML engagement: assigned tasks, reviewed test cases and the team's code, tracked risk, schedule, and tickets, and reported team status and training needs to ASML management.
- **Unattended Test Lifecycle Design:** Architected the end-to-end test execution flow for HMI eP5 modules `iCDU`, `MM Flow`, and `ADEL`, covering Simulator startup, initialization, Recipe loading, execution, reporting, cleanup, and environment reset, within the existing TestComplete architecture and enabling **unattended normal-path execution** via `.bat` and Atlassian Bamboo triggers (while isolating connection failures for manual investigation).
- **Modular Reuse & Feasibility:** Assessed manual test cases for full vs. partial automation, planned shared modules prior to assignment to eliminate duplicate coding, authored Test System Design docs in Confluence, and delivered client technical handover (TOI) sessions and live demos.
- **Hands-on Contribution:** The six engineers wrote most of the code. I implemented a portion of the test cases as Python automation scripts within the TestComplete framework and reviewed the team's code.

### Trend Micro | Senior QA Engineer & Senior Customer Service Engineer

Jul 2014–Jan 2023 | Taipei, Taiwan | On-site · [Incident & Beta Case Study](https://sanyoii.github.io/trend-support-case.html) · [DLP Compatibility & Perf. Case Study](https://sanyoii.github.io/dlp-case.html)

- **QA & SEG Leadership:** Served as **QA Leader and SEG (Sustain Engineering Group) Leader** for the Data Loss Prevention (DLP) SDK and enterprise security products (`OfficeScan`, Worry-Free Business Security Services, InterScan Messaging Security Virtual Appliance), connecting system/performance QA with global customer-escalation RCA and hotfix validation.
- **Customer-Site Issue RCA to Regression Coverage:** Reproduced complex customer crashes/leaks across VMware, VirtualBox, Hyper-V, and Azure labs using `WinDbg`, `ProcMon`, and `Process Explorer` to trace them to root cause; validated hotfixes for target behavior and side effects; carried recurring incident patterns into regression coverage; automated regression suites (Python, Selenium, Robot Framework, TMSTAF, Jenkins).
- **Proactive Chrome Compatibility Automation:** Built Python monitoring via Google APIs (`googleapis.com`) to detect Chrome Beta and Stable releases, trigger browser updates and sensitive-file upload tests, and send email alerts when DLP failed to block an upload—catching browser breaks before customer reports.
- **Performance Optimization (Supported-Site Scanning):** Proposed **supported-site scanning**, adopted and implemented by the team during a DLP refactor; based on my recollection of the QA performance test report, **CPU and memory usage each fell by at least 10%** relative to the previous design (unlisted sites were explicitly unsupported; users could test adding sites to a configuration file and report failures to Support for team assessment).
- **Escalation Intake Standardization (-20pp Returns, manager-reported):** Initiated an issue-type-based DLP diagnostic guide; in its first month, **the share of cases SEG returned to Level 2 (L2) support for missing information fell by 20 percentage points** according to figures shared by my manager.

### Trend Micro | Senior Customer Service Engineer

Jun 2013–Jul 2014 | Taipei, Taiwan | On-site

- Served as SEG Leader and final escalation point for critical Worry-Free Business Security (WFBS) Advanced incidents across APAC, Europe, and the US; led dump/upgrade-log RCA, reconstructed customer-upgrade-path hotfix validation, and proposed the WFBS Guide Book to reduce missing-info case returns.

### Trend Micro | QA Engineer

May 2010–Jun 2013 | Taipei, Taiwan | On-site

- Owned module, system, and long-running performance testing (Python + Windows Performance Monitor) for Worry-Free Business Security Advanced (`6.0 SP1–7.0 SP1`); served as **Internal & External Beta Owner**, leading on-site production beta deployments and field diagnostics across Europe.

### Tatung | Firmware Engineer

Apr 2006–Apr 2010 | Taipei, Taiwan | On-site

- Developed and validated embedded C firmware for European/US LCD TVs (from-scratch OSD UI and A/V hardware calibration) and Java control systems for smart meters, supporting stable mass-production releases and a GE OEM engagement.

## Selected case studies

- [ASML Automation and Leadership](https://sanyoii.github.io/asml-case.html): test workflow design, leadership of six automation engineers, training, and technical handover.
- [Trend Micro Incident, Beta, and Support](https://sanyoii.github.io/trend-support-case.html): proactive Chrome regression checks, SEG intake improvement, incident RCA, and external beta work.
- [Trend Micro DLP Compatibility & Performance](dlp-case.html): proactive Chrome compatibility guard, supported-site scanning optimization, and SEG-led diagnostic guidance for L2.
- [BTSE CEX Product Quality](https://sanyoii.github.io/btse-case.html): trading, referral commission, and conversion cases, with test methods and known outcomes.

The case studies describe my direct work without confidential customer or implementation details. Original employer records are no longer available for independent verification. The DLP case-return change comes from figures shared by my manager; resource reductions come from my recollection of the QA performance report. Baseline values and original reports are unavailable.

## Selected portfolio (personal practice, 2025–Present)

- [QA Portfolio & Risk-Based QA Decision Desk](https://sanyoii.github.io/): bilingual work and employment evidence with static, runtime, responsive, and accessibility smoke checks.
- [Public repository](https://github.com/sanyoii/sanyoii.github.io): source, tests, and publication evidence.
- [CEX Market Data Quality Lab](https://github.com/sanyoii/cex-market-data-quality-lab): Python/pytest checks for REST snapshots, WebSocket sequencing, and order-book invariants. Public market data only; no accounts, orders, or funds. The repository records tested revisions and limitations.
- [How I lead QA](https://sanyoii.github.io/how-i-lead-qa.html): people, process, quality, and stakeholder practices at ASML and Trend Micro, each linked to a published case section.
- [Multi-Agent Quality Gate demo](https://sanyoii.github.io/quality-gate/): six roles review one release candidate in order across four synthetic data sets (not a real release or trading).

## Education

### MS, Information Engineering & Computer Science

Feng Chia University, Taiwan | 2003–2005

### BS, Information Engineering & Computer Science

Feng Chia University, Taiwan | 1998–2003

## Remote availability

Based in Taiwan (UTC+8). Seeking Fully Remote roles with flexible working hours; open to teams in the Americas, EMEA, and APAC. Languages: Mandarin Chinese (Native), English (Professional work and technical communication). Weekend, holiday, shift, and on-call coverage require role-level confirmation.
