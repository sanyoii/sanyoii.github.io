from pathlib import Path
import re
root = Path(__file__).resolve().parents[2]
files = ['PUBLIC_QA_PRODUCT_QUALITY_RESUME.md','ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md','BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md','TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md']
for f in files:
    p=root/f;s=p.read_text(encoding='utf-8')
    s=re.sub(r'^> (Status|Revision|Evidence|Privacy boundary):.*\n','',s,flags=re.M)
    s=re.sub(r'^> Public boundary:.*\n','',s,flags=re.M)
    if f!='PUBLIC_QA_PRODUCT_QUALITY_RESUME.md':
        s=s.replace('## English','> Source: Based on my direct work and recollection. Original employer records are no longer available for independent verification. Confidential details are omitted.\n\n## English',1)
    s=s.replace('user-attested memory','my recollection').replace('user-attested evidence','firsthand accounts')
    s=s.replace('Test Cases','test cases').replace('Test Case','test case')
    p.write_text(s,encoding='utf-8',newline='\n')

def update(f,pairs):
    p=root/f;s=p.read_text(encoding='utf-8')
    for a,b in pairs:
        assert a in s,(f,a)
        s=s.replace(a,b)
    p.write_text(s,encoding='utf-8',newline='\n')

update('PUBLIC_QA_PRODUCT_QUALITY_RESUME.md',[
('Initiated an issue-type-based DLP diagnostic-data collection guide.','Proposed a DLP troubleshooting guide organized by issue type, with step-by-step instructions for collecting diagnostic data.'),
('Delivered TOI and technical handover.','Provided operation training and technical handover.'),
('Led external beta deployments and expanded high-impact feature coverage through broader test cases and scope.','Led external beta deployments and expanded scan, system, and performance tests using patterns from customer incidents.'),
('automation lifecycle design, six-engineer delivery leadership, enablement evidence, and technical handoff.','test workflow design, leadership of six automation engineers, training, and technical handover.'),
('The case studies use sanitized categories and firsthand accounts. Former-employer source records are inaccessible. They do not disclose customer identities, raw internal data, proprietary implementation details, or blocked metrics. The DLP case-return change is attributed to manager-reported figures; baseline and final percentages are unavailable.','The case studies describe my direct work without confidential customer or implementation details. Original employer records are no longer available for independent verification. The DLP case-return change comes from figures shared by my manager; resource reductions come from my recollection of the QA performance report. Baseline values and original reports are unavailable.'),
('sanitized trading, referral commission, and conversion risk cases with explicit evidence limits.','trading, referral commission, and conversion cases, with test methods and known outcomes.'),
])
update('ASML_AUTOMATION_LEADERSHIP_CASE_STUDY.md',[
('I combined technical planning with visible delivery controls.','I planned the technical work and tracked progress, risks, and requests for help across teams.'),
('### Enablement and feedback','### Training and feedback'),
('I delivered TOI, live demos, operation guidance, and technical documentation to cross-functional client-side engineers. Approximately 20–30 people attended those sessions. Attendance did not prove adoption.','I provided training, live demonstrations, operating instructions, and technical documentation to client engineers across functions. Approximately 20–30 people attended.'),
('I can identify approximately 2–3 engineers who used the automation independently because they ran it after the sessions and submitted modification requests.','I can confirm that approximately 2–3 engineers ran the automation independently after training and submitted change requests. I do not know how many of the other attendees used it.'),
('\nMy leadership contribution was preparing capability evidence and coordinating the transition. ASML controlled the budget, and its Engineering leadership and HR made the final staffing decisions.\n','\n'),
('TOI participation shows reach.','Training attendance shows who took part.'),
('TOI attendance','training attendance'),
('The old setup-time, operating-cost, and coverage percentages are excluded because the source data is unavailable.','Setup-time, cost, and coverage improvements are described without percentages because the source measurements are unavailable.'),
('- Approximately 20–30 people attended TOI or demos; I can identify approximately 2–3 independent users. The remaining attendees\' usage is unknown.\n',''),
('The case comes from direct work and my recollection. Former-project records are no longer accessible.','This case is based on my direct work and recollection. Original project records are no longer accessible.'),
])
update('BTSE_CEX_PRODUCT_QUALITY_CASE_STUDY.md',[
('During my three-month role','During my three months at BTSE'),
('I kept Browser network and API inspection separate from log analysis. I did not perform direct server-log analysis at BTSE.','These checks used browser network records and API data. I did not directly inspect server logs at BTSE.'),
('return one usable error contract across UI and API layers','provide consistent, actionable error responses across the UI and API'),
('The three findings come from direct work and my recollection. Former-employer records are no longer accessible.','The three findings are based on my direct work and recollection. Original employer records are no longer accessible.'),
])
update('TREND_MICRO_INCIDENT_BETA_SUPPORT_CASE_STUDY.md',[
('Enterprise endpoint security has two quality obligations at the same time: enforce protection without interruption, and keep the customer\'s business environment usable.','Endpoint security needs to protect data while allowing customers to keep working.'),
('My responsibility was to turn incomplete symptoms into a reviewable evidence package, recover the affected environment when possible, and give Engineering a testable failure model.','I gathered diagnostic information, helped restore the affected environment where possible, and gave Engineering the evidence needed to reproduce and test the problem.'),
('### SEG intake quality and support enablement','### Case information and support training'),
('support enablement','support training'),
('According to the QA performance test report at the time, switching this site-list design alone','Based on my recollection of the QA performance test report, switching this site-list design alone'),
('if it did not work, they could open a Support case for the team to assess whether to support that site.','if it did not work, they could open a Support case for the team to assess whether to support that site. Adding a site did not guarantee protection.'),
('Raw case volumes, customer counts, unsupported support-reduction and coverage percentages, and turnaround figures remain excluded. The 20-percentage-point DLP case-return change is manager-reported and user-attested, not independently verified; it does not validate older percentage claims. The supported-site CPU and memory reductions are separately attributed to the QA performance report and a change in scanning scope.','The 20-percentage-point case-return change comes from figures shared by my manager. CPU and memory reductions come from my recollection of the QA performance report and apply to a change in scanning scope. These are separate outcomes, and neither has been independently verified.'),
])
print('Public Markdown copy and source notes updated')
