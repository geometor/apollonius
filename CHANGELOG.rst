=========
Changelog
=========

0.1.0 (Initial Codex)
---------------------

* Initialized ``geometor-apollonius`` completing the Heath Cambridge Greek Trilogy (Apollonius 1896, Archimedes 1897, Euclid 1908).
* Authored the 8-Unit, 3-Track synchronized Digital Scriptorium Book Codex (``docsrc/conics/``: ``-en.rst``, ``-summary.rst``, ``-notes.rst``) covering Apollonius's Prefatory Letters, Books I–VII (387 classical propositions / 147 Heath consolidated propositions), and the Lost Analytic Treasury in Pappus Book VII.
* Built 12 standalone theme-adaptive ``.euclid-graphic`` SVG plates via ``scripts/build_figures.py`` including exact solvers for 4 ellipse normals inside the astroidal evolute, all 8 tangent circles of the Problem of Apollonius (``CCC``), and the coaxal Circle of Apollonius pencil through ``X(15)`` and ``X(16)``.
* Added SHA-256 provenance manifest (``sources_manifest.json``), cross-corpus concordance and ``sympy.geometry`` conic gap audit (``concordance.json``), prosopography, bibliography, Greek-Latin-English glossary, and ``geometor.apollonius`` verification CLI and test suite.
