=========
Changelog
=========

0.1.6 (2026-11-15)
------------------

- **fixed**: Eliminated black-fill and dark-on-dark CSS fallback failures across all 12 ``.euclid-graphic`` SVG plates by emitting explicit ``fill="none"`` presentation attributes on every stroke primitive in ``scripts/build_figures.py`` and pairing with ``photon-platform/publish`` ``v0.4.7`` extended palette rules (``--geom-muted``, ``--geom-hyper``, ``--geom-rose``, ``.geom-hyper-line``, ``.geom-rose-line``, ``.geom-polygon-hyper``, ``.geom-polygon-rose``, ``.geom-point-hyper``, ``.geom-point-rose``, and ``.geom-label-{accent,assert,hyper,rose}``).
- **changed**: Calibrated geometry and glyph typography across all 12 SVG plates (``g1``–``g12``): rim-anchored oblique double-cone arches and separated ``E₂``/``H₁`` labels (``g1``), clean harmonic ruler below the ellipse (``g3``), on-canvas ``405px`` auxiliary circle (``g6``), interior ``L₂``/``L₄`` four-line locus labels (``g7``), ``365px`` 4-point conic pencil (``g8``), ``a=180, b=128`` astroidal evolute keeping all four cusps strictly inside the ellipse (``g9``), ``380px`` conjugate-diameter parallelogram with clear ``D`` offset (``g10``), centered ``C₁..C₃`` Problem of Apollonius circles (``g11``), and scalene ``ABC`` coaxal pencil placing both Isodynamic Points ``X(15)`` and ``X(16)`` centrally inside the right panel (``g12``).

0.1.5 (2026-11-15)
------------------

- Rebuilt codex documentation with ``photon-platform/publish`` ``v0.4.6`` so every inline ``.euclid-graphic`` SVG carries explicit ``viewBox`` pixel dimensions, per-diagram scoped ``<style>`` rules, and Nocturnal Codex dark/light theme parity.

0.1.4 (2026-11-14)
------------------

- Standardized top-level ``About`` page (``docsrc/about/index.rst`` promoted to top header ``:order: 10``) with the three-pillar GEOMETOR semantic-extraction mission and archival provenance; retired ``docsrc/mission/`` stubs cleanly into Home and ``About``.

0.1.3 (2026-11-14)
------------------

- **changed**: Standardized Book Title Page, top-level Header Navigation (``Book``, ``People``, ``Bibliography``, ``Usage``), Reader's Guide (``docsrc/usage/``), featured Author/Translator profiles in ``People``, and English structural terminology.

0.1.2 (2026-11-13)
------------------

* Added track-aware primary-source folio map (``resources/conics/folio_map.json``) resolving 27/27 folio directives to Internet Archive Heath facsimile locus pages.

0.1.0 (Initial Codex)
---------------------

* Initialized ``geometor-apollonius`` completing the Heath Cambridge Greek Trilogy (Apollonius 1896, Archimedes 1897, Euclid 1908).
* Authored the 8-Unit, 3-Track synchronized Digital Scriptorium Book Codex (``docsrc/conics/``: ``-en.rst``, ``-summary.rst``, ``-notes.rst``) covering Apollonius's Prefatory Letters, Books I–VII (387 classical propositions / 147 Heath consolidated propositions), and the Lost Analytic Treasury in Pappus Book VII.
* Built 12 standalone theme-adaptive ``.euclid-graphic`` SVG plates via ``scripts/build_figures.py`` including exact solvers for 4 ellipse normals inside the astroidal evolute, all 8 tangent circles of the Problem of Apollonius (``CCC``), and the coaxal Circle of Apollonius pencil through ``X(15)`` and ``X(16)``.
* Added SHA-256 provenance manifest (``sources_manifest.json``), cross-corpus concordance and ``sympy.geometry`` conic gap audit (``concordance.json``), prosopography, bibliography, Greek-Latin-English glossary, and ``geometor.apollonius`` verification CLI and test suite.
