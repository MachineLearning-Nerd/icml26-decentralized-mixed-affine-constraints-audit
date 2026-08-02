# Current verification run

This is the obvious current verifier. The historical `python3 repro/src/verify.py` page is preserved only under **Historical rejected baseline** and is superseded by this revision.

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

The command exits nonzero if any scientific, control, embedded-evidence, figure, report-link, or notebook gate fails. The pinned environment is `pyproject.toml` plus `uv.lock`. Executable files are [reproduce.py](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/reproduce.py) and [research/](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/tree/main/research).

Latest frozen scientific release evidence: Git SHA `050227ad5b4f72ef3c5c5bd8c563d2da6ab43f44`, run `05a428a4-0570-4cef-954a-6c421fdf20d8`, HF `cpu-upgrade`, 16 cores estimated, 64 logical CPUs observed, 44.6086 s verifier runtime, 86/86 gates true. The exact payload was published at Space revision `cf6997e179e72435d967de1d26ef51a924ceff91`; a fresh post-publication download matched every payload hash, every protected non-logbook hash, every canonical page, and every displayed headline number against raw JSON.

This page supersedes stale pre-publication wording in that first published revision. The correction changes status/provenance text only; the same fixed command, lock, algorithms, raw data, and scientific gates are retained and rerun before the correction can be uploaded.

Environment versions observed: Python 3.12.12, NumPy 2.3.2, SciPy 1.16.1. GPU allowed: `false`.

Every raw file is downloadable from `current/evidence/claim_<n>/`. Seeds: `20260802` for APAPC construction and `202608020..202608027` for learning applications. Complexity grids and horizons are literal constants in source.

The paper HTML was retrieved on 2026-08-02 from `https://ar5iv.labs.arxiv.org/html/2602.04479`; SHA-256 `f7b9689819c04bee20e8ccc46e51e52d1fbc0c4d5dbb34eae3ac53cf9d2e647a`. Every claim page links its exact contract, theorem anchors, assumptions, method, limitations, raw data, checker, and control.
