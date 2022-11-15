# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import mastermind

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mastermind'
copyright = '2022, Constance GANOT & Olivia VIDAL VELAZQUEZ'
author = 'Constance GANOT & Olivia VIDAL VELAZQUEZ'
release = '2022'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [# Standard extensions
    'sphinx.ext.autodoc',       # automatic documentation
    'sphinx.ext.autosummary',   # automatic summary
    #'sphinx.ext.mathjax',       # (or pngmath) support for equations
    #'sphinx.ext.viewcode',      # link to code source
    #'sphinx.ext.extlinks',      # support for external links
    #'sphinx.ext.autosectionlabel',  # automatic section label
    #'sphinx.ext.coverage',      # documentation coverage
    # 'matplotlib.sphinxext.plot_directive',  # support for embedded plots
    # 'sphinx-git',  # create a changelog from git history
]

# Autodoc configuration
autodoc_default_options = {
    'members': True,            # Document all members
    #'undoc-members': True,      # ... including undocumented ones
    #'ignore-module-all': True,  # do not stick to __all__
}

autoclass_content = "both"              # Insert class and __init__ docstrings
autodoc_member_order = "bysource"       # Keep source order

templates_path = ['_templates']
#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

#language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']
master_doc = 'index'
langage = 'en'


# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

