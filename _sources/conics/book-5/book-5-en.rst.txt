:layout: book

.. _unit-5-book-5-en:

Book V — Normals, Minimum & Maximum Lines, Subnormals & the Evolute
===================================================================

.. folio:: Heath 1896, Props. 84–113 [V. 1–77], pp. 139–196 (PDF 319–376)

Preserved solely through :person:`Thābit ibn Qurra's <thabit-ibn-qurra>` ninth-century Arabic translation (:cite:`Halley 1710 <halley:1710>`, :cite:`Nix 1889 <nix:1889>`), **Book V** is universally acclaimed by historians of mathematics as the supreme masterpiece of ancient synthetic geometry—anticipating differential curvature, centers of osculation, and the :term:`evolute <evolute>` of a conic nearly two millennia before Huygens, Leibniz, and Newton.

1. Normals as Maxima and Minima & the Subnormal Laws [Props. 84–94 / V. 1–34]
-----------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 139–159 (PDF 319–339)

Extending :person:`Euclid's <euclid>` theorems on the shortest and longest segments from an eccentric point to a circle (:just:`III.7`, :just:`III.8`), :person:`Apollonius <apollonius>` investigates the minimum and maximum straight lines :g:`GP` drawn to a conic from a point :g:`G` on its principal axis:

* **Constant Subnormal of the Parabola [Props. 87, 90 / V. 8, 13, 27]**: If :g:`G` lie on the axis of a parabola with :eq:`AG > \tfrac{1}{2} p_a`, the minimum straight line from :g:`G` to the curve is :g:`GP` whose ordinate foot :g:`N` cuts off a **constant subnormal**:

  .. math::

     NG = \tfrac{1}{2}\, p_a,

  and :g:`GP` is strictly **perpendicular to the tangent** at :g:`P` (hence a **normal**).
* **Proportional Subnormal of Central Conics [Props. 88–91 / V. 9–15, 28–29]**: For an ellipse or hyperbola with center :g:`C`, transverse axis :g:`AA'`, and principal parameter :eq:`p_a = \frac{2b^2}{a}`, a segment :g:`GP` from an axis point :g:`G` is a minimum or maximum line (and perpendicular to the tangent at :g:`P`) if and only if its subnormal :g:`NG` satisfies:

  .. math::

     NG : CN = p_a : AA' \quad \bigl(= b^2 : a^2\bigr).

2. Determination of the Evolute Diorismos [Props. 99–100 / V. 51–52]
--------------------------------------------------------------------

.. folio:: Heath 1896, pp. 168–179 (PDF 348–359)

Apollonius next poses the profound :term:`diorismos <diorismos>` problem for an **arbitrary point** :g:`O` off the axis: *how many normals can be drawn through* :g:`O` *that cut the axis between* :g:`O` *and the vertex?*

.. picture:: /_static/figures/fig_normals_evolute.svg
   :alt: Ellipse with astroidal evolute envelope and four normals from an interior point O

**Plate 9 — Normals & the Astroidal Evolute Envelope (Book V.51–63 [Props. 99–106])**. Inside the four-cusped :term:`evolute <evolute>` :eq:`(ax)^{2/3} + (by)^{2/3} = (a^2 - b^2)^{2/3}`, an interior point :g:`O` admits **four distinct normals** :g:`OP_1, OP_2, OP_3, OP_4` to the ellipse; on the evolute two normals coalesce at a center of curvature; outside the evolute only two real normals exist.

.. enunciation::

   **Proposition 99 [V. 51, 52] — Exact Evolute Threshold**. If :g:`AM` measured along the axis from vertex :g:`A` be greater than :eq:`\tfrac{1}{2} p_a` (and in the ellipse less than :g:`AC`), and if :g:`MO` be drawn perpendicular to the axis, then a critical length :eq:`y_c` can be assigned by pure cubic/mean-proportional division along the axis such that:

   - **(a)** if :eq:`OM > y_c`, **no normal** can be drawn through :g:`O` cutting the axis in that quadrant (only 2 normals exist globally on an ellipse);
   - **(b)** if :eq:`OM = y_c`, **one unique coalesced normal** can be so drawn through :g:`O` (hence :g:`O` lies directly on the **evolute**!);
   - **(c)** if :eq:`OM < y_c`, **two distinct normals** can be so drawn in that quadrant (yielding **4 real normals** globally on an ellipse, or 3 on the evolute!).

3. Constructing Normals via Apollonius's Rectangular Hyperbola [Props. 105–106 / V. 58–63]
------------------------------------------------------------------------------------------

.. folio:: Heath 1896, pp. 180–186 (PDF 360–366)

Because finding the feet :g:`P_i` of the four normals from :g:`O = (x_0, y_0)` is a **solid (degree-4 / cubic-resolvent) problem**, Apollonius constructs the normal feet synthetically (`V.62–63 [Prop. 106]`) by intersecting the given conic with an **auxiliary rectangular hyperbola** (the *Hyperbola of Apollonius*) whose asymptotes are parallel to the conic's axes!
