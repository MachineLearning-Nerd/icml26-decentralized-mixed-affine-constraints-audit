# Claim 4 source audit

Section 1 equation (4) defines HFL as sample-wise data partition with equal local model weights. The VFL formulation partitions features by party, imposes `sum_i F_i,j X_i = Z_j` for sample blocks, and uses consensus copies of the top model. Appendix B's MTL formulation applies `r(x^(j)) = ||x^(j)||_2` or infinity norms per feature and introduces coupled variables `y_j = sum_i Q_ij x_i`.

The paper does not specifically state that its Appendix B MTL example has node-specific local constraints. This verifier therefore distinguishes the paper-exact coupled MTL reduction from a node-specific zero-coordinate affine extension that lies in the general mixed framework.
