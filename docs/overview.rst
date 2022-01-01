Overview
========

Pretend this is the tutorial that gives a general introduction to the
library, providing usage examples and all that.

This is a stand-alone document, in this case a file named ``overview.rst``
inside the project's ``docs`` folder. So it is separate from the actual
Python library in the, unimaginatively named, ``package`` folder. Both
folders are right underneath the project's root in the repo.

We have set up the `api` documentation as a different chapter. It is
also a stand-alone document, named ``api.rst``, and is linked in the
side bar on the left. Readers can go there to understand how the library
is to be used in application code. That is, it documents the *public*
API. Not every doc-string defined in ``package`` needs to show up there,
only the ones that are important. So we kick things off with a general
summary of the top-level objects, courtesy of Sphinx's Autosummary_
extension, which links to in-depth API documentation provided by the
Autodoc_ extension.

We can then link to objects from the API documentation, such as
`Class1` or `action <package.action>`. The syntax is just ```Class1```
and ```action <package.action>``` (as the latter reference happens to
be ambiguous). This works as long as we have set ``default_role = 'any'``
in Sphinx's configuration file ``conf.py``. We could also do that on a
per-document basis with ``.. default-role:: any``, but the ``any`` role
is so useful, it rarely makes sense to assign anything else as the
default.

Unless you want single back-ticks to denote ``literals``, as they do in
Markdown. Then you might configure ```default_role = 'literal'``, but
would have to write ``:any:`Class1``` to create a reference to the API
documentation of :any:`Class1`. So pick your poison.

Some people like to document the API within the hand-written general
documentation as they go along. So instead of just referring to `Class1`,
they pull in its doc-string somewhere in the text:

.. autoclass:: package.classes.Class1
    :noindex:

Many projects also like to have Intersphinx_ references, so that they
can easily link to, for example, Python's `pathlib <python:pathlib>`
module. This needs to be set up in ``conf.py``, but makes for shorter
link targets.

One noteworthy shortcoming of using reST as the markup language is that
we cannot have ``literals``, or even *emphasis*, inside link text.
That's because `reStructuredText does not support nested markup
<not_nested_>`_ of any kind. Note how `this <https://example.org>`_
works (which is ```this <https://example.org>`_`` in the source), but
```this`` <https://example.org>`_ is broken on this very page. Even
though it's the same syntax as before, only with back-ticks around
"this". (You'll have to click "Show Source" at the bottom of the page
to see the original markup, as it doesn't seem possible to actually
reproduce it on the rendered page, at least not inline.)


.. _first-steps:

First steps
-----------

This is a section inside the Overview chapter. We have marked it as
a possible link target by putting ``.. _first-steps:`` right above
the section header. Though we could also generate section labels
automatically, once and for all, if we used the Autosectionlabel_
extension.

Maybe it's time for a code example:

.. code-block:: python

    from package.classes import Class1

    class1 = Class1()
    class1.action()

This requires a ``.. code-block::`` directive, followed by a blank line,
followed by the actual code indented one level. It's automatically
highlighted in the colors defined by the theme, which in this case
is Furo_. Click the icon at the top right of the page to switch between
dark and light mode and notice how the syntax highlighting changes along
with it. We could easily replace Furo with any of a number of
`Sphinx themes <themes_>`_. As themes are completely independent of the
documentation semantics, all it takes is assigning another name to
``html_theme`` in ``conf.py`` (and ``pip install``-ing the corresponding
package).

.. _Autodoc:          https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _Autosummary:      https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
.. _Intersphinx:      https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
.. _not_nested:       https://docutils.sourceforge.io/FAQ.html#is-nested-inline-markup-possible
.. _Autosectionlabel: https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html
.. _Furo:             https://pradyunsg.me/furo
.. _themes:           https://sphinx-themes.org
