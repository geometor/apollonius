:layout: book

.. _unit-7-lost-works-pappus-en:

Appendix — The Lost Analytic Treasury in Pappus Book VII
========================================================

.. folio:: Heath 1896, Intro pp. lxviii, cxxv–clvi (PDF 76, 133–164); Pappus Synagoge VII

Beyond the *Conics*, :person:`Apollonius of Perga <apollonius>` authored **six major two-book treatises** forming the core of the ancient **Domain of Analysis** (*Τόπος ἀναλυόμενος*) preserved for posterity in Book VII of :person:`Pappus of Alexandria's <pappus>` *Mathematical Collection* (*Synagoge*, :cite:`ed. Hultsch 1877 <hultsch:1877>`; ``geometor/pappus``). Five of these treatises were lost in Greek, while one (*Cutting Off of a Ratio*) survived in Arabic (:cite:`Halley 1706 <halley:1706>`).

1. *On Tangencies* (Περὶ ἐπαφῶν) — The Problem of Apollonius (`CCC`)
--------------------------------------------------------------------

Pappus summarizes the famous **ten contact problems** of Apollonius's two-book treatise :term:`On Tangencies <epaphai>`: given any three geometric elements in a plane—each being a **Point (`P`)**, a **Straight Line (`L`)**, or a **Circle (`C`)**—construct by straightedge and compass a circle tangent to all three (`PPP`, `PPL`, `PPC`, `PLL`, `PLC`, `PCC`, `LLL`, `LLC`, `LCC`, and `CCC`). While `PPP` (`IV.5`) and `LLL` (`IV.4`) belong to :person:`Euclid's <euclid>` *Elements*, the crowning tenth problem **`CCC` (Three Given Circles)** admits up to **eight distinct tangent circles**:

.. picture:: /_static/figures/fig_problem_of_apollonius_ccc.svg
   :alt: All eight Apollonius tangent circles to three given mutually external circles C1, C2, C3

**Plate 11 — The Problem of Apollonius (`CCC`: All 8 Solutions)**. Given three mutually exterior circles :g:`C1, C2, C3` (bold), exact algebraic solution yields **8 tangent circles**: the inner externally-tangent Soddy/Apollonius circle (gold solid), the outer internally-enclosing Apollonius circle (gold dashed, defining ``ETC`` ``X(181)``), and three conjugate pairs of mixed-contact circles (teal and rose).

Reconstructed by :person:`François Viète <viete>` in *Apollonius Gallus* (:cite:`1600 <viete:1600>`) by concentric radius dilation (reducing `CCC` to `PCC`) and by Gergonne via the radical center and pole-polar duality of the four similarity axes, the `CCC` configuration connects directly to ``geometor/elements`` and ``geometor/etc``!

2. *Plane Loci* (Τόποι ἐπίπεδοι) — The Circle of Apollonius
-----------------------------------------------------------

In Book II of *Plane Loci*, Apollonius proved one of the most fertile theorems of Euclidean and triangle geometry:

.. enunciation::

   **Locus of Apollonius (Plane Loci II)**. Whereas the locus of a point :g:`P` whose distances to two fixed points :g:`A, B` are equal (:eq:`PA : PB = 1`) is the perpendicular bisector of :g:`AB`, the locus of :g:`P` whose distances bear any **given unequal ratio** :eq:`PA : PB = k` (:eq:`k \neq 1`) is a **circle** (**the Circle of Apollonius**), whose diameter :g:`H_{\mathrm{in}} H_{\mathrm{ex}}` divides :g:`AB` internally and externally in the ratio :eq:`k` (:just:`VI.3`).

.. picture:: /_static/figures/fig_apollonius_circle_locus.svg
   :alt: Locus PA:PB = k and the three coaxal Apollonius circles of a triangle meeting at X(15) and X(16)

**Plate 12 — Circle of Apollonius & Coaxal Triangle Pencil (`X(15)`, `X(16)`)**. Left: Harmonic division :eq:`(A, B; H_{\mathrm{in}}, H_{\mathrm{ex}}) = -1` generates the Apollonius circle :eq:`PA : PB = k`. Right: On any scalene triangle :g:`ABC`, the three Apollonius circles (:eq:`PB/PC = c/b`, :eq:`PC/PA = a/c`, :eq:`PA/PB = b/a`) belong to a coaxal pencil orthogonal to the circumcircle and intersect at the **First and Second Isodynamic Points** ``X(15)`` and ``X(16)``.

3. The Remaining Four Analytic Treatises in Pappus VII
------------------------------------------------------

1. **Cutting Off of a Ratio** (*Περὶ λόγου ἀποτομῆς*, 2 Books — extant in Arabic, :cite:`ed. Halley 1706 <halley:1706>`): Through a given point draw a straight line cutting off segments on two given lines (measured from given base points) bearing a prescribed ratio—exhaustively classified across 21 loci and :term:`diorismoi <diorismos>`.
2. **Cutting Off of an Area** (*Περὶ χωρίου ἀποτομῆς*, 2 Books — restored by Halley 1706): Same construction except the two intercepted segments must contain a **given rectangle** (hyperbolic/quadratic counterpart of *Cutting Off of a Ratio*).
3. **Determinate Section** (*Περὶ διωρισμένης τομῆς*, 2 Books): Given four collinear points :g:`A, B, C, D`, find :g:`P` on the line such that :eq:`PA \cdot PB : PC \cdot PD = k` (or :eq:`PA^2 : PB \cdot PC = k`)—a complete 1D projective involution theory with exact extrema!
4. **Inclinations** (*Περὶ νεύσεων*, 2 Books — :term:`Neusis <neusis>`): Construct by pure straightedge and compass a segment of given length between two given lines/circles verging through a given pole (e.g., inserting a given chord in a circle or rhombus).
