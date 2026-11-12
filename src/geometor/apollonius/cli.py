"""Command-line interface for GEOMETOR • apollonius."""

from __future__ import annotations

import argparse
import sys

from geometor.apollonius.compile_codex import (
    EXPECTED_SVG_FIGURES,
    verify_codex_tracks,
    write_apparatus_pages,
)
from geometor.apollonius.concordance import (
    CODEX_UNITS,
    load_concordance,
    verify_concordance,
)


def build_parser() -> argparse.ArgumentParser:
    """Construct the ``geometor-apollonius`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-apollonius",
        description="Scholarly Book Codex & Concordance utilities for Apollonius of Perga's Conics.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("summary", help="Print a summary of codex units, propositions, and figures.")
    sub.add_parser("verify", help="Verify provenance hashes, concordance, 24 track files, and 12 SVGs.")
    sub.add_parser("compile-apparatus", help="Generate concordance, bibliography, persons, and glossary RST pages.")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Execute the ``geometor-apollonius`` CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "summary":
        raw, mappings = load_concordance()
        meta = raw["metadata"]
        print(f"{meta['title']}")
        print(f"Edition: {meta['edition']}")
        print(
            f"Propositions: {meta['classical_propositions_total']} classical "
            f"-> {meta['heath_consolidated_propositions_total']} Heath consolidated"
        )
        print(f"Codex Units: {len(CODEX_UNITS)} (3 synchronized tracks each = {len(CODEX_UNITS) * 3} track pages)")
        print(f"Concordance Loci: {len(mappings)} | Standalone SVG Plates: {len(EXPECTED_SVG_FIGURES)}")
        for unit in CODEX_UNITS:
            print(f"  [{unit.unit_number}] {unit.slug}: {unit.title} ({unit.heath_loci})")
        return 0

    if args.command == "compile-apparatus":
        written = write_apparatus_pages()
        for path in written:
            print(f"Wrote {path}")
        return 0

    if args.command == "verify":
        errors = verify_concordance() + verify_codex_tracks()
        if errors:
            for err in errors:
                print(f"ERROR: {err}", file=sys.stderr)
            return 1
        print("OK: Provenance SHA-256 hashes, 387/147 concordance, 24 codex tracks, and 12 SVGs verified.")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
