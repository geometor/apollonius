# GEOMETOR • apollonius

Scholarly **3-Track Digital Scriptorium Book Codex** (`:layout: book`) and cross-corpus concordance of **Apollonius of Perga: *Treatise on Conic Sections* (Books I–VII, ed. Sir Thomas Little Heath, Cambridge University Press, 1896)**, completing the Heath Cambridge Greek Trilogy alongside `geometor/euclid` (1908) and `geometor/archimedes` (1897/1912).

## Architectural Mandates

1. **100% Public Domain & Folio-Verified Vision**:
   - Grounded strictly in Public Domain sources: T. L. Heath (1896, Internet Archive `treatiseonconics00apolrich`), J. L. Heiberg (1891–1893, `apolloniipergaei01apoluoft` & `02`), and Edmond Halley (1706, 1710, `bub_gb_6N__e_V4xbAC`).
   - Leaf-to-page mapping in Heath 1896 PDF: Roman frontmatter `pdf_page = roman + 8`; Arabic treatise `pdf_page = page + 180`.
   - Always inspect rendered 300 DPI page images directly via multimodal vision (`view_file`); never rely on OCR text layers.
2. **Strict Content / Code Separation**:
   - Zero embedded `py_file` or `.. code-block:: python` directives inside `docsrc/conics/`.
   - All 12 standalone `.euclid-graphic` SVG plates are built deterministically by `scripts/build_figures.py` into `docsrc/_static/figures/`.
3. **Key Modules (`src/geometor/apollonius/`)**:
   - `concordance.py`: `CODEX_UNITS` (`0`–`7`), `load_concordance`, `verify_concordance` (validating SHA-256 hashes in `sources_manifest.json`, 387 classical / 147 Heath propositions, and `sympy.geometry` conic gap audit).
   - `compile_codex.py`: Generates `docsrc/conics/{concordance,bibliography,persons,glossary}.rst` and verifies all 24 synchronized track files + 12 SVGs (`verify_codex_tracks`).
   - `cli.py`: `geometor-apollonius {summary,compile-apparatus,verify}`.

## Verification Commands (Python 3.13 Offline Sandbox)

```bash
pytest
ruff check src scripts tests
publish build
```
