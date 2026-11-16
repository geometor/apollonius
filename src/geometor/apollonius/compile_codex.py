"""Apparatus RST generator and 3-track Book Codex integrity verifier for GEOMETOR • apollonius."""

from __future__ import annotations

import json
import re
from pathlib import Path

from geometor.apollonius.concordance import (
    CODEX_UNITS,
    default_resources_dir,
    load_concordance,
)

EXPECTED_SVG_FIGURES: tuple[str, ...] = (
    "fig_oblique_cone_sections.svg",
    "fig_application_of_areas.svg",
    "fig_tangent_harmonic_division.svg",
    "fig_hyperbola_asymptotes_secant.svg",
    "fig_harmonic_pole_polar.svg",
    "fig_central_conic_foci.svg",
    "fig_three_four_line_locus.svg",
    "fig_four_point_conic_pencil.svg",
    "fig_normals_evolute.svg",
    "fig_conjugate_diameters_theorems.svg",
    "fig_problem_of_apollonius_ccc.svg",
    "fig_apollonius_circle_locus.svg",
)


def _apparatus_slug(key: str) -> str:
    """Match ``photon_platform.publish.roles.geometry._apparatus_slug``."""
    return re.sub(r"[^a-z0-9]+", "-", (key or "").lower()).strip("-")


def _rst_heading(title: str, char: str) -> str:
    bar = char * max(len(title), 4)
    return f"{title}\n{bar}"


def render_concordance_rst(resources_dir: Path | None = None) -> str:
    """Render ``docsrc/conics/concordance.rst`` from ``concordance.json``."""
    res_dir = resources_dir or default_resources_dir()
    raw, mappings = load_concordance(res_dir)
    meta = raw["metadata"]
    book_counts = meta["book_counts"]
    gaps = raw.get("sympy_geometry_gaps", [])

    lines: list[str] = [
        ":layout: book",
        "",
        ".. _conics-concordance:",
        "",
        _rst_heading("Cross-Corpus Concordance & Symbolic Gap Audit", "="),
        "",
        "This concordance maps the **387 classical Greek and Arabic propositions** of",
        "Apollonius's *Conics* (Books I–VII) and **T. L. Heath's 147 consolidated",
        "propositions** (1896) across the Digital Scriptorium Codex units,",
        "Euclid's *Elements*, Archimedes, Pappus's *Synagoge* Book VII, Kepler,",
        "Kimberling's *Encyclopedia of Triangle Centers* (``etc``), Wildberger's",
        "Rational Trigonometry (``wildberger``), Lean ``mathlib4``, and current",
        "symbolic conic gaps in ``sympy.geometry``.",
        "",
        _rst_heading("1. Classical vs. Heath Proposition Synopsis (Books I–VII)", "-"),
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 10 14 24 16 36",
        "",
        "   * - Book",
        "     - Classical Props.",
        "     - Heath (1896) Range",
        "     - Heath Pages",
        "     - Primary Textual Witness",
    ]
    for book_num, info in book_counts.items():
        lines.extend(
            [
                f"   * - **Book {book_num}**",
                f"     - {info['classical_propositions']}",
                f"     - {info['heath_range']}",
                f"     - pp. {info['heath_pages']}",
                f"     - {info['source_tradition']}",
            ]
        )
    lines.extend(
        [
            "   * - **Total**",
            f"     - **{meta['classical_propositions_total']}**",
            f"     - **Propositions 1–{meta['heath_consolidated_propositions_total']}**",
            "     - **pp. 1–254**",
            "     - **Books I–IV Greek; Books V–VII Arabic/Latin**",
            "",
            _rst_heading("2. Locus-by-Locus Cross-Corpus Concordance", "-"),
            "",
        ]
    )

    for m in mappings:
        euclid_str = ", ".join(m.euclid_refs) if m.euclid_refs else "—"
        eco_str = ", ".join(f"``{e}``" for e in m.ecosystem_links) if m.ecosystem_links else "—"
        fig_str = f"``{m.figure}``" if m.figure else "—"
        doc_link = (
            "/reconstructed/index"
            if m.codex_unit == "reconstructed"
            else f"/conics/{m.codex_unit}/index"
        )
        lines.extend(
            [
                f".. _{m.id}:",
                "",
                _rst_heading(f"{m.classical_locus} — {m.heath_prop}", "~"),
                "",
                (
                    f"- **Codex Unit**: :doc:`{doc_link}` "
                    f"(Heath pp. {m.heath_pages} · PDF {m.pdf_pages})"
                ),
                f"- **Geometric Plate**: {fig_str}",
                f"- **Euclid Foundations**: {euclid_str}",
                f"- **GEOMETOR & Formal Links**: {eco_str}",
                f"- **Doctrinal Summary**: {m.topic}",
                "",
            ]
        )

    lines.extend(
        [
            _rst_heading("3. Symbolic Conic Capabilities & sympy.geometry Gap Audit", "-"),
            "",
            "A central architectural purpose of ``geometor-apollonius`` is specifying the",
            "exact algebraic and projective operations required for a future constructive",
            "conic engine beyond the axis-aligned limitations of ``sympy.geometry``:",
            "",
        ]
    )
    for gap in gaps:
        lines.extend(
            [
                f".. _{gap['id']}:",
                "",
                _rst_heading(f"{gap['feature']} ({gap['apollonius_locus']})", "~"),
                "",
                f"- **Current ``sympy.geometry`` Status**: {gap['sympy_status']}",
                f"- **GEOMETOR Constructive Target**: {gap['geometor_target']}",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def render_bibliography_rst(resources_dir: Path | None = None) -> str:
    """Render ``docsrc/conics/bibliography.rst`` from ``citations.json``."""
    res_dir = resources_dir or default_resources_dir()
    citations = json.loads((res_dir / "citations.json").read_text(encoding="utf-8"))

    lines: list[str] = [
        ":navigation: header",
        ":order: 6",
        ":nav_title: Bibliography",
        ":layout: book",
        ":title: Bibliography",
        "",
        ".. _bibliography:",
        ".. _conics-bibliography:",
        "",
        _rst_heading("Bibliography", "="),
        "",
        ".. rubric:: Editions, Manuscripts, and Critical Studies of the Conic Tradition",
        "",
        "Primary Public Domain editions, ancient and medieval witnesses, early-modern",
        "reconstructions, and GEOMETOR ecosystem references cited via ``:cite:`` across",
        "the *Conics* codex.",
        "",
    ]
    for key, entry in citations.items():
        slug = _apparatus_slug(key)
        heading = f"{entry['author']} ({entry['year']})"
        lines.extend(
            [
                f".. _cite-{slug}:",
                "",
                _rst_heading(heading, "-"),
                "",
                f"- **Citation Key**: ``{key}``",
                f"- **Work**: *{entry['work']}*",
                f"- **Publication / Locus**: {entry['locus']}",
                f"- **Apparatus Note**: {entry['note']}",
            ]
        )
        if entry.get("url"):
            lines.append(f"- **Archival / Ecosystem Link**: {entry['url']}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_persons_rst(resources_dir: Path | None = None) -> str:
    """Render ``docsrc/conics/persons.rst`` from ``persons.json``."""
    res_dir = resources_dir or default_resources_dir()
    persons = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    ordered = sorted(persons.items(), key=lambda kv: kv[1].get("sort_year", 0))

    lines: list[str] = [
        ":navigation: header",
        ":order: 5",
        ":nav_title: People",
        ":layout: book",
        ":title: People",
        "",
        ".. _persons:",
        ".. _conics-persons:",
        "",
        _rst_heading("People", "="),
        "",
        ".. rubric:: Prosopographical Register of Geometers, Translators, Patrons, and Editors",
        "",
        "Chronological register of ancient Greek geometers, Pergamene dedicatees,",
        "Alexandrian commentators, ninth-century Baghdad translators, seventeenth-century",
        "projective and analytic pioneers, and modern critical editors referenced via",
        "``:person:`` across the codex.",
        "",
        _rst_heading("Authors, Translators & Editors", "-"),
        "",
    ]

    top_slugs = ["apollonius", "heath", "eutocius", "halley", "heiberg"]
    for slug in top_slugs:
        if slug in persons:
            entry = persons[slug]
            heading = f"{entry['name']} ({entry['dates']})"
            lines.extend(
                [
                    f".. _person-{slug}:",
                    "",
                    _rst_heading(heading, "~"),
                    "",
                    f"- **Original Name / Form**: {entry.get('greek', entry['name'])}",
                    f"- **Role**: {entry['role']}",
                    f"- **Heath (1896) Loci**: {entry.get('heath_loci', '—')}",
                    f"- **Contribution**: {entry['summary']}",
                ]
            )
            if slug == "apollonius":
                lines.extend(
                    [
                        "",
                        "Born at Perga in Pamphylia around **240 BCE** during the reign of Ptolemy III Euergetes and flourishing under Ptolemy IV Philopator (*Heath 1896, p. lxviii*), :person:`Apollonius of Perga <apollonius>` studied as a young man at **Alexandria** under the successors of :person:`Euclid <euclid>`. As :person:`Geminus <geminus>` (quoted by :person:`Eutocius <eutocius>`) records, his contemporaries held him in such awe for his mastery of conic sections that they named him simply **ὁ μέγας γεωμέτρης — \"The Great Geometer.\"**",
                        "",
                        "From Apollonius's own epistolary Prefaces (:doc:`Preface </conics/preface/index>`), we trace an unusually vivid intellectual network across the Hellenistic eastern Mediterranean: at **Alexandria**, prompted by :person:`Naucrates <naucrates>`, he drafted the initial eight books of the *Conics*; at **Ephesus**, he conversed with the Epicurean mathematician :person:`Philonides <philonides>`; at **Pergamum**, home of the Attalid royal library, he dedicated Books I–III to :person:`Eudemus of Pergamum <eudemus-pergamum>` and Books IV–VIII to :person:`Attalus <attalus>`.",
                        "",
                        "In addition to the *Conics* and the six analytic treatises preserved in syllabus by :person:`Pappus <pappus>`, ancient sources credit Apollonius with proving the geometric equivalence of eccentric and epicyclic planetary models (Ptolemy, *Almagest* XII.1), comparing the regular dodecahedron and icosahedron inscribed in the same sphere (*Elements* Book XIV), and calculating closer approximations to :eq:`\\pi` in his *Quick-Delivery* (*Ὠκυτόκιον*).",
                    ]
                )
            lines.append("")

    lines.extend(
        [
            _rst_heading("Cited Geometers, Philosophers & Scholars", "-"),
            "",
        ]
    )

    for key, entry in ordered:
        if key in top_slugs:
            continue
        slug = _apparatus_slug(key)
        heading = f"{entry['name']} ({entry['dates']})"
        lines.extend(
            [
                f".. _person-{slug}:",
                "",
                _rst_heading(heading, "~"),
                "",
                f"- **Original Name / Form**: {entry.get('greek', entry['name'])}",
                f"- **Role**: {entry['role']}",
                f"- **Heath (1896) Loci**: {entry.get('heath_loci', '—')}",
                f"- **Contribution**: {entry['summary']}",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def render_glossary_rst(resources_dir: Path | None = None) -> str:
    """Render ``docsrc/conics/glossary.rst`` from ``glossary.json``."""
    res_dir = resources_dir or default_resources_dir()
    glossary = json.loads((res_dir / "glossary.json").read_text(encoding="utf-8"))

    lines: list[str] = [
        ":layout: book",
        "",
        ".. _conics-glossary:",
        "",
        _rst_heading("Technical Glossary of Apollonian Conics", "="),
        "",
        "Greek, Latin, and English geometrical terminology of Apollonius of Perga,",
        "verified against T. L. Heath's *Notes on the Terminology of Greek Geometry*",
        "(1896, pp. clvii–clxx) and Heiberg's *Index Graecitatis* (1893).",
        "",
    ]
    for key, entry in glossary.items():
        slug = _apparatus_slug(key)
        lines.extend(
            [
                f".. _term-{slug}:",
                "",
                _rst_heading(entry["headword"], "-"),
                "",
                f"- **Greek**: {entry['greek']}",
                f"- **Latin**: {entry['latin']}",
                f"- **English Rendering**: {entry['english']}",
                f"- **Heath (1896) Loci**: {entry['heath_loci']}",
                f"- **Definition**: {entry['definition']}",
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def write_apparatus_pages(
    docsrc_conics_dir: Path | None = None,
    resources_dir: Path | None = None,
) -> list[Path]:
    """Generate and write all four scholarly apparatus RST files into ``docsrc/conics/``."""
    repo_root = Path(__file__).resolve().parents[3]
    target_dir = docsrc_conics_dir or (repo_root / "docsrc" / "conics")
    res_dir = resources_dir or default_resources_dir()
    target_dir.mkdir(parents=True, exist_ok=True)

    outputs = {
        "concordance.rst": render_concordance_rst(res_dir),
        "bibliography.rst": render_bibliography_rst(res_dir),
        "persons.rst": render_persons_rst(res_dir),
        "glossary.rst": render_glossary_rst(res_dir),
    }
    written: list[Path] = []
    for filename, content in outputs.items():
        out_path = target_dir / filename
        out_path.write_text(content, encoding="utf-8")
        written.append(out_path)
    return written


def verify_codex_tracks(docsrc_dir: Path | None = None) -> list[str]:
    """Verify 9 units, companion tracks in all sections, 12 SVGs, and zero embedded Python."""
    repo_root = Path(__file__).resolve().parents[3]
    docs_root = docsrc_dir or (repo_root / "docsrc")
    conics_dir = docs_root / "conics"
    reconstructed_dir = docs_root / "reconstructed"
    figures_dir = docs_root / "_static" / "figures"
    errors: list[str] = []

    index_rst = conics_dir / "index.rst"
    if not index_rst.is_file():
        errors.append(f"Missing codex root index: {index_rst}")
    else:
        idx_text = index_rst.read_text(encoding="utf-8")
        if ":layout: book" not in idx_text:
            errors.append("docsrc/conics/index.rst must declare ':layout: book'")

    forbidden_patterns = (
        re.compile(r"\.\.\s+code-block::\s*python", re.IGNORECASE),
        re.compile(r":py_file:"),
        re.compile(r"\.\.\s+py_file::"),
    )

    for unit in CODEX_UNITS:
        unit_dir = reconstructed_dir if unit.slug == "reconstructed" else conics_dir / unit.slug
        unit_index = unit_dir / "index.rst"
        if not unit_index.is_file():
            errors.append(f"Missing unit index file: {unit_index}")
            continue
        text = unit_index.read_text(encoding="utf-8")
        if ":layout: book" not in text:
            errors.append(f"Unit index missing ':layout: book': {unit_index}")
        if ".. folio::" not in text:
            errors.append(f"Unit index missing '.. folio::' marker: {unit_index}")

        # Check all child section directories in unit_dir
        sec_dirs = sorted([d for d in unit_dir.iterdir() if d.is_dir() and d.name.startswith("sec_")])
        if not sec_dirs:
            errors.append(f"Unit '{unit.slug}' has no sec_* section directories in {unit_dir}")
        for sec_dir in sec_dirs:
            for suffix in ("index", "summary", "notes"):
                track_file = sec_dir / f"{suffix}.rst"
                if not track_file.is_file():
                    errors.append(f"Missing companion track file: {track_file}")
                    continue
                ttext = track_file.read_text(encoding="utf-8")
                if ":layout: book" not in ttext:
                    errors.append(f"Track file missing ':layout: book': {track_file}")
                if suffix == "index" and ".. folio::" not in ttext:
                    errors.append(f"Primary section track missing '.. folio::' marker: {track_file}")
                for pat in forbidden_patterns:
                    if pat.search(ttext):
                        errors.append(
                            f"Forbidden embedded Python directive '{pat.pattern}' in historical codex: {track_file}"
                        )

    # Also scan all docsrc RST files for forbidden embedded Python
    for rst_file in docs_root.rglob("*.rst"):
        text = rst_file.read_text(encoding="utf-8")
        for pat in forbidden_patterns:
            if pat.search(text):
                msg = f"Forbidden embedded Python directive '{pat.pattern}' in historical codex: {rst_file}"
                if msg not in errors:
                    errors.append(msg)

    for svg_name in EXPECTED_SVG_FIGURES:
        svg_path = figures_dir / svg_name
        if not svg_path.is_file():
            errors.append(f"Missing standalone .euclid-graphic SVG plate: {svg_path}")
        else:
            svg_text = svg_path.read_text(encoding="utf-8")
            if "euclid-graphic" not in svg_text:
                errors.append(f"SVG plate missing '.euclid-graphic' class: {svg_path}")

    return errors
