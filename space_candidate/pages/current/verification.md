# Current verification run

This is the obvious current verifier. The historical `python3 repro/src/verify.py` page is preserved only under **Historical rejected baseline** and is superseded by this revision.

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

The command exits nonzero if any scientific, control, embedded-evidence, figure, report-link, or notebook gate fails. The pinned environment is `pyproject.toml` plus `uv.lock`. Executable files are [reproduce.py](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/reproduce.py) and [research/](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/tree/main/research).

Latest frozen cumulative evidence: Git SHA `495e488521643a1b44dc884fc64975a7e536ac1b`, run `4f12c980-815f-4f7f-bd9e-1c4b7d60f49c`, HF `cpu-upgrade`, 16 cores estimated, 64 logical CPUs observed, 44.3397 s scientific-verifier runtime, 65/65 gates true. The release child adds only navigation, manifests, and evaluator-blind checks, then reruns this cumulative suite.

Environment versions observed: Python 3.12.12, NumPy 2.3.2, SciPy 1.16.1. GPU allowed: `false`.

Every raw file is downloadable from `current/evidence/claim_<n>/`. Seeds: `20260802` for APAPC construction and `202608020..202608027` for learning applications. Complexity grids and horizons are literal constants in source.

The paper HTML was retrieved on 2026-08-02 from `https://ar5iv.labs.arxiv.org/html/2602.04479`; SHA-256 `f7b9689819c04bee20e8ccc46e51e52d1fbc0c4d5dbb34eae3ac53cf9d2e647a`. Every claim page links its exact contract, theorem anchors, assumptions, method, limitations, raw data, checker, and control.
