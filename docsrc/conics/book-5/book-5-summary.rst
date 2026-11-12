:layout: book

.. _unit-5-book-5-summary:

Summary — Book V (Propositions 84–113 [V. 1–77])
================================================

1. Subnormals, Evolute Equations & Normal Multiplicity
------------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 24 34 24

   * - Conic
     - Subnormal :g:`NG`
     - Evolute Equation Derived from `Prop. 99 [V. 51–52]`
     - Real Normals from :g:`O`
   * - **Parabola** (:eq:`y^2 = px`)
     - :eq:`NG = \tfrac{1}{2} p` (constant)
     - :eq:`27 p y^2 = 4\bigl(x - \tfrac{1}{2}p\bigr)^3` (Semicubical Parabola)
     - **3** (inside), **2** (on cusp-arc), **1** (outside)
   * - **Ellipse** (:eq:`\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1`)
     - :eq:`NG = \frac{b^2}{a^2} CN`
     - :eq:`(a x)^{2/3} + (b y)^{2/3} = (a^2 - b^2)^{2/3}` (Astroidal Lamé Curve)
     - **4** (inside), **3** (on arc), **2** (outside / at cusps)
   * - **Hyperbola** (:eq:`\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1`)
     - :eq:`NG = \frac{b^2}{a^2} CN`
     - :eq:`(a x)^{2/3} - (b y)^{2/3} = (a^2 + b^2)^{2/3}`
     - **4**, **3**, or **2** across branches

2. The Hyperbola of Apollonius (`V. 62–63 [Prop. 106]`)
-------------------------------------------------------

For an ellipse :eq:`\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1` and target point :g:`O = (x_0, y_0)`, the normal at :g:`P = (x, y)` passes through :g:`O` if and only if :g:`P` lies on the auxiliary rectangular hyperbola:

.. math::

   (a^2 - b^2)\, x y + b^2 y_0\, x - a^2 x_0\, y = 0,

which passes through the center :g:`C = (0,0)`, the target point :g:`O = (x_0, y_0)`, and has asymptotes parallel to the principal axes—intersecting the conic in at most **4 points** by :doc:`Book IV Prop. 78 </conics/book-4/book-4-en>`!
