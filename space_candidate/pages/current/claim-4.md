# Claim 4 — HFL, VFL, and MTL applications

**Verdict: VERIFIED · Confidence: MEDIUM**

## Exact source and contract

Section 1 equation (4) models HFL as sample-wise data partition with model consensus. Its VFL formulation partitions features, imposes `sum_i F_i,j X_i=Z_j`, and makes top-model copies agree. Appendix B uses per-feature group norms with coupled variables `y_j=sum_i Q_ij x_i` for MTL.

Contract: train actual held-out models for all three formulations over eight deterministic seeds; compare HFL/VFL distributed solutions to independent centralized oracles; verify MTL subgradient KKT conditions; report 95% intervals; remove the defining constraint in each control.

## Evidence

| Application | Full test MSE, mean (95% CI) | Improvement over control, mean (95% CI) |
|---|---:|---:|
| HFL | 0.4943 (0.4676, 0.5210) | 0.5626 (0.4053, 0.7198) |
| VFL | 0.3318 (0.2630, 0.4005) | 6.0967 (2.7052, 9.4881) |
| MTL | 1.1621 (1.0171, 1.3071) | 1.6271 (0.8077, 2.4464) |

HFL consensus is below `2e-14`; VFL representation residual is below `2.1e-13`; MTL KKT is below `9.8e-8`. Controls violate the intended structures. Appendix B's MTL example is coupled-only; node-specific zero-coordinate affine constraints are a disclosed extension into the general mixed framework, not misattributed to Appendix B.

- [Learning source](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/research/round4.py)
- [Raw JSON](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_4/raw.json)
- [Checker](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_4/checker_output.json)
- [Controls](https://huggingface.co/spaces/DineshAI/KS6RbZMt8L/blob/main/current/evidence/claim_4/negative_control_output.json)
