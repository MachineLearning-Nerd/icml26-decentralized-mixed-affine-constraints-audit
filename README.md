# Reproduction: Complexity of Decentralized Optimization with Mixed Affine Constraints

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/blob/main/notebooks/reproduction.py)

We tested all five judged claims from [arXiv:2602.04479](https://arxiv.org/abs/2602.04479). The reproduction is published in the existing [Hugging Face Space](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L) at revision `2d7aae33c177c464725dee5a8c4a4c5398f5e1a2`. The current live judge score is **9/10** at the preceding judged revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`; Claims 1, 2, 4, and 5 are live VERIFIED. The new revision targets the remaining Claim 3 criticism, but no 10/10 result is claimed before a later live verdict.

The strengthened Claim 3 experiment runs Gradient Sliding on 12 nodes and 70 variables. A formula-independent 12-cell grid reaches joint objective/feasibility accuracy `0.001` at iteration 2,751, with 5,502 matrix actions and 176,064 subgradient calls. The exact arXiv TeX leaves `tilde u^0` undefined; its natural completion misses all targets through 8,192 iterations, while the Lan recurrence invoked by Appendix E passes. This is finite corroboration, not a proof of universal asymptotics.

- [Illustrated claim-by-claim report](reports/full-reproduction/report.md)
- [Final release and provenance report](reports/full-reproduction/release-report.md)
- [Tutorial marimo notebook](notebooks/reproduction.py)
- [Executable fixed entrypoint](reproduce.py)
- [Claim contracts and raw evidence](.openresearch/artifacts)

Run the complete verifier with exactly:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

All research runs used Hugging Face `cpu-upgrade`; GPU use was forbidden. The generated tasks are deliberately moderate synthetic benchmarks, not production federated deployments. Claim 3 remains MEDIUM confidence because paper Algorithm 2 line 12 differs from the Lan recurrence invoked by Appendix E. Claim 4 remains MEDIUM confidence because Appendix B's MTL example is coupled-only; the node-specific affine mask is a disclosed extension.

Notebook validation note: the pinned marimo 0.15.5 CLI does not provide the requested `marimo check` subcommand. The cumulative verifier records that unsupported command and requires the supported `marimo export html notebooks/reproduction.py` path to parse and execute the notebook successfully instead; the lock is not changed between experiment nodes.

## Experiment log

| Branch / experiment | Purpose | Exact run command | Assessment / outcome | Compute |
|---|---|---|---|---|
| `main` | Publication surface | Not run as an experiment (publication surface) | README, report, notebook, and Space mirror | — |
| [`orx/locked-baseline-historical-verifier-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/locked-baseline-historical-verifier-audit) | Freeze judged toy baseline | `uv sync --frozen && uv run --frozen python reproduce.py` | Five claims honestly BLOCKED at baseline | HF `cpu-upgrade`, 64 logical CPUs |
| [`orx/exact-apapc-and-communication-factor-calibration`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/exact-apapc-and-communication-factor-calibration) | Exact APAPC, all communication factors, lower certificate | `uv sync --frozen && uv run --frozen python reproduce.py` | Claims 1 and 5 VERIFIED | HF `cpu-upgrade`, 64 logical CPUs |
| [`orx/full-mixed-apapc-additive-work-calibration`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/full-mixed-apapc-additive-work-calibration) | Full Appendix J mixed operator | `uv sync --frozen && uv run --frozen python reproduce.py` | Claim 2 VERIFIED | HF `cpu-upgrade`, 64 logical CPUs |
| [`orx/source-consistent-lan-gradient-sliding-interpret`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/source-consistent-lan-gradient-sliding-interpret) | Gradient Sliding and printed-line audit | `uv sync --frozen && uv run --frozen python reproduce.py` | Claim 3 VERIFIED, MEDIUM confidence | HF `cpu-upgrade`, 64 logical CPUs |
| [`orx/faithful-hfl-vfl-and-constrained-mtl-application`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/faithful-hfl-vfl-and-constrained-mtl-application) | Actual HFL, VFL, MTL learning tasks | `uv sync --frozen && uv run --frozen python reproduce.py` | Claim 4 VERIFIED, MEDIUM confidence | HF `cpu-upgrade`, 64 logical CPUs |
| [`orx/materialized-report-notebook-and-protected-space`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/materialized-report-notebook-and-protected-space) | Cumulative verifier and publication gates | `uv sync --frozen && uv run --frozen python reproduce.py` | 65/65 gates pass; protected Space candidate materialized | HF `cpu-upgrade`, 64 logical CPUs, 44.3397 s verifier |
| [`orx/evaluator-blind-release-candidate-and-publicatio`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/evaluator-blind-release-candidate-and-publicatio) | Exact release allowlist, subset proof, and evaluator-blind traversal | `uv sync --frozen && uv run --frozen python reproduce.py` | 86/86 cumulative release gates pass | HF `cpu-upgrade`, 64 logical CPUs, 28.1083 s verifier |
| [`orx/final-release-gate-and-existing-space-publicatio`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/final-release-gate-and-existing-space-publicatio) | Hash-locked publication candidate for the existing Space | `uv sync --frozen && uv run --frozen python reproduce.py` | 86/86 gates pass; published as Space revision `cf6997e179e72435d967de1d26ef51a924ceff91` | HF `cpu-upgrade`, 64 logical CPUs, 44.6086 s verifier |
| [`orx/post-publication-status-correction`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/post-publication-status-correction) | Replace stale future-tense release metadata without changing scientific evidence | `uv sync --frozen && uv run --frozen python reproduce.py` | 87/87 gates pass; final Space revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe` | HF `cpu-upgrade`, 64 logical CPUs, 29.5702 s verifier |
| [`orx/high-accuracy-gradient-sliding-and-source-certif`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/high-accuracy-gradient-sliding-and-source-certif) | 70D, `0.001` Gradient Sliding route and exact-TeX certificate | `uv sync --frozen && uv run --frozen python reproduce.py` | Scientific checks pass; inherited packaging checks reject unmaterialized evidence | HF `cpu-upgrade`, 64 logical CPUs, 2m12s job wall time |
| [`orx/materialized-high-accuracy-claim-3-release`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/materialized-high-accuracy-claim-3-release) | Materialize high-accuracy raw data, checker, control, and source | `uv sync --frozen && uv run --frozen python reproduce.py` | 96/96 cumulative gates pass | HF `cpu-upgrade`, 64 logical CPUs, 65.6603 s verifier |
| [`orx/final-high-accuracy-claim-3-release`](https://github.com/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/tree/orx/final-high-accuracy-claim-3-release) | Parent-lock, final cumulative gate, and text-only release | `uv sync --frozen && uv run --frozen python reproduce.py` | 96/96 gates pass; published as Space revision `2d7aae33c177c464725dee5a8c4a4c5398f5e1a2` | HF `cpu-upgrade`, 64 logical CPUs, 64.9194 s verifier |

The exact-text Gradient Sliding route is retained because it explains the source-level initialization defect; it is a negative control, not the current verifier.

## Upstream workspace

ICML 2026 agent reproduction workspace for KS6RbZMt8L.
