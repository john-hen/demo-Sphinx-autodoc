"""Logs the output of the Autodoc extension to a file."""

import logging


def setup(app):
    """Sets up the extension."""
    logger    = logging.getLogger('sphinx.sphinx.ext.autodoc')
    handler   = logging.FileHandler('autodoc.txt', mode='w', encoding='UTF-8')
    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
