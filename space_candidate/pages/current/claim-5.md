# Claim 5 — APAPC is the core building block

**Verdict: VERIFIED · Confidence: HIGH**

Algorithm 1's accelerated proximal alternating predictor-corrector—not a generic Chambolle–Pock substitute—is the executed core of every smooth calibration. The implementation contains the extrapolated gradient point, predictor, preconditioned residual image, dual update, corrected primal update, and accelerated fast sequence.

The hard smooth cell reaches `1e-6` in 213 iterations. Removing the corrector delays the same target to 359 iterations; replacing the outer Chebyshev polynomial by degree one misses the matched budget. The exact source and counter ledger are shared with Claim 1, because the claimed rate and the named core are tested in the same APAPC runs.

Limitations: finite deterministic quadratics corroborate the predicted behavior but do not prove every admissible instance.

- [Exact Algorithm 1 source](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/research/round1.py)
- [Raw JSON](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_5/raw.json)
- [Checker](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_5/checker_output.json)
- [Controls](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_5/negative_control_output.json)
