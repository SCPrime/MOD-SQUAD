"""
MOD SQUAD Framework - Meta Orchestration & Development System
Copyright © 2025 Dr. SC Prime. All Rights Reserved.

PROPRIETARY AND CONFIDENTIAL
Unauthorized copying, modification, or distribution is strictly prohibited.
🚨 THIS CODE IS MONITORED: Violators WILL be found.

ELITE SPECIALTY SQUADS - Permanent Deployment Configuration

ALPHA SQUAD   - Core Infrastructure & Security (<1% risk, always active)
BRAVO SQUAD   - Quality Validation & Testing (<3% risk, on-demand)
CHARLIE SQUAD - Security & Dependency Management (<2% risk, scheduled)
DELTA SQUAD   - Change Detection & Monitoring (<1% risk, continuous)
ECHO SQUAD    - Aggregation & Reporting (<1% risk, post-execution)
FOXTROT SQUAD - Orchestration & Coordination (<2% risk, meta-coordination)
SUN TZU SQUAD - Strategic Batch Planning (<2% risk, on-demand) - The Art of Parallel Warfare
ARMANI SQUAD  - Integration Weaving (<3% risk, on-demand) - Haute Couture Code Integration

Universal preloaded work environment with 190+ modules available.
"""

try:
    from .universal_loader import (
        REGISTRY,
        UniversalModuleRegistry,
        get_registry,
        load_all,
    )
except ImportError:
    # Fallback if universal_loader not available
    REGISTRY = None
    UniversalModuleRegistry = None
    get_registry = None
    load_all = None

# Import all extensions for direct access
from . import extensions

# Import elite squads
from . import squads

# Expose registry globally
modules = REGISTRY

# Auto-activate ALPHA SQUAD (always-on services)
try:
    squads.alpha.activate()
except Exception:
    pass  # Graceful degradation if squads not available


def list_all_modules():
    """List all available modules."""
    if REGISTRY:
        return REGISTRY.list_all()
    return []


def get_module(name: str):
    """Get a specific module by name."""
    if REGISTRY:
        return REGISTRY.get(name)
    return None


def deploy_full_stack(skip_slow=False):
    """Deploy all squads for full stack validation."""
    try:
        return squads.foxtrot.orchestrate_all(skip_slow=skip_slow)
    except Exception:
        return {"status": "error", "message": "Squads not available"}


def pre_deploy_check():
    """Run pre-deployment validation (BRAVO + CHARLIE)."""
    try:
        return squads.foxtrot.pre_deploy_check()
    except Exception:
        return {"status": "error", "message": "Squads not available"}


def squad_status():
    """Get status of all squads."""
    try:
        return squads.status_all()
    except Exception:
        return {"status": "error", "message": "Squads not available"}


__version__ = "2.2.0"
__all__ = [
    "extensions",
    "modules",
    "squads",
    "REGISTRY",
    "UniversalModuleRegistry",
    "get_registry",
    "load_all",
    "list_all_modules",
    "get_module",
    "deploy_full_stack",
    "pre_deploy_check",
    "squad_status",
]

