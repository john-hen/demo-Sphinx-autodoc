"""
This is the first line in the doc-string of module ``actions``.

We can reference other objects, such as `Class1` and `Class2`.
We can link back to one of the main documents as a whole, for example
:doc:`/overview`, or :ref:`a specific section <first-steps>`. We can
create external cross-references like to `Path <python:pathlib.Path>`
thanks to the Intersphinx_ extension.

And we can have highlighted code examples:

.. code-block::

    from package import action
    from package import Class1

    action(do='whatever')
    class1 = Class1()
    class1.action()

Sphinx created this page from a "stub" file named ``package.actions.rst``
in the ``api`` folder underneath ``docs``. As you can tell from clicking
"Show Source" at the bottom of this very page, it contains very little:

.. code-block:: rest

    actions
    -------

    .. automodule:: package.actions

Autodoc_ takes care of the rest and fills in the blanks, pulling in
signatures and doc-strings from the package's source code. Autosummary_
would even create these stubs automatically, unless we tell it not to.
We can also look at the source code of the ``action`` function, of this
whole module in fact, if we click on the ``[source]`` link on the right,
which is there courtesy of the Viewcode_ extension.

.. _Intersphinx: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
.. _Autodoc:     https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
.. _Autosummary: https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html
.. _Viewcode:    https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
"""


def action(do='something'):
    """
    This is the first line in the doc-string of function ``action``.

    It is defined in module `actions`.
    """
    pass
