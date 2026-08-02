# Final release report

- Previous live judged score: `5/10`
- Current live judged score before this targeted update: `9/10`
- Conservative projected score range after the proposed change: `9–10/10`
- Best-supported possible new score: `10/10` **forecast, not a judge result**

The first exact release was published to the existing Space `DineshAI/KS6RbZMt8L` at revision `cf6997e179e72435d967de1d26ef51a924ceff91`; its status correction `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe` was judged **9/10**. The targeted Claim 3 update is now published at `2d7aae33c177c464725dee5a8c4a4c5398f5e1a2` and is awaiting a later live judge verdict.

## Claim forecast

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 2/2 | 2/2 | MEDIUM | VERIFIED | Exact APAPC and three-factor first-hit sweep plus reconstructed lower certificate; no proof-assistant formalization |
| 2 | 2/2 | 2/2 | MEDIUM | VERIFIED | Full nonzero Appendix J blocks and additive-factor calibration; finite path-graph family |
| 3 | 1/2 | 2/2 | MEDIUM | VERIFIED | 70D joint `0.001` hit, LP oracle, separate work ledgers, and exact-TeX certificate; defined Lan recurrence still differs from print |
| 4 | 2/2 | 2/2 | MEDIUM | VERIFIED | Actual eight-seed HFL/VFL/MTL training; MTL node-local mask is a disclosed extension |
| 5 | 2/2 | 2/2 | HIGH | VERIFIED | Literal Algorithm 1 core with KKT oracle and discriminating corrector-removal control |

Current total score: **9/10**. Conservative projected total: **9–10/10**. Best-supported possible total: **10/10, forecast only**. Claims 1, 2, 4, and 5 changed from TOY to live VERIFIED after the original 5/10 verdict. Since the 9/10 verdict, only Claim 3 evidence changed; its points have not changed without a new judge result. No claim remains BLOCKED.

## Winning evidence

Winning branch: `orx/final-high-accuracy-claim-3-release` at Git SHA `1e0d3b2b994986479c6985e3cfac5a6bc5f0e5cd`. Final run `6781426c-1891-40c2-9295-dad545819799` passed 96/96 checks in 64.9194 verifier seconds. Its parent materialization run `c1f6af6f-23b5-43d3-9a74-19ca9658a3e7` passed the same 96 gates in 65.6603 seconds at `ae2b7b0731474b9884de281b5de525b9a180bbb1`. Both used 16 cores estimated, 64 logical CPUs allocated, and GPU disabled.

The strongest claim numbers are:

- Claim 1: 27/27 cells hit `1e-6`; communication slopes 0.520616, 0.370598, and 0.430116.
- Claim 2: additive relative RMSE 0.060185 versus multiplicative 0.282516; hard case 37,128 communications.
- Claim 3: the 70D joint `0.001` target at 5,502 matrix actions and 176,064 subgradient calls; the natural completion of the undefined printed state ends at residual 23.9182 without a hit.
- Claim 4: HFL/VFL/MTL held-out MSE means 0.4943/0.3318/1.1621 over eight seeds.
- Claim 5: exact APAPC needs 213 hard-case iterations versus 359 without the corrector.

## Experiment tree and commands

The stacked lineage is baseline → exact APAPC → full mixed APAPC → source-consistent Gradient Sliding → learning applications → cumulative figures → evaluator-blind release → high-accuracy Gradient Sliding → materialized Claim 3 evidence → parent-locked final release. The exact-text Gradient Sliding route is retained as a source-certified negative control.

Every experiment used the identical fixed command:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

Every launch used:

```bash
orx exp run <experiment-id> --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim --timeout 30m
```

The campaign recorded 1,213 seconds (20m13s) of Hugging Face job wall time across successful, diagnostic, source-audit, and final verification runs. The backend exposed no monetary charge, so cost is reported as **not available** instead of guessed. No GPU hardware was used.

## Release proof

- [Exact 77-path upload allowlist](../../release/UPLOAD_ALLOWLIST.json)
- [Exact 76-entry SHA-256 payload manifest](../../release/UPLOAD_SHA256SUMS.txt)
- [Protected judged-revision manifest](../../.openresearch/artifacts/historical_judged_space/MANIFEST.sha256)
- [Old/new subset proof](../../release/OLD_NEW_SUBSET.json)
- [Evaluator-blind traversal](../../release/EVALUATOR_TRAVERSAL.json)
- [Claim contracts and evidence](../../.openresearch/artifacts)

The pre-publication candidate contained 93 files and 16 reachable pages. All 16 historical non-logbook files remained byte-identical; `logbook.json` was the only replaced path and keeps every old page reachable under **Historical rejected baseline**. All 77 uploaded files are UTF-8 text. The upload-manifest hash is `7468a3abb8d89762821bfb2122417db95026df3c3665311087ec506097eaa8be`; the allowlist hash is `76453fb192bad9afbe5399ca3681ef2b5669988d6e627c942600f6299ea462bc`.

Post-publication download of exact revision `2d7aae33c177c464725dee5a8c4a4c5398f5e1a2` reproduced all 76 manifested payload hashes and all 16 protected non-logbook hashes. All 16 canonical pages resolved, the current verifier was obvious, and every displayed Claim 3 headline number matched raw JSON.

Publication action performed: `python release/publish_space.py --execute` committed the parent-locked 77-path text payload only to the existing `DineshAI/KS6RbZMt8L` Space. This GitHub `main` mirror contains the same reader-facing code, evidence, report, notebook, and release manifests. No second Space was created. Only the live judge can change the current 9/10 score.
