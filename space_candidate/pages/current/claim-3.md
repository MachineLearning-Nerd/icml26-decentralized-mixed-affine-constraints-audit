# Claim 3 — smooth APAPC and nonsmooth Gradient Sliding

**Verdict: VERIFIED · Confidence: MEDIUM**

## Exact source and contract

Algorithm 2 evaluates the smooth penalty once per outer iteration and repeatedly solves equation (7) models using nonsmooth subgradients. Theorem 2.5 assumes convexity, bounded subgradients on the domain, a consistent nonzero affine matrix, and bounded initial distance. Appendix E invokes Lan's Gradient Sliding theorem and schedule.

Contract: use the nested equation-(7) minimizer on a full mixed affine system, a bounded-domain weighted-L1 objective, an independent LP oracle, separate matrix/subgradient first-hit counts, and omission controls. The grid is calibrated from observed behavior rather than the theorem formula.

## Evidence

The 22-dimensional problem has exact subgradient bound `0.391983`; the LP equality residual is `1.23e-15`. Joint accuracy `0.01` is first reached at 140 outer evaluations, 280 matrix actions, and 8,960 subgradient calls, with objective gap `0.009953` and constraint residual `0.009023`.

Omitting the subgradient leaves gap `0.027542`; omitting the constraint operator leaves residual `4.574719`. Paper line 12 differs from the Lan outer-average recurrence invoked by Appendix E: the exact printed route has no hit and ends with residual `11.710247`. The source-consistent Lan route is accepted; the unresolved text discrepancy limits confidence.

- [Gradient Sliding source](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/research/round3.py)
- [Machine-readable contract](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/claim_contract.json)
- [Source audit and exact quantifiers](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/source_audit.md)
- [Method](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/method.md) · [limitations](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/limitations.md) · [evaluator gate](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/EVAL.md)
- [Raw JSON](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/raw.json)
- [LP/checker output](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/checker_output.json)
- [Controls and line-12 audit](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_3/negative_control_output.json)
