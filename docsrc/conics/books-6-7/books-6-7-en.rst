:layout: book

.. _unit-6-books-6-7-en:

Books VI & VII — Equal and Similar Conics & Conjugate Diameters
===============================================================

.. folio:: Heath 1896, Props. 114–147 [VI. 1–33 & VII. 1–51], pp. 197–254 (PDF 377–434)

Preserved alongside Book V in :person:`Thābit ibn Qurra's <thabit-ibn-qurra>` Arabic translation (:cite:`Halley 1710 <halley:1710>`), **Books VI and VII** complete the extant treatise: Book VI establishes the invariants of congruence, similarity, and 3D cone embedding, while Book VII crowns ancient geometric algebra with **Apollonius's Theorems on Conjugate Diameters** and the inequality :term:`diorismoi <diorismos>` built for the lost Book VIII.

1. Book VI — Equal & Similar Conics and Cone Embedding [Props. 114–122 / VI. 1–33]
----------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 197–220 (PDF 377–400)

Book VI opens with **six explicit Definitions** (*p. 197*): two conics are **equal** (*ἴσαι*) when one can be applied to the other so as everywhere to coincide, and **similar** (*ὅμοιαι*) when ordinates drawn to the axis at proportional distances from the vertex are everywhere proportional to their abscissae.

* **Universal Similarity of Parabolas [Prop. 115 / VI. 11]**: **All parabolas are similar to one another** (scaling all lengths by the ratio of their latera recta :eq:`p_1 : p_2` maps one onto the other).
* **Criterion for Similar Central Conics [Prop. 116 / VI. 12–13]**: Two ellipses or two hyperbolas are **similar** if and only if the :term:`characteristic figures <eidos>` :eq:`AA' \times p_a` on their axes are similar rectangles (:eq:`p_1 : AA'_1 = p_2 : AA'_2`, i.e. equal eccentricity!). Parabolas, ellipses, and hyperbolas are mutually dissimilar (`VI.14–15`).
* **Cutting Any Given Conic from Any Given Right Cone [Props. 120–122 / VI. 28–30]**: Given *any* right circular cone and *any* prescribed parabola (`VI.28`), hyperbola (`VI.29`), or ellipse (`VI.30`), Apollonius constructs the exact cutting plane—proving that a **single right cone suffices to generate every possible parabola and ellipse, and every hyperbola whose asymptotic angle does not exceed the cone's vertical angle**!

2. Book VII — Apollonius's Conjugate Diameter Theorems [Props. 123–147 / VII. 1–51]
-----------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 221–254 (PDF 401–434)

Using two ingenious focal-like **auxiliary points** :g:`H, H'` laid off along the principal axis :g:`AA'` such that :eq:`AH : HA' = p_a : AA'` (`Props. 123–128 [VII. 1–11]`), Apollonius reduces the lengths of *any* pair of oblique :term:`conjugate diameters <diametros>` :g:`PP'` (:eq:`= 2a'`) and :g:`DD'` (:eq:`= 2b'`) to pure focal-style segments along the axis, proving his two celebrated invariance theorems:

.. picture:: /_static/figures/fig_conjugate_diameters_theorems.svg
   :alt: Ellipse with principal axes AA', BB', oblique conjugate diameters PP', DD', and circumscribed tangent parallelogram LL'MM'

**Plate 10 — Apollonius's Conjugate Diameter Theorems (Book VII.12, 13, 31 [Props. 129 & 136])**. On an ellipse with semi-axes :eq:`CA = a`, :eq:`CB = b` and any oblique conjugate semi-diameters :eq:`CP = a'`, :eq:`CD = b'` inclined at angle :eq:`\omega`: (1) :eq:`a'^2 + b'^2 = a^2 + b^2`; (2) the circumscribed tangent parallelogram :g:`LL'MM'` has constant area :eq:`4 a' b' \sin\omega = 4ab`.

.. enunciation::

   **Proposition 129 [VII. 12, 13, 29, 30] — Apollonius's First Theorem (Quadratic Trace Invariance)**. In every ellipse the **sum**, and in every hyperbola the **difference**, of the squares on any two conjugate diameters :g:`PP'`, :g:`DD'` is equal to the sum or difference respectively of the squares on the principal axes :g:`AA'`, :g:`BB'`:

   .. math::

      PP'^2 + DD'^2 = AA'^2 + BB'^2 \quad (\text{ellipse}: a'^2 + b'^2 = a^2 + b^2),

   .. math::

      PP'^2 - DD'^2 = AA'^2 - BB'^2 \quad (\text{hyperbola}: a'^2 - b'^2 = a^2 - b^2).

.. enunciation::

   **Proposition 136 [VII. 31] — Apollonius's Second Theorem (Circumscribed Parallelogram Area Invariance)**. If :g:`PP'`, :g:`DD'` be conjugate diameters of an ellipse or of conjugate hyperbolas, and tangents drawn at their extremities :g:`P, P', D, D'` form the circumscribed parallelogram :g:`LL'MM'`, its **area is invariant** and equal to the rectangle contained by the principal axes:

   .. math::

      \operatorname{Area}(\square LL'MM') = AA' \cdot BB' \qquad \bigl(a' b' \sin\omega = a b\bigr).

3. Extrema of Conjugate Functions for Book VIII [Props. 131–147 / VII. 21–51]
-----------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 231–254 (PDF 411–434)

Propositions `131–147 [VII. 21–51]` establish monotonic variations and global maxima/minima for :eq:`PP' \pm DD'`, :eq:`PP' \cdot DD'`, parameter :eq:`p`, and :eq:`PP'^2 \pm p^2` as :g:`P` moves from major vertex :g:`A` to minor vertex :g:`B` (e.g., `Prop. 133 [VII. 25–26]`: :eq:`PP' + DD'` attains its unique **maximum** on an ellipse at the **equal conjugate diameters**, and its **minimum** at the axes :eq:`AA' + BB'`), ending at **Proposition 147 [VII. 51]** (*pp. 253–254*).
