# sanyoii.github.io

[![Tests](https://github.com/sanyoii/sanyoii.github.io/actions/workflows/tests.yml/badge.svg)](https://github.com/sanyoii/sanyoii.github.io/actions/workflows/tests.yml)

Personal site — William Lu, QA & Solutions Engineer.

Single `index.html`, no framework, no build step, no external requests.
Bilingual (EN / 繁體中文) via `data-en` / `data-zh` attributes.

Local preview: open `index.html` directly, or `python -m http.server`.

## Tests

The QA suite combines static HTML checks with Chromium browser tests for bilingual
behavior, responsive layout, privacy regressions, reduced motion, and the 404 page.
See [TESTPLAN.md](TESTPLAN.md) for the risk analysis and coverage map.

```powershell
C:/Python314/python.exe -m pip install -r tests/requirements.txt
C:/Python314/python.exe -m playwright install chromium
C:/Python314/python.exe -m pytest tests/ -v
```
