:layout: book

.. _conics-concordance:

Cross-Corpus Concordance & Symbolic Gap Audit
=============================================

This concordance maps the **387 classical Greek and Arabic propositions** of
Apollonius's *Conics* (Books I–VII) and **T. L. Heath's 147 consolidated
propositions** (1896) across the Digital Scriptorium Codex units,
Euclid's *Elements*, Archimedes, Pappus's *Synagoge* Book VII, Kepler,
Kimberling's *Encyclopedia of Triangle Centers* (``etc``), Wildberger's
Rational Trigonometry (``wildberger``), Lean ``mathlib4``, and current
symbolic conic gaps in ``sympy.geometry``.

1. Classical vs. Heath Proposition Synopsis (Books I–VII)
---------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 10 14 24 16 36

   * - Book
     - Classical Props.
     - Heath (1896) Range
     - Heath Pages
     - Primary Textual Witness
   * - **Book I**
     - 60
     - Props. 1–27 (plus Cone Lemmas I.1–10)
     - pp. 1–52
     - Greek (Heiberg Vol. I, 1891; Vat. gr. 206)
   * - **Book II**
     - 53
     - Props. 28–53
     - pp. 53–94
     - Greek (Heiberg Vol. I, 1891; Vat. gr. 206)
   * - **Book III**
     - 56
     - Props. 54–76
     - pp. 95–125
     - Greek (Heiberg Vol. I, 1891; Vat. gr. 206)
   * - **Book IV**
     - 57
     - Props. 77–83
     - pp. 126–138
     - Greek (Heiberg Vol. II, 1893; Vat. gr. 206)
   * - **Book V**
     - 77
     - Props. 84–113
     - pp. 139–196
     - Arabic of Thābit ibn Qurra / Latin of Halley (1710; Bodleian Marsh 667)
   * - **Book VI**
     - 33
     - Props. 114–122
     - pp. 197–220
     - Arabic of Thābit ibn Qurra / Latin of Halley (1710; Bodleian Marsh 667)
   * - **Book VII**
     - 51
     - Props. 123–147
     - pp. 221–254
     - Arabic of Thābit ibn Qurra / Latin of Halley (1710; Bodleian Marsh 667)
   * - **Total**
     - **387**
     - **Propositions 1–147**
     - **pp. 1–254**
     - **Books I–IV Greek; Books V–VII Arabic/Latin**

2. Locus-by-Locus Cross-Corpus Concordance
------------------------------------------

.. _conc-prefaces-letters:

Books I, II, IV, V, VI, VII Prefaces — Intro Part II, Ch. I
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/preface-intro/preface-intro-en` (Heath pp. lxix–lxxv · PDF 77–83)
- **Geometric Plate**: —
- **Euclid Foundations**: VI.27, VI.28, VI.29, XII.10
- **GEOMETOR & Formal Links**: ``euclid``, ``archimedes``, ``pappus``
- **Doctrinal Summary**: Epistolary prefaces to Eudemus and Attalus dividing Books I–IV (elementary foundation, ἀγωγὴ στοιχειώδης) from Books V–VIII (special extensions, περιουσιαστικώτερα).

.. _conc-i-1-10-cone:

I. 1–10 — The Cone (Introductory Props.)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 1–8 · PDF 181–188)
- **Geometric Plate**: ``fig_oblique_cone_sections.svg``
- **Euclid Foundations**: III.35, VI.4, XI.Def.18
- **GEOMETOR & Formal Links**: ``euclid``, ``elements``, ``pappus``
- **Doctrinal Summary**: Generation of the arbitrary oblique scalene circular double cone, axial triangle, parallel circular sections (I.4), and antiparallel subcontrary circular sections (I.5, I.9).

.. _conc-i-11-parabola:

I. 11 — Proposition 1
~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 8–9 · PDF 188–189)
- **Geometric Plate**: ``fig_application_of_areas.svg``
- **Euclid Foundations**: I.44, II.14, VI.4, VI.27
- **GEOMETOR & Formal Links**: ``euclid``, ``elements``, ``archimedes``, ``wildberger``
- **Doctrinal Summary**: Fundamental symptom of the Parabola (παραβολή): cutting plane parallel to a generator of the axial triangle yields QV² = PL · PV (y² = px), exact application of area.

.. _conc-i-12-hyperbola:

I. 12 — Proposition 2
~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 9–11 · PDF 189–191)
- **Geometric Plate**: ``fig_application_of_areas.svg``
- **Euclid Foundations**: II.6, VI.4, VI.29
- **GEOMETOR & Formal Links**: ``euclid``, ``elements``, ``wildberger``
- **Doctrinal Summary**: Fundamental symptom of the Hyperbola (ὑπερβολή): cutting plane meeting both napes yields QV² = PV · PL + (PL/PP') PV², application exceeding by a figure similar to d × p.

.. _conc-i-13-ellipse:

I. 13 — Proposition 3
~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 11–13 · PDF 191–193)
- **Geometric Plate**: ``fig_application_of_areas.svg``
- **Euclid Foundations**: II.5, VI.4, VI.28
- **GEOMETOR & Formal Links**: ``euclid``, ``elements``, ``archimedes``, ``wildberger``
- **Doctrinal Summary**: Fundamental symptom of the Ellipse (ἔλλειψις): cutting plane meeting all generators of one nape yields QV² = PV · PL − (PL/PP') PV², application falling short by a figure similar to d × p.

.. _conc-i-14-opposites:

I. 14, 15, 16 — Propositions 4–6
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 13–17 · PDF 193–197)
- **Geometric Plate**: ``fig_oblique_cone_sections.svg``
- **Euclid Foundations**: VI.4, VI.29
- **GEOMETOR & Formal Links**: ``euclid``, ``pappus``
- **Doctrinal Summary**: Opposite branches (αἱ ἀντικείμεναι) cut from the double cone have equal latus rectum and form a single two-branched curve with center bisecting PP' and secondary conjugate diameter.

.. _conc-i-33-38-tangents:

I. 33–38 — Propositions 12–15
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 25–30 · PDF 205–210)
- **Geometric Plate**: ``fig_tangent_harmonic_division.svg``
- **Euclid Foundations**: II.5, II.6, III.16, VI.17
- **GEOMETOR & Formal Links**: ``euclid``, ``pappus``, ``mathlib4``
- **Doctrinal Summary**: Tangent construction and harmonic division: TP = PV for the parabola (I.33, 35) and TP : TP' = PV : VP' (equivalently CT · CV = CP²) for central conics (I.34, 36–37).

.. _conc-i-49-51-coordinate-change:

I. 49–51 — Propositions 20–21
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-1/book-1-en` (Heath pp. 36–41 · PDF 216–221)
- **Geometric Plate**: ``fig_tangent_harmonic_division.svg``
- **Euclid Foundations**: I.43, VI.4
- **GEOMETOR & Formal Links**: ``euclid``, ``wildberger``
- **Doctrinal Summary**: Invariance of the conic symptom under transformation from the original cone-derived diameter to any new diameter QQ' and tangent at Q.

.. _conc-ii-1-14-asymptotes:

II. 1–14 — Propositions 28–35
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-2/book-2-en` (Heath pp. 53–62 · PDF 233–242)
- **Geometric Plate**: ``fig_hyperbola_asymptotes_secant.svg``
- **Euclid Foundations**: II.5, II.6, X.1
- **GEOMETOR & Formal Links**: ``euclid``, ``archimedes``, ``descartes``
- **Doctrinal Summary**: Construction of asymptotes (PL² = ¼ p·d), proof of non-intersection, bisected tangent segment LL' at P (II.3, 9), equal secant intercepts RQ = Q'R' (II.8, 16), asymptotic equation xy = const (II.12), and indefinite approach (II.14).

.. _conc-ii-15-23-conjugate-hyperbolas:

II. 15–23 — Propositions 28, 36–39
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-2/book-2-en` (Heath pp. 53, 62–64 · PDF 233, 242–244)
- **Geometric Plate**: ``fig_hyperbola_asymptotes_secant.svg``
- **Euclid Foundations**: II.6, VI.4
- **GEOMETOR & Formal Links**: ``euclid``, ``wildberger``
- **Doctrinal Summary**: Opposite branches and conjugate hyperbolas share common asymptotes; conjugate diameters of original hyperbola swap transverse and secondary roles on the conjugate hyperbola.

.. _conc-ii-44-53-axes-tangents:

II. 44–53 — Propositions 47–53
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-2/book-2-en` (Heath pp. 72–83 · PDF 252–263)
- **Geometric Plate**: ``fig_tangent_harmonic_division.svg``
- **Euclid Foundations**: III.17, III.31
- **GEOMETOR & Formal Links**: ``euclid``, ``elements``, ``pappus``
- **Doctrinal Summary**: Finding a diameter, center, and principal orthogonal axes of a given conic; constructing tangents from an external point by harmonic division and compass-and-straightedge.

.. _conc-iii-16-29-chord-rectangles:

III. 16–29 — Propositions 57–61
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-3/book-3-en` (Heath pp. 97–101 · PDF 277–281)
- **Geometric Plate**: ``fig_three_four_line_locus.svg``
- **Euclid Foundations**: III.35, III.36, III.37
- **GEOMETOR & Formal Links**: ``euclid``, ``pappus``, ``newton``
- **Doctrinal Summary**: Ratio of rectangles under segments of intersecting chords PO·OQ : RO·OS equals the ratio of squares on parallel tangents—generalizing Euclid III.35–36 (power of a point) from circles to all conics.

.. _conc-iii-30-40-poles-polars:

III. 30–40 — Propositions 62–66
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-3/book-3-en` (Heath pp. 102–108 · PDF 282–288)
- **Geometric Plate**: ``fig_harmonic_pole_polar.svg``
- **Euclid Foundations**: VI.2, VI.4
- **GEOMETOR & Formal Links**: ``pappus``, ``mathlib4``, ``wildberger``
- **Doctrinal Summary**: Harmonic properties of poles and polars: any secant through pole T is divided harmonically by the conic at R, R' and the chord of contact (polar) Qq at M: TR : TR' = MR : MR'.

.. _conc-iii-45-52-foci:

III. 45–52 — Propositions 69–73
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-3/book-3-en` (Heath pp. 113–118 · PDF 293–298)
- **Geometric Plate**: ``fig_central_conic_foci.svg``
- **Euclid Foundations**: I.47, II.5, II.6, III.21, III.31
- **GEOMETOR & Formal Links**: ``euclid``, ``pappus``, ``kepler``, ``wildberger``
- **Doctrinal Summary**: Focal properties of central conics ('points arising out of the application', AS·SA' = b²): optical reflection equality (III.48 [Prop. 71]), pedal auxiliary circle (III.49 [Prop. 72]), and constant sum/difference SP ± S'P = AA' = 2a (III.51–52 [Prop. 73]).

.. _conc-iii-53-56-four-line-locus:

III. 53–56 — Propositions 74–76
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-3/book-3-en` (Heath pp. 119–125 · PDF 299–305)
- **Geometric Plate**: ``fig_three_four_line_locus.svg``
- **Euclid Foundations**: VI.16, VI.23
- **GEOMETOR & Formal Links**: ``pappus``, ``descartes``
- **Doctrinal Summary**: Projective product of tangent intercepts and synthetic key to the Three-Line and Four-Line Locus of Euclid, Apollonius, Pappus (Book VII), and Descartes (La Géométrie, 1637).

.. _conc-iv-1-23-polar-converse:

IV. 1–23 — Introductory Note to Book IV
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-4/book-4-en` (Heath pp. 126 · PDF 306)
- **Geometric Plate**: ``fig_harmonic_pole_polar.svg``
- **Euclid Foundations**: III.17, VI.4
- **GEOMETOR & Formal Links**: ``pappus``, ``mathlib4``
- **Doctrinal Summary**: Converse harmonic polar construction of tangents from an external point across single-branch and opposite-branch hyperbolas.

.. _conc-iv-24-57-intersections:

IV. 24–57 — Propositions 77–83
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-4/book-4-en` (Heath pp. 126–138 · PDF 306–318)
- **Geometric Plate**: ``fig_four_point_conic_pencil.svg``
- **Euclid Foundations**: III.10, III.13
- **GEOMETOR & Formal Links**: ``euclid``, ``pappus``
- **Doctrinal Summary**: Two distinct conics cannot share an arc (IV.24 [Prop. 77]), intersect in at most four points (IV.25, 38, 43, 55 [Props. 78–83]), and if tangent at one point meet in at most two others—the ancient foundation of Bézout's theorem (2 × 2 = 4) and five-point conic uniqueness.

.. _conc-v-1-34-subnormals:

V. 1–34 — Propositions 84–94
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-5/book-5-en` (Heath pp. 139–159 · PDF 319–339)
- **Geometric Plate**: ``fig_normals_evolute.svg``
- **Euclid Foundations**: I.19, III.7, III.8, III.16
- **GEOMETOR & Formal Links**: ``euclid``, ``archimedes``
- **Doctrinal Summary**: Minimum and maximum straight lines from axis points to a conic; constant parabola subnormal NG = ½ p_a (V.13, 27) and central-conic subnormal proportion NG : CN = p_a : AA' (V.14–15, 28–29); perpendicularity of minimum/maximum lines to the tangent (normals).

.. _conc-v-51-63-evolute:

V. 51–63 — Propositions 99–106
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/book-5/book-5-en` (Heath pp. 168–186 · PDF 348–366)
- **Geometric Plate**: ``fig_normals_evolute.svg``
- **Euclid Foundations**: II.5, V.8, VI.28
- **GEOMETOR & Formal Links**: ``archimedes``, ``descartes``, ``wildberger``
- **Doctrinal Summary**: Exact diorismos of the number of normals through an arbitrary point O (2, 3, or 4 normals), determining point-by-point the evolute envelope of every conic and constructing normal feet via an auxiliary rectangular hyperbola.

.. _conc-vi-1-33-similarity-cones:

VI. 1–33 — Definitions 1–6 & Propositions 114–122
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/books-6-7/books-6-7-en` (Heath pp. 197–220 · PDF 377–400)
- **Geometric Plate**: ``fig_oblique_cone_sections.svg``
- **Euclid Foundations**: VI.Def.1, VI.20, XI.24
- **GEOMETOR & Formal Links**: ``euclid``, ``elements``
- **Doctrinal Summary**: Congruence and similarity of conic sections and segments: all parabolas are similar (VI.11 [Prop. 115]); central conics are similar iff their figures d × p are similar (VI.12–13 [Prop. 116]); embedding any given conic inside a prescribed right cone (VI.28–30 [Props. 120–122]).

.. _conc-vii-12-31-apollonius-theorems:

VII. 12, 13, 29, 30, 31 — Propositions 129 & 136
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/books-6-7/books-6-7-en` (Heath pp. 228–236 · PDF 408–416)
- **Geometric Plate**: ``fig_conjugate_diameters_theorems.svg``
- **Euclid Foundations**: I.35, I.47, II.5, II.6, VI.23
- **GEOMETOR & Formal Links**: ``euclid``, ``wildberger``
- **Doctrinal Summary**: Apollonius's First and Second Conjugate Diameter Theorems: (1) PP'² ± DD'² = AA'² ± BB'² (a'² ± b'² = a² ± b²); (2) area of circumscribed conjugate parallelogram LL'MM' equals rectangle of axes AA' · BB' (a'b' sin ω = ab).

.. _conc-vii-33-51-extrema:

VII. 33–51 — Propositions 137–147
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/books-6-7/books-6-7-en` (Heath pp. 236–254 · PDF 416–434)
- **Geometric Plate**: ``fig_conjugate_diameters_theorems.svg``
- **Euclid Foundations**: V.8, V.10, VI.27
- **GEOMETOR & Formal Links**: ``euclid``, ``ibn-al-haytham``, ``halley``
- **Doctrinal Summary**: Extrema and monotonic variations of d' ± d'', d'·d'', p', and d'² ± p'² across conjugate diameters, forged explicitly as diorismos machinery for the lost Book VIII.

.. _conc-pappus-vii-tangencies-ccc:

Pappus Synagoge VII (Περὶ ἐπαφῶν) — Intro Part II, Ch. I & Viète (1600)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/lost-works-pappus/lost-works-pappus-en` (Heath pp. lxviii · PDF 76)
- **Geometric Plate**: ``fig_problem_of_apollonius_ccc.svg``
- **Euclid Foundations**: III.17, III.36, IV.4, IV.5
- **GEOMETOR & Formal Links**: ``pappus``, ``elements``, ``etc``
- **Doctrinal Summary**: Apollonius's On Tangencies: the ten contact problems (PPP through CCC, up to 8 tangent circles), reconstructed by Viète's Apollonius Gallus (1600) and connected to ETC X(181) (Apollonius Point).

.. _conc-pappus-vii-plane-loci-apollonius-circle:

Pappus Synagoge VII (Τόποι ἐπίπεδοι II) — Circle of Apollonius & Analytic Treasury
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Codex Unit**: :doc:`/conics/lost-works-pappus/lost-works-pappus-en` (Heath pp. lxviii, cxxv–cxxvi · PDF 76, 133–134)
- **Geometric Plate**: ``fig_apollonius_circle_locus.svg``
- **Euclid Foundations**: VI.3, VI.A
- **GEOMETOR & Formal Links**: ``pappus``, ``elements``, ``etc``, ``wildberger``
- **Doctrinal Summary**: Apollonius's Plane Loci Book II: the locus PA : PB = k (k ≠ 1) is the Circle of Apollonius on harmonic diameter H_in H_ex; the three Apollonius circles of a triangle form a coaxal pencil intersecting at the Isodynamic Points X(15) and X(16), alongside Cutting Off of a Ratio, Determinate Section, and Inclinations.

3. Symbolic Conic Capabilities & sympy.geometry Gap Audit
---------------------------------------------------------

A central architectural purpose of ``geometor-apollonius`` is specifying the
exact algebraic and projective operations required for a future constructive
conic engine beyond the axis-aligned limitations of ``sympy.geometry``:

.. _gap-general-conic-quadratic:

General planar conic Ax² + Bxy + Cy² + Dx + Ey + F = 0 & oblique-diameter frame (I.11–14, I.49–60)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Current ``sympy.geometry`` Status**: Partial / Axis-Aligned Only (`sympy.geometry.ellipse.Ellipse` and `parabola.Parabola` lack general rotated/projective hyperbola and two-branch oblique-diameter conic kernel)
- **GEOMETOR Constructive Target**: geometor.model exact algebraic/projective Conic element over Q(sqrt(d)) and Q(phi)

.. _gap-pole-polar-duality:

Harmonic pole-polar bijection, chord of contact, and self-polar triangle (III.30–40 [Props. 62–66])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Current ``sympy.geometry`` Status**: Missing in `sympy.geometry` (no `polar_line(point)` or `pole_point(line)` on conics; formalized in Lean `mathlib4` `PolePolar.lean`)
- **GEOMETOR Constructive Target**: geometor.pappus & geometor.model symmetric 3×3 matrix polarity P ↦ C·P

.. _gap-five-point-pencil:

Four-line locus conic pencil C₁ + λ C₂ = 0, five-point conic constructor, and exact 4-point intersection solver (III.53–56 [Props. 74–76] & IV.24–57 [Props. 77–83])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Current ``sympy.geometry`` Status**: Missing in `sympy.geometry` (no `conic_through_five_points` or 4-point pencil resolver)
- **GEOMETOR Constructive Target**: geometor.pappus Braikenridge–Maclaurin / determinant 6×6 exact symbolic constructor

.. _gap-normals-evolute:

Exact 4-normal cubic/quartic foot resolver from arbitrary point O and rational/algebraic evolute envelope (V.51–63 [Props. 99–109])
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Current ``sympy.geometry`` Status**: Missing in `sympy.geometry` (`Ellipse.normal_lines` uses numeric/Groebner fallbacks that stall on symbolic parameters; no `evolute` method)
- **GEOMETOR Constructive Target**: Apollonius rectangular-hyperbola intersection constructor (V.62–63 [Prop. 106])

.. _gap-apollonius-ccc:

Exact symbolic solver for all 8 tangent circles to three given circles (Problem of Apollonius CCC) (Lost Tangencies (Pappus VII) / Viète (1600))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Current ``sympy.geometry`` Status**: Missing in `sympy.geometry` (`Circle` supports only basic tangent lines from a point)
- **GEOMETOR Constructive Target**: Gergonne radical-center / pole-polar 8-solution algebraic solver in geometor.elements / geometor.etc
