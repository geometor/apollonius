:layout: book
:canonical_id: III.30–40 (Notes)
:breadcrumb_title: Notes
:order: 2
:tracks: English: index | Summary: summary | Notes: notes
:folio: Heath 1896, pp. 102–108 (PDF 282–288)

Notes — Bridge to Lean mathlib4 & sympy Gaps
============================================

2. Bridge to ``geometor/pappus`` & Lean ``mathlib4`` (``PolePolar.lean``)
-------------------------------------------------------------------------

Propositions 62–66 (`III.30–40`) are the historical birthplace of **projective polarity**:

* In homogeneous coordinates with symmetric :eq:`3 \times 3` conic matrix :eq:`Q`, the polar of :g:`T` is the linear form :eq:`x \mapsto x^\top Q T`, and harmonic cross-ratio :eq:`(T, M; R, R') = -1` holds over any field of characteristic :eq:`\neq 2`—formalized algebraically in Lean 4's :cite:`Mathlib QuadraticForm.PolePolar <mathlib4:polepolar>` and modeled constructively in ``geometor/pappus``.
* Crucially, ``sympy.geometry`` still **lacks** general conic `polar_line` and `pole_point` methods—one of the primary capabilities catalogued in our :doc:`Concordance Gap Audit </conics/concordance>`.
