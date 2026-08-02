"""Generate publication figures and validate embedded evidence on compute."""

from __future__ import annotations

import html
import json
import math
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_claim(claim: int) -> dict:
    return json.loads(
        (ROOT / f".openresearch/artifacts/claim_{claim}/raw.json").read_text(
            encoding="utf-8"
        )
    )


def close(left, right, tolerance: float = 1e-12) -> bool:
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(
            close(left[key], right[key], tolerance) for key in left
        )
    if isinstance(left, (list, tuple)) and isinstance(right, (list, tuple)):
        return len(left) == len(right) and all(
            close(a, b, tolerance) for a, b in zip(left, right)
        )
    if isinstance(left, (int, float)) and isinstance(right, (int, float)):
        return math.isclose(float(left), float(right), rel_tol=tolerance, abs_tol=tolerance)
    return left == right


def validate_embedded_evidence(round1: dict, round2: dict, round3: dict, round4: dict) -> dict:
    raw1, raw2, raw3, raw4, raw5 = [load_claim(index) for index in range(1, 6)]
    return {
        "all_five_claim_raw_files_parse": all(
            isinstance(value, dict) for value in (raw1, raw2, raw3, raw4, raw5)
        ),
        "claim1_slopes_regenerate_exactly": close(
            raw1["round1"]["observed_log_log_slopes"], round1["observed_log_log_slopes"]
        ),
        "claim2_model_comparison_regenerates_exactly": close(
            raw2["round2"]["model_comparison"], round2["model_comparison"]
        ),
        "claim3_first_hits_regenerate_exactly": close(
            raw3["selected_first_hits"], round3["selected_first_hits"]
        ),
        "claim4_summaries_regenerate_exactly": close(
            raw4["summaries"], round4["summaries"]
        ),
        "claim5_is_same_apapc_evidence_as_claim1": close(raw5, raw1),
    }


def svg_frame(title: str, body: str, subtitle: str) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="960" height="540" viewBox="0 0 960 540" role="img">'
        '<rect width="960" height="540" fill="#0b1020"/>'
        f'<text x="48" y="58" fill="#f8fafc" font-family="sans-serif" font-size="28" font-weight="700">{html.escape(title)}</text>'
        f'<text x="48" y="88" fill="#94a3b8" font-family="sans-serif" font-size="15">{html.escape(subtitle)}</text>'
        f'{body}'
        '<text x="48" y="515" fill="#64748b" font-family="sans-serif" font-size="13">HF cpu-upgrade · fixed uv command · deterministic evidence</text>'
        '</svg>'
    )


def text(x: float, y: float, value: str, size: int = 15, color: str = "#cbd5e1", anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="sans-serif" font-size="{size}" text-anchor="{anchor}">{html.escape(value)}</text>'


def headline_figure(round1: dict) -> str:
    labels = ("κ_f", "κ̂_C̃ᵀ", "κ_W")
    values = tuple(round1["observed_log_log_slopes"][key] for key in ("kappa_f", "kappa_Ctilde_transpose", "kappa_W"))
    body = '<line x1="80" y1="392" x2="900" y2="392" stroke="#334155" stroke-width="2"/>'
    body += '<line x1="80" y1="167" x2="900" y2="167" stroke="#f59e0b" stroke-dasharray="8 8"/>'
    body += text(895, 158, "square-root reference = 0.5", 14, "#fbbf24", "end")
    for index, (label, value) in enumerate(zip(labels, values)):
        x = 160 + 270 * index
        height = 450 * value
        body += f'<rect x="{x}" y="{392-height}" width="120" height="{height}" rx="8" fill="#22d3ee"/>'
        body += text(x + 60, 420, label, 18, "#e2e8f0", "middle")
        body += text(x + 60, 378 - height, f"{value:.3f}", 19, "#67e8f9", "middle")
    return svg_frame(
        "Exact APAPC recovers all three square-root factors",
        body,
        "Observed log-log communication slopes across 27 first-hit cells; theorem reference shown, not fitted.",
    )


def mixed_figure(round2: dict) -> str:
    model = round2["model_comparison"]
    values = (model["additive_relative_rmse"], model["multiplicative_relative_rmse"])
    labels = ("Paper additive factor", "Multiplicative alternative")
    colors = ("#34d399", "#fb7185")
    body = ""
    for index, (label, value, color) in enumerate(zip(labels, values, colors)):
        y = 175 + index * 145
        width = 650 * value / max(values)
        body += text(70, y - 16, label, 18)
        body += f'<rect x="70" y="{y}" width="{width}" height="52" rx="8" fill="{color}"/>'
        body += text(90 + width, y + 35, f"relative RMSE {value:.4f}", 17, "#f8fafc")
    body += text(70, 450, f"Hard case: {round2['hard_case']['hits']['1e-06']['iterations']} iterations · {round2['hard_case']['hits']['1e-06']['communications']:,} communications", 17)
    return svg_frame(
        "The full mixed operator favors the theorem's additive work factor",
        body,
        "Post-hoc fit on a formula-independent sweep; lower relative RMSE is better.",
    )


def sliding_figure(round3: dict) -> str:
    selected = round3["selected_first_hits"]
    tolerances = ("0.05", "0.02", "0.01")
    body = '<line x1="90" y1="410" x2="900" y2="410" stroke="#334155" stroke-width="2"/>'
    for index, tolerance in enumerate(tolerances):
        hit = selected[tolerance]["hits"][tolerance]
        x = 135 + index * 270
        height = 245 * math.log10(hit["subgradient_calls"] + 1) / 4.0
        body += f'<rect x="{x}" y="{410-height}" width="120" height="{height}" rx="8" fill="#a78bfa"/>'
        body += text(x + 60, 438, f"tol {tolerance}", 17, "#e2e8f0", "middle")
        body += text(x + 60, 390 - height, f"{hit['matrix_actions']} matrix", 15, "#c4b5fd", "middle")
        body += text(x + 60, 410 - height + 28, f"{hit['subgradient_calls']:,} subgrad", 15, "#f8fafc", "middle")
    literal = round3["line_12_interpretation_audit"]["paper_literal"]
    body += text(895, 475, f"Printed line-12 control: residual {literal['final_constraint_residual']:.2f}, no hit", 16, "#fb7185", "end")
    return svg_frame(
        "Gradient Sliding separates matrix and nonsmooth-oracle work",
        body,
        "First-hit budgets use Lan's source-consistent recurrence; vertical height is log-scaled subgradient work.",
    )


def applications_figure(round4: dict) -> str:
    summaries = round4["summaries"]
    groups = (
        ("HFL", summaries["hfl_test_mse"]["mean"], summaries["hfl_test_mse"]["mean"] + summaries["hfl_improvement_over_no_consensus"]["mean"]),
        ("VFL", summaries["vfl_test_mse"]["mean"], summaries["vfl_test_mse"]["mean"] + summaries["vfl_improvement_over_dropped_party"]["mean"]),
        ("MTL", summaries["mtl_test_mse"]["mean"], summaries["mtl_test_mse"]["mean"] + summaries["mtl_improvement_over_independent"]["mean"]),
    )
    body = ""
    for index, (label, full, control) in enumerate(groups):
        x = 55 + index * 300
        scale = 190 / control
        body += text(x + 125, 150, label, 22, "#f8fafc", "middle")
        body += f'<rect x="{x+35}" y="{390-full*scale}" width="78" height="{full*scale}" fill="#34d399" rx="6"/>'
        body += f'<rect x="{x+145}" y="{390-control*scale}" width="78" height="{control*scale}" fill="#fb7185" rx="6"/>'
        body += text(x + 74, 420, f"full {full:.3f}", 14, "#a7f3d0", "middle")
        body += text(x + 184, 420, f"control {control:.3f}", 14, "#fecdd3", "middle")
    body += text(55, 470, "Each panel is scaled to its own control; values are eight-seed held-out MSE means.", 15)
    return svg_frame(
        "Actual HFL, VFL, and MTL models beat structure-omission controls",
        body,
        "Green: full paper-aligned formulation. Rose: no-consensus, dropped-party, or independent-task control.",
    )


def controls_figure(round1: dict, round2: dict, round3: dict, round4: dict) -> str:
    hard = round1["hard_case"]
    control = round1["negative_controls"]["omitted_corrector"]
    values = (
        ("APAPC omitted corrector", hard["hits"]["1e-06"]["iterations"], control["hits"]["1e-06"]["iterations"]),
        ("Mixed dropped shared", round2["hard_case"]["final_relative_residual"], round2["negative_controls"]["drop_shared"]["final_relative_residual"]),
        ("GS printed line 12", round3["selected_first_hits"]["0.01"]["hits"]["0.01"]["constraint_residual"], round3["line_12_interpretation_audit"]["paper_literal"]["final_constraint_residual"]),
        ("VFL omitted mapping", max(row["representation_residual"] for row in round4["vfl_rows"]), min(row["omitted_representation_constraint_residual"] for row in round4["vfl_rows"])),
    )
    body = ""
    for index, (label, accepted, rejected) in enumerate(values):
        y = 145 + index * 88
        body += text(55, y, label, 17)
        body += text(410, y, f"accepted {accepted:.3g}", 16, "#34d399")
        body += text(650, y, f"control {rejected:.3g}", 16, "#fb7185")
    body += text(55, 465, "Controls intentionally omit an essential update or structural equation; each misses for that reason.", 15)
    return svg_frame(
        "Negative controls are discriminating, not ceremonial",
        body,
        "Raw units differ by row and are printed explicitly; comparisons are within rows only.",
    )


def build_publication(round1: dict, round2: dict, round3: dict, round4: dict) -> dict:
    figures = {
        "headline_complexity.svg": headline_figure(round1),
        "mixed_bound.svg": mixed_figure(round2),
        "gradient_sliding.svg": sliding_figure(round3),
        "applications.svg": applications_figure(round4),
        "negative_controls.svg": controls_figure(round1, round2, round3, round4),
    }
    checks = {
        "five_svg_figures_generated": len(figures) == 5,
        "all_figures_are_standalone_svg": all(
            value.startswith("<svg") and value.endswith("</svg>") for value in figures.values()
        ),
        "all_figures_have_accessibility_role": all('role="img"' in value for value in figures.values()),
        "no_figure_contains_secret_markers": not any(
            marker in value.lower()
            for value in figures.values()
            for marker in ("hf_token", "api_key", "authorization:")
        ),
    }
    return {"figures": figures, "checks": checks}


def validate_materialized_artifacts(publication: dict) -> dict:
    report_path = ROOT / "reports/full-reproduction/report.md"
    readme_path = ROOT / "README.md"
    notebook_path = ROOT / "notebooks/reproduction.py"
    report = report_path.read_text(encoding="utf-8")
    readme = readme_path.read_text(encoding="utf-8")
    image_links = re.findall(r"!\[[^]]*\]\((images/[^)]+)\)", report)
    materialized_figures = {}
    xml_roots = []
    for name in publication["figures"]:
        path = report_path.parent / "images" / name
        materialized_figures[name] = path.read_text(encoding="utf-8").strip()
        xml_roots.append(ET.fromstring(materialized_figures[name]).tag)
    marimo = subprocess.run(
        ["marimo", "check", str(notebook_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    raw_links = re.findall(r"\]\((\.\./\.\./\.openresearch/artifacts/[^)]+)\)", report)
    checks = {
        "all_five_report_images_are_linked": sorted(image_links)
        == sorted(f"images/{name}" for name in publication["figures"]),
        "materialized_figures_equal_hf_generated_payloads": all(
            materialized_figures[name] == value
            for name, value in publication["figures"].items()
        ),
        "all_materialized_figures_parse_as_svg_xml": all(
            root.endswith("svg") for root in xml_roots
        ),
        "all_report_raw_links_resolve": len(raw_links) == 15
        and all((report_path.parent / link).resolve().is_file() for link in raw_links),
        "readme_leads_with_reproduction": readme.startswith("# Reproduction:"),
        "readme_contains_exact_fixed_command": "uv sync --frozen && uv run --frozen python reproduce.py" in readme,
        "readme_accounts_for_main": "Not run as an experiment (publication surface)" in readme,
        "marimo_check_passes": marimo.returncode == 0,
    }
    return {
        "report": str(report_path.relative_to(ROOT)),
        "notebook": str(notebook_path.relative_to(ROOT)),
        "marimo_command": f"marimo check {notebook_path.relative_to(ROOT)}",
        "marimo_exit_code": marimo.returncode,
        "marimo_stdout": marimo.stdout,
        "marimo_stderr": marimo.stderr,
        "image_links": image_links,
        "raw_links": raw_links,
        "checks": checks,
    }


def logbook_files(node: dict) -> list[str]:
    return [node["file"], *sum((logbook_files(child) for child in node["children"]), [])]


def validate_space_candidate() -> dict:
    candidate_root = ROOT / "space_candidate"
    logbook = json.loads((candidate_root / "logbook.json").read_text(encoding="utf-8"))
    manifest_lines = (
        ROOT / ".openresearch/artifacts/historical_judged_space/MANIFEST.sha256"
    ).read_text(encoding="utf-8").splitlines()
    historical_paths = {line.split("  ", 1)[1] for line in manifest_lines if "  " in line}
    files = logbook_files(logbook["root"])
    current_files = [name for name in files if name.startswith("pages/current/")]
    historical_files = [name for name in files if not name.startswith("pages/current/")]
    current_text = "\n".join(
        (candidate_root / name).read_text(encoding="utf-8") for name in current_files
    )
    claim_pages = [
        (candidate_root / f"pages/current/claim-{index}.md").read_text(encoding="utf-8")
        for index in range(1, 6)
    ]
    visibility = (candidate_root / "pages/current/visibility.md").read_text(
        encoding="utf-8"
    )
    checks = {
        "space_id_is_exact_target": logbook["space_id"] == "DineshAI/KS6RbZMt8L",
        "canonical_root_is_current": logbook["root"]["file"] == "pages/current/index.md",
        "historical_tree_has_exact_label": any(
            child["title"] == "Historical rejected baseline"
            for child in logbook["root"]["children"]
        ),
        "all_current_logbook_pages_exist": len(current_files) == 8
        and all((candidate_root / name).is_file() for name in current_files),
        "all_historical_page_paths_are_protected": all(
            name in historical_paths for name in historical_files
        ),
        "all_claim_pages_expose_code_raw_checker_and_control": all(
            ("source]" in page.lower() or "executable" in page.lower())
            and "raw json" in page.lower()
            and "checker" in page.lower()
            and "control" in page.lower()
            for page in claim_pages
        ),
        "all_claim_pages_have_status_and_confidence": all(
            "Verdict: VERIFIED" in page and "Confidence:" in page for page in claim_pages
        ),
        "visibility_matrix_has_five_complete_rows": sum(
            line.startswith("| ") and "| VERIFIED |" in line
            for line in visibility.splitlines()
        ) == 5,
        "historical_baseline_is_not_called_current": "supersedes" in current_text
        and "Historical rejected baseline" in current_text,
        "candidate_pages_contain_no_secret_markers": not any(
            marker in current_text.lower()
            for marker in ("hf_token", "api_key", "authorization:", "bearer ")
        ),
    }
    return {
        "logbook": "space_candidate/logbook.json",
        "canonical_entrypoint": logbook["root"]["file"],
        "reachable_current_files": current_files,
        "reachable_historical_files": historical_files,
        "protected_historical_path_count": len(historical_paths),
        "checks": checks,
    }
