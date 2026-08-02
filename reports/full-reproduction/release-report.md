# Final release report

- Previous live judged score: `5/10`
- Conservative projected score range after the proposed change: `8–10/10`
- Best-supported possible new score: `10/10` **forecast, not a judge result**

The exact candidate was published to the existing Space `DineshAI/KS6RbZMt8L` at revision `cf6997e179e72435d967de1d26ef51a924ceff91`. The paper is awaiting a live judge evaluation; the current score remains 5/10.

## Claim forecast

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 1/2 | 2/2 | MEDIUM | VERIFIED | Exact APAPC and three-factor first-hit sweep plus reconstructed lower certificate; no proof-assistant formalization |
| 2 | 1/2 | 2/2 | MEDIUM | VERIFIED | Full nonzero Appendix J blocks and additive-factor calibration; finite path-graph family |
| 3 | 1/2 | 2/2 | MEDIUM | VERIFIED | Named Gradient Sliding, LP oracle, separate work ledgers; printed line-12 discrepancy remains material |
| 4 | 1/2 | 2/2 | MEDIUM | VERIFIED | Actual eight-seed HFL/VFL/MTL training; MTL node-local mask is a disclosed extension |
| 5 | 1/2 | 2/2 | HIGH | VERIFIED | Literal Algorithm 1 core with KKT oracle and discriminating corrector-removal control |

Current total score: **5/10**. Conservative projected total: **8–10/10**. Best-supported possible total: **10/10, forecast only**. All five claims changed from TOY evidence in the prior verdict to candidate VERIFIED evidence. No claim remains BLOCKED.

## Winning evidence

Winning branch: `orx/final-release-gate-and-existing-space-publicatio` at Git SHA `050227ad5b4f72ef3c5c5bd8c563d2da6ab43f44`. Final HF run `05a428a4-0570-4cef-954a-6c421fdf20d8` passed 86/86 checks in 44.6086 verifier seconds with 16 cores estimated, 64 logical CPUs allocated, and GPU disabled.

The strongest claim numbers are:

- Claim 1: 27/27 cells hit `1e-6`; communication slopes 0.520616, 0.370598, and 0.430116.
- Claim 2: additive relative RMSE 0.060185 versus multiplicative 0.282516; hard case 37,128 communications.
- Claim 3: the 0.01 target at 280 matrix actions and 8,960 subgradient calls; the literal printed line-12 route ends at residual 11.710247.
- Claim 4: HFL/VFL/MTL held-out MSE means 0.4943/0.3318/1.1621 over eight seeds.
- Claim 5: exact APAPC needs 213 hard-case iterations versus 359 without the corrector.

## Experiment tree and commands

The stacked lineage is baseline → exact APAPC → full mixed APAPC → source-consistent Gradient Sliding → learning applications → cumulative figures → materialized report/Space → evaluator-blind audit → hash-locked release. The exact-text Gradient Sliding sibling is retained as a rejected interpretation.

Every experiment used the identical fixed command:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

Every launch used:

```bash
orx exp run <experiment-id> --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 30m
```

The campaign recorded 865 seconds (14m25s) of Hugging Face job wall time across successful and diagnostic runs. The backend exposed no monetary charge, so cost is reported as **not available** instead of guessed. No GPU hardware was used.

## Release proof

- [Exact 73-path upload allowlist](../../release/UPLOAD_ALLOWLIST.json)
- [Exact 72-entry SHA-256 payload manifest](../../release/UPLOAD_SHA256SUMS.txt)
- [Protected judged-revision manifest](../../.openresearch/artifacts/historical_judged_space/MANIFEST.sha256)
- [Old/new subset proof](../../release/OLD_NEW_SUBSET.json)
- [Evaluator-blind traversal](../../release/EVALUATOR_TRAVERSAL.json)
- [Claim contracts and evidence](../../.openresearch/artifacts)

The pre-publication candidate contained 89 files and 16 reachable pages. All 16 historical non-logbook files remained byte-identical; `logbook.json` was the only replaced path and keeps every old page reachable under **Historical rejected baseline**. The 73 uploaded files are UTF-8 text. The upload-manifest hash is `28c4a301b208aa5292c8d256c0fbce97946b2ded14eef85aa0bfc9dc4affbacd`; the allowlist hash is `88e76c957ae673cb8a21bd41a8c3fd9ba4f8f4391a0e5c82c0354bb8d8f72bb1`.

Post-publication download of exact revision `cf6997e179e72435d967de1d26ef51a924ceff91` reproduced all payload hashes, all protected non-logbook hashes, all 16 canonical pages, and all headline numbers from raw JSON. GitHub `main` was then fast-forwarded from baseline `f26962394513c490e7654b04c004e7ab189d7f56` to the validated publication history.

Publication action performed: one text-only Hugging Face Hub commit to the existing `DineshAI/KS6RbZMt8L` Space, followed by a GitHub `main` mirror. No second Space was created. Only the live judge can change the 5/10 score.
