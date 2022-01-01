Introduction
============

This is a demo show-casing how to document a Python library with Sphinx_,
including the library's public API via the Autodoc_ and Autosummary_
extensions. It uses reStructuredText_ (reST) in its hand-written documents
as well as in the doc-strings embedded with the library code.

The demo here is the yard stick to compare a Markdown-based workflow
against:

* demo-MyST-docstring_:
  Also uses the Sphinx documentation system, but has MyST_ parse the
  source files and doc-strings as Markdown instead of reST.
* demo-MkDocstrings_:
  Uses MkDocs_ with the MkDocstrings_ plug-in. This is an entirely
  different documentation build system that uses Markdown throughout.

As for this demo, you can click on "Show Source" at the bottom of every
page to see the reStructuredText from which it was rendered.

.. _Sphinx:              https://www.sphinx-doc.org
.. _Autodoc:             https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _Autosummary:         https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
.. _reStructuredText:    https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _demo-MyST-docstring: https://demo-MyST-docstring.readthedocs.io
.. _MyST:                https://myst-parser.readthedocs.io
.. _demo-MkDocstrings:   https://demo-MkDocstrings.readthedocs.io
.. _MkDocs:              https://www.mkdocs.org
.. _MkDocstrings:        https://mkdocstrings.github.io

.. toctree::
   :hidden:

   overview
   api
