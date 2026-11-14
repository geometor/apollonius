:navigation: header
:order: 20
:nav_title: Usage

Using This Edition
==================

.. rubric:: Interactive Reader's Guide to Apollonius of Perga's *Treatise on Conic Sections*

This digital critical edition of Apollonius of Perga's *Conics* (ed. Sir Thomas Little Heath, 1896) provides an interactive reading environment engineered for geometric deduction, archival witness cross-examination, and symbolic conic analysis.

Interactive Features
--------------------

1. Synchronized Reading Tracks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Each unit of the *Conics* Book Codex presents three synchronized reading tracks available via the top track toggle buttons:

* **English Track**: T. L. Heath's definitive modern English mathematical paraphrase and translation, preserving all 387 classical Greek and Arabic proposition references.
* **Summary Track**: Executive overviews of major mathematical milestones, theorems, and structural developments across each book.
* **Notes Track**: Detailed mathematical, historical, and philological commentary examining Greek geometric algebra, Arabo-Latin transmissions, and projective connections.

2. Primary-Source Folio Milestones
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Marginal milestones (e.g., ``[p. 1]``, ``[PDF 181]``) and header badges link propositions directly to high-resolution scans of the 1896 Cambridge University Press edition on Internet Archive, enabling instant cross-checking of proofs and diagrams.

3. Interactive Diagrams & Deductive Links
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
All twelve major conic figures are rendered as interactive vector graphics (``.euclid-graphic`` SVGs):

* Hovering over geometric element references (e.g. :term:`latus rectum <orthia>`, :term:`diameter <diametros>`, :term:`asymptotes <asymptotoi>`) or assertions highlights the corresponding curves, tangents, asymptotes, and vertices in the SVG.
* Inline mathematical equations (``:eq:``) and justification references link directly to propositions and figures.

4. Full-Text Search with In-Page Highlighting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The full-text search engine scans the complete treatise text, commentary, glossary, and apparatus. Selecting search results navigates directly to matching sections with terms dynamically highlighted via ``?highlight=`` parameters.

5. Categories, Tags, Document Types & Collection Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **Taxonomy Facets**: Browse topics by conic type (*parabola*, *ellipse*, *hyperbola*), analytical concept (*conjugate diameters*, *harmonic poles and polars*, *normals and evolutes*), and historical reception (*Pappus*, *Descartes*, *Kepler*, *Halley*).
* **Collection View Toggles**: Switch between **Cards**, **Banners**, and **List** views on collection index pages.

6. People, Bibliography & Glossary Tooltips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* **People**: Historical figures like :person:`Apollonius <apollonius>`, :person:`Heath <heath>`, :person:`Eutocius <eutocius>`, or :person:`Halley <halley>` open rich biographical cards detailing their lives, roles, and loci.
* **Bibliography**: Bibliographic references (e.g. :cite:`heath:1896`) link to canonical entries with archival links.
* **Glossary**: Conic terms like :term:`parabole`, :term:`elleipsis`, and :term:`hyperbole` provide instant Greek, Latin, and English terminology definitions on hover.
* **Theme Switching**: Toggle between Light and Dark display modes in the top navigation bar with color-adapted figures and high-contrast typography.

Command-Line & Python Tools
---------------------------

``geometor.apollonius`` provides CLI commands and programmatic utilities for verifying concordance data and generating codex apparatus:

.. code-block:: bash

   # Display concordance summary table of classical and Heath propositions
   uv run --offline apollonius summary

   # Verify provenance manifest, SHA-256 hashes, and folio mappings
   uv run --offline apollonius verify

   # Compile the scholarly apparatus RST pages
   uv run --offline apollonius compile-apparatus

   # Build HTML documentation site
   publish build
