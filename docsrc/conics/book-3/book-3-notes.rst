:layout: book

.. _unit-3-book-3-notes:

Notes — Book III: Why Apollonius Omitted the Parabola Focus, Lean Polarity & Descartes
======================================================================================

1. Why Book III Omits the Focus of the Parabola
-----------------------------------------------

Every attentive reader of **Book III.45–52** asks why :person:`Apollonius <apollonius>` proves the optical reflection property and focal properties for the **ellipse and hyperbola**, yet never mentions the focus of the **parabola** (treated contemporaneously by :person:`Diocles <diocles>` in *On Burning Mirrors* and via focus-directrix in :person:`Pappus <pappus>`, *Synagoge* VII.238):

* Apollonius defines the foci :g:`S, S'` strictly as :term:`"the points arising out of the application" <semeia-ek-tes-paraboles>` along the **finite two-vertex transverse axis** :g:`AA'` (:eq:`AS \cdot SA' = \tfrac{1}{4} p_a \cdot AA'`).
* Because the parabola has **no center** :g:`C` and **no second vertex** :g:`A'` at finite distance, a two-vertex area application along :g:`AA'` cannot even be stated without passing to the projective limit :eq:`A' \to \infty` (:eq:`AS \cdot (SA'/AA') \to \tfrac{1}{4} p_a`, placing :g:`S` at distance :eq:`\tfrac{1}{4} p_a` from the vertex, as :person:`Kepler <kepler>` first articulated in :cite:`1604 <kepler:1604>`)!

2. Bridge to ``geometor/pappus`` & Lean ``mathlib4`` (``PolePolar.lean``)
-------------------------------------------------------------------------

Propositions 62–66 (`III.30–40`) are the historical birthplace of **projective polarity**:

* In homogeneous coordinates with symmetric :eq:`3 \times 3` conic matrix :eq:`Q`, the polar of :g:`T` is the linear form :eq:`x \mapsto x^\top Q T`, and harmonic cross-ratio :eq:`(T, M; R, R') = -1` holds over any field of characteristic :eq:`\neq 2`—formalized algebraically in Lean 4's :cite:`Mathlib QuadraticForm.PolePolar <mathlib4:polepolar>` and modeled constructively in ``geometor/pappus``.
* Crucially, ``sympy.geometry`` still **lacks** general conic `polar_line` and `pole_point` methods—one of the primary capabilities catalogued in our :doc:`Concordance Gap Audit </conics/concordance>`.

3. From Book III.53–56 to Pappus VII & Descartes's *La Géométrie* (1637)
------------------------------------------------------------------------

In Book III (`III.41–43` too!), Note `Prop. 67 [III. 41]` already gives the **quadratic Bézier / Steiner tangent envelope** of a parabola (:eq:`QP : Pr = r'Q : r'P'`)! And `III.53–56` (`Props. 74–76`), preserved alongside :person:`Pappus's <pappus>` commentary in *Synagoge* VII (:cite:`Hultsch 1877 <hultsch:1877>`), inspired :person:`René Descartes <descartes>` (:cite:`1637 <descartes:1637>`) to translate oblique distances :eq:`d_1 d_3 = \lambda d_2 d_4` into bivariate polynomial equations :eq:`F(x, y) = 0`, founding modern algebraic geometry.
