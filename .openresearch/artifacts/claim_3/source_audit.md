# Claim 3 source audit

Paper Algorithm 2 nests repeated nonsmooth subgradient models inside an outer smooth-penalty evaluation. Theorem 2.5 assumes convexity, bounded subgradients on the domain, a consistent nonzero affine matrix, and a bounded initial distance. Appendix E derives separate B/B-transpose and nonsmooth-subgradient complexities. Theorem 5.2 applies this method with Chebyshev acceleration to the full mixed formulation.

Lan's primary Gradient Sliding source (arXiv:1406.0919, Corollary 1) gives `eta_t=t/2`, `theta_t=2(t+1)/(t(t+3))`, `gamma_k=2/(k+1)`, and `beta_k=2L/k`. The paper's printed line 12 differs from Lan's canonical outer-average recurrence; both interpretations are tested.
