#!/usr/bin/env python3
"""Fail-closed check for the final paper-first repository surface."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CANONICAL_NAME = "MachineLearning-Nerd"
CANONICAL_EMAIL = "MachineLearning-Nerd@users.noreply.github.com"
REMOTE_MARKER = "MachineLearning-Nerd/icml26-decentralized-mixed-affine-constraints-audit"
REQUIRED_FILES = {
    "README.md",
    "STATUS.md",
    "REPORT.md",
    "CLAIM_EVIDENCE.md",
    "BRANCH_AUDIT.md",
    "SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
}
EXPECTED_BRANCHES = {
    "main",
    "research/locked-baseline",
    "research/exact-apapc",
    "research/full-mixed-apapc",
    "research/exact-gradient-sliding",
    "research/source-consistent-gradient-sliding",
    "research/faithful-learning-applications",
    "research/cumulative-publication",
    "research/materialized-report-notebook",
    "research/high-accuracy-gradient-sliding",
    "research/materialized-high-accuracy-claim3",
    "research/post-publication-status-correction",
    "release/evaluator-blind-candidate",
    "release/final-space-candidate",
    "release/final-high-accuracy-claim3",
    "release/final-main-report",
    "release/final-status-mirror",
    "release/high-accuracy-claim3-mirror",
}
FAILED_GATES = {
    "embedded.claim2_model_comparison_regenerates_exactly",
    "embedded.claim3_high_accuracy_evidence_regenerates_exactly",
    "embedded.claim3_high_accuracy_checker_matches_first_hit",
    "embedded.claim3_high_accuracy_control_regenerates_exactly",
    "materialized.materialized_figures_equal_hf_generated_payloads",
}


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def check_files() -> None:
    missing = sorted(name for name in REQUIRED_FILES if not (ROOT / name).is_file())
    if missing:
        fail(f"missing required files: {', '.join(missing)}")


def check_manifest() -> None:
    manifest = json.loads((ROOT / "EVIDENCE_MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("repository") != REMOTE_MARKER:
        fail("manifest does not use the final repository name")
    if manifest.get("overall_status") != "MIXED_RESULTS / RELEASE_REPLAY_DRIFT":
        fail("unexpected overall status")

    replay = manifest.get("current_replay", {})
    if replay.get("total_gates") != 96 or replay.get("passed_gates") != 91:
        fail("current replay result is not the recorded 91/96 audit")
    if set(replay.get("failed_gates", [])) != FAILED_GATES:
        fail("current failed-gate record changed")

    claims = {claim.get("id"): claim for claim in manifest.get("claims", [])}
    if set(claims) != {"C1", "C2", "C3", "C4", "C5"}:
        fail("manifest must contain exactly C1-C5")
    for claim in claims.values():
        for evidence in claim.get("evidence", []):
            if not (ROOT / evidence).is_file():
                fail(f"missing evidence referenced by {claim['id']}: {evidence}")


def check_branch_inventory() -> None:
    local = set(git("for-each-ref", "--format=%(refname:short)", "refs/heads").splitlines())
    remote = set(
        line
        for line in git(
            "for-each-ref", "--format=%(refname:strip=3)", "refs/remotes/origin"
        ).splitlines()
        if line and line != "HEAD"
    )
    inventory = local | remote
    if inventory != EXPECTED_BRANCHES:
        fail(f"branch inventory mismatch: {sorted(inventory)}")


def check_attribution() -> None:
    rows = git("log", "--all", "--format=%an%x09%ae%x09%cn%x09%ce").splitlines()
    expected = f"{CANONICAL_NAME}\t{CANONICAL_EMAIL}\t{CANONICAL_NAME}\t{CANONICAL_EMAIL}"
    if any(row != expected for row in rows):
        fail("reachable history contains non-canonical author or committer identity")
    if "Co-authored-by:" in git("log", "--all", "--format=%B"):
        fail("co-author trailer found")


def check_remote_and_docs() -> None:
    remote = git("remote", "get-url", "origin")
    if REMOTE_MARKER not in remote:
        fail(f"origin is not the final repository: {remote}")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "91/96" not in readme or "CLAIM_EVIDENCE.md" not in readme:
        fail("README does not expose the current status and claim ledger")
    for legacy in ("orx/", "publication/"):
        if legacy in (ROOT / "BRANCH_AUDIT.md").read_text(encoding="utf-8"):
            continue
        fail("branch audit no longer records the legacy lineage")


def main() -> None:
    check_files()
    check_manifest()
    check_branch_inventory()
    check_attribution()
    check_remote_and_docs()
    print("PASS: paper metadata, claim ledger, evidence paths, branch inventory, and attribution are consistent")


if __name__ == "__main__":
    main()
