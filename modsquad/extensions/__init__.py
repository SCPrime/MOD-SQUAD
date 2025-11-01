"""MOD SQUAD extension suite - Universal preloaded extensions for all projects."""

# Core extensions (pre-existing)
# Validation extensions
# Infrastructure & health
# Scheduling & orchestration
# Reporting & analysis
# Testing & simulation
# Coordination
# SUN TZU Squad - Strategic Batch Planning
# ARMANI Squad - Integration Weaving
from . import (
    accessibility_scheduler,
    batch_optimizer,
    browser_validator,
    bundle_analyzer,
    circuit_breaker,
    component_diff_reporter,
    conflict_resolver,
    contract_enforcer,
    data_latency_tracker,
    dependency_tracker,
    docs_sync,
    elite_strategist,
    elite_weaver,
    glue_code_generator,
    guardrail_scheduler,
    infra_health,
    integration_validator,
    interface_predictor,
    intersection_executor,
    intersection_mapper,
    maintenance_notifier,
    metrics_streamer,
    persona_simulator,
    quality_inspector,
    review_aggregator,
    risk_profiler,
    runtime_error_monitor,
    secrets_watchdog,
    security_patch_advisor,
    strategy_verifier,
    stream_coordinator,
    subprocess_manager,
    task_graph_analyzer,
    test_orchestrator,
    visual_regression_advanced,
)
from .utils import ExtensionConfig, load_extension_config

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
    "bundle_analyzer",
    "runtime_error_monitor",
    "visual_regression_advanced",
    # Infrastructure & health
    "infra_health",
    "dependency_tracker",
    "subprocess_manager",
    "circuit_breaker",
    "test_orchestrator",
    # Scheduling & orchestration
    "guardrail_scheduler",
    "accessibility_scheduler",
    "data_latency_tracker",
    # Reporting & analysis
    "component_diff_reporter",
    "security_patch_advisor",
    "docs_sync",
    "review_aggregator",
    "quality_inspector",
    # Testing & simulation
    "persona_simulator",
    # Coordination
    "stream_coordinator",
    # SUN TZU Squad - Strategic Batch Planning
    "elite_strategist",
    "task_graph_analyzer",
    "risk_profiler",
    "batch_optimizer",
    "intersection_mapper",
    # ARMANI Squad - Integration Weaving
    "elite_weaver",
    "interface_predictor",
    "glue_code_generator",
    "conflict_resolver",
    "intersection_executor",
]
