:layout: book
:canonical_id: Book I
:breadcrumb_title: Book I
:order: 1
:title: Book I: Generation of the Cone & Fundamental Symptoms
:hero: /_static/figures/fig_application_of_areas.svg

.. _unit-1-book-1-en:
.. _unit-1-book-1-summary:
.. _unit-1-book-1-notes:
.. _conics-book-1:

Book I: Generation of the Cone & Fundamental Symptoms
=====================================================

.. rubric:: Propositions 1–27 [Classical I. 1–60] — Apollonius of Perga (ed. T. L. Heath, 1896)

.. folio:: Heath 1896, Props. 1–27 [I. 1–60], pp. 1–52 (PDF 181–232)

Book I unifies the generation of second-degree curves by producing the parabola, hyperbola, ellipse, and two-branched opposite sections from a single arbitrary oblique circular double cone. Through the Pythagorean-Euclidean technique of the *application of areas*, Apollonius defines the fundamental symptom (:term:`symptōma <symptoma>`) of each curve, discovers harmonic division on diameters by tangents and ordinates, and proves that every conic maintains its symptom under transformation to any new oblique diameter and tangent frame.

Deductive Chain of Book I
-------------------------

1. **The Cone (`I.1–10`)**: Oblique double cone, axial triangle, parallel circular sections (`I.4`), and antiparallel :term:`subcontrary sections <hypenantia>` (`I.5, 9`).
2. **Fundamental Symptoms (`Props. 1–4 [I.11–14]`)**:
   - **Parabola (`I.11`)**: :eq:`y^2 = p x` (exact application).
   - **Hyperbola (`I.12`)**: :eq:`y^2 = p x + \frac{p}{d}x^2` (application with excess; two-vertex ratio :eq:`y^2 : x(d + x) = p : d`).
   - **Ellipse (`I.13`)**: :eq:`y^2 = p x - \frac{p}{d}x^2` (application with defect; two-vertex ratio :eq:`y^2 : x(d - x) = p : d`).
   - **Opposite Branches (`I.14`)**: Equal parameter :eq:`p` on both napes.
3. **Conjugate Diameters (`Props. 5–6 [I.15–16]`)**: Existence of center :g:`C` bisecting :g:`PP'` and secondary conjugate diameter :g:`DD'` of length :eq:`d'` satisfying :eq:`d'^2 = p \cdot d`.
4. **Secants & Tangents (`Props. 7–15 [I.17–38]`)**:
   - Parabola subtangent law: :eq:`TP = PV`.
   - Central conic harmonic tangent law: :eq:`(P, P'; V, T) = -1` and :eq:`CT \cdot CV = CP^2 = a^2`.
5. **Transformation of Oblique Coordinates (`Props. 16–21 [I.42–51]`)**: Area-equivalence of trapezoids between diameter, tangent, and ordinate transfers the symptom from the original cone-derived diameter to *any* diameter :g:`QQ'` on the conic.
6. **Synthetic Construction of Conics (`Props. 22–27 [I.52–60]`)**: Given in a plane a diameter :g:`PP'`, ordinate angle :eq:`\omega`, and parameter :eq:`p`, Apollonius constructs in 3D a *right* circular cone whose plane section reproduces the prescribed parabola, hyperbola, conjugate hyperbolas, or ellipse—proving existence and completeness of planar quadratic curves.

Sections
--------

.. collection::
   :sort: order

.. toctree::
   :hidden:
   :maxdepth: 1

   sec_01_cone_sections/index
   sec_02_application_of_areas/index
   sec_03_tangents_coordinates/index
