# Current claim-by-claim verification

**Previous live judged score: 5/10.** This page is a candidate update; no score increase is claimed until the live judge evaluates its published revision.

The current verifier supersedes the toy methods in the historical baseline. It implements paper Algorithm 1 APAPC, Appendix J's full mixed block, and Algorithm 2's equation-(7) Gradient Sliding subproblem; it also trains actual HFL, VFL, and MTL models.

| Claim | Status | Confidence | Strongest inline evidence |
|---|---|---|---|
| 1 | VERIFIED | MEDIUM | APAPC slopes 0.521 / 0.371 / 0.430 for κ_f / κ̂_C̃ᵀ / κ_W |
| 2 | VERIFIED | MEDIUM | Additive factor RMSE 0.0602 versus multiplicative 0.2825; hard case 37,128 communications |
| 3 | VERIFIED | MEDIUM | Joint 0.01 hit at 280 matrix and 8,960 subgradient calls; printed line-12 route fails |
| 4 | VERIFIED | MEDIUM | Eight-seed HFL/VFL/MTL held-out learning tasks with structural/KKT checks |
| 5 | VERIFIED | HIGH | Exact APAPC predictor-corrector; omitted-corrector and degree-one controls discriminate |

Run every current claim with exactly:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

Environment: Python 3.12, `uv.lock`, NumPy 2.3.2, SciPy 1.16.1. Compute: Hugging Face `cpu-upgrade`, 16 cores estimated, 64 logical CPUs observed, GPU forbidden. Seeds and all grids are committed in the verifier.

Current pages: [Claim 1](#/current-claim-1) · [Claim 2](#/current-claim-2) · [Claim 3](#/current-claim-3) · [Claim 4](#/current-claim-4) · [Claim 5](#/current-claim-5) · [verification](#/current-verification) · [visibility matrix](#/current-visibility)

The old pages are preserved unchanged and reachable under [Historical rejected baseline](#/historical-index). They are not the current verifier.
