# Current verification run

This is the obvious current verifier. The historical `python3 repro/src/verify.py` page is preserved only under **Historical rejected baseline** and is superseded by this revision.

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

The command exits nonzero if any scientific, control, embedded-evidence, figure, report-link, or notebook gate fails. The pinned environment is `pyproject.toml` plus `uv.lock`. Executable files are [reproduce.py](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/reproduce.py) and [research/](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/tree/main/research).

The current live release is Space revision `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`, judged 9/10. Its status-correction run `8a7754ad-13b6-47ff-9b06-90fcdad7df73` at Git SHA `e7ecf1f2e10343f886b07c4a23fdc7fff87bd47c` passed 87/87 gates on HF `cpu-upgrade` with 16 cores estimated, 64 logical CPUs observed, and no GPU.

The targeted Claim 3 source run `15a485b2-6051-44ef-9443-9bd1b430f18c` at `47452809998f3a253a6ed67fba602f60004a05c8` generated the 70-dimensional `0.001` evidence and exact-TeX certificate. It reached the scientific target; its wrapper exited nonzero solely because these newly generated artifacts had not yet been materialized into the inherited release manifest. Materialization run `c1f6af6f-23b5-43d3-9a74-19ca9658a3e7` at `ae2b7b0731474b9884de281b5de525b9a180bbb1` then regenerated the evidence exactly and passed all 96 cumulative gates in 65.6603 seconds on HF `cpu-upgrade`, with 16 cores estimated, 64 logical CPUs observed, and no GPU.

Environment versions observed: Python 3.12.12, NumPy 2.3.2, SciPy 1.16.1. GPU allowed: `false`.

Every raw file is downloadable from `current/evidence/claim_<n>/`. Seeds: `20260802` for APAPC construction and `202608020..202608027` for learning applications. Complexity grids and horizons are literal constants in source.

The paper HTML was retrieved on 2026-08-02 from `https://ar5iv.labs.arxiv.org/html/2602.04479`; SHA-256 `f7b9689819c04bee20e8ccc46e51e52d1fbc0c4d5dbb34eae3ac53cf9d2e647a`. Every claim page links its exact contract, theorem anchors, assumptions, method, limitations, raw data, checker, and control.
