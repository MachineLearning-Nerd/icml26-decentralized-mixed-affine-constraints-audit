# Claim 3 source audit

Paper Algorithm 2 nests repeated nonsmooth subgradient models inside an outer smooth-penalty evaluation. Theorem 2.5 assumes convexity, bounded subgradients on the domain, a consistent nonzero affine matrix, and a bounded initial distance. Appendix E derives separate B/B-transpose and nonsmooth-subgradient complexities. Theorem 5.2 applies this method with Chebyshev acceleration to the full mixed formulation.

Lan's primary Gradient Sliding source (arXiv:1406.0919, Corollary 1) gives `eta_t=t/2`, `theta_t=2(t+1)/(t(t+3))`, `gamma_k=2/(k+1)`, and `beta_k=2L/k`. The paper's printed line 12 differs from Lan's canonical outer-average recurrence. Appendix E explicitly proves Theorem 2.5 by applying Lan's result, so the canonical recurrence is the source-consistent route; the literal printed recurrence is also tested and cannot silently be treated as equivalent.

The paper quantifies the separate matrix and nonsmooth-subgradient upper bounds for every admissible convex instance under these assumptions. The experiment tests first-hit scaling and oracle separation on one audited family; it does not turn the finite family into a universal proof.

The authoritative arXiv TeX provides a second, machine-checkable source issue: line 3 initializes only `\overline u^0`, while line 12 reads `\tilde u^{k-1}` and therefore reads undefined outer state `\tilde u^0` at `k=1`. The exact excerpt is preserved with source-tar SHA-256 `5f481911add79c8eaa45b946bb0d9a4cb29df256b68fc7d894eb492e2476f4aa` and full-TeX SHA-256 `8f7b09d693b6dca3d06a8e2b3e31e4e0bf32a744ad117d0976968a079f4e55d4`. The literal control supplies only the natural missing initialization `\tilde u^0:=u^0`; it is not represented as an exact executable algorithm.

Paper HTML retrieved 2026-08-02 from `https://ar5iv.labs.arxiv.org/html/2602.04479`; SHA-256 `f7b9689819c04bee20e8ccc46e51e52d1fbc0c4d5dbb34eae3ac53cf9d2e647a`. The TeX source was retrieved the same day from `https://arxiv.org/e-print/2602.04479` with an explicit User-Agent. Anchors: Algorithm 2 lines 3 and 12, Theorem 2.5, Theorem 5.2, Appendix E, equation (7).
