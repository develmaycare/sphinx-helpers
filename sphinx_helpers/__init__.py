"""
These helpers provide Python-based support for various actions.

1. Copy this directory to documentation root (above ``source/``).
2. Customize as needed.
3. Include them in your ``conf.py`` file like so:

.. code-block:: python

    sys.path.insert(0, os.path.abspath('../'))

    from helpers import get_release, get_version, lucidchart, wistia

"""

from embed import lucidchart, youtube, wistia

__all__ = [
    "get_release",
    "get_version",
    "lucidchart",
    "youtube",
    "wistia",
]

try:
    # noinspection PyPackageRequirements
    from .django import process_help_text
    __all__.append("process_help_text")
except ImportError:
    process_help_text = None


# Functions


def get_version(path):
    """Read the version from the VERSION.txt file. Returns the major version if
    it's greater than or equal to 1, or the whole release number if it's 0.

    :param path: The path to the VERSION.txt file.
    :type path: str

    :rtype: str

    """
    with open(path, "rb") as f:
        # noinspection PyShadowingNames
        release = f.read()
        f.close()

    # Use strip() or it will break the search.
    if release[0] == "0":
        return u"%s" % release.strip()
    else:
        return u"%s" % release[0].strip()


def get_release(path):
    """Read the version from VERSION.txt file and return the whole release
    number.

    :param path: The path to the VERSION.txt file.
    :type path: str

    :rtype: str

    """
    with open(path, "rb") as f:
        # noinspection PyShadowingNames
        release = f.read()
        f.close()

    # Use strip() or it will break the search.
    return u"%s" % release.strip()
