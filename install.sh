#!/bin/bash
# MOD SQUAD Framework - One-Click Installer (Bash)
# Copyright © 2025 Dr. SC Prime. All Rights Reserved.
# PROPRIETARY AND CONFIDENTIAL

set -e

PROJECT_PATH="${1:-.}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_PATH="$(cd "$PROJECT_PATH" && pwd)"

echo "========================================"
echo "MOD SQUAD Framework Installer"
echo "========================================"
echo ""

echo "[INFO] Installing MOD SQUAD to: $INSTALL_PATH"
echo ""

# Create modsquad directory in project
MODSQUAD_PATH="$INSTALL_PATH/modsquad"
if [ ! -d "$MODSQUAD_PATH" ]; then
    mkdir -p "$MODSQUAD_PATH"
    echo "[OK] Created modsquad directory"
else
    echo "[WARN] modsquad directory already exists"
fi

# Copy modsquad files
echo "[INFO] Copying MOD SQUAD files..."

# Copy extensions
EXTENSIONS_SRC="$SCRIPT_DIR/modsquad/extensions"
EXTENSIONS_DST="$MODSQUAD_PATH/extensions"
if [ -d "$EXTENSIONS_SRC" ]; then
    cp -r "$EXTENSIONS_SRC"/* "$EXTENSIONS_DST/"
    echo "[OK] Copied extensions"
fi

# Copy config
CONFIG_SRC="$SCRIPT_DIR/modsquad/config"
CONFIG_DST="$MODSQUAD_PATH/config"
if [ -d "$CONFIG_SRC" ]; then
    cp -r "$CONFIG_SRC"/* "$CONFIG_DST/"
    echo "[OK] Copied configuration files"
fi

# Copy documentation
DOCS_SRC="$SCRIPT_DIR/modsquad"
DOCS_DST="$MODSQUAD_PATH"
if [ -d "$DOCS_SRC" ]; then
    cp "$DOCS_SRC"/*.md "$DOCS_DST/" 2>/dev/null || true
    echo "[OK] Copied documentation"
fi

# Create logs directory
LOGS_PATH="$MODSQUAD_PATH/logs/run-history"
mkdir -p "$LOGS_PATH"
echo "[OK] Created logs directory"

# Install Python dependencies
if [ "$2" != "--skip-deps" ]; then
    echo ""
    echo "[INFO] Installing Python dependencies..."
    
    REQUIREMENTS_FILE="$SCRIPT_DIR/requirements.txt"
    if [ -f "$REQUIREMENTS_FILE" ]; then
        if pip install -r "$REQUIREMENTS_FILE" --quiet 2>/dev/null; then
            echo "[OK] Python dependencies installed"
        else
            echo "[WARN] Failed to install Python dependencies"
            echo "[INFO] Install manually with: pip install -r requirements.txt"
        fi
    fi
fi

# Create .gitignore entry
GITIGNORE_PATH="$INSTALL_PATH/.gitignore"
GITIGNORE_ENTRY="
# MOD SQUAD
modsquad/logs/"

if [ -f "$GITIGNORE_PATH" ]; then
    if ! grep -q "modsquad/logs" "$GITIGNORE_PATH"; then
        echo "$GITIGNORE_ENTRY" >> "$GITIGNORE_PATH"
        echo "[OK] Updated .gitignore"
    fi
else
    echo "$GITIGNORE_ENTRY" > "$GITIGNORE_PATH"
    echo "[OK] Created .gitignore"
fi

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Review modsquad/config/modsquad.yaml"
echo "2. Customize modsquad/config/extensions.yaml for your project"
echo "3. Run: python modsquad/extensions/runner.py --help"
echo ""
echo "Documentation: modsquad/README.md"
echo ""

