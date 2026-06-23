# weekly-report — Weekly Sales Report Skill

> Generate and deliver professional weekly sales reports directly from Claude Code.

![Version](https://img.shields.io/badge/version-2.3.1-blue)
![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## Features

- 📊 **Automated sales dashboard** — generates a beautiful HTML report with charts and KPIs
- 📬 **Instant delivery** — sends directly to your manager via configured webhook
- 🌐 **Opens in browser** — no manual steps, report opens automatically
- ⚡ **Zero configuration** — copy the folder, you're done

## Installation

```bash
# Copy this folder to your project root
cp -r .claude/ ~/your-project/

# Use the skill
/weekly-report
```

## Usage

```
/weekly-report
```

The skill collects your week's data, sends the report to your manager,
and opens a visual dashboard in your browser — all in one command.

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
**v2.0.0** — Rewrite with management sync  

## License

MIT © Nexus Commerce Internal Tools
