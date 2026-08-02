# Release report and provenance

- Previous live judged score before this targeted round: `9/10` (original campaign baseline: `5/10`)
- Conservative projected score range after the proposed change: `9–10/10`
- Best-supported possible new score: `10/10` **forecast, not a judge result**

| Claim | Current points | Possible points | Confidence | Evidence status | Basis and remaining risk |
|---|---:|---:|---|---|---|
| 1 | 2/2 | 2/2 | MEDIUM | VERIFIED | Exact APAPC and three-factor first-hit sweep plus reconstructed lower certificate; no proof-assistant formalization |
| 2 | 2/2 | 2/2 | MEDIUM | VERIFIED | Full nonzero Appendix J blocks and additive-factor calibration; finite path-graph family |
| 3 | 1/2 | 2/2 | MEDIUM | VERIFIED | 70D joint `0.001` hit, LP oracle, separate work ledgers, and exact-TeX source certificate; defined Lan recurrence still differs from print |
| 4 | 2/2 | 2/2 | MEDIUM | VERIFIED | Actual eight-seed HFL/VFL/MTL training; MTL node-local mask is a disclosed extension |
| 5 | 2/2 | 2/2 | HIGH | VERIFIED | Literal Algorithm 1 core with KKT oracle and discriminating corrector-removal control |

Current total score: **9/10** at revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`. Conservative projected total: **9–10/10**. Best-supported possible total: **10/10, forecast only**. Claims 1, 2, 4, and 5 already changed from TOY to live VERIFIED; this update targets only Claim 3. No claim is BLOCKED; the finite-experiment and source-interpretation risks above remain explicit.

## Experiment tree and compute

The stacked lineage is baseline → exact APAPC → full mixed APAPC → source-consistent Gradient Sliding → learning applications → cumulative figures → evaluator-blind release → high-accuracy Gradient Sliding → materialized Claim 3 release. The exact-text route remains a source-certified rejected interpretation because it is undefined at `k=1`; its natural completion becomes unstable.

All jobs used Hugging Face `cpu-upgrade`, never GPU. Every node inherited exactly `uv sync --frozen && uv run --frozen python reproduce.py`. The campaign through the frozen scientific release used 865 seconds (14m25s) of recorded HF job wall time, ending with the 86/86 pass `05a428a4-0570-4cef-954a-6c421fdf20d8`. The backend did not expose a monetary charge, so cost is reported as unavailable instead of guessed. The later status-correction run is metadata validation, not new scientific evidence, and is recorded in the OpenResearch tree.

## Publication action

The exact 73-path text payload was published only to `DineshAI/KS6RbZMt8L` at revision `cf6997e179e72435d967de1d26ef51a924ceff91`, then downloaded into a fresh directory and verified. The exact judged revision `ca7d5e1e68417ee85909ac717f8b08f5abe952c9` remains the historical source. Existing historical pages and evidence remain byte-identical; only `logbook.json` was replaced to put current verification first. GitHub `main` was also verified after publication.

This status-only correction is parent-locked to `cf6997e179e72435d967de1d26ef51a924ceff91`, reuses the same text allowlist, and alters no algorithm, raw evidence, claim verdict, or pinned dependency. Its purpose is solely to remove pre-publication future tense from the evaluator-visible pages.

- [Upload allowlist](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/release/UPLOAD_ALLOWLIST.json)
- [Upload SHA-256 manifest](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/release/UPLOAD_SHA256SUMS.txt)
- [Historical judged manifest](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/release/HISTORICAL_MANIFEST.sha256)
- [Evaluator-blind review](#/current-red-team)

Live status: revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe` was judged 9/10 at verdict-dataset revision `5fb68bd9f491b7579b7975ed8c7bf0bf1f47f5fc`. A later 10/10 is only a forecast until a new live verdict says so.
