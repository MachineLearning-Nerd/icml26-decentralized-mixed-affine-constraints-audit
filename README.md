# ICML 2026 — Complexity of Decentralized Optimization with Mixed Affine Constraints

This repository is an independent, CPU-only audit of the ICML 2026 paper
[*Complexity of Decentralized Optimization with Mixed Affine Constraints*](https://openreview.net/forum?id=KS6RbZMt8L).
The arXiv preprint is titled [*Decentralized Optimization with Mixed Affine
Constraints*](https://arxiv.org/abs/2602.04479). It records exactly what was
implemented, how each claim is produced, which branch contains each stage, and
where the evidence stops.

## Status at a glance

`MIXED_RESULTS / RELEASE_REPLAY_DRIFT`

The committed claim artifacts contain finite, scoped evidence for all five
claims. A fresh local replay of the current `main` mirror on 2026-08-16
completed 91 of 96 gates and failed five artifact-identity gates. Therefore
this repository does **not** claim a current 96/96 replay or a new judge score.

| Claim | Scoped assessment | What the evidence establishes |
| --- | --- | --- |
| C1 — APAPC communication complexity | **VERIFIED_SCOPED** | The exact APAPC route reaches `1e-6` on all 27 stored cells; KKT, factor-slope, lower-certificate, and negative-control checks pass. |
| C2 — full mixed additive work | **VERIFIED_SCOPED_WITH_ARTIFACT_DRIFT** | The stored checker supports the full nonzero mixed operator and additive-vs-multiplicative comparison; the current replay regenerates the scientific checks but not the stored model-comparison payload byte-for-byte. |
| C3 — nonsmooth Gradient Sliding | **VERIFIED_SCOPED_WITH_SOURCE_CAVEAT** | The stored 70-dimensional Lan-consistent route reaches joint `0.001`; the exact printed Algorithm 2 initialization is undefined at `k=1`, and the current replay finds three high-accuracy payload mismatches. |
| C4 — HFL, VFL, and MTL applications | **VERIFIED_SCOPED_WITH_EXTENSION** | Eight seeded synthetic learning tasks pass structural, KKT, centralized-oracle, and omission-control checks; the node-local MTL mask is labeled as an extension. |
| C5 — APAPC core identity | **VERIFIED_SCOPED** | The predictor-corrector core is the same exact APAPC evidence as C1, with a discriminating corrector-removal control. |

The status vocabulary is deliberately narrower than a theorem proof:
finite experiments corroborate the declared contracts; they do not establish
universal asymptotic statements.

## What the paper does

The paper studies decentralized convex optimization with three kinds of affine
constraints on top of a network consensus constraint:

- coupled constraints on the collection of local variables;
- node-local constraints on each local variable; and
- node-specific constraints on a shared global variable.

It develops optimal or near-optimal first-order methods for smooth strongly
convex, smooth convex, and nonsmooth regimes. The audit follows the named
APAPC and Gradient Sliding algorithms, measures primitive matrix/communication
work, and instantiates the HFL, VFL, and distributed MTL application routes.

## Paper record

- **Published title:** *Complexity of Decentralized Optimization with Mixed
  Affine Constraints*.
- **Authors:** Demyan Yarmoshik, Nhat Trung Nguyen, Alexander Rogozin, and
  Alexander Gasnikov.
- **Venue:** ICML 2026, Proceedings of Machine Learning Research 306.
- **Primary record:** [OpenReview KS6RbZMt8L](https://openreview.net/forum?id=KS6RbZMt8L).
- **Preprint:** [arXiv:2602.04479](https://arxiv.org/abs/2602.04479), whose title is
  *Decentralized Optimization with Mixed Affine Constraints*.
- **Source used by the audit:**
  [`.openresearch/sources/arxiv_2602.04479_algorithm2.tex`](.openresearch/sources/arxiv_2602.04479_algorithm2.tex).

This is a clean-room reproduction and evidence audit. It does not claim to be
an authors' implementation, and no external official code is required for the
stored contracts.

## Claim-to-evidence path

Every claim follows the same chain:

```text
paper anchor → source-faithful producer → raw JSON
             → independent checker → negative control → scoped verdict
```

The complete mapping is in [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md). The
machine-readable ledger is [`claims.json`](claims.json), while the original
claim contracts, raw results, checkers, controls, and limitations remain under
[`.openresearch/artifacts`](.openresearch/artifacts).

| Claim | Paper anchor | Producer | Primary evidence | Independent check / control |
| --- | --- | --- | --- | --- |
| C1 | Theorem 4.1, Table 1, Appendix G | `research/round1.py` | `.openresearch/artifacts/claim_1/raw.json` | `checker_output.json`, `negative_control_output.json` |
| C2 | Theorem 4.6, Table 1, Appendix J | `research/round2.py` | `.openresearch/artifacts/claim_2/raw.json` | `checker_output.json`, `negative_control_output.json` |
| C3 | Algorithm 2, Theorems 2.5/5.2, Appendix E | `research/round3.py` | `raw.json` and `high_accuracy_raw.json` | both checker files and both negative-control files |
| C4 | Section 1 and Appendix B | `research/round4.py` | `.openresearch/artifacts/claim_4/raw.json` | `checker_output.json`, `negative_control_output.json` |
| C5 | Algorithm 1, Theorems 4.1/4.5 | `research/round1.py` | same APAPC artifact as C1 | corrector-removal and degree-one controls |

## Current replay versus historical release

The fixed command is:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

At current `main` commit `9df8a67a39819fa7588091be4590b30755f703a1`, the local
replay took 49.67 seconds under Python 3.12.11, passed 91/96 gates, and failed:

```text
embedded.claim2_model_comparison_regenerates_exactly
embedded.claim3_high_accuracy_evidence_regenerates_exactly
embedded.claim3_high_accuracy_checker_matches_first_hit
embedded.claim3_high_accuracy_control_regenerates_exactly
materialized.materialized_figures_equal_hf_generated_payloads
```

Those failures concern equality between regenerated values and frozen
publication payloads. The round-level scientific gates were green; the
release package is therefore reported as drifted rather than silently
rewritten. See [`STATUS.md`](STATUS.md), [`REPORT.md`](REPORT.md), and
[`ENVIRONMENT.md`](ENVIRONMENT.md) for the exact boundary.

The historical high-accuracy release recorded 96/96 gates at source tip
`1e0d3b2b994986479c6985e3cfac5a6bc5f0e5cd` and was published to the existing
[Hugging Face Space](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L) at
revision `2d7aae33c177c464725dee5a8c4a4c5398f5e1a2`. The preceding live judged
revision scored 9/10 at `cbf9ad1348a00e86543c9edf16c1c2fd1a275cbe`.
Both are historical records; no later score is claimed here.

## Repository map

| Path | Role |
| --- | --- |
| [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md) | Claim-by-claim production paths, checks, metrics, and limitations. |
| [`BRANCH_AUDIT.md`](BRANCH_AUDIT.md) | Every historical branch, its clean reader-facing name, tip, and purpose. |
| [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md) | Paper identity, pinned source hashes, and the Algorithm 2 discrepancy audit. |
| [`STATUS.md`](STATUS.md) | Current replay status and historical evaluator boundary. |
| [`REPORT.md`](REPORT.md) | Short audit report and decision record. |
| [`ENVIRONMENT.md`](ENVIRONMENT.md) | Dependency, interpreter, compute, and command record. |
| [`AUTHOR_THANK_YOU.md`](AUTHOR_THANK_YOU.md) | Thank-you note to the paper authors. |
| [`CITATION.cff`](CITATION.cff) | Machine-readable paper and repository citation. |
| [`claims.json`](claims.json) | Machine-readable claim/evidence ledger. |
| [`EVIDENCE_MANIFEST.json`](EVIDENCE_MANIFEST.json) | Published evidence, status, and provenance manifest. |
| [`verify_final.py`](verify_final.py) | Fail-closed check for the final repository surface. |
| [`reproduce.py`](reproduce.py) | Fixed cumulative experiment entrypoint. |
| [`notebooks/reproduction.py`](notebooks/reproduction.py) | Marimo tutorial/report notebook. |
| [`reports/full-reproduction`](reports/full-reproduction) | Historical detailed report and release report. |
| [`space_candidate`](space_candidate) | Frozen evaluator-facing Space payload and its release manifests. |

## Published branch roles

The final branch names are descriptive; a branch label never substitutes for
a claim contract. The complete mapping, old source refs, and exact tips are in
[`BRANCH_AUDIT.md`](BRANCH_AUDIT.md).

| Branch | Purpose |
| --- | --- |
| `main` | Complete paper-first documentation and evidence surface. |
| `research/locked-baseline` | Immutable five-claim blocked baseline. |
| `research/exact-apapc` | Exact APAPC and communication-factor calibration for C1/C5. |
| `research/full-mixed-apapc` | Full Appendix J mixed operator and additive-work calibration for C2. |
| `research/exact-gradient-sliding` | Literal printed-recurrence and nonsmooth calibration controls. |
| `research/source-consistent-gradient-sliding` | Lan-consistent Gradient Sliding interpretation for C3. |
| `research/faithful-learning-applications` | HFL, VFL, and constrained MTL applications for C4. |
| `research/cumulative-publication` | Cumulative evidence and publication figure gates. |
| `research/materialized-report-notebook` | Supported marimo export and protected Space candidate. |
| `research/high-accuracy-gradient-sliding` | 70-dimensional source-audited C3 evidence. |
| `research/materialized-high-accuracy-claim3` | Materialized C3 raw/checker/control artifacts. |
| `research/post-publication-status-correction` | Historical Space metadata correction. |
| `release/evaluator-blind-candidate` | Evaluator-visible allowlist and traversal gates. |
| `release/final-space-candidate` | Hash-locked release candidate for the existing Space. |
| `release/final-high-accuracy-claim3` | Parent-locked high-accuracy release. |
| `release/final-main-report` | Published report mirror. |
| `release/final-status-mirror` | Published status mirror. |
| `release/high-accuracy-claim3-mirror` | Final main mirror of the high-accuracy release. |

## Environment and limitations

- Python `>=3.12,<3.13`, with exact packages in `uv.lock`.
- `numpy==2.3.2`, `scipy==1.16.1`, `marimo==0.15.5`, and
  `matplotlib==3.10.5`.
- All stored formal runs used Hugging Face `cpu-upgrade`; GPU use was
  forbidden. The local replay also used CPU only.
- The synthetic studies use finite path-graph grids and seeded convex tasks;
  they are not production federation, privacy, or real-private-data claims.
- Appendix G is reconstructed but not proof-assistant formalized.
- The exact arXiv TeX leaves outer `\tilde{u}^0` undefined while Algorithm 2
  line 12 reads it. The Lan recurrence used by Appendix E is retained as the
  primary C3 route, and the natural literal completion is a negative control.
- The MTL node-local affine restriction is a disclosed extension of the
  paper's coupled Appendix B example.

## Citation and thanks

Please cite the paper when discussing the method and cite this repository when
using the audit code or evidence. See [`CITATION.cff`](CITATION.cff) and
[`AUTHOR_THANK_YOU.md`](AUTHOR_THANK_YOU.md). We thank Demyan Yarmoshik, Nhat
Trung Nguyen, Alexander Rogozin, and Alexander Gasnikov for making the work
available and for a clear, technically rich problem formulation that can be
audited constructively.
