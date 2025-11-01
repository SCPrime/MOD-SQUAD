# MOD SQUAD - Cursor IDE Setup Guide

**Quick reference for installing and configuring MOD SQUAD in Cursor.**

---

## ⚡ Quick Install (5 minutes)

### Step 1: Clone MOD SQUAD
```bash
cd ~/Documents/GitHub  # or your preferred location
git clone https://github.com/SCPrime/mod-squad.git
cd mod-squad
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Install to Your Project
```bash
# Navigate to your project
cd /path/to/your/project

# Run installer
../mod-squad/install.sh  # Linux/macOS
# OR
..\mod-squad\install.ps1  # Windows PowerShell
```

### Step 4: Verify Installation
```bash
cd /path/to/your/project
python modsquad/extensions/runner.py --help
```

---

## 🎯 Cursor-Specific Configuration

### 1. Open Your Project in Cursor

1. Launch Cursor IDE
2. File → Open Folder → Select your project directory
3. Wait for Cursor to index the project

### 2. Configure Cursor Models

MOD SQUAD works with these models (ensure they're available in Cursor):

**Required Models:**
- `deepseek-coder` (or similar code generation model)
- `claude-4.5-sonnet` (or similar reasoning model)

**Optional Models:**
- `deepseek-r1` - Architecture & validation
- `gpt-5-pro` - Executive reasoning
- `claude-4.5-haiku` - Fast summaries

**Check Available Models:**
1. Open Cursor Settings (Ctrl/Cmd + ,)
2. Navigate to "Models"
3. Verify your subscription includes required models

### 3. Set Up Environment Variables

Create `.env` file in your project root:

```env
# API Keys (if using external API providers)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# MOD SQUAD Webhook (optional)
MODSQUAD_NOTIFICATION_WEBHOOK=https://your-webhook-url.com
```

**Cursor will automatically load `.env` files.**

### 4. Configure MOD SQUAD for Your Project

Edit `modsquad/config/modsquad.yaml`:

```yaml
modsquad:
  enabled: true
  mode: non_interfering

models:
  # Update model IDs to match your Cursor model list
  your-primary-model:
    provider: cursor
    model_id: deepseek-coder:latest
    description: Your primary coding assistant
```

Edit `modsquad/config/extensions.yaml`:

```yaml
extensions:
  # Enable/disable extensions based on your needs
  concealment_validator:
    enabled: true
  secrets_watchdog:
    enabled: true
  browser_validator:
    enabled: false  # Disable if no web UI
```

---

## 🔧 Using MOD SQUAD in Cursor

### Method 1: Terminal Commands

Open Cursor's integrated terminal (Ctrl/Cmd + `) and run:

```bash
# Run all extensions
python modsquad/extensions/runner.py

# Run specific extension
python modsquad/extensions/concealment_validator.py
python modsquad/extensions/secrets_watchdog.py

# Check status
python modsquad/extensions/metrics_streamer.py
```

### Method 2: Cursor Chat Integration

Ask Cursor AI to run MOD SQUAD extensions:

```
"Run MOD SQUAD concealment validator"
"Check secrets with MOD SQUAD watchdog"
"Validate copyright headers"
```

### Method 3: Pre-Commit Hooks

Add to `.husky/pre-commit`:

```bash
#!/bin/sh
python modsquad/extensions/concealment_validator.py || exit 1
python modsquad/extensions/secrets_watchdog.py || exit 1
```

---

## 📋 Cursor Workspace Settings

### Recommended `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "python3",
  "python.terminal.activateEnvironment": true,
  "files.exclude": {
    "**/modsquad/logs/**": true
  },
  "files.watcherExclude": {
    "**/modsquad/logs/**": true
  }
}
```

### Recommended `.gitignore` additions:

```gitignore
# MOD SQUAD
modsquad/logs/
*.jsonl
```

---

## 🐛 Troubleshooting

### Issue: "Module not found: modsquad"

**Solution:**
```bash
# Ensure you're in project root
cd /path/to/your/project

# Verify modsquad directory exists
ls modsquad/

# Check Python path
python -c "import sys; print(sys.path)"
```

### Issue: "Config file not found"

**Solution:**
```bash
# Verify config files exist
ls modsquad/config/*.yaml

# Check working directory
pwd

# Run from project root
cd /path/to/your/project
python modsquad/extensions/runner.py
```

### Issue: Models not available in Cursor

**Solution:**
1. Check Cursor subscription level
2. Update `modsquad/config/modsquad.yaml` to use available models
3. Use fallback models defined in config

### Issue: Extensions fail silently

**Solution:**
```bash
# Enable verbose logging
export MODSQUAD_LOG_LEVEL=DEBUG

# Run with verbose output
python modsquad/extensions/runner.py --verbose
```

---

## ✅ Verification Checklist

After installation, verify:

- [ ] `modsquad/` directory exists in project root
- [ ] `modsquad/config/modsquad.yaml` is configured
- [ ] `modsquad/config/extensions.yaml` is configured
- [ ] Python dependencies installed (`pip list | grep yaml`)
- [ ] `modsquad/logs/run-history/` directory exists
- [ ] `.gitignore` includes `modsquad/logs/`
- [ ] Environment variables set (if needed)
- [ ] Cursor models configured
- [ ] Test run: `python modsquad/extensions/runner.py --help`

---

## 🚀 Next Steps

1. **Review Configuration:**
   - `modsquad/config/modsquad.yaml` - Core settings
   - `modsquad/config/extensions.yaml` - Extension settings
   - `modsquad/config/quality_gates.yaml` - Quality gates

2. **Run First Test:**
   ```bash
   python modsquad/extensions/concealment_validator.py
   ```

3. **Set Up Pre-Commit:**
   - Add MOD SQUAD checks to `.husky/pre-commit`
   - Test with: `git commit --dry-run`

4. **Customize for Your Project:**
   - Update model configurations
   - Enable/disable extensions
   - Configure quality gates

---

## 📚 Additional Resources

- **Main README:** [README.md](./README.md)
- **Protocol:** [modsquad/PROTOCOL.md](./modsquad/PROTOCOL.md)
- **Runbook:** [modsquad/OPERATOR_RUNBOOK.md](./modsquad/OPERATOR_RUNBOOK.md)

---

**Need Help?** Check [README.md](./README.md) for full documentation.

