:navigation: header
:order: 40

.. _apollonius-modules:

Modules
=======

The ``geometor.apollonius`` Python package provides deterministic provenance and SHA-256 verification, cross-corpus proposition concordance queries, scholarly RST apparatus compilation, and CLI inspection tools for the *Conics* codex.

CLI Usage
---------

.. code-block:: bash

   geometor-apollonius summary
   geometor-apollonius compile-apparatus
   geometor-apollonius verify

Submodules
----------

.. toctree::
   :maxdepth: 2

   api/geometor/apollonius/concordance/index
   api/geometor/apollonius/compile_codex/index
   api/geometor/apollonius/cli/index
