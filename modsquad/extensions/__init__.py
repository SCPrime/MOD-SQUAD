"""
MOD SQUAD Framework - Extension Suite
Copyright © 2025 Dr. SC Prime. All Rights Reserved.

PROPRIETARY AND CONFIDENTIAL
Unauthorized copying, modification, or distribution is strictly prohibited.
🚨 THIS CODE IS MONITORED: Violators WILL be found.

MOD SQUAD extension suite - Universal preloaded extensions for all projects.
"""

from .utils import ExtensionConfig, load_extension_config

# Core extensions
from . import maintenance_notifier
from . import metrics_streamer
from . import secrets_watchdog
from . import strategy_verifier

# Validation extensions
from . import browser_validator
from . import contract_enforcer
from . import integration_validator
from . import concealment_validator
from . import copyright_scanner
from . import visibility_lockdown
from . import concealment_reporter

# Production extensions (if available)
try:
    from . import bundle_analyzer
except ImportError:
    bundle_analyzer = None

try:
    from . import runtime_error_monitor
except ImportError:
    runtime_error_monitor = None

try:
    from . import visual_regression_advanced
except ImportError:
    visual_regression_advanced = None

# Infrastructure & health
from . import infra_health
from . import dependency_tracker
from . import stream_coordinator

# Production extensions (optional)
try:
    from . import subprocess_manager
except ImportError:
    subprocess_manager = None

try:
    from . import circuit_breaker
except ImportError:
    circuit_breaker = None

try:
    from . import test_orchestrator
except ImportError:
    test_orchestrator = None

# Scheduling & orchestration
try:
    from . import guardrail_scheduler
except ImportError:
    guardrail_scheduler = None

try:
    from . import accessibility_scheduler
except ImportError:
    accessibility_scheduler = None

try:
    from . import data_latency_tracker
except ImportError:
    data_latency_tracker = None

# Reporting & analysis
try:
    from . import component_diff_reporter
except ImportError:
    component_diff_reporter = None

try:
    from . import security_patch_advisor
except ImportError:
    security_patch_advisor = None

try:
    from . import docs_sync
except ImportError:
    docs_sync = None

try:
    from . import review_aggregator
except ImportError:
    review_aggregator = None

try:
    from . import quality_inspector
except ImportError:
    quality_inspector = None

# Testing & simulation
try:
    from . import persona_simulator
except ImportError:
    persona_simulator = None

# SUN TZU Squad - Strategic Batch Planning
try:
    from . import elite_strategist
    from . import task_graph_analyzer
    from . import risk_profiler
    from . import batch_optimizer
    from . import intersection_mapper
except ImportError:
    elite_strategist = None
    task_graph_analyzer = None
    risk_profiler = None
    batch_optimizer = None
    intersection_mapper = None

# ARMANI Squad - Integration Weaving
try:
    from . import elite_weaver
    from . import interface_predictor
    from . import glue_code_generator
    from . import conflict_resolver
    from . import intersection_executor
except ImportError:
    elite_weaver = None
    interface_predictor = None
    glue_code_generator = None
    conflict_resolver = None
    intersection_executor = None

__all__ = [
    # Utilities
    "ExtensionConfig",
    "load_extension_config",
    # Core extensions
    "maintenance_notifier",
    "metrics_streamer",
    "secrets_watchdog",
    "strategy_verifier",
    # Validation extensions
    "browser_validator",
    "contract_enforcer",
    "integration_validator",
    "concealment_validator",
    "copyright_scanner",
    "visibility_lockdown",
    "concealment_reporter",
    # Infrastructure
    "infra_health",
    "dependency_tracker",
    "stream_coordinator",
    "runner",
    "utils",
]
