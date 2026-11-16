"""Sphinx configuration for GEOMETOR • apollonius."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
if str(_REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT / "src"))

from photon_platform.publish.global_conf import *

import geometor.apollonius as module

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "apollonius"
repo_name = "apollonius"

setup_globals(org, org_name, repo, repo_name)

site_title = "Apollonius of Perga"
project = site_title
html_title = f"{site_title} • {org_name}"
author = "Apollonius of Perga (ed. T. L. Heath)"
copyright = "c. 200 BCE · 1896 Cambridge University Press · Digital Codex GEOMETOR"

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/apollonius/index.rst" not in exclude_patterns:
    exclude_patterns.append("modules/api/geometor/apollonius/index.rst")

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
        intersphinx_mapping[_sister_repo] = (
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )

# Drop remote-only inventories lacking local files so offline sandbox builds emit zero warnings
for _inv_key in list(intersphinx_mapping.keys()):
    _uri, _inv_target = intersphinx_mapping[_inv_key]
    if _inv_target is None:
        intersphinx_mapping.pop(_inv_key, None)
