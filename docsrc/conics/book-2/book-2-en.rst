:layout: book

.. _unit-2-book-2-en:

Book II — Asymptotes, Conjugate Hyperbolas & Secant Intercepts
==============================================================

.. folio:: Heath 1896, Props. 28–53 [II. 1–53], pp. 53–94 (PDF 233–274)

1. Construction & Non-Meeting of the Asymptotes [Props. 28–29 / II. 1–2, 15, 17, 21]
------------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 53–56 (PDF 233–236)

Book II opens with the geometric construction of the :term:`asymptotes <asymptotoi>` (*αἱ ἀσύμπτωτοι*) of a hyperbola, its opposite branch, and its conjugate hyperbolas from the :term:`characteristic figure <eidos>` of any diameter :g:`PP'`:

.. enunciation::

   **Proposition 28 [II. 1, 15, 17, 21] — Construction of the Asymptotes**.
   (1) If :g:`PP'` be a diameter of a hyperbola and :eq:`p` the corresponding parameter, and if on the tangent at :g:`P` there be set off on each side equal lengths :g:`PL`, :g:`PL'` such that

   .. math::

      PL^2 = PL'^2 = \tfrac{1}{4}\, p \cdot PP' \quad [= CD^2],

   then :g:`CL`, :g:`CL'` produced from the center :g:`C` will **not meet the curve in any finite point** and are accordingly defined as **asymptotes**.
   (2) The :term:`opposite branches <antikeimenai>` have the same asymptotes.
   (3) **Conjugate hyperbolas** (having :g:`DD'` as transverse diameter and :g:`PP'` as secondary diameter) share the exact same asymptotes.

.. enunciation::

   **Proposition 29 [II. 2] — Uniqueness of the Asymptotic Sector**. No straight line through the center :g:`C` within the angle between the asymptotes :g:`CL`, :g:`CL'` can itself be an asymptote; every such ray meets the hyperbola.

2. Secant Intercepts, Bisected Tangents & the Asymptotic Equation [Props. 30–35 / II. 3–16]
-------------------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 56–63 (PDF 236–243)

.. picture:: /_static/figures/fig_hyperbola_asymptotes_secant.svg
   :alt: Hyperbola, conjugate hyperbola, common asymptotes, bisected tangent, and equal secant intercepts

**Plate 4 — Asymptotes, Conjugate Hyperbolas & Equal Secant Intercepts (Book II.1–21 [Props. 28–38])**. Both conjugate hyperbolas share asymptotes :g:`CL`, :g:`CL'`; any tangent segment :g:`LL'` between the asymptotes is bisected at its point of contact :g:`P`; any secant meeting the hyperbola at :g:`Q, Q'` and the asymptotes at :g:`R, R'` cuts off equal intercepts :eq:`RQ = Q'R'` with :eq:`RQ \cdot QR' = PL^2`.

* **Bisected Tangent Segment [Prop. 30 / II. 3, 9]**: If a straight line touch a hyperbola at :g:`P` and meet the asymptotes in :g:`L, L'`, then :g:`LL'` is **bisected at** :g:`P` (:eq:`LP = PL'`), and :eq:`PL^2 = \tfrac{1}{4}\, p \cdot PP'`.
* **Equal Secant Intercepts [Prop. 33 / II. 8, 10, 16]**: If any straight line meet a hyperbola in :g:`Q, Q'` and its asymptotes in :g:`R, R'` (whether across a single branch or across opposite branches), the outer intercepts between curve and asymptotes are strictly equal:

  .. math::

     RQ = Q'R' \qquad \text{and} \qquad RQ \cdot QR' = PL^2 = b'^2,

  where :g:`PL` is the half-tangent parallel to the secant (:just:`II.5`, :just:`II.6`).
* **Asymptotic Coordinate Equation [Prop. 34 / II. 12]**: If from any two points :g:`Q`, :g:`q` on a hyperbola straight lines :g:`QM, QN` and :g:`qm, qn` be drawn in given directions to meet the two asymptotes, the rectangles contained by those asymptotic coordinates are equal:

  .. math::

     QM \cdot QN = qm \cdot qn \qquad \bigl(x y = \text{const.}\bigr).

* **Arbitrary Closeness without Contact [Prop. 35 / II. 14]**: The asymptotes and the hyperbola, when produced indefinitely, approach continually nearer to one another and eventually come within a distance **less than any assigned length** (:just:`X.1`).

3. Finding Diameters, Axes & Tangents by Compass and Straightedge [Props. 47–53 / II. 44–53]
--------------------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 72–94 (PDF 252–274)

In the closing chapters of Book II (`II.44–53`), Apollonius solves the fundamental **problems of geometric recovery** on a ready-drawn conic arc whose cone and parameters are unknown:

1. **Finding a Diameter & Center (`II.44–45 [Props. 47–48]`)**: Bisecting two parallel chords gives a diameter; intersecting two non-parallel diameters gives the center :g:`C`.
2. **Finding the Principal Orthogonal Axes (`II.46–48 [Props. 49–50]`)**: For the parabola, dropping a chord perpendicular to the found diameter locates the unique axis; for a central conic, describing a circle around :g:`C` intersecting the conic in :g:`K, H` yields the two orthogonal axes bisecting :g:`KH` and its supplement (:just:`III.3`).
3. **Drawing Tangents from Any Point (`II.49 [Prop. 51]`)**: Given an external point :g:`T`, Apollonius constructs the contact points :g:`Q, Q'` via harmonic division on the diameter through :g:`T` (:eq:`CT \cdot CV = CP^2` for central conics; :eq:`TP = PV` for the parabola), proving that at most two tangents pass through :g:`T`.
