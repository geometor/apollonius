:layout: book

.. _unit-1-book-1-en:

Book I — Generation of the Cone & Fundamental Symptoms
======================================================

.. folio:: Heath 1896, Props. 1–27 [I. 1–60], pp. 1–52 (PDF 181–232)

1. Definitions & Sections of the Oblique Cone [I. Defs. 1–8, I. 1–10]
---------------------------------------------------------------------

.. folio:: Heath 1896, pp. 1–8 (PDF 181–188)

Apollonius defines the **conic surface** with complete projective generality: if from a fixed apex :g:`A` a straight line, indefinitely produced both ways, moves around the circumference of a circle :g:`BC` not in the same plane with :g:`A`, the double surface traced out consists of two **vertically opposite cones** meeting at :g:`A`. The cone is **right** (*ὀρθός*) when the axis from :g:`A` to the center of the base is perpendicular to the base, and **oblique / scalene** (*σκαληνός*) otherwise.

* **Axial Triangle & Parallel Circular Sections [I. 3–4]**: Any plane through the apex :g:`A` cuts the cone in a triangle; any plane parallel to the circular base :g:`BC` cuts the cone in a circle.
* **Subcontrary (Antiparallel) Circular Sections [I. 5, I. 9]**: If an oblique cone be cut through the axis at right angles to the base in the axial triangle :g:`ABC`, and also cut by a second plane perpendicular to :g:`ABC` cutting off toward the apex a triangle :g:`AKH` *similar but antiparallel* (:term:`hypenantia <hypenantia>`) so that :eq:`\angle AKH = \angle ABC`, the resulting section is likewise an **exact circle** (proved via :just:`III.35` and :just:`VI.4`). Every oblique circular cone thus carries two distinct conjugate families of circular sections.

2. Fundamental Symptoms via Application of Areas [Props. 1–4 / I. 11–14]
------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 8–14 (PDF 188–194)

Let a cutting plane intersect the base in :g:`DE` perpendicular to the base of the axial triangle :g:`ABC`, cutting out on the cone a curve with diameter :g:`PM` (starting at vertex :g:`P` on generator :g:`AB`). For any point :g:`Q` on the curve with :term:`ordinate <tetagmenos>` :g:`QV` parallel to :g:`DE`, the parallel circular section through :g:`V` with diameter :g:`FG` satisfies :eq:`QV^2 = FV \cdot VG` (:just:`III.35`). Translating the product :eq:`FV \cdot VG` along the axial triangle yields the three immortal species:

.. picture:: /_static/figures/fig_application_of_areas.svg
   :alt: Geometric application of areas for Parabola, Ellipse, and Hyperbola

**Plate 2 — Application of Areas (Book I.11–13 [Props. 1–3])**. Left: :term:`parabolē <parabole>` (:eq:`y^2 = px`, exact application to :term:`orthia <orthia>` :g:`p`). Center: :term:`elleipsis <elleipsis>` (:eq:`y^2 = px - \frac{p}{d}x^2`, falling short by a similar rectangle). Right: :term:`hyperbolē <hyperbole>` (:eq:`y^2 = px + \frac{p}{d}x^2`, exceeding by a similar rectangle).

.. enunciation::

   **Proposition 1 [I. 11] — The Parabola (παραβολή)**. If a cone be cut by a plane through its axis, and also by another plane cutting the base in a straight line perpendicular to the base of the axial triangle, and if further the diameter of the section be **parallel to one of the sides of the axial triangle**, then any straight line :g:`QV` drawn from the section parallel to the common section of the cutting plane and the base to meet the diameter :g:`PM` will be **equal in square** to the rectangle contained by :g:`PV` and a certain fixed straight line :g:`PL` (:term:`latus rectum <orthia>`), where :eq:`PL : PA = BC^2 : BA \cdot AC`:

   .. math::

      QV^2 = PL \cdot PV \qquad \bigl(y^2 = p x\bigr).

.. enunciation::

   **Proposition 2 [I. 12] — The Hyperbola (ὑπερβολή)**. If the diameter of the section meet one side of the axial triangle and **the other side produced beyond the vertex** :g:`A` at :g:`P'`, and if :g:`PL` (:eq:`= p`) be erected perpendicular to :g:`PP'` (:eq:`= d`) with :eq:`PL : PP' = BF \cdot FC : AF^2` (for :g:`AF \parallel PP'`), then :g:`QV^2` equals the rectangle applied to :g:`PL` with width :g:`PV`, **exceeding** (*ὑπερβάλλον*, :just:`VI.29`) by a figure similar and similarly situated to the rectangle :eq:`PP' \cdot PL`:

   .. math::

      QV^2 = PV \cdot PL + \frac{PL}{PP'} PV^2 \qquad \Longleftrightarrow \qquad QV^2 : PV \cdot VP' = p : d.

.. enunciation::

   **Proposition 3 [I. 13] — The Ellipse (ἔλλειψις)**. If the cutting plane meet **both sides of the axial triangle** on the same nape at :g:`P` and :g:`P'`, then :g:`QV^2` equals the rectangle applied to :g:`PL` with width :g:`PV`, **falling short** (*ἐλλεῖπον*, :just:`VI.28`) by a figure similar and similarly situated to the rectangle :eq:`PP' \cdot PL`:

   .. math::

      QV^2 = PV \cdot PL - \frac{PL}{PP'} PV^2 \qquad \Longleftrightarrow \qquad QV^2 : PV \cdot VP' = p : d.

.. enunciation::

   **Proposition 4 [I. 14] — The Opposite Branches (αἱ ἀντικείμεναι)**. If the vertically opposite surfaces of the double cone be cut by a plane not passing through the vertex, the sections on the two napes have a common transverse diameter :g:`PP'` and **equal parameters (latera recta)** corresponding to it.

3. Tangents, Harmonic Division & Change of Diameter [Props. 12–27 / I. 33–60]
-----------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 22–52 (PDF 202–232)

Apollonius establishes tangent lines without limits by proving that no straight line can fall between the tangent and the curve (extending :just:`III.16`), and discovers that **tangency is governed by harmonic division**:

.. picture:: /_static/figures/fig_tangent_harmonic_division.svg
   :alt: Harmonic division of conic diameter by tangent and ordinate foot

**Plate 3 — Tangent & Harmonic Division (Book I.34, 36–37 [Props. 13–14])**. On diameter :g:`PP'` with center :g:`C`, the ordinate foot :g:`V` of contact point :g:`Q` and the tangent meet :g:`T` divide the vertices :g:`P, P'` harmonically: :eq:`TP : TP' = PV : VP'`, equivalently :eq:`CT \cdot CV = CP^2`.

* **Parabola Tangent Bisection [Prop. 12 / I. 33, 35]**: If :g:`QV` be an ordinate to diameter :g:`PV` of a parabola and :g:`TP = PV` be set off outside the vertex :g:`P`, then :g:`TQ` touches the parabola, and conversely every tangent satisfies :eq:`TP = PV` (subtangent equals twice the abscissa).
* **Central Conic Harmonic Tangent [Props. 13–14 / I. 34, 36, 37]**: For a hyperbola, ellipse, or circle with diameter :g:`PP'` and center :g:`C`, :g:`TQ` is tangent at :g:`Q` if and only if :g:`T` and the ordinate foot :g:`V` divide :g:`PP'` **harmonically**:

  .. math::

     \frac{TP}{TP'} = \frac{PV}{VP'} \qquad \Longleftrightarrow \qquad CT \cdot CV = CP^2 \qquad \Longleftrightarrow \qquad CV \cdot VT = PV \cdot VP'.

* **Reference to Any New Conjugate Diameter [Props. 20–21 / I. 49–51]**: Using pure Euclidean quadrangle-area identities (:just:`I.43`), Apollonius proves that if any point :g:`Q` on a conic be taken as a new vertex, the diameter through :g:`Q` and the tangent at :g:`Q` form a new oblique coordinate frame in which **the exact same area-application equation holds** with a transformed parameter :eq:`p'`.
