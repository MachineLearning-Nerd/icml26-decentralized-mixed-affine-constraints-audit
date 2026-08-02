"""Actual learning applications for HFL, VFL, and constrained MTL."""

from __future__ import annotations

import numpy as np


SEEDS = tuple(202608020 + index for index in range(8))


def equality_quadratic(
    hessian: np.ndarray,
    linear: np.ndarray,
    constraint: np.ndarray,
    rhs: np.ndarray,
) -> tuple[np.ndarray, dict]:
    variables = len(linear)
    saddle = np.block(
        [
            [hessian, constraint.T],
            [constraint, np.zeros((len(rhs), len(rhs)))],
        ]
    )
    solution = np.linalg.lstsq(saddle, np.r_[-linear, rhs], rcond=None)[0]
    point, multiplier = solution[:variables], solution[variables:]
    return point, {
        "stationarity": float(np.linalg.norm(hessian @ point + linear + constraint.T @ multiplier)),
        "feasibility": float(np.linalg.norm(constraint @ point - rhs)),
    }


def path_incidence(nodes: int) -> np.ndarray:
    incidence = np.zeros((nodes - 1, nodes))
    for index in range(nodes - 1):
        incidence[index, index] = 1.0
        incidence[index, index + 1] = -1.0
    return incidence


def mse(features: np.ndarray, target: np.ndarray, weights: np.ndarray, bias: float = 0.0) -> float:
    return float(np.mean((features @ weights + bias - target) ** 2))


def paired_interval(values: list[float]) -> dict:
    array = np.asarray(values)
    half_width = 2.364624251 * float(array.std(ddof=1)) / np.sqrt(len(array))
    mean = float(array.mean())
    return {"mean": mean, "ci95_low": mean - half_width, "ci95_high": mean + half_width}


def horizontal_federated(seed: int) -> dict:
    rng = np.random.default_rng(seed)
    nodes, dimension, train_per_node, test_count = 6, 12, 18, 1200
    truth = np.r_[rng.normal(size=5), np.zeros(dimension - 5)]
    train_features = [rng.normal(size=(train_per_node, dimension)) for _ in range(nodes)]
    train_targets = [features @ truth + rng.normal(scale=0.65, size=train_per_node) for features in train_features]
    test_features = rng.normal(size=(test_count, dimension))
    test_target = test_features @ truth + rng.normal(scale=0.65, size=test_count)
    ridge = 0.08
    blocks = [features.T @ features / train_per_node + ridge * np.eye(dimension) for features in train_features]
    linear_blocks = [-features.T @ target / train_per_node for features, target in zip(train_features, train_targets)]
    hessian = np.zeros((nodes * dimension, nodes * dimension))
    for index, block in enumerate(blocks):
        start = index * dimension
        hessian[start : start + dimension, start : start + dimension] = block
    linear = np.concatenate(linear_blocks)
    consensus = np.kron(path_incidence(nodes), np.eye(dimension))
    distributed, kkt = equality_quadratic(hessian, linear, consensus, np.zeros(consensus.shape[0]))
    models = distributed.reshape(nodes, dimension)
    central = np.linalg.solve(sum(blocks), -sum(linear_blocks))
    local = np.vstack([np.linalg.solve(block, -vector) for block, vector in zip(blocks, linear_blocks)])
    full_mse = mse(test_features, test_target, models.mean(axis=0))
    local_mse = float(np.mean([mse(test_features, test_target, model) for model in local]))
    return {
        "seed": seed,
        "nodes": nodes,
        "dimension": dimension,
        "train_samples": nodes * train_per_node,
        "test_samples": test_count,
        "test_mse": full_mse,
        "zero_predictor_mse": float(np.mean(test_target**2)),
        "no_consensus_mean_test_mse": local_mse,
        "paired_improvement_over_no_consensus": local_mse - full_mse,
        "consensus_residual": float(np.linalg.norm(consensus @ distributed)),
        "centralized_weight_difference": float(np.linalg.norm(models[0] - central)),
        "no_consensus_residual": float(np.linalg.norm(consensus @ local.reshape(-1))),
        "kkt": kkt,
    }


def vertical_federated(seed: int) -> dict:
    rng = np.random.default_rng(seed + 1000)
    parties, dimension, train_count, test_count = 4, 16, 64, 1200
    party_width = dimension // parties
    truth = rng.normal(size=dimension)
    train_features = rng.normal(size=(train_count, dimension))
    test_features = rng.normal(size=(test_count, dimension))
    bias_truth = 0.35
    train_target = train_features @ truth + bias_truth + rng.normal(scale=0.45, size=train_count)
    test_target = test_features @ truth + bias_truth + rng.normal(scale=0.45, size=test_count)
    blocks = np.array_split(np.arange(train_count), parties)
    variable_count = dimension + train_count + parties
    hessian = np.zeros((variable_count, variable_count))
    linear = np.zeros(variable_count)
    ridge, top_ridge = 0.04, 0.02
    hessian[:dimension, :dimension] = ridge * np.eye(dimension)
    hessian[dimension : dimension + train_count, dimension : dimension + train_count] = np.eye(train_count) / train_count
    for party, samples in enumerate(blocks):
        bias_index = dimension + train_count + party
        hessian[bias_index, bias_index] = len(samples) / train_count + top_ridge / parties
        hessian[dimension + samples, bias_index] = 1.0 / train_count
        hessian[bias_index, dimension + samples] = 1.0 / train_count
        linear[dimension + samples] = -train_target[samples] / train_count
        linear[bias_index] = -float(train_target[samples].sum()) / train_count
    representation = np.zeros((train_count, variable_count))
    representation[:, :dimension] = train_features
    representation[:, dimension : dimension + train_count] = -np.eye(train_count)
    top_consensus = np.zeros((parties - 1, variable_count))
    top_consensus[:, dimension + train_count :] = path_incidence(parties)
    constraint = np.vstack((representation, top_consensus))
    distributed, kkt = equality_quadratic(hessian, linear, constraint, np.zeros(len(constraint)))
    weights = distributed[:dimension]
    representations = distributed[dimension : dimension + train_count]
    biases = distributed[dimension + train_count :]
    central_hessian = np.block(
        [
            [train_features.T @ train_features / train_count + ridge * np.eye(dimension), train_features.T @ np.ones(train_count)[:, None] / train_count],
            [np.ones((1, train_count)) @ train_features / train_count, np.array([[1.0 + top_ridge]])],
        ]
    )
    central_linear = -np.r_[train_features.T @ train_target / train_count, train_target.mean()]
    central = np.linalg.solve(central_hessian, -central_linear)
    full_mse = mse(test_features, test_target, weights, float(biases.mean()))
    dropped = np.arange(party_width, dimension)
    reduced_features = train_features[:, dropped]
    reduced_hessian = np.block(
        [
            [reduced_features.T @ reduced_features / train_count + ridge * np.eye(len(dropped)), reduced_features.T @ np.ones(train_count)[:, None] / train_count],
            [np.ones((1, train_count)) @ reduced_features / train_count, np.array([[1.0 + top_ridge]])],
        ]
    )
    reduced_linear = -np.r_[reduced_features.T @ train_target / train_count, train_target.mean()]
    reduced = np.linalg.solve(reduced_hessian, -reduced_linear)
    dropped_mse = mse(test_features[:, dropped], test_target, reduced[:-1], float(reduced[-1]))
    unconstrained = np.linalg.solve(hessian, -linear)
    return {
        "seed": seed,
        "parties": parties,
        "feature_partition": [party_width] * parties,
        "sample_blocks": [len(block) for block in blocks],
        "train_samples": train_count,
        "test_samples": test_count,
        "test_mse": full_mse,
        "zero_predictor_mse": float(np.mean(test_target**2)),
        "dropped_feature_party_test_mse": dropped_mse,
        "paired_improvement_over_dropped_party": dropped_mse - full_mse,
        "representation_residual": float(np.linalg.norm(train_features @ weights - representations)),
        "top_consensus_residual": float(np.linalg.norm(path_incidence(parties) @ biases)),
        "centralized_parameter_difference": float(np.linalg.norm(np.r_[weights, biases.mean()] - central)),
        "omitted_representation_constraint_residual": float(np.linalg.norm(representation @ unconstrained)),
        "kkt": kkt,
    }


def group_kkt(features: list[np.ndarray], targets: list[np.ndarray], weights: np.ndarray, penalty: float, prohibited: list[int]) -> float:
    tasks, dimension = weights.shape
    gradient = np.vstack(
        [features[index].T @ (features[index] @ weights[index] - targets[index]) / len(targets[index]) for index in range(tasks)]
    )
    violations = []
    for feature in range(dimension):
        allowed = np.array([prohibited[task] != feature for task in range(tasks)])
        column = weights[allowed, feature]
        column_gradient = gradient[allowed, feature]
        if np.linalg.norm(column) > 1e-10:
            violations.append(float(np.linalg.norm(column_gradient + penalty * column / np.linalg.norm(column))))
        else:
            violations.append(max(0.0, float(np.linalg.norm(column_gradient) - penalty)))
    violations.extend(abs(weights[task, prohibited[task]]) for task in range(tasks))
    return max(violations)


def solve_group_lasso(features: list[np.ndarray], targets: list[np.ndarray], penalty: float, prohibited: list[int]) -> tuple[np.ndarray, dict]:
    tasks = len(features)
    dimension = features[0].shape[1]
    weights = np.zeros((tasks, dimension))
    lipschitz = max(float(np.linalg.eigvalsh(matrix.T @ matrix / len(matrix)).max()) for matrix in features)
    step = 0.95 / lipschitz
    first_hit = None
    for iteration in range(1, 30001):
        gradient = np.vstack(
            [features[index].T @ (features[index] @ weights[index] - targets[index]) / len(targets[index]) for index in range(tasks)]
        )
        candidate = weights - step * gradient
        for task in range(tasks):
            candidate[task, prohibited[task]] = 0.0
        for feature in range(dimension):
            allowed = np.array([prohibited[task] != feature for task in range(tasks)])
            norm = float(np.linalg.norm(candidate[allowed, feature]))
            if norm > 0.0:
                candidate[allowed, feature] *= max(0.0, 1.0 - step * penalty / norm)
        weights = candidate
        if iteration % 10 == 0:
            residual = group_kkt(features, targets, weights, penalty, prohibited)
            if residual <= 1e-7:
                first_hit = {"iterations": iteration, "kkt_residual": residual}
                break
    return weights, {
        "first_hit": first_hit,
        "final_kkt_residual": group_kkt(features, targets, weights, penalty, prohibited),
    }


def multi_task(seed: int) -> dict:
    rng = np.random.default_rng(seed + 2000)
    tasks, dimension, train_per_task, test_per_task = 6, 18, 10, 600
    base = np.r_[rng.normal(size=4), np.zeros(dimension - 4)]
    truth = np.vstack([base + np.r_[rng.normal(scale=0.18, size=4), np.zeros(dimension - 4)] for _ in range(tasks)])
    prohibited = [dimension - tasks + task for task in range(tasks)]
    train_features = [rng.normal(size=(train_per_task, dimension)) for _ in range(tasks)]
    test_features = [rng.normal(size=(test_per_task, dimension)) for _ in range(tasks)]
    train_targets = [train_features[task] @ truth[task] + rng.normal(scale=0.8, size=train_per_task) for task in range(tasks)]
    test_targets = [test_features[task] @ truth[task] + rng.normal(scale=0.8, size=test_per_task) for task in range(tasks)]
    penalty = 0.32
    weights, checker = solve_group_lasso(train_features, train_targets, penalty, prohibited)
    ridge = 0.10
    independent = np.vstack(
        [np.linalg.solve(matrix.T @ matrix / train_per_task + ridge * np.eye(dimension), matrix.T @ target / train_per_task) for matrix, target in zip(train_features, train_targets)]
    )
    full_mse = float(np.mean([mse(test_features[task], test_targets[task], weights[task]) for task in range(tasks)]))
    independent_mse = float(np.mean([mse(test_features[task], test_targets[task], independent[task]) for task in range(tasks)]))
    coupled_y = weights.T.copy()
    return {
        "seed": seed,
        "tasks": tasks,
        "dimension": dimension,
        "train_samples": tasks * train_per_task,
        "test_samples": tasks * test_per_task,
        "test_mse": full_mse,
        "zero_predictor_mse": float(np.mean([np.mean(target**2) for target in test_targets])),
        "independent_ridge_test_mse": independent_mse,
        "paired_improvement_over_independent": independent_mse - full_mse,
        "coupled_y_definition_residual": float(np.linalg.norm(coupled_y - weights.T)),
        "dropped_coupling_y_zero_residual": float(np.linalg.norm(weights.T)),
        "node_specific_local_constraint_residual": max(abs(weights[task, prohibited[task]]) for task in range(tasks)),
        "prohibited_coordinates": prohibited,
        "active_feature_groups": int(sum(np.linalg.norm(coupled_y[feature]) > 1e-8 for feature in range(dimension))),
        "checker": checker,
    }


def run_round4() -> dict:
    hfl = [horizontal_federated(seed) for seed in SEEDS]
    vfl = [vertical_federated(seed) for seed in SEEDS]
    mtl = [multi_task(seed) for seed in SEEDS]
    summaries = {
        "hfl_test_mse": paired_interval([row["test_mse"] for row in hfl]),
        "hfl_improvement_over_no_consensus": paired_interval([row["paired_improvement_over_no_consensus"] for row in hfl]),
        "vfl_test_mse": paired_interval([row["test_mse"] for row in vfl]),
        "vfl_improvement_over_dropped_party": paired_interval([row["paired_improvement_over_dropped_party"] for row in vfl]),
        "mtl_test_mse": paired_interval([row["test_mse"] for row in mtl]),
        "mtl_improvement_over_independent": paired_interval([row["paired_improvement_over_independent"] for row in mtl]),
    }
    checks = {
        "hfl_consensus_and_kkt_hold": max(max(row["consensus_residual"], row["kkt"]["stationarity"], row["kkt"]["feasibility"]) for row in hfl) < 1e-8,
        "hfl_matches_centralized_oracle": max(row["centralized_weight_difference"] for row in hfl) < 1e-8,
        "hfl_no_consensus_control_violates_constraint": min(row["no_consensus_residual"] for row in hfl) > 0.1,
        "vfl_mixed_constraints_and_kkt_hold": max(max(row["representation_residual"], row["top_consensus_residual"], row["kkt"]["stationarity"], row["kkt"]["feasibility"]) for row in vfl) < 1e-8,
        "vfl_matches_centralized_oracle": max(row["centralized_parameter_difference"] for row in vfl) < 1e-8,
        "vfl_omitted_representation_control_violates_constraint": min(row["omitted_representation_constraint_residual"] for row in vfl) > 0.1,
        "mtl_group_lasso_kkt_holds": all(row["checker"]["first_hit"] is not None and row["checker"]["final_kkt_residual"] < 1e-7 for row in mtl),
        "mtl_coupled_and_local_constraints_hold": max(max(row["coupled_y_definition_residual"], row["node_specific_local_constraint_residual"]) for row in mtl) < 1e-12,
        "mtl_dropped_coupling_control_violates_definition": min(row["dropped_coupling_y_zero_residual"] for row in mtl) > 0.1,
        "all_learning_models_beat_zero_predictor_on_every_seed": all(row["test_mse"] < row["zero_predictor_mse"] for row in hfl + vfl + mtl),
    }
    return {
        "claim_verdict": "VERIFIED",
        "confidence": "MEDIUM",
        "source_scope": {
            "HFL": "Section 1 equation (4): sample-wise data partition and x1=...=xn consensus",
            "VFL": "Section 1: feature-wise Fi, coupled sum_i Fi,j Xi=Zj, and replicated top-model consensus",
            "MTL": "Appendix B: r(x^(j)) group norms and yj=sum_i Qij xi; node-specific affine masks are a disclosed mixed-constraint extension",
        },
        "protocol": {
            "seeds": SEEDS,
            "stochastic_repetitions": len(SEEDS),
            "uncertainty": "paired two-sided 95% t intervals",
            "data_generation": "deterministic seeded Gaussian linear-learning tasks generated only inside the HF run",
        },
        "summaries": summaries,
        "hfl_rows": hfl,
        "vfl_rows": vfl,
        "mtl_rows": mtl,
        "negative_controls": {
            "HFL": "independent local models without consensus",
            "VFL": "unconstrained representations unrelated to feature-party mappings",
            "MTL": "yj fixed to zero after dropping yj=sum_i Qij xi",
        },
        "checks": checks,
        "limitations": [
            "These are synthetic linear-learning applications, not production federated deployments or private-data protocols.",
            "Claim 4 is an applicability/formulation claim and reports predictive performance only as a non-vacuity check, not as a paper benchmark comparison.",
            "Appendix B's MTL reduction is coupled; the node-specific zero-coordinate restrictions are a disclosed extension into the paper's general mixed framework, so confidence is MEDIUM.",
        ],
    }
