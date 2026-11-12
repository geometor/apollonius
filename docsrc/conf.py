"""Sphinx configuration for GEOMETOR • apollonius."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.apollonius as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "apollonius"
repo_name = "apollonius"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • apollonius"
author = "Apollonius of Perga (ed. T. L. Heath)"
copyright = "c. 200 BCE · 1896 Cambridge University Press · Digital Codex GEOMETOR"

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/apollonius/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/apollonius/index.rst")  # noqa: F405

# Register offline-first local intersphinx inventories across the GEOMETOR canon
for _sister_repo in (
    "euclid",
    "archimedes",
    "elements",
    "pappus",
    "etc",
    "wildberger",
    "proclus",
    "hilbert",
    "hoenen",
):
    _local_inv = (_WORKSPACE_ROOT / _sister_repo / "docs" / "objects.inv").resolve()
    if _local_inv.is_file():
        intersphinx_mapping[_sister_repo] = (  # noqa: F405
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )

# Drop remote-only inventories lacking local files so offline sandbox builds emit zero warnings
for _inv_key in list(intersphinx_mapping.keys()):  # noqa: F405
    _uri, _inv_target = intersphinx_mapping[_inv_key]  # noqa: F405
    if _inv_target is None:
        intersphinx_mapping.pop(_inv_key, None)  # noqa: F405
