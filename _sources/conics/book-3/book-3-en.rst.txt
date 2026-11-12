:layout: book

.. _unit-3-book-3-en:

Book III — Chord Rectangles, Poles & Polars, Foci & the 4-Line Locus
====================================================================

.. folio:: Heath 1896, Props. 54–76 [III. 1–56], pp. 95–125 (PDF 275–305)

In the General Preface (:doc:`Unit 0 </conics/preface-intro/preface-intro-en>`), :person:`Apollonius <apollonius>` singles out **Book III** with special pride: it contains *"many remarkable theorems useful for the syntheses of solid loci and for diorismoi, the majority and prettiest of which are new"*, culminating in the long-sought synthesis of the :term:`Three-Line and Four-Line Locus <topos-pros-treis-kai-tessaras-grammas>`.

1. Equality of Tangent Triangles & Intersecting Chord Rectangles [Props. 54–61 / III. 1–29]
-------------------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 95–101 (PDF 275–281)

* **Equal Tangent-Diameter Triangles [Prop. 54 / III. 1, 4, 11]**: If tangents at :g:`P` and :g:`Q` meet at :g:`O`, and diameters through :g:`P`, :g:`Q` meet the opposite tangents in :g:`E`, :g:`T`, the triangles :g:`OPT` and :g:`OQE` have **equal area**—the foundational lemma behind every chord-product theorem.
* **Generalization of Euclid III.35–36 to All Conics [Props. 57–61 / III. 16–29]**: If two chords :g:`PQ`, :g:`pq` parallel to two fixed directions intersect at *any* interior or exterior point :g:`O`, the ratio of the rectangles under their segments is **invariant** with respect to the position of :g:`O`, being equal to the ratio of the squares on the parallel tangents :g:`TP`, :g:`Tp` (or parallel diameters):

  .. math::

     PO \cdot OQ : pO \cdot Oq = TP^2 : Tp^2.

  When the conic is a circle, :eq:`TP = Tp` by symmetry, immediately recovering :just:`III.35` and :just:`III.36`!

2. Harmonic Properties of Poles & Polars [Props. 62–66 / III. 30–40]
--------------------------------------------------------------------

.. folio:: Heath 1896, pp. 102–108 (PDF 282–288)

Starting with transversals parallel to an asymptote (`Prop. 62 [III. 30–34]`) and chords parallel to an asymptote (`Prop. 63 [III. 35–36]`), Apollonius ascends in **Propositions 64–66 (`III. 37–40`)** to the universal theorem of **projective polarity**:

.. picture:: /_static/figures/fig_harmonic_pole_polar.svg
   :alt: Harmonic pole T, chord of contact polar Qq, and harmonically divided secants

**Plate 5 — Harmonic Pole & Polar Duality (Book III.37–40 [Props. 64–66])**. From exterior pole :g:`T`, tangents touch the conic at :g:`Q, Q'` defining the chord of contact (polar) :g:`QQ'`; every secant through :g:`T` meets the conic in :g:`R, R'` and the polar in :g:`M` in harmonic cross-ratio :eq:`(T, M; R, R') = -1`.

.. enunciation::

   **Proposition 64 [III. 37–40] — Universal Harmonic Polar Theorem**. If :g:`TQ`, :g:`Tq` be two tangents to any conic section (parabola, ellipse, single-branch or opposite-branch hyperbola) and any straight line drawn through :g:`T` meet the conic in :g:`R`, :g:`R'` and the chord of contact :g:`Qq` in :g:`M` (or conversely if :g:`M` lie inside the conic on :g:`Qq` and a secant through :g:`M` meet the curve in :g:`R, R'` and the parallel through :g:`T` in :g:`N`), the transversal is **divided harmonically**:

   .. math::

      TR : TR' = MR : MR' \qquad \bigl((T, M; R, R') = -1\bigr).

3. Focal Properties of Central Conics [Props. 69–73 / III. 45–52]
-----------------------------------------------------------------

.. folio:: Heath 1896, pp. 113–118 (PDF 293–298)

Apollonius introduces the two foci :g:`S`, :g:`S'` on the principal axis :g:`AA'` without using a word for "burning point" (coined by :person:`Kepler <kepler>` in 1604), naming them strictly from his area-application geometry **τὰ ἐκ τῆς παραβολῆς γινόμενα σημεῖα** (:term:`"the points arising out of the application" <semeia-ek-tes-paraboles>`): apply along the axis :g:`AA'` a rectangle :eq:`AS \cdot SA' = AS' \cdot S'A' = \tfrac{1}{4}\, p_a \cdot AA' = CB^2 = b^2` (falling short by a square on the ellipse so :eq:`CS^2 = a^2 - b^2`, exceeding by a square on the hyperbola so :eq:`CS^2 = a^2 + b^2`).

.. picture:: /_static/figures/fig_central_conic_foci.svg
   :alt: Central conic foci, equal tangent reflection angles, focal sum 2a, and auxiliary pedal circle

**Plate 6 — Focal Properties of Central Conics (Book III.45–52 [Props. 69–73])**. For foci :g:`S, S'` determined by :eq:`AS \cdot SA' = b^2`, the focal radii :g:`SP, S'P` make equal angles with the tangent at :g:`P` (`III.48`), the perpendicular feet :g:`Y, Y'` lie on the auxiliary circle of diameter :g:`AA'` (`III.49`), and :eq:`SP + S'P = AA' = 2a` (`III.52`).

* **Optical Reflection Law [Prop. 71 / III. 48]**: The focal distances :g:`SP`, :g:`S'P` of any point :g:`P` on an ellipse or hyperbola make **equal angles with the tangent** at :g:`P`.
* **Auxiliary Pedal Circle [Prop. 72 / III. 49–50]**: If from either focus :g:`S` a perpendicular :g:`SY` be dropped upon the tangent at :g:`P`, the locus of :g:`Y` is the **circle on the principal axis** :g:`AA'` as diameter (:eq:`\angle AYA' = 90^\circ`).
* **Focal Sum & Difference [Prop. 73 / III. 51–52]**: In a hyperbola :eq:`|S'P - SP| = AA'`, and in an ellipse :eq:`SP + S'P = AA'`.

4. The Locus with Respect to Three and Four Lines [Props. 74–76 / III. 53–56]
-----------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 119–125 (PDF 299–305)

.. picture:: /_static/figures/fig_three_four_line_locus.svg
   :alt: Inscribed quadrilateral in a conic illustrating the Four-Line Locus distance product law

**Plate 7 — The Three-Line and Four-Line Locus (Book III.53–56 [Props. 74–76])**. For a point :g:`P` on a conic inscribed with quadrilateral :g:`ABCD`, the product of oblique distances to opposite side-pairs maintains a constant ratio :eq:`d_1 \cdot d_3 = \lambda\, d_2 \cdot d_4` (degenerating when two sides coalesce into a tangent and chord of contact to the Three-Line Locus :eq:`d_1 \cdot d_3 = \lambda\, d_2^2`).

Propositions 74–76 (`III.53–56`) prove that if from two fixed points :g:`Q, Q'` on any conic rays :g:`QR, Q'R` from a variable curve point :g:`R` intercept segments on the tangents at :g:`Q, Q'` (or parallel lines), the **product of those intercepts is constant**—from which (:cite:`Zeuthen 1886 <zeuthen:1886>`, :cite:`Heath 1896, pp. cxxxviii–cl <heath:1896>`) the Three-Line and Four-Line Locus follows immediately by compound ratios!
