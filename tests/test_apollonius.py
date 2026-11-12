"""Comprehensive test suite for GEOMETOR • apollonius."""

from __future__ import annotations

import importlib.util
import json
import math
import xml.etree.ElementTree as ET
from pathlib import Path

from geometor.apollonius import (
    CODEX_UNITS,
    CODEX_UNITS_BY_SLUG,
    __version__,
    default_resources_dir,
    load_concordance,
    render_bibliography_rst,
    render_concordance_rst,
    render_glossary_rst,
    render_persons_rst,
    verify_codex_tracks,
    verify_concordance,
    write_apparatus_pages,
)
from geometor.apollonius.cli import main as cli_main
from geometor.apollonius.compile_codex import EXPECTED_SVG_FIGURES

REPO_ROOT = Path(__file__).resolve().parents[1]


def _load_build_figures_module():
    script_path = REPO_ROOT / "scripts" / "build_figures.py"
    spec = importlib.util.spec_from_file_location("apollonius_build_figures", script_path)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_version_and_codex_unit_registry() -> None:
    assert __version__ == "0.1.0"
    assert len(CODEX_UNITS) == 8
    expected_slugs = [
        "preface-intro",
        "book-1",
        "book-2",
        "book-3",
        "book-4",
        "book-5",
        "books-6-7",
        "lost-works-pappus",
    ]
    assert [u.slug for u in CODEX_UNITS] == expected_slugs
    assert set(CODEX_UNITS_BY_SLUG.keys()) == set(expected_slugs)


def test_provenance_manifest_and_concordance_integrity() -> None:
    errors = verify_concordance()
    assert errors == [], f"Concordance verification errors: {errors}"

    res_dir = default_resources_dir()
    manifest = json.loads((res_dir / "sources_manifest.json").read_text(encoding="utf-8"))
    heath_ed = manifest["editions"][0]
    assert heath_ed["id"] == "heath-1896-conics"
    assert heath_ed["archival_pdf_bytes"] == 20397578
    assert (
        heath_ed["archival_pdf_sha256"]
        == "b8c059610cfdb28c5a3ca0d397223327d6dce1803a791dc278daf2ff576ed7ad"
    )

    raw_conc, mappings = load_concordance()
    assert raw_conc["metadata"]["classical_propositions_total"] == 387
    assert raw_conc["metadata"]["heath_consolidated_propositions_total"] == 147
    assert len(mappings) >= 20
    assert len(raw_conc["sympy_geometry_gaps"]) >= 5


def test_codex_tracks_and_zero_embedded_python() -> None:
    errors = verify_codex_tracks()
    assert errors == [], f"Codex track verification errors: {errors}"

    conics_dir = REPO_ROOT / "docsrc" / "conics"
    track_files = list(conics_dir.glob("*/*-*.rst"))
    assert len(track_files) == 24


def test_all_twelve_svg_plates_valid_xml_and_euclid_graphic() -> None:
    figures_dir = REPO_ROOT / "docsrc" / "_static" / "figures"
    assert len(EXPECTED_SVG_FIGURES) == 12
    for svg_name in EXPECTED_SVG_FIGURES:
        svg_path = figures_dir / svg_name
        assert svg_path.is_file(), f"Missing SVG figure {svg_name}"
        raw_svg = svg_path.read_text(encoding="utf-8")
        assert "euclid-graphic" in raw_svg
        assert "data-ref=" in raw_svg
        root = ET.fromstring(raw_svg)
        assert root.tag.endswith("svg")


def test_exact_geometric_solvers_in_build_figures() -> None:
    bf = _load_build_figures_module()

    # 1. Verify all 8 solutions to the Problem of Apollonius (CCC)
    c1 = (0.0, 1.85, 0.92)
    c2 = (-1.95, -1.25, 1.05)
    c3 = (2.10, -1.10, 0.78)
    solutions = bf._solve_apollonius_ccc(c1, c2, c3)
    assert len(solutions) == 8
    for x, y, r, _signs in solutions:
        for cx, cy, cr in (c1, c2, c3):
            dist = math.hypot(x - cx, y - cy)
            tangency_err = min(abs(dist - (r + cr)), abs(dist - abs(r - cr)))
            assert tangency_err < 1e-6

    # 2. Verify 4 distinct real normals to the ellipse from an interior point of the evolute
    a, b = 3.2, 2.0
    ox, oy = 0.52, 0.36
    thetas = bf._solve_ellipse_normals(a, b, ox, oy)
    assert len(thetas) == 4
    for th in thetas:
        px, py = a * math.cos(th), b * math.sin(th)
        tx, ty = -a * math.sin(th), b * math.cos(th)
        dot = (ox - px) * tx + (oy - py) * ty
        assert abs(dot) < 1e-6


def test_apparatus_rendering_and_cli(tmp_path: Path, capsys) -> None:
    conc_rst = render_concordance_rst()
    bib_rst = render_bibliography_rst()
    per_rst = render_persons_rst()
    glo_rst = render_glossary_rst()

    assert ".. _conics-concordance:" in conc_rst
    assert ".. _cite-heath-1896:" in bib_rst
    assert ".. _person-apollonius:" in per_rst
    assert ".. _term-parabole:" in glo_rst

    written = write_apparatus_pages(docsrc_conics_dir=tmp_path)
    assert len(written) == 4
    for p in written:
        assert p.is_file() and p.stat().st_size > 500

    assert cli_main(["summary"]) == 0
    out_summary = capsys.readouterr().out
    assert "387 classical -> 147 Heath consolidated" in out_summary

    assert cli_main(["verify"]) == 0
    out_verify = capsys.readouterr().out
    assert "OK:" in out_verify
