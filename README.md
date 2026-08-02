# Reproduction: Complexity of Decentralized Optimization with Mixed Affine Constraints

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-KS6RbZMt8L-complexity-of-decentralized-optimization-with-mixed-affine-constraints/blob/main/notebooks/reproduction.py)

We tested all five judged claims from [arXiv:2602.04479](https://arxiv.org/abs/2602.04479). The reproduction is published in the existing [Hugging Face Space](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L) at revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`. The current live judge score is still **5/10** at the historical judged revision `ca7d5e1e68417ee85909ac717f8b08f5abe952c9`; no score increase is claimed before a new live verdict. The cumulative verifier implements paper Algorithm 1 APAPC, the full mixed operator, the source-consistent Gradient Sliding recurrence, and actual HFL/VFL/MTL learning tasks.

The strongest result is a 27-cell exact-APAPC first-hit sweep: observed communication slopes are `0.521` for κ_f, `0.371` for κ̂_C̃ᵀ, and `0.430` for κ_W, versus the theorem's square-root exponent `0.5`. The full mixed hard case reaches `1e-6` in 221 iterations and 37,128 counted communications. These finite results corroborate the theorem factors; they are not a proof of universal asymptotic big-O.

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

The failed exact-text Gradient Sliding route is retained in the experiment tree because it explains the source-level line-12 discrepancy; it is not the current verifier.

## Upstream workspace

ICML 2026 agent reproduction workspace for KS6RbZMt8L.
