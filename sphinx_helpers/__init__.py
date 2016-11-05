"""
These helpers provide Python-based support for various actions.

1. Copy this directory to documentation root (above ``source/``).
2. Customize as needed.
3. Include them in your ``conf.py`` file like so:

.. code-block:: python

    sys.path.insert(0, os.path.abspath('../'))

    from helpers import get_release, get_version, lucidchart, wistia

"""

from embed import lucidchart, vimeo, wistia, youtube
from utils import extract_template_comments, get_release, get_version

__all__ = [
    "extract_template_comments",
    "get_release",
    "get_version",
    "lucidchart",
    "vimeo",
    "wistia",
    "youtube",
]

# Make process_help_text available through the helpers.
try:
    # noinspection PyPackageRequirements
    from .django import process_help_text
    __all__.append("process_help_text")
except ImportError:
    process_help_text = None
