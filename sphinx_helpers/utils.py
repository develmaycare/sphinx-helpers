# Imports

import os

# Exports

__all__ = (
    "extract_template_comments",
    "get_release",
    "get_version",
)

# Functions


def extract_template_comments(path, heading="Templates", level="="):
    """Extract comments from the templates on a given path.

    :param path: The path to the templates. This path is *not* searched recursively.
    :type path: str

    :param heading: The heading to display at the top of the output. Use ``None`` to suppress heading output.
    :type heading: str | None

    :param level: The ReStructuredText character used to indicate the heading level of templates.
    :type level: str

    :return: Outputs the template comments in ReStructuredText format.
    :rtype: str

    Comments are extracted from a comment block.

    .. code-block:: text

        {% comment %}
        Create an alert.

        **enable_close** (bool) Make it possible to close the alert.

        **label** (str) Optional. Introduces the message.

        **message** (str) The message to be displayed.

        **status** (str) The nature of the alert: ``info``, ``success``, ``warning``, or ``error``.
        Defaults to ``error``.
        {% endcomment %}

        <!-- template code goes here -->
    """

    def get_comments(input_path):
        with open(input_path, "r") as f:
            content = f.read()
            f.close()

            inner = False
            lines = list()
            for line in content.split("\n"):
                if line == '{% comment %}':
                    inner = True
                    continue
                elif line == '{% endcomment %}':
                    break
                else:
                    pass

                if inner:
                    lines.append(str(line))

            return "\n".join(lines)

    # Get entries on the input path.
    entries = os.listdir(path)
    templates = list()
    for e in entries:
        _path = os.path.join(path, e)
        if os.path.isfile(_path):
            templates.append(_path)

    # Start output for the documentation file.
    output = list()
    output.append(".. Generated by sphinx-helpers")
    output.append("")

    if heading:
        output.append("*********")
        output.append("Templates")
        output.append("*********")
        output.append("")

    # Load each template and extract the comments.
    for t in templates:

        file_name = os.path.basename(t)
        output.append(file_name)
        output.append(level * len(file_name))
        output.append("")

        comment = get_comments(t)
        output.append(comment)
        output.append("")

    # Return the output.
    return "\n".join(output)


def get_release(path):
    """Read the version from VERSION.txt file and return the whole release
    number.

    :param path: The path to the VERSION.txt file.
    :type path: str

    :rtype: str

    """
    return get_version(path, full=True)


def get_version(path, full=False):
    """Read the version from the VERSION.txt file.

    :param path: The path to the VERSION.txt file.
    :type path: str

    :param full: Return the full version (release) string. See ``get_release()``.
    :type full: bool

    :rtype: str

    """

    # TODO: Update `get_version()` to use semver package? Requires a new dependency in setup, though.

    # Load the content of the file.
    with open(path, "r") as f:
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
            # status = None

        tokens = version.split(".")

        # if len(tokens) == 3:
        #     patch = tokens[2]

        if len(tokens) >= 2:
            minor = tokens[1]
        else:
            minor = "0"

        major = tokens[0]

        # Return the version.
        return "%s.%s" % (major, minor)
