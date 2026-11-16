:layout: book
:canonical_id: VII.1–32 (Notes)
:breadcrumb_title: Notes
:order: 1
:tracks: English: index | Summary: summary | Notes: notes

Notes — Linear-Algebraic Spectral Meaning of Book VII
=====================================================

1. Linear-Algebraic Meaning of Apollonius's Two Theorems
--------------------------------------------------------

From the vantage point of modern linear algebra and Rational Trigonometry (:cite:`Wildberger 2005 <wildberger:2005>`), **Propositions 129 and 136 (`VII.12–13, 31`)** express the two fundamental **orthogonal invariants (trace and determinant)** of a :eq:`2 \times 2` matrix!

Let :eq:`\mathbf{u} = \overrightarrow{CP}` and :eq:`\mathbf{v} = \overrightarrow{CD}` be any pair of conjugate semi-diameter vectors of the ellipse :eq:`\mathbf{x}^\top Q \mathbf{x} = 1`, where :eq:`Q = \operatorname{diag}(a^{-2}, b^{-2})`. Conjugacy means :eq:`[\mathbf{u}, \mathbf{v}]` maps the unit circle :eq:`\xi^2 + \eta^2 = 1` (or unit hyperbola :eq:`\xi^2 - \eta^2 = 1`) onto the conic, so :eq:`M = [\mathbf{u}\ \mathbf{v}]` satisfies :eq:`M M^\top = Q^{-1} = \operatorname{diag}(a^2, b^2)`:

1. **Trace Invariance (`VII.12`)**: :eq:`\operatorname{tr}(M^\top M) = \operatorname{tr}(M M^\top) \implies \|\mathbf{u}\|^2 + \|\mathbf{v}\|^2 = a'^2 + b'^2 = a^2 + b^2`!
2. **Determinant Invariance (`VII.31`)**: :eq:`\det(M)^2 = \det(Q^{-1}) \implies (\|\mathbf{u}\|\,\|\mathbf{v}\|\sin\omega)^2 = a^2 b^2 \implies a' b' \sin\omega = ab`!

Apollonius discovered and proved both spectral invariants synthetically in 200 BCE using solely Euclidean proportions and auxiliary segments :g:`MH, MH'` on the axis!
