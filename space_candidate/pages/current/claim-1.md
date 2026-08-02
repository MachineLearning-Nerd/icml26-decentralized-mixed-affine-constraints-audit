# Claim 1 — APAPC communication complexity

**Verdict: VERIFIED · Confidence: MEDIUM**

## Exact source and contract

Theorem 4.1 applies Algorithm 1 to the shared-variable formulation (10), with graph and constraint Chebyshev preconditioning. Table 1 gives communication work proportional to `sqrt(κ_f) sqrt(κ̂_C̃ᵀ) sqrt(κ_W) log(1/ε)` and states optimality in the paper's decentralized first-order oracle class. Assumptions audited numerically: smooth strong convexity, consistent affine right-hand side, positive nonzero spectra, connected path graph, and exact KKT solution.

Contract: run exact APAPC; execute and count nested graph/constraint actions; independently vary all three condition factors; use formula-independent first-hit horizons; compare to KKT; require omitted-corrector and degree-one-Chebyshev controls to miss the matched budget; reconstruct Appendix G's lower-bound identities.

## Evidence

All 27 cells reach `1e-6`. Observed communication slopes are κ_f `0.520616`, κ̂_C̃ᵀ `0.370598`, and κ_W `0.430116`, versus the square-root exponent `0.5`. The hard cell takes 213 APAPC iterations and 20,448 communications. The no-corrector control takes 359 iterations; the degree-one preconditioner misses the exact budget. All KKT residuals are below `1e-10`.

Appendix G certificate: both exact parameter identities pass and all 32 path spectral cells for `n=3..96` pass. Limitation: the quantified span argument is independently reconstructed, not formalized in a proof assistant; finite sweeps do not prove universal big-O.

- [Executable APAPC source](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/research/round1.py)
- [Raw JSON](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_1/raw.json)
- [Independent checker](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_1/checker_output.json)
- [Negative controls](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_1/negative_control_output.json)
