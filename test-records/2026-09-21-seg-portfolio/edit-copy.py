from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]

def replace_pairs(filename, pairs):
    p = ROOT / filename
    s = p.read_text(encoding='utf-8')
    for old, new in pairs:
        assert old in s, (filename, old)
        s = s.replace(old, new)
    p.write_text(s, encoding='utf-8', newline='\n')

replace_pairs('index.html', [
('My work sits at the intersection of product risk, technical investigation, and operational response—from crypto exchange logic to enterprise security incidents.', 'My experience spans crypto exchange testing, security incident investigation, and test automation.'),
('我的工作涵蓋產品風險、技術調查與事故處理，從加密交易所的計算邏輯到企業資安事件都有。','我的經驗涵蓋加密貨幣交易所測試、資安事件調查與測試自動化。'),
('從環境設定到無人值守測試','從環境設定到自動執行測試'),
('让正常路徑能無人值守執行'.replace('让','讓'),'讓正常流程不需全程人工操作'),
('依優先序、複雜度與負載分派工作','依優先序、複雜度與成員手上的工作量分派案件'),
('I built Python release monitoring, proposed supported-site scanning, and improved L2 diagnostic guidance. Read the decisions, measured outcomes, and support boundaries together.','I wrote a Python release monitor, proposed scanning based on a supported-site list, and improved the diagnostic guide used by L2 support.'),
('我撰寫 Python 版本監測、提出支援網站掃描範圍設計，並改善 L2 診斷指南。案例一起呈現決策、量測成果與支援範圍。','我撰寫 Python 版本監測程式、提出依支援網站清單掃描的設計，並改善 L2 技術支援使用的診斷指南。'),
('I led six automation engineers, designed the TestComplete test lifecycle and reusable modules, and supported training and technical handoff. The case separates my leadership and design work from the team\'s implementation.','I led six automation engineers, designed the test workflow and reusable modules within the existing TestComplete architecture, and provided training and technical handover. The team wrote most of the code.'),
('我帶領 6 位自動化測試工程師，設計 TestComplete 測試生命週期與共用模組，並協助培訓及技術交接。案例分開說明我的帶領、設計工作與團隊的程式實作。','我帶領 6 位自動化測試工程師，在既有 TestComplete 架構中設計測試流程與共用模組，並提供操作訓練與技術交接。多數程式由團隊完成。'),
('Low-tech, evidence-first testing dashboard','A dashboard for reviewing test results and evidence'),
('低維護、以證據為主的測試 Dashboard','集中查看測試結果與證據的儀表板'),
('A green test run means little without a release, scope, and evidence trail.','A passing result needs a tested version, a clear scope, and supporting evidence.'),
('測試顯示 PASS，如果沒有對應的版本、測試範圍與證據紀錄，幾天後就很難再相信這個結果。','測試通過的結果，需要對應的版本、明確的測試範圍與佐證資料。'),
('Most personality readings are a voice memo or a flat PDF you forget by the next day.','A personal project that presents Human Design readings as a visual report.'),
('一般的命理解讀不是一段錄音就是一頁 PDF，看完隔天就忘了。','這是我的人類圖報告專案，以視覺化版面呈現解讀。'),
('Takes a birth time, runs the chart calculation, and generates a 13-section visual report that leads with plain language. The jargon is folded away, so someone who knows nothing about the system can still finish it.','Uses birth details to calculate a chart and generate a 13-section visual report. Each section starts with a plain-language explanation, with terminology available in expandable sections.'),
('輸入出生資料就自動排盤，產出 13 個章節的視覺化報告。每一段都先講白話，術語收在摺疊區，完全沒碰過這套系統的人也讀得完。','輸入出生資料後自動排盤，產出 13 個章節的視覺化報告。每段先用白話說明，讀者可展開查看術語解釋。'),
('The slow part of job hunting isn\'t writing the resume. It\'s re-cutting it for every single posting.','I use this project to compare job requirements with resume content and prepare tailored drafts.'),
('投履歷最花時間的不是寫履歷，是把同一份履歷改成每個職缺想看的樣子。','我用這個專案比對職缺要求與履歷內容，準備對應職缺的草稿。'),
('Parses job postings, matches them against the resume, and exports ATS-safe PDFs. Guardrails cap how many keywords it may infer, so it cannot quietly fabricate experience.','Parses job postings, compares them with a resume, and exports PDFs. It includes ATS compatibility checks and limits on inferred keywords. Generated content still needs review.'),
('解析職缺內容、跟履歷比對，再匯出 ATS 讀得懂的 PDF。關鍵字推導設了上限、解析也加了防呆，避免它自己編出你沒有的經歷。','解析職缺、比對履歷，再匯出 PDF。功能包含 ATS 相容性檢查與關鍵字推導上限；產生的內容仍需人工核對。'),
('檢查公開市場資料的 snapshot 與更新','檢查公開市場資料的快照與更新'),
('可執行測試與版本結果','可執行的測試與各版本的結果'),
('Building a Web3 product where correctness, trust, and money meet? Tell me what must not fail.','Hiring for a Web3 QA role? Contact me to discuss your product and testing needs.'),
('你的 Web3 產品同時牽涉正確性、信任和資金嗎？告訴我哪些地方絕對不能出錯。','正在招募 Web3 QA 嗎？歡迎聯絡我，討論產品與測試需求。'),
])
p=ROOT/'index.html';s=p.read_text(encoding='utf-8');s,n=re.subn(r'\s*<p data-en="Designed, written, tested, and shipped as one dependency-free file\.".*?</p>', '', s, flags=re.S);assert n==1;p.write_text(s,encoding='utf-8',newline='\n')
replace_pairs('404.html', [('The address may have changed, or it never was.','The page may have moved, or the address may be incorrect.'),('找不到這個頁面。網址可能已經變更，也可能從來沒有這一頁。','找不到這個頁面。頁面可能已移動，或網址輸入有誤。')])
replace_pairs('dlp-case.html', [
('接入瀏覽器更新','串接至瀏覽器更新'),
('Relative reductions from switching this design alone, according to the QA performance report at the time, recalled by the author. Not a combined result for the whole refactor.','These relative reductions came from switching the site-list design alone, based on my recollection of the QA performance report. The original report is unavailable; the figures do not represent the whole refactor.'),
('依本人回憶的當時 QA 效能報告，單獨切換此設計的相對降幅；不是整體重構的合併結果。','數據依我對當時 QA 效能報告的回憶整理，指單獨切換網站清單設計的相對降幅，不是整體重構的合併結果。目前無法提供原始報告。'),
('改善升級案件的進件品質','改善轉交 SEG 的案件資料完整度'),
('Improve escalation intake','Improve the information in escalated cases'),
('若無效，向 Support 開 case','若無效，向技術支援團隊回報'),
('完整案件依優先序、複雜度與負載分派','完整案件依優先序、複雜度與成員手上的工作量分派'),
('The performance result belongs to a narrower scanning scope.','These resource savings came with a narrower default scanning scope.'),
('效能結果伴隨掃描範圍縮小','降低資源消耗的同時，預設掃描範圍也縮小了'),
('所有網站覆蓋不變','所有網站的防護範圍不變'),
('workload 細節','測試負載細節'),
('These are direct-work accounts recalled by the author. Original reports and proprietary artifacts are not available for independent verification.','These cases describe my own work. I no longer have access to the original reports or internal records for independent verification.'),
('案例來自本人直接參與及回憶確認，原始報告與專有資料未能提供獨立核實。','這些案例來自我直接參與的工作。目前已無法取得原始報告與內部紀錄供獨立核實。'),
('I wrote the Python monitor and proposed the site-list design; team adoption and implementation are not claimed as my sole work. Monitoring savings were qualitative. The guide\'s 20-percentage-point result is separate from performance testing.','I wrote the Python monitor and proposed the site-list design, which the team implemented. Time saved through monitoring was not measured. The guide\'s 20-percentage-point result is separate from the performance tests.'),
('我撰寫 Python 監測程式並提出網站清單設計；團隊採用與實作不歸為我獨力完成。監測效益維持定性描述，指南的 20 個百分點與效能測試是不同成果。','我撰寫 Python 監測程式並提出網站清單設計，設計由團隊實作。監測節省的時間未經量測；指南的 20 個百分點與效能測試是不同成果。'),
('Memory：降低至少 10%','記憶體：降低至少 10%'),
])
print('HTML copy updated')
