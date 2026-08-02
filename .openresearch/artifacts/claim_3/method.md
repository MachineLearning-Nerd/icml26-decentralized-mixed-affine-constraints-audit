# Claim 3 method

The nonsmooth test is a weighted L1 objective on `[-1,1]^d` under the cumulative full mixed constraint matrix. A separate linear program supplies the optimum. The exact equation (7) subproblem has a closed-form clipped quadratic minimizer.

Outer, inner, and penalty budgets form a calibrated grid independent of the claimed epsilon formula. The first pilot bracketed the feasibility/objective crossover but did not reach `0.01`; this route refines that observed bracket and extends the horizon. The accepted route is Lan's canonical recurrence, because Appendix E derives the paper result by invoking Lan's theorem. The differing recurrence printed on paper Algorithm 2 line 12 is retained as a failing interpretation control. Omitting the nonsmooth subgradient and omitting the constraint operator while holding the schedule fixed are negative controls.
