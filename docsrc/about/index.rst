:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:
.. _apollonius-about:
.. _apollonius-mission:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

**GEOMETOR • apollonius** presents the Digital Scriptorium **3-Track Book Codex** and cross-corpus concordance of :person:`Apollonius of Perga's <apollonius>` *Treatise on Conic Sections* (*Κωνικά*, Books I–VII, c. 200 BCE). This critical digital edition is grounded directly on folio-inspected 300 DPI scans of :person:`Sir Thomas Little Heath's <heath>` landmark 1896 Cambridge University Press edition (:cite:`Heath 1896 <heath:1896>`), cross-referenced to :person:`Johan Ludvig Heiberg's <heiberg>` Teubner Greek text of Books I–IV (:cite:`1891–1893 <heiberg:1891>`) and :person:`Edmond Halley's <halley>` monumental 1710 Oxford folio of :person:`Thābit ibn Qurra's <thabit-ibn-qurra>` Arabic Books V–VII (:cite:`Halley 1710 <halley:1710>`).

The codex extracts Apollonius's monumental deductive corpus—387 classical propositions consolidated into 147 propositions across Books I–VII, plus the analytic treasury in Pappus Book VII—into synchronized **English**, **Summary**, and **Notes** tracks across 8 structural units. Following the Digital Scriptorium architecture, zero executable Python blocks are embedded into the treatise source; all interactive ``.euclid-graphic`` SVG plates are deterministically compiled. Every proposition, definition, enunciation, step, and historical annotation is rendered addressable, establishing the blueprint for symbolic conics far beyond the capabilities of conventional computer algebra systems: arbitrary oblique conjugate diameters (Book I), asymptotic coordinates (Book II), harmonic pole-polar duality (Book III), four-point conic pencils (Book IV), rectangular-hyperbola normal resolvers and evolutes (Book V), trace/determinant matrix invariants (Book VII), and eight-circle ``CCC`` tangency (Pappus VII).

Within the GEOMETOR ecosystem, this edition completes Heath's celebrated Cambridge Greek Trilogy alongside ``geometor/archimedes`` (*The Works of Archimedes* and *The Method*) and ``geometor/euclid`` (*The Thirteen Books of Euclid's Elements*). It provides the definitive projective and quadratic bridge linking Euclidean plane foundations (``geometor.elements``), projective and harmonic ranges (``geometor.pappus``, ``geometor.divine``), Kimberling triangle center structures (``geometor.etc``), and Rational Trigonometry (``geometor.wildberger``).

The GEOMETOR Mission
--------------------

The GEOMETOR project, directed by **phi ARCHITECT**, is dedicated to the systematic recovery, exact formalization, and dynamic re-expression of foundational geometric and philosophical knowledge. The mission unfolds across three essential pillars:

* **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans and OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises—elevating prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs.
* **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions in 100% exact symbolic algebra (using ``SymPy``) and Rational Trigonometry invariants (quadrance, spread, cross-ratio) over exact algebraic fields rather than floating-point approximations.
* **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and EPUB 3 editions (via ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG laboratories (``geometor.explorer``), QHD visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across ``geometor.com``.

Sources, Provenance & Methodology
---------------------------------

Archival Sources & Critical Editions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **T. L. Heath (1896)**: *Treatise on Conic Sections*, edited in modern notation with introductions including an essay on the earlier history of the subject by T. L. Heath. Cambridge: Cambridge University Press, 1896.
* **J. L. Heiberg (1891–1893)**: *Apollonii Pergaei quae Graece exstant cum commentariis antiquis*, 2 vols. Leipzig: B. G. Teubner (critical Greek text and Latin translation of Books I–IV and Eutocius's commentary).
* **Edmond Halley (1710)**: *Apollonii Pergaei Conicorum Libri Octo et Sereni Antissensis De Sectione Cylindri & Coni Libri Duo*. Oxford: Theater Sheldonian (Latin translation of Thābit ibn Qurra's Arabic text of Books V–VII, Greek Books I–IV, and Halley's conjectural restoration of Book VIII).

Digital Scriptorium Methodology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Strict Content / Code Separation**: RST source files maintain absolute textual purity; all diagrammatic representations are compiled to standalone, accessible SVG graphics with exact mathematical coordinates.
* **Synchronized Multi-Track Codex**: Readers navigate side-by-side between unabridged English demonstrations, concise modern synopses, and deep historical/mathematical commentary notes.
* **Systematic Concordance & Prosopography**: Biographies of 29 ancient and early modern mathematicians are cross-linked via ``:person:`` roles, accompanied by complete bibliographic citations and citation keys.

Historical & Textual Transmission Essays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :doc:`Apollonius of Perga: The Great Geometer <apollonius-of-perga>` — Life at Perga, Alexandria, Ephesus, and Pergamum; astronomical epicycles and lost works.
* :doc:`The Heath Cambridge Greek Trilogy (1896–1912) <heath-trilogy>` — How Heath's 1896 *Apollonius* inaugurated the unified edition of Apollonius, Archimedes, and Euclid.
* :doc:`Greek & Arabic Textual Transmission <textual-transmission>` — From Eutocius's Byzantine Greek recension (Books I–IV) and the Banū Mūsā / Thābit ibn Qurra Baghdad translation (Books V–VII) to Halley (1710) and Heiberg (1891–1893).

.. toctree::
   :maxdepth: 1
   :hidden:

   apollonius-of-perga
   heath-trilogy
   textual-transmission
