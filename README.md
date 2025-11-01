# MOD SQUAD Framework

## ⚠️ PROPRIETARY AND CONFIDENTIAL

**Copyright © 2025 Dr. SC Prime - MOD SQUAD Framework. All Rights Reserved.**

This framework contains proprietary and confidential information. Unauthorized copying, modification, or distribution is strictly prohibited and will be prosecuted to the fullest extent of the law.

🚨 **THIS CODE IS MONITORED:** We employ advanced fingerprinting and tracking systems to detect unauthorized use. Violators WILL be found.

For licensing inquiries: contact@paiid.com

---

## 🚀 Quick Start

MOD SQUAD is a multi-agent orchestration framework for AI-assisted development in Cursor. It provides automated maintenance, quality gates, extensions, and coordinated multi-model workflows.

### One-Click Installation

**Windows (PowerShell):**
```powershell
.\install.ps1
```

**Linux/macOS (Bash):**
```bash
chmod +x install.sh
./install.sh
```

**Install to specific project:**
```powershell
# Windows
.\install.ps1 -ProjectPath "C:\path\to\your\project"

# Linux/macOS
./install.sh /path/to/your/project
```

---

## 📦 Installation in Cursor

### Method 1: One-Click Install (Recommended)

1. **Clone or download this repository:**
   ```bash
   git clone https://github.com/SCPrime/mod-squad.git
   cd mod-squad
   ```

2. **Run the installer:**
   - **Windows:** Open PowerShell in Cursor terminal and run:
     ```powershell
     .\install.ps1
     ```
   - **Linux/macOS:** Run:
     ```bash
     chmod +x install.sh
     ./install.sh
     ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MOD SQUAD:**
   - Edit `modsquad/config/modsquad.yaml` to match your project
   - Customize `modsquad/config/extensions.yaml` for your needs
   - Update model configurations if needed

5. **Verify installation:**
   ```bash
   python modsquad/extensions/runner.py --help
   ```

### Method 2: Manual Installation

1. **Copy MOD SQUAD to your project:**
   ```bash
   cp -r modsquad/ /path/to/your/project/
   ```

2. **Create logs directory:**
   ```bash
   mkdir -p modsquad/logs/run-history
   ```

3. **Install dependencies:**
   ```bash
   pip install PyYAML requests
   ```

4. **Add to .gitignore:**
   ```gitignore
   # MOD SQUAD
   modsquad/logs/
   ```

---

## 🎯 Cursor Integration

### Setting Up Cursor Workspace

1. **Open your project in Cursor**

2. **Create `.cursorrules` file** (optional but recommended):
   ```markdown
   # MOD SQUAD Integration
   
   This project uses MOD SQUAD Framework for automated development workflows.
   
   - Quality gates run before commits
   - Extensions provide automated maintenance
   - Multi-agent coordination via modsquad/config/
   ```

3. **Configure Cursor Models:**
   - Ensure your Cursor subscription includes access to models configured in `modsquad/config/modsquad.yaml`
   - Models like `deepseek-coder`, `deepseek-r1`, `claude-4.5-sonnet` should be available in Cursor's model list

4. **Set Environment Variables:**
   Create a `.env` file in your project root:
   ```env
   # API Keys (if using external models)
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   
   # MOD SQUAD Notifications (optional)
   MODSQUAD_NOTIFICATION_WEBHOOK=your_webhook_url
   ```

### Using MOD SQUAD in Cursor

1. **Run Extensions Manually:**
   ```bash
   # In Cursor terminal
   python modsquad/extensions/runner.py
   ```

2. **Run Specific Extension:**
   ```bash
   python modsquad/extensions/concealment_validator.py
   python modsquad/extensions/secrets_watchdog.py
   python modsquad/extensions/browser_validator.py
   ```

3. **Check Status:**
   ```bash
   python modsquad/extensions/metrics_streamer.py
   ```

### Pre-Commit Integration

Add to `.husky/pre-commit` or `.git/hooks/pre-commit`:

```bash
#!/bin/bash
# MOD SQUAD Pre-Commit Checks

echo "🔒 Running MOD SQUAD concealment validation..."
python modsquad/extensions/concealment_validator.py
if [ $? -ne 0 ]; then
  echo "❌ Concealment validation failed!"
  exit 1
fi

echo "🔍 Running secrets scan..."
python modsquad/extensions/secrets_watchdog.py
if [ $? -ne 0 ]; then
  echo "❌ Secrets validation failed!"
  exit 1
fi

echo "✅ MOD SQUAD checks passed"
```

---

## 📋 Configuration

### Core Configuration (`modsquad/config/modsquad.yaml`)

- **Models:** Configure AI models and their capabilities
- **Budgets:** Set daily/monthly spending limits
- **Analytics:** Enable/disable logging and metrics
- **Logging:** Configure log levels and redaction

### Extensions (`modsquad/config/extensions.yaml`)

Enable/disable and configure:
- `maintenance_notifier` - Webhook notifications
- `metrics_streamer` - Metrics collection
- `secrets_watchdog` - Secret rotation tracking
- `browser_validator` - Browser testing
- `concealment_validator` - IP protection checks
- `copyright_scanner` - Copyright header validation
- And more...

### Quality Gates (`modsquad/config/quality_gates.yaml`)

Define gates that run before commits/deployments:
- Linting
- Testing
- Security scans
- Concealment checks
- API health

---

## 🔧 Usage Examples

### Run All Extensions

```bash
python modsquad/extensions/runner.py
```

### Run Specific Extension

```bash
# Browser validation
python modsquad/extensions/browser_validator.py

# Secrets check
python modsquad/extensions/secrets_watchdog.py

# Concealment validation
python modsquad/extensions/concealment_validator.py
```

### Check Metrics

```bash
# View latest metrics
cat modsquad/logs/run-history/metrics.jsonl | tail -1 | python -m json.tool
```

---

## 📁 Project Structure

```
your-project/
├── modsquad/
│   ├── config/
│   │   ├── modsquad.yaml          # Core configuration
│   │   ├── extensions.yaml        # Extension settings
│   │   ├── quality_gates.yaml     # Quality gate definitions
│   │   ├── maintenance_schedule.yaml
│   │   └── browser_guardrails.yaml
│   ├── extensions/
│   │   ├── __init__.py
│   │   ├── runner.py              # Main orchestrator
│   │   ├── utils.py               # Shared utilities
│   │   ├── concealment_validator.py
│   │   ├── secrets_watchdog.py
│   │   └── ... (other extensions)
│   ├── logs/
│   │   └── run-history/           # Extension logs (gitignored)
│   └── README.md                  # MOD SQUAD documentation
├── install.ps1                    # Windows installer
├── install.sh                     # Linux/macOS installer
└── requirements.txt               # Python dependencies
```

---

## 🛠️ Extensions Overview

### Core Extensions

- **concealment_validator** - Validates IP protection measures
- **copyright_scanner** - Scans for copyright headers
- **secrets_watchdog** - Monitors secret rotation
- **browser_validator** - Browser testing automation
- **metrics_streamer** - Metrics collection
- **maintenance_notifier** - Webhook notifications

### Quality Extensions

- **contract_enforcer** - API contract validation
- **integration_validator** - Integration testing
- **strategy_verifier** - Strategy validation
- **infra_health** - Infrastructure health checks

### Coordination Extensions

- **stream_coordinator** - Parallel execution coordination
- **dependency_tracker** - Dependency tracking

---

## 🔒 Security & Concealment

MOD SQUAD includes built-in concealment measures:

- **Concealment Validator** - Checks for LICENSE, robots.txt, copyright headers
- **Copyright Scanner** - Ensures all files have copyright notices
- **Visibility Lockdown** - Monitors repository visibility settings
- **Secrets Watchdog** - Prevents secret exposure

Run concealment checks:
```bash
python modsquad/extensions/concealment_validator.py
```

---

## 📚 Documentation

- **`modsquad/README.md`** - Framework overview
- **`modsquad/PROTOCOL.md`** - Multi-agent protocol
- **`modsquad/OPERATOR_RUNBOOK.md`** - Operator guide
- **`modsquad/EXEC_SUMMARY.md`** - Executive summary

---

## 🐛 Troubleshooting

### Installation Issues

**Problem:** `pip install` fails
```bash
# Solution: Use Python 3.8+
python --version
pip install --upgrade pip
pip install -r requirements.txt
```

**Problem:** Extensions can't find config
```bash
# Solution: Ensure you're in project root
cd /path/to/your/project
python modsquad/extensions/runner.py
```

### Cursor Integration Issues

**Problem:** Models not available in Cursor
- Check Cursor subscription level
- Verify models are enabled in Cursor settings
- Update `modsquad/config/modsquad.yaml` to use available models

**Problem:** Extensions not running
- Check Python path: `which python` or `where python`
- Verify dependencies: `pip list | grep -i yaml`
- Check config paths in `modsquad/config/modsquad.yaml`

---

## 🤝 Sharing & Distribution

This framework is designed to be shared with trusted collaborators:

1. **Clone this repository:**
   ```bash
   git clone https://github.com/SCPrime/mod-squad.git
   ```

2. **Share with collaborators:**
   - Grant repository access
   - Provide installation instructions
   - Share configuration templates

3. **Customize for your project:**
   - Update `modsquad/config/modsquad.yaml`
   - Modify `modsquad/config/extensions.yaml`
   - Add project-specific extensions

---

## 📝 License

See [LICENSE](./LICENSE) for full terms.

**Summary:** Proprietary and Confidential - All Rights Reserved

---

## 📧 Support

For licensing inquiries: contact@paiid.com

---

## 🎉 Quick Reference

```bash
# Install
./install.sh

# Run all extensions
python modsquad/extensions/runner.py

# Validate concealment
python modsquad/extensions/concealment_validator.py

# Check secrets
python modsquad/extensions/secrets_watchdog.py

# View logs
ls modsquad/logs/run-history/
```

---

**Version:** 1.0.0  
**Last Updated:** November 1, 2025  
**Status:** ✅ Production Ready

