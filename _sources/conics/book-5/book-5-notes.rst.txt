:layout: book

.. _unit-5-book-5-notes:

Notes — Book V: Evolutes Without Calculus & Solid-Problem Reduction
===================================================================

1. How Apollonius Derives the Evolute Without Derivatives
---------------------------------------------------------

In *Heath Intro pp. lxxv–lxxvi* and *pp. 168–179*, :person:`Heath <heath>` cautions against anachronistically imagining differential calculus in Book V while marveling at how :person:`Apollonius <apollonius>` achieves the **exact same algebraic envelope** by pure Euclidean ratio inequalities (:just:`V.8`):

* In `Prop. 99 [V. 51]` for the parabola, Apollonius divides :eq:`AH = x_0 - \tfrac{1}{2}p_a` at :g:`N_1` in the ratio :eq:`HN_1 = 2 N_1 A`, i.e., :eq:`AN_1 = \tfrac{1}{3}\bigl(x_0 - \tfrac{1}{2}p_a\bigr)`.
* Using Euclid's arithmetic-geometric inequality on three segments (:eq:`27 A \cdot B^2 \le 4(A + 2B)^3`), he shows that the two positive roots of the normal abscissa equation coalesce precisely at :g:`N_1`, which immediately yields :eq:`27 p_a y_0^2 = 4(x_0 - \tfrac{1}{2}p_a)^3`—Neil's semicubical parabola!
* For the ellipse and hyperbola (`V.52`), extracting two mean proportionals (:person:`Menaechmus's <menaechmus>` cube root!) gives :eq:`(ax_0)^{2/3} \pm (by_0)^{2/3} = (a^2 \mp b^2)^{2/3}`!

2. Architectural Relevance to ``geometor.model``
------------------------------------------------

Notice how Apollonius solves a quartic normal problem geometrically in `V.62–63`: instead of expanding a messy degree-4 trigonometric polynomial in :eq:`\theta`, he intersects the given conic :eq:`\mathcal{C}` with the **Hyperbola of Apollonius** :eq:`\mathcal{H}_O`. In ``geometor.model``, representing conics by exact :eq:`3 \times 3` symmetric matrices allows normal-foot construction from any rational point :g:`O` to be expressed directly as the intersection of two exact quadrics :eq:`\mathcal{C} \cap \mathcal{H}_O`!
