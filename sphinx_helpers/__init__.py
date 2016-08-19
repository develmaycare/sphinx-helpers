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

__all__ = [
    "get_release",
    "get_version",
    "lucidchart",
    "vimeo",
    "wistia",
    "youtube",
]

try:
    # noinspection PyPackageRequirements
    from .django import process_help_text
    __all__.append("process_help_text")
except ImportError:
    process_help_text = None


# Functions


def get_version(path, full=False):
    """Read the version from the VERSION.txt file. Returns the major version if
    it's greater than or equal to 1, or the whole release number if it's 0.

    :param path: The path to the VERSION.txt file.
    :type path: str

	:param full: Return the full version (release) string. See 
	             ``get_release()``.
	:type full: bool

    :rtype: str

    """
    
    # Load the content of the file.
    with open(path, "rb") as f:
        content = f.read()
        f.close()

	# Use strip() or it will break the search.
	content = content.strip()

	# Send back the string if a full release is requested.
	if full:
		return content

	# Parse the content for version tokens.
	# major . minor . patch - status
	try:
		version, status = content.strip().split("-")		
	except ValueError:
		version = content.strip()
		status = None
	
	tokens = version.split(".")
	
	if len(tokens) == 3:
		patch = tokens[2]

	if len(tokens) >= 2:
		minor = tokens[1]
	else:
		minor = "0"
		
	major = tokens[0]

	# Return the version.
	return u"%s.%s" % (major, minor)


def get_release(path):
    """Read the version from VERSION.txt file and return the whole release
    number.

    :param path: The path to the VERSION.txt file.
    :type path: str

    :rtype: str

    """
    return get_version(path, full=True)
