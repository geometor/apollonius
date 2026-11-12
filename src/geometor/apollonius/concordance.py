"""Canonical Codex Unit registry and cross-corpus concordance verifier for Apollonius's Conics."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CodexUnitSpec:
    """Metadata specification for one 3-track unit in ``docsrc/conics/``."""

    unit_number: int
    slug: str
    title: str
    heath_loci: str
    classical_scope: str
    figures: tuple[str, ...]


@dataclass(frozen=True)
class PropositionMapping:
    """Typed cross-corpus mapping record loaded from ``concordance.json``."""

    id: str
    classical_locus: str
    heath_prop: str
    heath_pages: str
    pdf_pages: str
    codex_unit: str
    figure: str | None
    topic: str
    euclid_refs: tuple[str, ...]
    ecosystem_links: tuple[str, ...]


CODEX_UNITS: tuple[CodexUnitSpec, ...] = (
    CodexUnitSpec(
        unit_number=0,
        slug="preface-intro",
        title="Unit 0 — Preface, General Introduction & Apollonius's Prefatory Letters",
        heath_loci="Heath pp. vii–clxx (PDF 15–178)",
        classical_scope="Prefatory Letters to Eudemus (Books I–II) & Attalus (Books IV–VII); Menaechmus, Aristaeus, Euclid & Archimedes",
        figures=("fig_oblique_cone_sections.svg",),
    ),
    CodexUnitSpec(
        unit_number=1,
        slug="book-1",
        title="Unit 1 — Book I: Generation of the Cone & Fundamental Symptoms",
        heath_loci="Heath Props. 1–27, pp. 1–52 (PDF 181–232)",
        classical_scope="Book I Defs. & Props. I.1–60 (Parabola, Hyperbola, Ellipse, Opposite Branches, Tangents & Coordinate Change)",
        figures=(
            "fig_oblique_cone_sections.svg",
            "fig_application_of_areas.svg",
            "fig_tangent_harmonic_division.svg",
        ),
    ),
    CodexUnitSpec(
        unit_number=2,
        slug="book-2",
        title="Unit 2 — Book II: Asymptotes, Conjugate Hyperbolas & Secant Intercepts",
        heath_loci="Heath Props. 28–53, pp. 53–94 (PDF 233–274)",
        classical_scope="Book II Props. II.1–53 (Asymptotes xy = const, Bisected Tangents, Equal Secant Intercepts & Finding Axes)",
        figures=("fig_hyperbola_asymptotes_secant.svg",),
    ),
    CodexUnitSpec(
        unit_number=3,
        slug="book-3",
        title="Unit 3 — Book III: Chord Rectangles, Harmonic Poles & Polars, Foci & the 4-Line Locus",
        heath_loci="Heath Props. 54–76, pp. 95–125 (PDF 275–305)",
        classical_scope="Book III Props. III.1–56 (Power of Chords, Harmonic Polarity, Central Foci & Three-/Four-Line Locus)",
        figures=(
            "fig_harmonic_pole_polar.svg",
            "fig_central_conic_foci.svg",
            "fig_three_four_line_locus.svg",
        ),
    ),
    CodexUnitSpec(
        unit_number=4,
        slug="book-4",
        title="Unit 4 — Book IV: Number of Intersections & Tangencies of Conics",
        heath_loci="Heath Props. 77–83, pp. 126–138 (PDF 306–318)",
        classical_scope="Book IV Props. IV.1–57 (Converse Polar Tangents, At Most Four Intersection Points & Conic Pencils)",
        figures=("fig_four_point_conic_pencil.svg",),
    ),
    CodexUnitSpec(
        unit_number=5,
        slug="book-5",
        title="Unit 5 — Book V: Normals, Minimum & Maximum Lines, Subnormals & the Evolute",
        heath_loci="Heath Props. 84–113, pp. 139–196 (PDF 319–376)",
        classical_scope="Book V Props. V.1–77 (Subnormals, Evolute Diorismos of 2/3/4 Normals & Rectangular-Hyperbola Construction)",
        figures=("fig_normals_evolute.svg",),
    ),
    CodexUnitSpec(
        unit_number=6,
        slug="books-6-7",
        title="Unit 6 — Books VI & VII: Equal and Similar Conics & Conjugate Diameters",
        heath_loci="Heath Props. 114–147, pp. 197–254 (PDF 377–434)",
        classical_scope="Book VI Props. VI.1–33 & Book VII Props. VII.1–51 (Similarity, Cone Embedding & Apollonius's Conjugate Diameter Theorems)",
        figures=("fig_conjugate_diameters_theorems.svg",),
    ),
    CodexUnitSpec(
        unit_number=7,
        slug="lost-works-pappus",
        title="Unit 7 — Appendix: The Lost Analytic Treasury in Pappus Book VII",
        heath_loci="Heath Intro pp. lxviii, cxxv–clvi; Pappus Synagoge VII",
        classical_scope="Tangencies (Problem of Apollonius CCC), Plane Loci (Circle of Apollonius), Cutting Off of a Ratio, Determinate Section & Inclinations",
        figures=(
            "fig_problem_of_apollonius_ccc.svg",
            "fig_apollonius_circle_locus.svg",
        ),
    ),
)

CODEX_UNITS_BY_SLUG: dict[str, CodexUnitSpec] = {u.slug: u for u in CODEX_UNITS}


def default_resources_dir() -> Path:
    """Return the repository ``resources/conics`` directory."""
    return Path(__file__).resolve().parents[3] / "resources" / "conics"


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_concordance(resources_dir: Path | None = None) -> tuple[dict[str, Any], list[PropositionMapping]]:
    """Load ``concordance.json`` and parse typed :class:`PropositionMapping` records."""
    res_dir = resources_dir or default_resources_dir()
    raw = json.loads((res_dir / "concordance.json").read_text(encoding="utf-8"))
    mappings = [
        PropositionMapping(
            id=item["id"],
            classical_locus=item["classical_locus"],
            heath_prop=item["heath_prop"],
            heath_pages=item["heath_pages"],
            pdf_pages=item["pdf_pages"],
            codex_unit=item["codex_unit"],
            figure=item.get("figure"),
            topic=item["topic"],
            euclid_refs=tuple(item.get("euclid_refs", ())),
            ecosystem_links=tuple(item.get("ecosystem_links", ())),
        )
        for item in raw.get("entries", [])
    ]
    return raw, mappings


def verify_concordance(resources_dir: Path | None = None) -> list[str]:
    """Validate provenance SHA-256 hashes, classical proposition totals, and apparatus registries.

    Returns an empty list when all checks pass, or human-readable error strings otherwise.
    """
    res_dir = resources_dir or default_resources_dir()
    errors: list[str] = []

    required_files = (
        "sources_manifest.json",
        "concordance.json",
        "persons.json",
        "citations.json",
        "glossary.json",
    )
    for filename in required_files:
        if not (res_dir / filename).is_file():
            errors.append(f"Missing required resource file: {res_dir / filename}")
    if errors:
        return errors

    manifest = json.loads((res_dir / "sources_manifest.json").read_text(encoding="utf-8"))
    for tracked in manifest.get("tracked_files", []):
        fpath = res_dir / tracked["filename"]
        if not fpath.is_file():
            errors.append(f"Missing tracked provenance file: {fpath}")
            continue
        actual_bytes = fpath.stat().st_size
        actual_sha = _sha256_file(fpath)
        if actual_bytes != tracked["bytes"]:
            errors.append(
                f"Byte-size mismatch for {tracked['filename']}: expected {tracked['bytes']}, got {actual_bytes}"
            )
        if actual_sha != tracked["sha256"]:
            errors.append(
                f"SHA-256 mismatch for {tracked['filename']}: expected {tracked['sha256']}, got {actual_sha}"
            )

    raw_conc, mappings = load_concordance(res_dir)
    meta = raw_conc.get("metadata", {})
    book_counts = meta.get("book_counts", {})
    summed_classical = sum(int(b["classical_propositions"]) for b in book_counts.values())
    if summed_classical != 387:
        errors.append(f"Classical Books I–VII proposition sum must equal 387, got {summed_classical}")
    if int(meta.get("heath_consolidated_propositions_total", 0)) != 147:
        errors.append("Heath consolidated proposition count must equal 147")

    covered_units = {m.codex_unit for m in mappings}
    for unit in CODEX_UNITS:
        if unit.slug not in covered_units:
            errors.append(f"Codex unit '{unit.slug}' has zero concordance entries")

    for mapping in mappings:
        if mapping.codex_unit not in CODEX_UNITS_BY_SLUG:
            errors.append(f"Concordance entry '{mapping.id}' references unknown unit '{mapping.codex_unit}'")

    gaps = raw_conc.get("sympy_geometry_gaps", [])
    if len(gaps) < 5:
        errors.append("Concordance must document at least 5 sympy.geometry symbolic conic gaps")

    persons = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    for must_have_person in (
        "apollonius",
        "menaechmus",
        "aristaeus",
        "euclid",
        "archimedes",
        "eudemus-pergamum",
        "attalus",
        "pappus",
        "eutocius",
        "thabit-ibn-qurra",
        "halley",
        "heiberg",
        "heath",
    ):
        if must_have_person not in persons:
            errors.append(f"Missing required prosopography entry '{must_have_person}' in persons.json")

    return errors
