# MOD SQUAD Framework - One-Click Installer (PowerShell)
# Copyright © 2025 Dr. SC Prime. All Rights Reserved.
# PROPRIETARY AND CONFIDENTIAL

param(
    [string]$ProjectPath = ".",
    [switch]$SkipDependencies = $false
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "MOD SQUAD Framework Installer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Get absolute path
$ScriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$InstallPath = Resolve-Path $ProjectPath

Write-Host "[INFO] Installing MOD SQUAD to: $InstallPath" -ForegroundColor Yellow
Write-Host ""

# Create modsquad directory in project
$ModSquadPath = Join-Path $InstallPath "modsquad"
if (-not (Test-Path $ModSquadPath)) {
    New-Item -ItemType Directory -Path $ModSquadPath -Force | Out-Null
    Write-Host "[OK] Created modsquad directory" -ForegroundColor Green
} else {
    Write-Host "[WARN] modsquad directory already exists" -ForegroundColor Yellow
}

# Copy modsquad files
Write-Host "[INFO] Copying MOD SQUAD files..." -ForegroundColor Yellow

# Copy extensions
$ExtensionsSrc = Join-Path $ScriptPath "modsquad\extensions"
$ExtensionsDst = Join-Path $ModSquadPath "extensions"
if (Test-Path $ExtensionsSrc) {
    Copy-Item -Path "$ExtensionsSrc\*" -Destination $ExtensionsDst -Recurse -Force
    Write-Host "[OK] Copied extensions" -ForegroundColor Green
}

# Copy config
$ConfigSrc = Join-Path $ScriptPath "modsquad\config"
$ConfigDst = Join-Path $ModSquadPath "config"
if (Test-Path $ConfigSrc) {
    Copy-Item -Path "$ConfigSrc\*" -Destination $ConfigDst -Recurse -Force
    Write-Host "[OK] Copied configuration files" -ForegroundColor Green
}

# Copy documentation
$DocsSrc = Join-Path $ScriptPath "modsquad\*.md"
$DocsDst = $ModSquadPath
if (Test-Path (Split-Path $DocsSrc -Parent)) {
    Copy-Item -Path $DocsSrc -Destination $DocsDst -Force -ErrorAction SilentlyContinue
    Write-Host "[OK] Copied documentation" -ForegroundColor Green
}

# Create logs directory
$LogsPath = Join-Path $ModSquadPath "logs\run-history"
if (-not (Test-Path $LogsPath)) {
    New-Item -ItemType Directory -Path $LogsPath -Force | Out-Null
    Write-Host "[OK] Created logs directory" -ForegroundColor Green
}

# Install Python dependencies
if (-not $SkipDependencies) {
    Write-Host ""
    Write-Host "[INFO] Installing Python dependencies..." -ForegroundColor Yellow
    
    $RequirementsFile = Join-Path $ScriptPath "requirements.txt"
    if (Test-Path $RequirementsFile) {
        try {
            pip install -r $RequirementsFile --quiet
            Write-Host "[OK] Python dependencies installed" -ForegroundColor Green
        } catch {
            Write-Host "[WARN] Failed to install Python dependencies: $_" -ForegroundColor Yellow
            Write-Host "[INFO] Install manually with: pip install -r requirements.txt" -ForegroundColor Yellow
        }
    }
}

# Create .gitignore entry
$GitIgnorePath = Join-Path $InstallPath ".gitignore"
$GitIgnoreEntry = "`n# MOD SQUAD`nmodsquad/logs/`n"

if (Test-Path $GitIgnorePath) {
    $Content = Get-Content $GitIgnorePath -Raw
    if ($Content -notmatch "modsquad/logs") {
        Add-Content -Path $GitIgnorePath -Value $GitIgnoreEntry
        Write-Host "[OK] Updated .gitignore" -ForegroundColor Green
    }
} else {
    Set-Content -Path $GitIgnorePath -Value $GitIgnoreEntry
    Write-Host "[OK] Created .gitignore" -ForegroundColor Green
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Installation Complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Review modsquad/config/modsquad.yaml" -ForegroundColor White
Write-Host "2. Customize modsquad/config/extensions.yaml for your project" -ForegroundColor White
Write-Host "3. Run: python modsquad/extensions/runner.py --help" -ForegroundColor White
Write-Host ""
Write-Host "Documentation: modsquad/README.md" -ForegroundColor Cyan
Write-Host ""

