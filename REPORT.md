# Audit report

## Decision

The repository is suitable as a documented, scoped reproduction archive, but
its current cumulative replay is not a clean release pass. The correct public
status is:

```text
MIXED_RESULTS / RELEASE_REPLAY_DRIFT
```

The historical claim artifacts and their independent checkers are retained.
The current replay is recorded separately so a reader can distinguish a
scientific claim result from an exact-payload reproducibility result.

## Current replay

Command:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

At `main` commit `9df8a67a39819fa7588091be4590b30755f703a1`, the run completed
in 49.67 seconds and passed 91 of 96 gates. The five failures were:

1. `embedded.claim2_model_comparison_regenerates_exactly`;
2. `embedded.claim3_high_accuracy_evidence_regenerates_exactly`;
3. `embedded.claim3_high_accuracy_checker_matches_first_hit`;
4. `embedded.claim3_high_accuracy_control_regenerates_exactly`; and
5. `materialized.materialized_figures_equal_hf_generated_payloads`.

The round-level scientific gates passed. The failures mean that the current
code path and the frozen high-accuracy/publication payloads have drifted in
some numerical values. This report does not convert those mismatches into a
new claim verdict.

## Stored claim assessment

| Claim | Stored evidence | Scoped assessment | Main boundary |
| --- | --- | --- | --- |
| C1 | 27-cell APAPC sweep, KKT/lower certificate, and controls | `VERIFIED_SCOPED` | Finite cells; no proof-assistant formalization. |
| C2 | Full Appendix J block construction, structural checks, additive fit, and dropped-block controls | `VERIFIED_SCOPED_WITH_ARTIFACT_DRIFT` | Finite graph/operator family; stored model comparison is not regenerated exactly today. |
| C3 | 22D route, 70D high-accuracy route, LP oracle, source certificate, and controls | `VERIFIED_SCOPED_WITH_SOURCE_CAVEAT` | Algorithm 2 line 12 reads undefined outer `tilde u^0`; Lan recurrence is the accepted interpretation. |
| C4 | Eight-seed HFL/VFL/MTL tasks, KKT/oracle checks, and omission controls | `VERIFIED_SCOPED_WITH_EXTENSION` | Synthetic tasks; node-local MTL mask is a disclosed extension. |
| C5 | Exact Algorithm 1 identity and corrector-removal control | `VERIFIED_SCOPED` | Same finite APAPC family as C1. |

Detailed production paths are in [`CLAIM_EVIDENCE.md`](CLAIM_EVIDENCE.md).
Source provenance is in [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md), and the complete
branch lineage is in [`BRANCH_AUDIT.md`](BRANCH_AUDIT.md).

## Historical release boundary

The Hugging Face payload is preserved as a historical artifact. Its release
manifests, Space pages, and 96/96 run record are not silently rewritten to
match the later local replay. A later maintainer may produce a new release
after resolving the five identity mismatches, but that is a separate result.
