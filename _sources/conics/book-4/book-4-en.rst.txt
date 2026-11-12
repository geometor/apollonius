:layout: book

.. _unit-4-book-4-en:

Book IV — Number of Intersections & Tangencies of Conics
========================================================

.. folio:: Heath 1896, Props. 77–83 [IV. 1–57], pp. 126–138 (PDF 306–318)

In the Preface to **Book IV** (addressed to :person:`Attalus <attalus>` after the death of :person:`Eudemus <eudemus-pergamum>`), :person:`Apollonius <apollonius>` states the exact purpose of the fourth Book: *in how many points at most can sections of cones meet one another, or meet the circumference of a circle, whether by simple intersection or by tangency—and in particular how a double-branch hyperbola meets another conic*, resolving the polemic between :person:`Conon of Samos <conon>` and :person:`Nicoteles of Cyrene <nicoteles>`.

1. Converse Harmonic Polarity [IV. 1–23]
----------------------------------------

.. folio:: Heath 1896, p. 126 (PDF 306)

Propositions `IV.1–23` supply the exact **converse** of Book III's harmonic polar theorems (`III.30–40`): if from an external point :g:`T` secants meet a conic in :g:`R, R'` and harmonic conjugates :g:`M` of :g:`T` with respect to :g:`R, R'` are marked on each secant, those harmonic conjugates lie along the **straight polar chord of contact** joining the points of tangency from :g:`T`—giving a pure straightedge-only construction of tangents!

2. Non-Coincidence of Arcs & the Four-Point Intersection Bound [Props. 77–83 / IV. 24–57]
-----------------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 126–138 (PDF 306–318)

.. picture:: /_static/figures/fig_four_point_conic_pencil.svg
   :alt: Pencil of conics intersecting in at most four common base points A, B, C, D

**Plate 8 — At Most Four Intersections & the Four-Point Conic Pencil (Book IV.24–57 [Props. 77–83])**. Two distinct conics (here an ellipse, a circle, and a two-branch hyperbola) can intersect in at most **four points** :g:`A, B, C, D`; their diagonal triangle :g:`EFG` is self-polar with respect to every conic in the pencil.

.. enunciation::

   **Proposition 77 [IV. 24] — Identity Principle for Conic Arcs**. No two conics can intersect in such a way that part of one of them is common to both, while the rest is not. (Proved via chord-bisection diameters: two curves sharing an arc :g:`q'Q'PQ` must share the same diameter :g:`PV` and half-chords everywhere.)

.. enunciation::

   **Proposition 78 [IV. 25, 38, 43] — Maximum of Four Intersection Points**. Two conics (including a circle or a double-branch hyperbola) **cannot intersect in more than four points**.

   *Proof Method via Harmonic Polarity*: Suppose two conics met in five points :g:`A, B, C, D, E` taken in order along a convex arc. Join :g:`AB` and :g:`CD` meeting at :g:`T`. On both conics simultaneously, the harmonic conjugate of :g:`T` with respect to :g:`A, B` is a single point :g:`M_1`, and with respect to :g:`C, D` is a single point :g:`M_2`. Hence both conics share the exact same polar line :g:`M_1 M_2` of pole :g:`T`, forcing any fifth common point :g:`E` to yield contradictory harmonic conjugates on a secant through :g:`T`!

.. enunciation::

   **Propositions 79–83 [IV. 26–57] — Tangency Multiplicity Counting**.
   - **Single Tangency (`Prop. 79 [IV. 26, 41–42, 46]`)**: Two conics touching at one point cannot intersect in more than **two** other points (:eq:`2 + 1 + 1 = 4`).
   - **Double Tangency / Bitangency (`Prop. 80 [IV. 27–30, 49–54]`)**: Two conics touching one another at **two** distinct points cannot intersect at any other point (:eq:`2 + 2 = 4`).
   - **Opposite-Branch Separations (`Props. 81–83 [IV. 35–37, 55–57]`)**: Complete enumeration of how single-branch conics and opposite hyperbolic branches distribute up to four intersections across napes.
