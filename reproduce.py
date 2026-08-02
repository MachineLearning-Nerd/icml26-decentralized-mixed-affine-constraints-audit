#!/usr/bin/env python3
"""Run every accepted reproduction gate for the checked-out experiment."""

from __future__ import annotations

import json
import os
import platform
import subprocess
import time
from pathlib import Path

import numpy as np

from research.round1 import run_round1


ROOT = Path(__file__).resolve().parent
BASELINE_CONTRACT = ROOT / ".openresearch/artifacts/baseline/claim_contract.json"
RUN_COMMAND = "uv sync --frozen && uv run --frozen python reproduce.py"


def git_sha() -> str:
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()


def verify_baseline() -> dict:
    contract = json.loads(BASELINE_CONTRACT.read_text(encoding="utf-8"))
    invalid = [
        claim["id"]
        for claim in contract["claims"]
        if claim["baseline_verdict"] != "BLOCKED"
    ]
    if invalid:
        raise AssertionError(f"baseline contract improperly upgrades claims: {invalid}")
    return {"passed": True, "blocked_claims": len(contract["claims"])}


def main() -> None:
    started = time.perf_counter()
    baseline = verify_baseline()
    round1 = run_round1()
    checks = round1.pop("checks")
    failed = [name for name, passed in checks.items() if not passed]

    result = {
        "experiment": "exact_apapc_and_communication_factor_calibration",
        "git_sha": git_sha(),
        "fixed_run_command": RUN_COMMAND,
        "environment": {
            "manager": "uv",
            "python": platform.python_version(),
            "numpy": np.__version__,
            "venv": str(ROOT / ".venv"),
        },
        "compute": {
            "requested_backend": "huggingface",
            "requested_flavor": "cpu-upgrade",
            "estimated_cores": 8,
            "actual_logical_cpus": os.cpu_count(),
            "gpu_allowed": False,
        },
        "baseline_regression": baseline,
        "round1": round1,
        "checks": checks,
        "runtime_seconds": time.perf_counter() - started,
    }
    print("EVIDENCE_JSON_BEGIN")
    print(json.dumps(result, indent=2, sort_keys=True))
    print("EVIDENCE_JSON_END")
    if failed:
        raise SystemExit(f"EVAL: FAIL — round-1 checks failed: {failed}")
    print("EVAL: PASS — exact APAPC and shared-variable communication checks verified")


if __name__ == "__main__":
    main()
