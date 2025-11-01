"""
MOD SQUAD Framework - Elite Specialty Squads
Copyright © 2025 Dr. SC Prime. All Rights Reserved.

PROPRIETARY AND CONFIDENTIAL
Unauthorized copying, modification, or distribution is strictly prohibited.
🚨 THIS CODE IS MONITORED: Violators WILL be found.

MOD SQUAD Elite Specialty Squads
Permanent deployment configuration for all environments
"""

try:
    from . import alpha, bravo, charlie, delta, echo, foxtrot, sun_tzu, armani

    # Auto-activate ALPHA SQUAD on import (always-on services)
    try:
        alpha.activate()
    except Exception:
        pass
except ImportError:
    # Graceful degradation if squads not available
    alpha = None
    bravo = None
    charlie = None
    delta = None
    echo = None
    foxtrot = None
    sun_tzu = None
    armani = None


def status_all():
    """Get status of all squads."""
    try:
        if foxtrot:
            return {
                "alpha": alpha.status() if alpha else {"status": "unavailable"},
                "bravo": bravo.status() if bravo else {"status": "unavailable"},
                "charlie": charlie.status() if charlie else {"status": "unavailable"},
                "delta": delta.status() if delta else {"status": "unavailable"},
                "echo": echo.status() if echo else {"status": "unavailable"},
                "foxtrot": foxtrot.status() if foxtrot else {"status": "unavailable"},
                "sun_tzu": sun_tzu.status() if sun_tzu else {"status": "unavailable"},
                "armani": armani.status() if armani else {"status": "unavailable"},
            }
    except Exception:
        pass
    return {"status": "error", "message": "Squads not available"}


def deploy_all(skip_slow=False):
    """Deploy all squads in optimal order."""
    try:
        if foxtrot:
            return foxtrot.orchestrate_all(skip_slow=skip_slow)
    except Exception:
        pass
    return {"status": "error", "message": "Squads not available"}


__all__ = [
    "alpha",
    "bravo",
    "charlie",
    "delta",
    "echo",
    "foxtrot",
    "sun_tzu",
    "armani",
    "status_all",
    "deploy_all",
]
