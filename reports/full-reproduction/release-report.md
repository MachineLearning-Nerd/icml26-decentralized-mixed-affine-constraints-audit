# Final release report

- Previous live judged score: `5/10`
- Conservative projected score range after the proposed change: `8–10/10`
- Best-supported possible new score: `10/10` **forecast, not a judge result**

The exact candidate was first published to the existing Space `DineshAI/KS6RbZMt8L` at revision `cf6997e179e72435d967de1d26ef51a924ceff91`. A status-only correction removed stale pre-publication wording and produced final revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`; scientific evidence is unchanged. The paper is awaiting a live judge evaluation, and the current score remains 5/10.

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

Winning scientific branch: `orx/final-release-gate-and-existing-space-publicatio` at Git SHA `050227ad5b4f72ef3c5c5bd8c563d2da6ab43f44`. Scientific release run `05a428a4-0570-4cef-954a-6c421fdf20d8` passed 86/86 checks in 44.6086 verifier seconds. The additive status-correction branch `orx/post-publication-status-correction` at `e7ecf1f2e10343f886b07c4a23fdc7fff87bd47c` passed 87/87 checks in run `8a7754ad-13b6-47ff-9b06-90fcdad7df73` with a 29.5702-second verifier runtime. Both used 16 cores estimated, 64 logical CPUs allocated, and GPU disabled.

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

The campaign recorded 913 seconds (15m13s) of Hugging Face job wall time across successful, diagnostic, and final status-verification runs. The backend exposed no monetary charge, so cost is reported as **not available** instead of guessed. No GPU hardware was used.

## Release proof

- [Exact 73-path upload allowlist](../../release/UPLOAD_ALLOWLIST.json)
- [Exact 72-entry SHA-256 payload manifest](../../release/UPLOAD_SHA256SUMS.txt)
- [Protected judged-revision manifest](../../.openresearch/artifacts/historical_judged_space/MANIFEST.sha256)
- [Old/new subset proof](../../release/OLD_NEW_SUBSET.json)
- [Evaluator-blind traversal](../../release/EVALUATOR_TRAVERSAL.json)
- [Claim contracts and evidence](../../.openresearch/artifacts)

The pre-publication candidate contained 89 files and 16 reachable pages. All 16 historical non-logbook files remained byte-identical; `logbook.json` was the only replaced path and keeps every old page reachable under **Historical rejected baseline**. The 73 uploaded files are UTF-8 text. For the final correction, the upload-manifest hash is `ccb1e196094c8ac360384eec2e656479f9a275fd47a00bce1b6e0f8de46c46ef`; the allowlist hash is `2cf7b0713b916b9dc1fdffc056b860717c81eda6ca1faa306b5ef74f0707a4f7`.

Post-publication download of exact final revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe` reproduced all payload hashes, all protected non-logbook hashes, all 16 canonical pages, all five SVG figures, and all headline numbers from raw JSON. It also found no broken evaluator-facing links, stale publication wording, or secret-pattern hits. GitHub `main` was then fast-forwarded from baseline `f26962394513c490e7654b04c004e7ab189d7f56` to the validated publication history.

Publication action performed: the hash-locked text-only release and one text-only status correction were committed to the existing `DineshAI/KS6RbZMt8L` Space, followed by a GitHub `main` mirror. No second Space was created. Only the live judge can change the 5/10 score.
