# Environment

- **Package manager:** `uv`
- **Python constraint:** `>=3.12,<3.13`
- **Pinned dependencies:** `numpy==2.3.2`, `scipy==1.16.1`,
  `marimo==0.15.5`, and `matplotlib==3.10.5`
- **Lock:** [`uv.lock`](uv.lock)
- **Formal campaign backend:** Hugging Face `cpu-upgrade`; estimated 16 cores,
  64 logical CPUs observed, GPU disabled
- **Current local replay:** Python 3.12.11, NumPy 2.3.2, SciPy 1.16.1,
  marimo 0.15.5, CPU only
- **Fixed command:**
  `uv sync --frozen && uv run --frozen python reproduce.py`
- **Current replay:** 49.67 seconds, 91/96 gates, at main commit
  `9df8a67a39819fa7588091be4590b30755f703a1`

The pinned marimo CLI does not expose a `marimo check` subcommand. The release
logic records that unsupported command and uses the supported HTML-export path
for notebook validation. No dependency or lockfile change is made to hide the
current artifact drift.

The numerical tasks are deterministic within their declared seed/grid
contracts, but the frozen publication payload and the later local replay are
not treated as identical until all 96 gates pass together.
