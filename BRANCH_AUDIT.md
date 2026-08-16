# Branch audit

The historical branches were created by an automated research workspace and
therefore used opaque `orx/` names. The final names describe what a reader
will find there. The old source tips below are recorded before attribution
normalization; after publication, the final non-main tip hashes are recorded in
[`EVIDENCE_MANIFEST.json`](EVIDENCE_MANIFEST.json).

| Old source ref | Source tip before normalization | Final branch | Reader-facing purpose |
| --- | --- | --- | --- |
| `main` | `9df8a67a39819fa7588091be4590b30755f703a1` | `main` | Complete paper-first documentation and evidence surface. |
| `orx/locked-baseline-historical-verifier-audit` | `027a9e3868cb3e6f5bfa56e2dacd75474d5f2fa9` | `research/locked-baseline` | Immutable five-claim blocked baseline and environment pin. |
| `orx/exact-apapc-and-communication-factor-calibration` | `b5dc1466dd61d31849e3afd020839a4928a8a2f1` | `research/exact-apapc` | Exact APAPC, factor calibration, and C1/C5 controls. |
| `orx/full-mixed-apapc-additive-work-calibration` | `fdfc091d3fefa9913b548e3d6e7bd47ef951c0e0` | `research/full-mixed-apapc` | Full Appendix J mixed operator and C2 additive-work calibration. |
| `orx/exact-gradient-sliding-nonsmooth-mixed-constrain` | `2503c1211a54dfe1b7e9964585c4e069c5d9ccf3` | `research/exact-gradient-sliding` | Exact printed Gradient Sliding route and nonsmooth controls. |
| `orx/source-consistent-lan-gradient-sliding-interpret` | `97f37fa87c0075d0fec7113e9d6901287fcbb553` | `research/source-consistent-gradient-sliding` | Lan-consistent recurrence and source-discrepancy audit for C3. |
| `orx/faithful-hfl-vfl-and-constrained-mtl-application` | `10f9caf9ef5c8c525eedf7ede1d93721bbe85420` | `research/faithful-learning-applications` | HFL, VFL, and constrained MTL application tasks for C4. |
| `orx/cumulative-publication-artifact-and-evaluator-ga` | `88d86fce01dfa22131af191a5329665e4520a2bd` | `research/cumulative-publication` | Cumulative evidence and publication figure gates. |
| `orx/materialized-report-notebook-and-protected-space` | `495e488521643a1b44dc884fc64975a7e536ac1b` | `research/materialized-report-notebook` | Supported marimo export and protected Space candidate. |
| `orx/evaluator-blind-release-candidate-and-publicatio` | `a6706674d87a60903bda4e673aa99510a53895b7` | `release/evaluator-blind-candidate` | Evaluator-visible allowlist, traversal, and release gates. |
| `orx/final-release-gate-and-existing-space-publicatio` | `050227ad5b4f72ef3c5c5bd8c563d2da6ab43f44` | `release/final-space-candidate` | Hash-locked release candidate for the existing Space. |
| `publication/final-main-report` | `13733eeaee2ac653859ff87b9231aa803faac97b` | `release/final-main-report` | Published final report mirror. |
| `orx/post-publication-status-correction` | `e7ecf1f2e10343f886b07c4a23fdc7fff87bd47c` | `research/post-publication-status-correction` | Historical Space status metadata correction. |
| `publication/final-status-mirror` | `92336a012c004bffb9abcb28207de8aeb5150026` | `release/final-status-mirror` | Published status mirror. |
| `orx/high-accuracy-gradient-sliding-and-source-certif` | `47452809998f3a253a6ed67fba602f60004a05c8` | `research/high-accuracy-gradient-sliding` | 70-dimensional source-audited C3 evidence. |
| `orx/materialized-high-accuracy-claim-3-release` | `ae2b7b0731474b9884de281b5de525b9a180bbb1` | `research/materialized-high-accuracy-claim3` | Materialized high-accuracy C3 raw/checker/control files. |
| `orx/final-high-accuracy-claim-3-release` | `1e0d3b2b994986479c6985e3cfac5a6bc5f0e5cd` | `release/final-high-accuracy-claim3` | Parent-locked high-accuracy release and Space revision. |
| `publication/high-accuracy-claim3-mirror` | `9df8a67a39819fa7588091be4590b30755f703a1` | `release/high-accuracy-claim3-mirror` | Final main mirror of the high-accuracy release. |

## Final tips after attribution normalization

All reachable commits on these branches use
`MachineLearning-Nerd <MachineLearning-Nerd@users.noreply.github.com>`.

| Final branch | Tip |
| --- | --- |
| `main` | tip containing this audit |
| `research/locked-baseline` | `08c1d84bf3b3ec99ba28bc22e89bc5c466383df1` |
| `research/exact-apapc` | `bca9a68189615d0a5232bc7393d99b50c71862db` |
| `research/full-mixed-apapc` | `d270dfa133aefac1c8862d655498d221611d0c3c` |
| `research/exact-gradient-sliding` | `b3bb2998f8db52d60a26a0801821f2e1b5bdaf5a` |
| `research/source-consistent-gradient-sliding` | `8c2eca581607a21d342fc9168451f05c495af3bf` |
| `research/faithful-learning-applications` | `f1e506f401632ca8fefa8c1215bc895ad798fbd8` |
| `research/cumulative-publication` | `aaa0b9026ac146b1008854a8a470a0089772f02d` |
| `research/materialized-report-notebook` | `4a85c47ae2771c07b8de261f0ccc7e1ee0ded4d2` |
| `research/high-accuracy-gradient-sliding` | `dab55fb5552da2d65371454c0af33cc0d6a97974` |
| `research/materialized-high-accuracy-claim3` | `7d7504f76e34d6701e141230605671844abb1f24` |
| `research/post-publication-status-correction` | `c0b1dbfb83dec65bf3f14251a24ac582c2d677de` |
| `release/evaluator-blind-candidate` | `b9d73d8a671dfe9960a55ef66061cdf9397daec4` |
| `release/final-space-candidate` | `aa88a32d9d765b80e2a7b7db921f359a1f913b9b` |
| `release/final-high-accuracy-claim3` | `7ee89c05bf697ace8d7882ed19b3a35cfa6f5f88` |
| `release/final-main-report` | `d8282dba1c6d5f561289e252e064c1a147655d8a` |
| `release/final-status-mirror` | `e6ebf759ea5fa91952020df7c9e74dd31415eef2` |
| `release/high-accuracy-claim3-mirror` | `f4b0408748c5979311f0502b165f8c70080724d0` |

## Lineage

```text
locked baseline
  → exact APAPC
  → full mixed APAPC
  → exact/source-consistent Gradient Sliding
  → learning applications
  → cumulative publication
  → evaluator-blind release
  → historical Space release/status correction
  → high-accuracy C3 release
  → final report/status mirrors
```

The high-accuracy path is intentionally separate from the original C3 route:
it materializes the 70-dimensional evidence and carries the source certificate
forward. The publication branches are mirrors or release assembly points,
not additional scientific claims.

## Branch invariants

- `main` is the default branch and contains the complete documentation and
  evidence surface.
- Every non-main branch has a readable `research/` or `release/` role.
- No final branch is named `orx/*` or `master`.
- Branch names describe lineage; claim verdicts are defined only by the claim
  contracts and evidence files.
- Final branch inventory and reachable commit identities are checked by
  [`verify_final.py`](verify_final.py) and then rechecked against GitHub.
