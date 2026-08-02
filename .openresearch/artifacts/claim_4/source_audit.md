# Claim 4 source audit

Section 1 equation (4) defines HFL as sample-wise data partition with equal local model weights. The VFL formulation partitions features by party, imposes `sum_i F_i,j X_i = Z_j` for sample blocks, and uses consensus copies of the top model. Appendix B's MTL formulation applies `r(x^(j)) = ||x^(j)||_2` or infinity norms per feature and introduces coupled variables `y_j = sum_i Q_ij x_i`.

The paper does not specifically state that its Appendix B MTL example has node-specific local constraints. This verifier therefore distinguishes the paper-exact coupled MTL reduction from a node-specific zero-coordinate affine extension that lies in the general mixed framework.

This claim is existential and motivational rather than a universal performance theorem: the paper presents these three application mappings. The reproduction checks that each mapping can train a non-vacuous held-out model and that removing its defining equation is detectable.

Paper HTML retrieved 2026-08-02 from `https://ar5iv.labs.arxiv.org/html/2602.04479`; SHA-256 `f7b9689819c04bee20e8ccc46e51e52d1fbc0c4d5dbb34eae3ac53cf9d2e647a`. Anchors: Section 1 equation (4), the VFL formulation immediately following it, and Appendix B.
