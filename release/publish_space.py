#!/usr/bin/env python3
"""Publish the audited text-only allowlist to the one authorized Space."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "release/UPLOAD_ALLOWLIST.json"
HASHES = ROOT / "release/UPLOAD_SHA256SUMS.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_and_verify() -> tuple[dict, list[dict]]:
    spec = json.loads(ALLOWLIST.read_text(encoding="utf-8"))
    expected = {}
    for line in HASHES.read_text(encoding="utf-8").splitlines():
        if line and not line.startswith("#"):
            digest, target = line.split("  ", 1)
            expected[target] = digest
    files = spec["files"]
    targets = [item["target"] for item in files]
    if len(targets) != len(set(targets)):
        raise SystemExit("duplicate upload target")
    for item in files:
        source = ROOT / item["source"]
        payload = source.read_bytes()
        payload.decode("utf-8")
        if b"\x00" in payload:
            raise SystemExit(f"non-text payload: {item['source']}")
        if item["target"] != "current/release/UPLOAD_SHA256SUMS.txt":
            if expected.get(item["target"]) != sha256(source):
                raise SystemExit(f"hash mismatch: {item['target']}")
    return spec, files


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()
    spec, files = load_and_verify()
    print(json.dumps({
        "space_id": spec["space_id"],
        "protected_revision": spec["protected_revision"],
        "publication_parent_revision": spec["publication_parent_revision"],
        "text_files": len(files),
        "mode": "execute" if args.execute else "dry-run",
    }, sort_keys=True))
    if not args.execute:
        return

    from huggingface_hub import CommitOperationAdd, HfApi

    operations = [
        CommitOperationAdd(
            path_in_repo=item["target"],
            path_or_fileobj=str(ROOT / item["source"]),
        )
        for item in files
    ]
    result = HfApi().create_commit(
        repo_id=spec["space_id"],
        repo_type="space",
        operations=operations,
        commit_message="Add high-accuracy Claim 3 evidence",
        parent_commit=spec["publication_parent_revision"],
    )
    print(json.dumps({"published_revision": result.oid, "space_id": spec["space_id"]}, sort_keys=True))


if __name__ == "__main__":
    main()
