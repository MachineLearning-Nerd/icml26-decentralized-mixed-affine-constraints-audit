# Claim-to-evidence map

This ledger explains how each paper claim is translated into executable
evidence. `VERIFIED_SCOPED` means that the declared finite contract and its
stored controls passed; it does not mean that a numerical experiment proves a
universal theorem.

## Common execution graph

```text
paper anchor
  → source-faithful producer
  → raw result
  → independent checker
  → negative control
  → scoped verdict
```

The cumulative entrypoint is:

```bash
uv sync --frozen && uv run --frozen python reproduce.py
```

The committed `reproduce.py` runs the baseline regression, four research
rounds, embedded-evidence checks, publication figures, Space-candidate checks,
and release checks. The current local replay result is recorded in
[`STATUS.md`](STATUS.md); the claim rows below describe the stored contracts.

## C1 — APAPC communication complexity

- **Paper anchors:** Theorem 4.1, Table 1, and Appendix G.
- **Contract:** smooth strongly convex shared-variable problem (10), with the
  naturally defined decentralized first-order oracle class; execute exact
  APAPC and count graph/affine primitive actions at independently selected
  first hits.
- **Producer:** [`research/round1.py`](research/round1.py), especially
  `run_round1` and the APAPC/Chebyshev routines.
- **Stored raw evidence:**
  [`.openresearch/artifacts/claim_1/raw.json`](.openresearch/artifacts/claim_1/raw.json).
- **Checker:**
  [`.openresearch/artifacts/claim_1/checker_output.json`](.openresearch/artifacts/claim_1/checker_output.json).
- **Control:**
  [`.openresearch/artifacts/claim_1/negative_control_output.json`](.openresearch/artifacts/claim_1/negative_control_output.json)
  removes the corrector or replaces the outer Chebyshev polynomial by degree
  one.
- **Stored result:** all 27 cells reach `1e-6`; observed log-log slopes are
  `0.5206155400` for `κ_f`, `0.3705981918` for
  `κ̂_C̃ᵀ`, and `0.4301159781` for `κ_W`. The hard case reaches `1e-6` in
  213 iterations and 20,448 communications.
- **Assessment:** `VERIFIED_SCOPED`. The Appendix G lower-bound identities are
  reconstructed separately; they are not proof-assistant verified.

## C2 — full mixed operator and additive work

- **Paper anchors:** Theorem 4.6, Table 1, Definition 4.2, Definition 3.4,
  and Appendix J.
- **Contract:** construct `K = diag(B1, B2)` with coupled, local, shared,
  and consensus blocks; execute both Chebyshev operator paths; compare the
  additive factor with a multiplicative alternative; require both dropped
  blocks to fail.
- **Producer:** [`research/round2.py`](research/round2.py), which builds the
  block operators and counts their primitive actions.
- **Stored raw evidence:**
  [`.openresearch/artifacts/claim_2/raw.json`](.openresearch/artifacts/claim_2/raw.json).
- **Checker:**
  [`.openresearch/artifacts/claim_2/checker_output.json`](.openresearch/artifacts/claim_2/checker_output.json).
- **Controls:**
  [`.openresearch/artifacts/claim_2/negative_control_output.json`](.openresearch/artifacts/claim_2/negative_control_output.json)
  drops the shared or coupled-local block.
- **Stored result:** additive relative RMSE `0.0601851046` versus
  multiplicative `0.2825164062`; dense-versus-structured operator error
  `2.48e-15`; hard case reaches `1e-6` in 221 iterations and 37,128
  communications.
- **Current replay qualification:** the round-2 scientific checks pass, but
  `embedded.claim2_model_comparison_regenerates_exactly` fails because the
  current regenerated comparison is not identical to the stored payload.
- **Assessment:** `VERIFIED_SCOPED_WITH_ARTIFACT_DRIFT`.

## C3 — nonsmooth Gradient Sliding

- **Paper anchors:** Algorithm 2, Theorems 2.5 and 5.2, Appendix E, and Lan
  (2016) Corollary 1.
- **Contract:** use the equation-(7) closed-form argmin over a bounded box,
  an exact subgradient bound, a full mixed affine matrix, separate matrix and
  subgradient counters, an independent LP oracle, and omission controls.
- **Producer:** [`research/round3.py`](research/round3.py). The primary route
  uses Lan's canonical outer-average recurrence because Appendix E invokes
  Lan's theorem; the printed line-12 recurrence is retained as a control.
- **Stored standard evidence:**
  [`.openresearch/artifacts/claim_3/raw.json`](.openresearch/artifacts/claim_3/raw.json),
  its checker, and its negative controls.
- **Stored high-accuracy evidence:**
  [`high_accuracy_raw.json`](.openresearch/artifacts/claim_3/high_accuracy_raw.json),
  [`high_accuracy_checker_output.json`](.openresearch/artifacts/claim_3/high_accuracy_checker_output.json),
  and [`high_accuracy_negative_control_output.json`](.openresearch/artifacts/claim_3/high_accuracy_negative_control_output.json).
- **Stored result:** on 70 dimensions and 12 nodes, a formula-independent
  12-cell grid reaches joint `0.001` at 2,751 outer iterations, 5,502 matrix
  actions, and 176,064 subgradient calls. The objective gap is
  `0.0009989587` and the constraint residual is `0.0009450382`. The natural
  literal completion of the source defect has no `0.001` hit and ends at
  residual `23.9182`.
- **Source audit:**
  [`.openresearch/sources/arxiv_2602.04479_algorithm2.tex`](.openresearch/sources/arxiv_2602.04479_algorithm2.tex)
  initializes `bar u^0`, but line 12 reads outer `tilde u^{k-1}` before
  `tilde u^0` is defined. The exact source certificate and hash are in
  [`SOURCE_AUDIT.md`](SOURCE_AUDIT.md).
- **Current replay qualification:** three high-accuracy evidence/checker/
  control equality gates fail; the round-level C3 scientific gates pass.
- **Assessment:** `VERIFIED_SCOPED_WITH_SOURCE_CAVEAT`.

## C4 — HFL, VFL, and MTL applications

- **Paper anchors:** Section 1 equations (4), the VFL formulation, and the
  coupled distributed MTL example in Appendix B.
- **Contract:** train held-out synthetic learning tasks, solve the constrained
  systems with KKT checks, compare HFL/VFL to centralized oracles, and use
  eight deterministic seeds plus structural omission controls.
- **Producer:** [`research/round4.py`](research/round4.py).
- **Stored raw evidence:**
  [`.openresearch/artifacts/claim_4/raw.json`](.openresearch/artifacts/claim_4/raw.json).
- **Checker:**
  [`.openresearch/artifacts/claim_4/checker_output.json`](.openresearch/artifacts/claim_4/checker_output.json).
- **Controls:**
  [`.openresearch/artifacts/claim_4/negative_control_output.json`](.openresearch/artifacts/claim_4/negative_control_output.json)
  removes consensus, a VFL party representation, or the MTL coupling.
- **Stored result:** eight-seed mean held-out MSE is `0.4943` for HFL,
  `0.3318` for VFL, and `1.1621` for MTL; each full formulation improves on
  its structure-omission control and satisfies the relevant KKT/consensus
  residuals.
- **Boundary:** Appendix B's displayed MTL example is coupled-only. The
  node-specific zero-coordinate restrictions are explicitly labeled as an
  extension within the paper's general mixed framework.
- **Assessment:** `VERIFIED_SCOPED_WITH_EXTENSION`.

## C5 — APAPC core identity

- **Paper anchors:** Algorithm 1 and Theorems 4.1 and 4.5.
- **Contract:** execute the paper's predictor and corrector updates, compare
  to an independent KKT optimum, and require the corrector-removal control to
  miss the accepted hard-case budget.
- **Producer and evidence:** C5 intentionally reuses the exact APAPC evidence
  produced by `research/round1.py` and stored under `claim_1`; the committed
  `claim_5/raw.json` is checked to be identical to `claim_1/raw.json`.
- **Control:** the omitted-corrector and degree-one controls in
  [`.openresearch/artifacts/claim_5/negative_control_output.json`](.openresearch/artifacts/claim_5/negative_control_output.json).
- **Stored result:** the hard case reaches `1e-6` in 213 iterations with the
  corrector and 359 iterations without it.
- **Assessment:** `VERIFIED_SCOPED`; the algorithm-identity evidence is
  finite and does not prove the universal rate theorem.

## Reproduction boundary

The stored artifacts were produced at historical experiment commits and are
kept immutable. The later current-main replay is an additional audit of
replayability, not a replacement for those artifacts. All results are finite,
synthetic, CPU-only evidence with disclosed controls and assumptions.
