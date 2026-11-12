.. _apollonius-home:

apollonius
==========

**GEOMETOR • apollonius** presents the Digital Scriptorium **3-Track Book Codex** and cross-corpus concordance of :person:`Apollonius of Perga's <apollonius>` **Treatise on Conic Sections** (*Κωνικά*, Books I–VII, c. 200 BCE), anchored on :person:`Sir Thomas Little Heath's <heath>` landmark 1896 Cambridge University Press edition (:cite:`Heath 1896 <heath:1896>`), :person:`Johan Ludvig Heiberg's <heiberg>` Teubner Greek text (:cite:`1891–1893 <heiberg:1891>`), and :person:`Edmond Halley's <halley>` 1710 Oxford edition of :person:`Thābit ibn Qurra's <thabit-ibn-qurra>` Arabic Books V–VII (:cite:`Halley 1710 <halley:1710>`).

.. picture:: /_static/figures/fig_oblique_cone_sections.svg
   :alt: Apollonius's oblique circular double cone generating parabola, ellipse, and opposite hyperbolic branches

**The Apollonian Synthesis**: Every circular cone—right or scalene—generates the :term:`parabola <parabole>`, :term:`ellipse <elleipsis>`, :term:`hyperbola <hyperbole>`, and :term:`opposite branches <antikeimenai>` by varying the inclination of a single cutting plane.

Completing the Heath Cambridge Greek Trilogy
--------------------------------------------

With ``geometor/apollonius``, the GEOMETOR Digital Scriptorium completes Sir Thomas Little Heath's Cambridge trilogy of classical Greek geometry:

1. **Apollonius (1896)** — *Treatise on Conic Sections* (``geometor/apollonius``): **387 classical propositions** consolidated into **147 propositions** across Books I–VII, plus the analytic treasury in Pappus Book VII.
2. **Archimedes (1897 / 1912)** — *The Works of Archimedes* & *The Method* (``geometor/archimedes``): Exhaustion, mechanical equilibrium, and quadrature of conic segments and paraboloids.
3. **Euclid (1908 / 1926)** — *The Thirteen Books of Euclid's Elements* (``geometor/euclid``): The axiomatic and area-application foundation (`G.1`–`G.601` in ``geometor/elements``).

Explore the Codex
-----------------

* :doc:`Conics (3-Track Book Codex) <conics/index>` — Synchronized **English**, **Summary**, and **Notes** tracks across **8 Units** (Prefaces & Introduction, Books I–VII, and the Lost Analytic Treasury in Pappus Book VII) illustrated with **12 standalone ``.euclid-graphic`` SVG plates**.
* :doc:`Mission & Architectural Scope <mission/index>` — Exact symbolic conic roadmap, strict content/code separation, and ``sympy.geometry`` capability audit.
* :doc:`About Apollonius & the Textual Tradition <about/index>` — Life of *The Great Geometer*, the Heath Trilogy, and the Greek-Arabic manuscript transmission.
* :doc:`Python Package & Concordance API <modules/index>` — Reference for ``geometor.apollonius`` concordance verification, apparatus generation, and CLI utilities.

.. toctree::
   :maxdepth: 2
   :hidden:

   conics/index
   mission/index
   about/index
   modules/index
   changelog
