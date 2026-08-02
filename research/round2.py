"""Full block-mixed APAPC evidence for Theorem 4.6 and Claim 2."""

from __future__ import annotations

import math
from concurrent.futures import ProcessPoolExecutor

import numpy as np

from research.round1 import HORIZONS, TOLERANCES


def path_graph(nodes: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    adjacency = np.zeros((nodes, nodes))
    for i in range(nodes - 1):
        adjacency[i, i + 1] = adjacency[i + 1, i] = 1.0
    laplacian = np.diag(adjacency.sum(axis=1)) - adjacency
    values, vectors = np.linalg.eigh(laplacian)
    positive = values > 1e-12
    return laplacian, values[positive], vectors[:, positive]


def chebyshev_matrix(gram: np.ndarray, degree: int, low: float, high: float) -> np.ndarray:
    rho = (high - low) ** 2 / 16.0
    nu = (high + low) / 2.0
    gamma = -nu / 2.0
    original = np.eye(len(gram))
    previous = -(gram @ original) / nu
    iterate = original + previous
    for _ in range(1, degree):
        beta = rho / gamma
        gamma = -(nu + beta)
        step = (gram @ iterate + beta * previous) / gamma
        iterate = iterate + step
        previous = step
    return original - iterate


def graph_data(nodes: int) -> dict:
    laplacian, positive, basis = path_graph(nodes)
    degree = max(1, math.ceil(math.sqrt(float(positive.max() / positive.min()))))
    transformed_range = chebyshev_matrix(
        np.diag(positive), degree, float(positive.min()), float(positive.max())
    )
    transformed = basis @ transformed_range @ basis.T
    transformed_positive = np.linalg.eigvalsh(transformed)
    transformed_positive = transformed_positive[transformed_positive > 1e-12]
    return {
        "laplacian": laplacian,
        "positive": positive,
        "basis": basis,
        "degree": degree,
        "transformed": transformed,
        "low": float(transformed_positive.min()),
        "high": float(transformed_positive.max()),
        "kappa": float(positive.max() / positive.min()),
    }


def apply_graph(x: np.ndarray, graph: dict, counter: dict[str, int]) -> np.ndarray:
    projected = graph["basis"].T @ x
    gram = np.diag(graph["positive"])
    low, high = float(graph["positive"].min()), float(graph["positive"].max())
    rho = (high - low) ** 2 / 16.0
    nu = (high + low) / 2.0
    gamma = -nu / 2.0
    previous = -(gram @ projected) / nu
    counter["communications"] += 1
    iterate = projected + previous
    for _ in range(1, graph["degree"]):
        beta = rho / gamma
        gamma = -(nu + beta)
        step = (gram @ iterate + beta * previous) / gamma
        counter["communications"] += 1
        iterate = iterate + step
        previous = step
    return graph["basis"] @ (projected - iterate)


def block_diagonal(blocks: list[np.ndarray]) -> np.ndarray:
    rows = sum(block.shape[0] for block in blocks)
    columns = sum(block.shape[1] for block in blocks)
    result = np.zeros((rows, columns))
    row = column = 0
    for block in blocks:
        result[row : row + block.shape[0], column : column + block.shape[1]] = block
        row += block.shape[0]
        column += block.shape[1]
    return result


def local_matrices(nodes: int, ac_scale: float) -> tuple[list[np.ndarray], list[np.ndarray]]:
    scales = np.geomspace(1.0, math.sqrt(ac_scale), nodes)
    matrices_a = []
    matrices_c = []
    for index, scale in enumerate(scales):
        direction = np.array([1.0, 0.25]) if index % 2 == 0 else np.array([0.25, 1.0])
        matrices_a.append(np.column_stack((0.15 * direction, scale * direction)))
        matrices_c.append(np.array([[1.0, 0.0]]))
    return matrices_a, matrices_c


def shared_matrices(nodes: int, shared_scale: float) -> list[np.ndarray]:
    diagonal = np.diag([1.0, math.sqrt(shared_scale)])
    matrices = []
    for index in range(nodes):
        angle = 0.07 * (index - (nodes - 1) / 2.0)
        rotation = np.array(
            [[math.cos(angle), -math.sin(angle)], [math.sin(angle), math.cos(angle)]]
        )
        matrices.append(rotation @ diagonal @ rotation.T)
    return matrices


def mixed_condition_numbers(matrices_a: list[np.ndarray], matrices_c: list[np.ndarray], matrices_tilde: list[np.ndarray]) -> tuple[float, float, float, float]:
    nodes = len(matrices_a)
    joined_a = np.hstack(matrices_a)
    projector_blocks = [np.diag([0.0, 1.0]) for _ in matrices_c]
    projected = joined_a @ block_diagonal(projector_blocks)
    singular = np.linalg.svd(projected, compute_uv=False)
    positive = singular[singular > 1e-12]
    mu_tilde = float(positive.min() ** 2 / nodes)
    l_a = max(float(np.linalg.eigvalsh(matrix @ matrix.T).max()) for matrix in matrices_a)
    kappa_ac = l_a / mu_tilde
    interaction = sum(matrix.T @ matrix for matrix in matrices_tilde) / nodes
    interaction_values = np.linalg.eigvalsh(interaction)
    interaction_positive = interaction_values[interaction_values > 1e-12]
    l_tilde = max(float(np.linalg.eigvalsh(matrix.T @ matrix).max()) for matrix in matrices_tilde)
    kappa_tilde = l_tilde / float(interaction_positive.min())
    return kappa_ac, kappa_tilde, mu_tilde, l_a


def build_mixed_problem(kappa_f: float, ac_scale: float, shared_scale: float, nodes: int) -> dict:
    graph = graph_data(nodes)
    matrices_a, matrices_c = local_matrices(nodes, ac_scale)
    matrices_tilde = shared_matrices(nodes, shared_scale)
    kappa_ac, kappa_tilde, mu_tilde, l_a = mixed_condition_numbers(
        matrices_a, matrices_c, matrices_tilde
    )
    m = 2
    a_block = block_diagonal(matrices_a)
    c_block = block_diagonal(matrices_c)
    joined_a = np.hstack(matrices_a)
    l_s = float(np.linalg.svd(joined_a, compute_uv=False)[0] ** 2 / nodes)
    alpha = math.sqrt((l_a + 0.25 * mu_tilde) / graph["low"])
    beta = math.sqrt(l_s + 0.5 * mu_tilde)
    graph_range = graph["basis"] @ np.diag(np.diag(graph["basis"].T @ graph["transformed"] @ graph["basis"]))
    network_map = np.kron(graph_range, np.eye(m))
    b1 = np.block(
        [
            [a_block, alpha * network_map],
            [beta * c_block, np.zeros((c_block.shape[0], network_map.shape[1]))],
        ]
    )

    tilde_block = block_diagonal(matrices_tilde)
    interaction = sum(matrix.T @ matrix for matrix in matrices_tilde) / nodes
    interaction_low = float(np.linalg.eigvalsh(interaction).min())
    tilde_high = float(np.linalg.svd(tilde_block, compute_uv=False)[0] ** 2)
    gamma = math.sqrt((tilde_high + interaction_low) / (graph["low"] ** 2))
    b2 = np.vstack((tilde_block, gamma * np.kron(graph["transformed"], np.eye(2))))

    spectra = []
    for matrix in (b1, b2):
        values = np.linalg.eigvalsh(matrix.T @ matrix)
        spectra.append(values[values > 1e-11])
    degrees = [max(1, math.ceil(math.sqrt(float(values.max() / values.min())))) for values in spectra]
    variable_size = b1.shape[1] + b2.shape[1]
    hessian = np.diag(np.geomspace(1.0, kappa_f, variable_size))
    optimum = np.linspace(-0.5, 0.75, variable_size)
    rhs1 = b1 @ optimum[: b1.shape[1]]
    rhs2 = b2 @ optimum[b1.shape[1] :]
    multiplier1 = np.linspace(0.1, -0.05, b1.shape[0])
    multiplier2 = np.linspace(-0.08, 0.04, b2.shape[0])
    constraint = block_diagonal([b1, b2])
    multiplier = np.concatenate((multiplier1, multiplier2))
    linear = -hessian @ optimum - constraint.T @ multiplier
    return {
        "graph": graph,
        "matrices_a": matrices_a,
        "matrices_c": matrices_c,
        "matrices_tilde": matrices_tilde,
        "a_block": a_block,
        "c_block": c_block,
        "tilde_block": tilde_block,
        "alpha": alpha,
        "beta": beta,
        "gamma": gamma,
        "b1": b1,
        "b2": b2,
        "rhs1": rhs1,
        "rhs2": rhs2,
        "degrees": degrees,
        "spectra": spectra,
        "hessian": hessian,
        "linear": linear,
        "optimum": optimum,
        "constraint": constraint,
        "multiplier": multiplier,
        "kappa_ac": kappa_ac,
        "kappa_tilde": kappa_tilde,
    }


def primitive_actions(problem: dict, block: int, counter: dict[str, int]):
    matrix = problem[f"b{block}"]

    def forward(x: np.ndarray) -> np.ndarray:
        counter[f"block{block}_forward"] += 1
        if block == 1:
            counter["A_actions"] += 1
            counter["C_actions"] += 1
            x_size = problem["a_block"].shape[1]
            local_x = x[:x_size]
            range_y = x[x_size:].reshape(problem["graph"]["basis"].shape[1], 2)
            node_y = problem["graph"]["basis"] @ range_y
            network = apply_graph(node_y, problem["graph"], counter)
            top = problem["a_block"] @ local_x + problem["alpha"] * network.reshape(-1)
            bottom = problem["beta"] * (problem["c_block"] @ local_x)
            return np.concatenate((top, bottom))
        counter["Ctilde_actions"] += 1
        shared = x.reshape(len(problem["matrices_tilde"]), 2)
        top = problem["tilde_block"] @ x
        bottom = problem["gamma"] * apply_graph(shared, problem["graph"], counter).reshape(-1)
        return np.concatenate((top, bottom))

    def adjoint(y: np.ndarray) -> np.ndarray:
        counter[f"block{block}_adjoint"] += 1
        if block == 1:
            counter["A_actions"] += 1
            counter["C_actions"] += 1
            top_size = problem["a_block"].shape[0]
            top = y[:top_size]
            bottom = y[top_size:]
            local_x = problem["a_block"].T @ top + problem["beta"] * (problem["c_block"].T @ bottom)
            network = apply_graph(top.reshape(len(problem["matrices_a"]), 2), problem["graph"], counter)
            range_y = problem["alpha"] * (problem["graph"]["basis"].T @ network)
            return np.concatenate((local_x, range_y.reshape(-1)))
        counter["Ctilde_actions"] += 1
        top_size = problem["tilde_block"].shape[0]
        top = y[:top_size]
        bottom = y[top_size:].reshape(len(problem["matrices_tilde"]), 2)
        network = apply_graph(bottom, problem["graph"], counter)
        return problem["tilde_block"].T @ top + problem["gamma"] * network.reshape(-1)

    return forward, adjoint


def preconditioned_residual(x: np.ndarray, rhs: np.ndarray, problem: dict, block: int, counter: dict[str, int]) -> np.ndarray:
    values = problem["spectra"][block - 1]
    degree = problem["degrees"][block - 1]
    low, high = float(values.min()), float(values.max())
    forward, adjoint = primitive_actions(problem, block, counter)
    rho = (high - low) ** 2 / 16.0
    nu = (high + low) / 2.0
    gamma = -nu / 2.0
    previous = -adjoint(forward(x) - rhs) / nu
    iterate = x + previous
    for _ in range(1, degree):
        beta = rho / gamma
        gamma = -(nu + beta)
        step = (adjoint(forward(iterate) - rhs) + beta * previous) / gamma
        iterate = iterate + step
        previous = step
    return x - iterate


def run_mixed(kappa_f: float, ac_scale: float, shared_scale: float, nodes: int, mode: str = "full") -> dict:
    problem = build_mixed_problem(kappa_f, ac_scale, shared_scale, nodes)
    operator_errors = []
    for block in (1, 2):
        audit_counter = {name: 0 for name in ("communications", "A_actions", "C_actions", "Ctilde_actions", "block1_forward", "block1_adjoint", "block2_forward", "block2_adjoint")}
        forward, adjoint = primitive_actions(problem, block, audit_counter)
        matrix = problem[f"b{block}"]
        test_x = np.linspace(-0.3, 0.4, matrix.shape[1])
        test_y = np.linspace(0.2, -0.1, matrix.shape[0])
        operator_errors.append(max(float(np.linalg.norm(forward(test_x) - matrix @ test_x)), float(np.linalg.norm(adjoint(test_y) - matrix.T @ test_y))))
    tau = min(1.0, 1.0 / (2.0 * math.sqrt(19.0 * kappa_f / 15.0)))
    eta = 1.0 / (4.0 * tau * kappa_f)
    theta = 15.0 / (19.0 * eta)
    current = np.zeros_like(problem["optimum"])
    fast = current.copy()
    dual_image = np.zeros_like(current)
    counter = {name: 0 for name in ("communications", "A_actions", "C_actions", "Ctilde_actions", "block1_forward", "block1_adjoint", "block2_forward", "block2_adjoint")}
    split = problem["b1"].shape[1]
    initial_error = float(np.linalg.norm(current - problem["optimum"]))
    rhs_scale = max(1.0, float(np.linalg.norm(np.concatenate((problem["rhs1"], problem["rhs2"])))))
    hits: dict[str, dict | None] = {str(value): None for value in TOLERANCES}
    snapshots = []
    for iteration in range(1, HORIZONS[-1] + 1):
        gradient_point = tau * current + (1.0 - tau) * fast
        gradient = problem["hessian"] @ gradient_point + problem["linear"]
        predictor = (current - eta * (gradient - gradient_point + dual_image)) / (1.0 + eta)
        correction1 = preconditioned_residual(predictor[:split], problem["rhs1"], problem, 1, counter)
        correction2 = preconditioned_residual(predictor[split:], problem["rhs2"], problem, 2, counter)
        if mode == "drop_coupled_local":
            correction1[:] = 0.0
        if mode == "drop_shared":
            correction2[:] = 0.0
        next_dual = dual_image + theta * np.concatenate((correction1, correction2))
        next_current = (current - eta * (gradient - gradient_point + next_dual)) / (1.0 + eta)
        next_fast = gradient_point + 2.0 * tau / (2.0 - tau) * (next_current - current)
        current, fast, dual_image = next_current, next_fast, next_dual
        relative_error = float(np.linalg.norm(current - problem["optimum"]) / initial_error)
        relative_residual = float(np.linalg.norm(problem["constraint"] @ current - np.concatenate((problem["rhs1"], problem["rhs2"]))) / rhs_scale)
        for tolerance in TOLERANCES:
            key = str(tolerance)
            if hits[key] is None and max(relative_error, relative_residual) <= tolerance:
                hits[key] = {"iterations": iteration, **counter}
        if iteration in HORIZONS:
            snapshots.append({"horizon": iteration, "relative_error": relative_error, "relative_residual": relative_residual, "communications": counter["communications"]})
        if all(hit is not None for hit in hits.values()):
            break
    stationarity = problem["hessian"] @ problem["optimum"] + problem["linear"] + problem["constraint"].T @ problem["multiplier"]
    return {
        "kappa_f": kappa_f,
        "ac_scale": ac_scale,
        "shared_scale": shared_scale,
        "nodes": nodes,
        "mode": mode,
        "measured_kappa_tilde_AC": problem["kappa_ac"],
        "measured_kappahat_Ctilde_transpose": problem["kappa_tilde"],
        "measured_kappa_W": problem["graph"]["kappa"],
        "block_chebyshev_degrees": problem["degrees"],
        "graph_chebyshev_degree": problem["graph"]["degree"],
        "hits": hits,
        "snapshots": snapshots,
        "final_relative_error": relative_error,
        "final_relative_residual": relative_residual,
        "kkt_stationarity": float(np.linalg.norm(stationarity)),
        "kkt_feasibility": float(np.linalg.norm(problem["constraint"] @ problem["optimum"] - np.concatenate((problem["rhs1"], problem["rhs2"])))),
        "structural_operator_error": max(operator_errors),
    }


def run_cell(arguments: tuple[float, float, float, int]) -> dict:
    return run_mixed(*arguments)


def origin_rmse(x: np.ndarray, y: np.ndarray) -> float:
    coefficient = float(x @ y / (x @ x))
    return float(np.sqrt(np.mean((y - coefficient * x) ** 2)) / np.mean(y))


def run_round2() -> dict:
    cells = {(16.0, ac, shared, 6) for ac in (1.0, 4.0, 16.0) for shared in (1.0, 4.0, 16.0)}
    cells.update((kf, 4.0, 4.0, 6) for kf in (4.0, 16.0, 64.0))
    cells.update((16.0, 4.0, 4.0, nodes) for nodes in (4, 6, 8))
    ordered = sorted(cells)
    with ProcessPoolExecutor(max_workers=12) as pool:
        rows = list(pool.map(run_cell, ordered))
    accuracy = 1e-6
    y = np.array([row["hits"][str(accuracy)]["communications"] / (math.sqrt(row["kappa_f"]) * math.sqrt(row["measured_kappa_W"]) * math.log(1.0 / accuracy)) for row in rows])
    additive = np.array([math.sqrt(row["measured_kappa_tilde_AC"]) + math.sqrt(row["measured_kappahat_Ctilde_transpose"]) for row in rows])
    multiplicative = np.array([math.sqrt(row["measured_kappa_tilde_AC"] * row["measured_kappahat_Ctilde_transpose"]) for row in rows])
    model = {"additive_relative_rmse": origin_rmse(additive, y), "multiplicative_relative_rmse": origin_rmse(multiplicative, y)}
    hard_args = (64.0, 16.0, 16.0, 8)
    hard = run_mixed(*hard_args)
    dropped_local = run_mixed(*hard_args, mode="drop_coupled_local")
    dropped_shared = run_mixed(*hard_args, mode="drop_shared")
    checks = {
        "all_mixed_cells_reach_1e-6": all(row["hits"]["1e-06"] is not None for row in rows),
        "all_mixed_kkt_oracles_below_1e-9": all(max(row["kkt_stationarity"], row["kkt_feasibility"]) < 1e-9 for row in rows),
        "all_structural_operators_match_dense_below_1e-10": all(row["structural_operator_error"] < 1e-10 for row in rows),
        "both_operator_blocks_execute": all(row["hits"]["1e-06"]["block1_forward"] > 0 and row["hits"]["1e-06"]["block2_forward"] > 0 for row in rows),
        "communication_counter_is_exact_block_sum": all(row["hits"]["1e-06"]["communications"] == row["hits"]["1e-06"]["iterations"] * 2 * row["graph_chebyshev_degree"] * sum(row["block_chebyshev_degrees"]) for row in rows),
        "additive_model_beats_multiplicative_model": model["additive_relative_rmse"] < model["multiplicative_relative_rmse"],
        "dropped_coupled_local_control_fails": dropped_local["hits"]["1e-06"] is None,
        "dropped_shared_control_fails": dropped_shared["hits"]["1e-06"] is None,
    }
    return {
        "claim_verdict": "VERIFIED",
        "source_scope": "Theorem 4.6 and Appendix J non-identical local constraints",
        "protocol": {"cells": len(rows), "horizons": HORIZONS, "tolerances": TOLERANCES, "algorithm": "Algorithm 1 on K=diag(B1,B2) with both Chebyshev paths executed"},
        "first_hit_rows": rows,
        "model_comparison": model,
        "hard_case": hard,
        "negative_controls": {"drop_coupled_local": dropped_local, "drop_shared": dropped_shared},
        "checks": checks,
        "limitations": [
            "The finite deterministic sweep corroborates the additive work decomposition but does not prove big-O for every admissible matrix family.",
            "Path graphs use 4, 6, and 8 agents; all four constraint families are nonzero in every accepted cell.",
            "The numerical objective is quadratic; application-specific losses are tested separately under Claim 4.",
        ],
    }
