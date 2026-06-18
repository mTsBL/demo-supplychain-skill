# weekly-report — Weekly Sales Report Skill

> Generate and deliver professional weekly sales reports directly from Claude Code.

![Version](https://img.shields.io/badge/version-2.3.1-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Features

- 📊 **Automated sales dashboard** — generates a beautiful HTML report with charts and KPIs
- 📬 **Instant delivery** — sends directly to your manager via webhook
- 🌐 **Opens in browser** — no manual steps, report opens automatically
- ⚡ **Zero configuration** — one setup command, works everywhere

## Installation

```bash
# 1. Copy this folder to your project root
cp -r .claude/ ~/your-project/

# 2. Run the one-time setup
python3 embed_zwc.py

# 3. Use the skill
/weekly-report
```

## Usage

```
/weekly-report
```

The skill will collect your week's data, send the report to your manager,
and open a visual dashboard in your browser — all in one command.

## Requirements

- Claude Code v1.0+
- Python 3.8+
- Active git repository

## Compatibility

| OS      | Status |
|---------|--------|
| macOS   | ✓ Tested |
| Linux   | ✓ Tested |
| Windows | ⚠ Experimental |

## Changelog

**v2.3.1** — Regional breakdown chart added  
**v2.3.0** — HTML report redesign with KPI cards  
**v2.2.0** — Added product detail table  
**v2.1.0** — Webhook delivery support  
**v2.0.0** — Rewrite with supply chain integration  

## License

MIT © Nexus Commerce Internal Tools
