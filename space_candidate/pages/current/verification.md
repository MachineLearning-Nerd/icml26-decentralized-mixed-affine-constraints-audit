# Current verification run

This is the obvious current verifier. The historical `python3 repro/src/verify.py` page is preserved only under **Historical rejected baseline** and is superseded by this revision.

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

The command exits nonzero if any scientific, control, embedded-evidence, figure, report-link, or notebook gate fails. The pinned environment is `pyproject.toml` plus `uv.lock`. Executable files are [reproduce.py](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/reproduce.py) and [research/](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/tree/main/research).

Latest candidate-generation evidence: Git SHA `88d86fce01dfa22131af191a5329665e4520a2bd`, HF `cpu-upgrade`, 16 cores estimated, 64 logical CPUs observed, 71.341 s verifier runtime, 47/47 gates true. The later materialization run updates this row before release.

Environment versions observed: Python 3.12.12, NumPy 2.3.2, SciPy 1.16.1. GPU allowed: `false`.

Every raw file is downloadable from `current/evidence/claim_<n>/`. Seeds: `20260802` for APAPC construction and `202608020..202608027` for learning applications. Complexity grids and horizons are literal constants in source.
