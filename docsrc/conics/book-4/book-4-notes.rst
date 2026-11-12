:layout: book

.. _unit-4-book-4-notes:

Notes — Book IV: Bézout's Theorem, Five-Point Uniqueness & Pencils
==================================================================

1. Ancient Precursor to Bézout's Theorem & Five-Point Conics
------------------------------------------------------------

Book IV (`IV.24–57`) is the direct synthetic ancestor of **Bézout's Theorem** for degree-2 plane curves (:eq:`2 \times 2 = 4`), generalizing :person:`Euclid's <euclid>` :just:`III.10` (*"A circle does not cut a circle at more points than two"*—which holds only because every circle already passes through the two complex circular points at infinity :eq:`I, J`, leaving :eq:`4 - 2 = 2` finite intersections!).

Moreover, `IV.25` (`Prop. 78`) immediately implies **uniqueness of the conic through five general points** (*Heath Intro Ch. VI, pp. cli–clvi*): no two distinct conics can pass through the same five points in general position, complementing :person:`Pascal's <pascal>` *Hexagrammum Mysticum* (1640) and :person:`Pappus's <pappus>` five-point ellipse construction in *Synagoge* VIII.

2. Desargues's Involution & the Self-Polar Diagonal Triangle
------------------------------------------------------------

Look closely at Apollonius's proof technique in `IV.25–57`: given four intersection points :g:`A, B, C, D`, the intersection :g:`T = AB \cap CD` has the **exact same polar line** with respect to every conic passing through :g:`A, B, C, D`! In modern projective geometry (``geometor/pappus``), the three diagonal points :g:`E = AB \cap CD`, :g:`F = AC \cap BD`, :g:`G = AD \cap BC` of the complete quadrangle :g:`ABCD` form a **common self-polar triangle** for the entire pencil :eq:`\mathcal{C}_1 + \lambda \mathcal{C}_2 = 0`, reducing the quartic intersection of two conics algebraically to solving a single resolvent cubic :eq:`\det(Q_1 + \lambda Q_2) = 0`!
