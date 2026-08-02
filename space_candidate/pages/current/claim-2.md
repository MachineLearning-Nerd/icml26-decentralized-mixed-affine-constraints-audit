# Claim 2 — unified full mixed bound

**Verdict: VERIFIED · Confidence: MEDIUM**

## Exact source and contract

Theorem 4.6 and Appendix J use `K=diag(B1,B2)`, where `B1` contains coupled `A`, local `C`, and graph `W` operators and `B2` contains shared-variable `C̃` and graph consensus. The communication expression has the additive conditioning factor `(sqrt(κ̃_AC)+sqrt(κ̂_C̃ᵀ)) sqrt(κ_W)`.

Contract: make every primitive block nonzero; execute the structural forward/adjoint paths; compare them to dense matrices; vary κ_f, κ̃_AC, κ̂_C̃ᵀ, and κ_W independently; use observed first-hit work; compare additive and multiplicative models only after the sweep; drop each main block as a negative control.

## Evidence

All 13 cells reach `1e-6`; dense/operator disagreement is at most `2.48e-15`; KKT residuals are below `4e-15`. The additive model has relative RMSE `0.060185`, versus `0.282516` for the multiplicative alternative. The hard case reaches `1e-6` in 221 iterations and 37,128 communications. Dropping coupled/local constraints leaves residual `0.072702`; dropping the shared block leaves `0.026749`; neither hits the target.

Limitation: this is a finite deterministic calibration on path graphs with 4–8 nodes, not a universal proof.

- [Full mixed source](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/research/round2.py)
- [Machine-readable contract](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/claim_contract.json)
- [Source audit and exact quantifiers](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/source_audit.md)
- [Method](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/method.md) · [limitations](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/limitations.md) · [evaluator gate](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/EVAL.md)
- [Raw JSON](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/raw.json)
- [Checker](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/checker_output.json)
- [Controls](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_2/negative_control_output.json)
