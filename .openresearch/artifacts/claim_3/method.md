# Claim 3 method

The nonsmooth test is a weighted L1 objective on `[-1,1]^d` under the cumulative full mixed constraint matrix. A separate linear program supplies the optimum. The exact equation (7) subproblem has a closed-form clipped quadratic minimizer.

Outer, inner, and penalty budgets form a calibrated grid independent of the claimed epsilon formula. The first pilot bracketed the feasibility/objective crossover but did not reach `0.01`; this repair refines that observed bracket and extends the horizon. The accepted route is the exact recurrence printed in paper Algorithm 2. Lan's canonical recurrence is retained only as an interpretation audit. Omitting the nonsmooth subgradient and omitting the constraint operator while holding the schedule fixed are negative controls.
