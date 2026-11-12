===================
GEOMETOR apollonius
===================

Scholarly **3-Track Digital Scriptorium Book Codex** (`English` · `Summary` · `Notes`), interactive ``.euclid-graphic`` SVG atlas, and cross-corpus proposition concordance of **Apollonius of Perga's Treatise on Conic Sections (Books I–VII)**, based on Sir Thomas Little Heath's Public Domain Cambridge University Press edition (1896), J. L. Heiberg's critical Greek text (1891–1893), and Edmond Halley's Oxford edition of Thābit ibn Qurra's Arabic Books V–VII (1710).

Completes the **Heath Cambridge Greek Trilogy** alongside ``geometor/archimedes`` (1897/1912) and ``geometor/euclid`` (1908).

Highlights
----------

* **8-Unit 3-Track Book Codex** (``docsrc/conics/``):
  - **Unit 0 (`preface-intro`)**: From Menaechmus, Aristaeus, Euclid & Archimedes to Apollonius's single oblique scalene double cone; Prefatory Letters to Eudemus & Attalus.
  - **Unit 1 (`book-1`)**: Generation of the cone, subcontrary circular sections, fundamental area-application symptoms (*parabola*, *hyperbola*, *ellipse*, *opposite branches*), harmonic tangents & coordinate transformations (`Props. 1–27 [I.1–60]`).
  - **Unit 2 (`book-2`)**: Asymptotes (`xy = const`), bisected tangents, equal secant intercepts, conjugate hyperbolas & compass-and-straightedge axis recovery (`Props. 28–53 [II.1–53]`).
  - **Unit 3 (`book-3`)**: Intersecting chord rectangles, harmonic poles & polars, central conic foci (`SP ± S'P = 2a`) & the Three- and Four-Line Locus (`Props. 54–76 [III.1–56]`).
  - **Unit 4 (`book-4`)**: Converse polar tangents & the four-point intersection bound (`Props. 77–83 [IV.1–57]`).
  - **Unit 5 (`book-5`)**: Normals as extrema, subnormals, exact evolute *diorismos* (2, 3, or 4 normals) & the Hyperbola of Apollonius (`Props. 84–113 [V.1–77]`).
  - **Unit 6 (`books-6-7`)**: Equal & similar conics, cone embedding, and Apollonius's Conjugate Diameter Theorems (`a'² ± b'² = a² ± b²`, `a'b' sin ω = ab`) (`Props. 114–147 [VI.1–33, VII.1–51]`).
  - **Unit 7 (`lost-works-pappus`)**: The Lost Analytic Treasury in Pappus Book VII (*Problem of Apollonius CCC*, *Circle of Apollonius*, *Cutting Off of a Ratio*, *Determinate Section*, *Inclinations*).
* **12 Standalone ``.euclid-graphic`` SVG Plates** (``scripts/build_figures.py`` -> ``docsrc/_static/figures/``).
* **Concordance & Symbolic Gap Audit** (``resources/conics/concordance.json`` & ``src/geometor/apollonius/``): Maps all **387 classical propositions** and **147 Heath propositions** across ``euclid``, ``elements``, ``archimedes``, ``pappus``, ``etc`` (`X(15)`, `X(16)`, `X(181)`), ``wildberger``, Lean ``mathlib4``, and ``sympy.geometry`` symbolic conic gaps.

Development & Verification
--------------------------

.. code-block:: bash

   pytest
   ruff check src scripts tests
   publish build
