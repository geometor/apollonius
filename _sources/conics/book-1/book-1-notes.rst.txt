:layout: book

.. _unit-1-book-1-notes:

Notes — Book I: Geometric Algebra, Order of Curves & Projective Frames
======================================================================

1. Why Apollonius Orders the Curves Parabola → Hyperbola → Ellipse
------------------------------------------------------------------

Modern textbooks routinely list *ellipse, parabola, hyperbola* by eccentricity (:eq:`e < 1`, :eq:`e = 1`, :eq:`e > 1`). In **Book I.11–13**, however, :person:`Apollonius <apollonius>` proves **Parabola (`I.11`)**, then **Hyperbola (`I.12`)**, then **Ellipse (`I.13`)**:

* In `I.11`, the cutting plane is parallel to a side of the axial triangle, giving the simplest one-parameter application :eq:`y^2 = px`.
* In `I.12` and `I.13`, the cutting plane is non-parallel to both sides; when the intersection :g:`P'` with the second generator falls above the apex :g:`A` on the opposite nape (`I.12`, hyperbola), the auxiliary parallel :g:`AF` falls *outside* the axial triangle, whereas for `I.13` (ellipse) it falls *inside*, and both proofs pave the immediate transition to `I.14` (:term:`opposite branches <antikeimenai>`).

2. Connection to Euclid VI.27–29 & Rational Trigonometry
--------------------------------------------------------

Apollonius's naming triad translates :person:`Euclid's <euclid>` Pythagorean **application of areas** (:just:`I.44`, :just:`VI.27`, :just:`VI.28`, :just:`VI.29` in ``geometor/euclid``) directly into curve theory:

* Because :eq:`d'^2 = p \cdot d` defines the conjugate diameter :eq:`d' = 2b` for transverse diameter :eq:`d = 2a` (so :eq:`p = \frac{2b^2}{a}`), shifting origin from the vertex :g:`P` (:eq:`x = a \mp X`) to the center :g:`C` converts Apollonius's two-vertex proportion :eq:`QV^2 : PV \cdot VP' = p : d = b^2 : a^2` immediately into the central quadratic form

  .. math::

     \frac{X^2}{a^2} \pm \frac{Y^2}{b^2} = 1,

  purely in **quadrances** (:cite:`Wildberger 2005 <wildberger:2005>`) without a single trigonometric function even when :eq:`X, Y` are measured along *oblique* conjugate diameters!

3. Tangent Harmonicity as 1D Projective Polarity
------------------------------------------------

Propositions 12–14 (`I.33–37`) reveal why the parabola's :eq:`TP = PV` is the exact projective limit of :eq:`TP : TP' = PV : VP'`: as the second vertex :g:`P'` recedes to infinity along the diameter, the ratio :eq:`TP' / VP' \to 1`, leaving :g:`P` as the midpoint of :g:`TV`—that is, :eq:`(P, \infty; V, T) = -1`.
