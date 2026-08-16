# Source audit

## Paper identity

The accepted ICML record is [*Complexity of Decentralized Optimization with
Mixed Affine Constraints*](https://openreview.net/forum?id=KS6RbZMt8L), by Demyan
Yarmoshik, Nhat Trung Nguyen, Alexander Rogozin, and Alexander Gasnikov. The
arXiv record is [2602.04479](https://arxiv.org/abs/2602.04479), titled
[*Decentralized Optimization with Mixed Affine Constraints*]. The distinction
is recorded so citations do not silently conflate the conference title with
the preprint title.

The paper's problem (P) minimizes a sum of local objectives over local and
shared variables subject to coupled, local, shared-variable, and consensus
constraints. The source presents APAPC for the smooth strongly convex setting,
Gradient Sliding routes for non-smooth/general-convex settings, and reductions
to HFL, VFL, and MTL.

## Retrieved source records

| Source | Location / identity | SHA-256 |
| --- | --- | --- |
| arXiv abstract and PDF | [arXiv:2602.04479](https://arxiv.org/abs/2602.04479) | external page; not replaced by a guessed local hash |
| arXiv HTML used by the historical claim audits | `https://ar5iv.labs.arxiv.org/html/2602.04479` | `f7b9689819c04bee20e8ccc46e51e52d1fbc0c4d5dbb34eae3ac53cf9d2e647a` |
| vendored Algorithm 2 source | [`.openresearch/sources/arxiv_2602.04479_algorithm2.tex`](.openresearch/sources/arxiv_2602.04479_algorithm2.tex) | full-main-TeX certificate: `8f7b09d693b6dca3d06a8e2b3e31e4e0bf32a744ad117d0976968a079f4e55d4` |
| source archive used by the high-accuracy certificate | recorded in the C3 artifact | `5f481911add79c8eaa45b946bb0d9a4cb29df256b68fc7d894eb492e2476f4aa` |

The local source file records retrieval on 2026-08-02 with an explicit
User-Agent. The conference title/authors were independently checked against
the published OpenReview record on 2026-08-16.

## Claim anchors

- **C1:** Theorem 4.1, Table 1, and Appendix G; the audit tests the shared-
  variable special case and reconstructs the lower-bound identities
  separately.
- **C2:** Theorem 4.6, Definitions 4.2/3.4, Table 1, and Appendix J; all four
  mixed block types are retained in `K = diag(B1, B2)`.
- **C3:** Algorithm 2, Theorems 2.5/5.2, Appendix E, and Lan (2016)
  Corollary 1; the audit retains both the source-consistent and literal
  interpretations.
- **C4:** Section 1 equation (4), the VFL formulation, and Appendix B's
  distributed MTL reduction.
- **C5:** Algorithm 1 and Theorems 4.1/4.5; the corrector is tested by an
  omission control rather than inferred from a name.

## Algorithm 2 discrepancy

The authoritative TeX initializes `\bar{u}^0` but does not initialize the
outer-average state `\tilde{u}^0`. The printed line 12 reads
`\tilde{u}^{k-1}` at the first iteration. The machine certificate therefore
records:

```text
exact_printed_algorithm_is_defined_at_k1: false
initializes_bar_u0: true
initializes_outer_tilde_u0: false
line_12_reads_tilde_u_k_minus_1: true
natural literal completion: \tilde{u}^0 := u^0
```

The primary C3 route uses Lan's canonical outer-average recurrence, because
Appendix E invokes Lan's theorem. The literal printed recurrence and the
natural completion are preserved as negative controls; the literal route
does not reach the target and is not silently passed off as the paper's
defined algorithm.

## Source boundary

This repository vendors the relevant source excerpt and records source hashes,
but it does not claim a formal proof of the paper. The experiments are an
independent finite audit of named algorithms, assumptions, and controls.
