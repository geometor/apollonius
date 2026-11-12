:layout: book

.. _unit-6-books-6-7-notes:

Notes — Books VI & VII: Spectral Matrix Invariants & the Lost Book VIII
=======================================================================

1. Linear-Algebraic Meaning of Apollonius's Two Theorems
--------------------------------------------------------

From the vantage point of modern linear algebra and Rational Trigonometry (:cite:`Wildberger 2005 <wildberger:2005>`), **Propositions 129 and 136 (`VII.12–13, 31`)** express the two fundamental **orthogonal invariants (trace and determinant)** of a :eq:`2 \times 2` matrix!

Let :eq:`\mathbf{u} = \overrightarrow{CP}` and :eq:`\mathbf{v} = \overrightarrow{CD}` be any pair of conjugate semi-diameter vectors of the ellipse :eq:`\mathbf{x}^\top Q \mathbf{x} = 1`, where :eq:`Q = \operatorname{diag}(a^{-2}, b^{-2})`. Conjugacy means :eq:`[\mathbf{u}, \mathbf{v}]` maps the unit circle :eq:`\xi^2 + \eta^2 = 1` (or unit hyperbola :eq:`\xi^2 - \eta^2 = 1`) onto the conic, so :eq:`M = [\mathbf{u}\ \mathbf{v}]` satisfies :eq:`M M^\top = Q^{-1} = \operatorname{diag}(a^2, b^2)`:

1. **Trace Invariance (`VII.12`)**: :eq:`\operatorname{tr}(M^\top M) = \operatorname{tr}(M M^\top) \implies \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 = a'^2 + b'^2 = a^2 + b^2`!
2. **Determinant Invariance (`VII.31`)**: :eq:`\det(M)^2 = \det(Q^{-1}) \implies (\|\mathbf{u}\|\,\|\mathbf{v}\|\sin\omega)^2 = a^2 b^2 \implies a' b' \sin\omega = ab`!

Apollonius discovered and proved both spectral invariants synthetically in 200 BCE using solely Euclidean proportions and auxiliary segments :g:`MH, MH'` on the axis!

2. How Book VII Reconstructs the Lost Book VIII
-----------------------------------------------

In the **Preface to Book VII** (*Heath p. lxxv*), Apollonius explicitly tells :person:`Attalus <attalus>` why he forged the intricate inequality theorems `VII.21–51`: *"Several examples of these occur in the determinate conic problems solved and demonstrated by me in the eighth book, which is by way of an appendix."* Both :person:`Ibn al-Haytham <ibn-al-haytham>` (c. 1024 CE) and :person:`Edmond Halley <halley>` (:cite:`1710 <halley:1710>`) used this clue—together with :person:`Pappus's <pappus>` preserved lemmas for Books VII and VIII intertwined in *Synagoge* VII—to reconstruct Book VIII as the constructive solution of conics given prescribed conjugate-diameter sums, differences, ratios, or parameters.
