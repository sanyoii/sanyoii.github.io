# Portfolio visual verification — 2026-09-21

Local main working tree. No commit, push or deployment.

Implemented: compact homepage, experience strip, cases before employment proof, editorial case rows, immediate content visibility; bilingual dlp-case.html with monitoring flow, scanning comparison, contextual metrics, unsupported-site policy and evidence limits.

Final command: `py -3 -m pytest tests/test_static.py tests/test_runtime.py tests/test_dlp_case.py -q -p no:cacheprovider`

Result: exit 0, **25 passed in 16.08s** after font and fade corrections. Coverage includes navigation, persistent language state, details interaction, JavaScript errors and overflow at 375 / 768 / 1440 px. Installed requests dependency warning did not fail tests.

`git diff --check`: exit 0; existing LF/CRLF conversion warnings.

Fresh screenshots: visual-1440-en.png, visual-390-zh.png, dlp-1440-en.png, dlp-390-zh.png. Homepage captures regenerated after correcting old fade specificity. Visual inspection corrected initial invisible homepage content and checked desktop and mobile case layout. First screenshot server logged an aborted image connection during navigation; screenshot generation completed and homepage recapture completed without the warning.

Limits: local Chromium only; live site, deployment, real device and screen reader not verified. Career metrics are user-attested; original company reports not independently verified. Existing dirty changes preserved.
