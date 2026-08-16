# Status

- **Collection status:** `MIXED_RESULTS / RELEASE_REPLAY_DRIFT`
- **Paper:** *Complexity of Decentralized Optimization with Mixed Affine
  Constraints*, ICML 2026; arXiv preprint `2602.04479`.
- **Authors:** Demyan Yarmoshik, Nhat Trung Nguyen, Alexander Rogozin, and
  Alexander Gasnikov.
- **Claim vector:** C1 `VERIFIED_SCOPED`; C2
  `VERIFIED_SCOPED_WITH_ARTIFACT_DRIFT`; C3
  `VERIFIED_SCOPED_WITH_SOURCE_CAVEAT`; C4
  `VERIFIED_SCOPED_WITH_EXTENSION`; C5 `VERIFIED_SCOPED`.
- **Current replay:** `91/96` gates passed on 2026-08-16 at main commit
  `9df8a67a39819fa7588091be4590b30755f703a1`, using
  `uv sync --frozen && uv run --frozen python reproduce.py`.
- **Current failed gates:** one C2 model-comparison equality gate, three C3
  high-accuracy equality/control gates, and one materialized-figure equality
  gate. These are release-payload identity failures, not a reason to erase or
  overwrite the stored evidence.
- **Historical release:** the parent-locked high-accuracy source run recorded
  `96/96` at `1e0d3b2b994986479c6985e3cfac5a6bc5f0e5cd` and was published to
  Hugging Face Space `DineshAI/KS6RbZMt8L` at revision
  `2d7aae33c177c464725dee5a8c4a4c5398f5e1a2`.
- **Historical judge record:** `9/10` at Space revision
  `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`; this repository makes no newer
  score claim.
- **Author of this audit:** `MachineLearning-Nerd`.

The stored claim-level artifacts are finite and scoped. They support the
declared experiments, controls, and source audits; they do not prove the
paper's universal asymptotic theorems.
