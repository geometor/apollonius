"""GEOMETOR • apollonius — Scholarly Book Codex & Concordance of Apollonius's Conics."""

from __future__ import annotations

from geometor.apollonius.compile_codex import (
    render_bibliography_rst,
    render_concordance_rst,
    render_glossary_rst,
    render_persons_rst,
    verify_codex_tracks,
    write_apparatus_pages,
)
from geometor.apollonius.concordance import (
    CODEX_UNITS,
    CODEX_UNITS_BY_SLUG,
    CodexUnitSpec,
    PropositionMapping,
    default_resources_dir,
    load_concordance,
    verify_concordance,
)

__version__ = "0.1.2"

__all__ = [
    "CODEX_UNITS",
    "CODEX_UNITS_BY_SLUG",
    "CodexUnitSpec",
    "PropositionMapping",
    "__version__",
    "default_resources_dir",
    "load_concordance",
    "render_bibliography_rst",
    "render_concordance_rst",
    "render_glossary_rst",
    "render_persons_rst",
    "verify_codex_tracks",
    "verify_concordance",
    "write_apparatus_pages",
]
