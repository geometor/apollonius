:navigation: header
:order: 20

.. _apollonius-mission:

Mission
=======

1. Unifying Classical Conics & Symbolic Algebra
-----------------------------------------------

``geometor/apollonius`` establishes the authoritative historical, terminological, and structural foundation for **conic sections and projective quadrics** across the GEOMETOR ecosystem:

* **100% Public Domain Scholarly Fidelity**: Grounded directly on folio-inspected 300 DPI scans of :person:`T. L. Heath's <heath>` 1896 Cambridge University Press edition (:cite:`Heath 1896 <heath:1896>`), cross-referenced to :person:`Heiberg's <heiberg>` Teubner Greek text of Books I–IV (:cite:`1891–1893 <heiberg:1891>`) and :person:`Halley's <halley>` 1710 Oxford edition of :person:`Thābit ibn Qurra's <thabit-ibn-qurra>` Arabic Books V–VII (:cite:`Halley 1710 <halley:1710>`).
* **Strict Content / Code Separation**: Following Digital Scriptorium architecture, zero executable Python blocks are embedded in the historical treatise RST; all **12 interactive ``.euclid-graphic`` SVG plates** are deterministically compiled via ``scripts/build_figures.py``.
* **Blueprint for Exact Symbolic Conics Beyond ``sympy.geometry``**: Whereas ``sympy.geometry`` restricts conics to axis-aligned ellipses and parabolas, Apollonius works natively in **arbitrary oblique conjugate diameters** (`Book I`), **asymptotic coordinates** (`Book II`), **harmonic pole-polar duality** (`Book III`), **four-point conic pencils** (`Book IV`), **rectangular-hyperbola normal resolvers and evolutes** (`Book V`), **trace/determinant matrix invariants** (`Book VII`), and **eight-circle `CCC` tangency** (`Pappus VII`)—defining the exact specification for future symbolic conic extensions in ``geometor.model``, ``geometor.pappus``, ``geometor.elements``, ``geometor.etc``, and ``geometor.wildberger``.
