.. _how-to:

******
How To
******

Dynamically Acquire Version and Release
=======================================

There are a couple of utilities you may use in your ``conf.py`` file to get the
version and release numbers of your project:

.. code-block:: python

    # conf.py
    from sphinx_helpers import get_release, get_version

    # Assuming docs/source/conf.py is relative to your project root.
    release = get_release("../../VERSION.txt")
    version = get_version("../../VERSION.txt")

Embed Remote Content
====================

You may use special directives to embed content from external services.

First, import an embed resource in your ``conf.py`` file.

.. code-block:: python

    # conf.py
    from sphinx_helpers import lucidchart, wistia

Then use the appropriate directive to embed the video.

.. code-block:: text

    # example.rst

    The diagram below shows something important:

    .. lucidchart:: asdf1234
        :width: 700px
        :height: 700px

    Watch this video ... it's awesome:

    .. wistia:: asdf1234
        :width: 50%
        :height: 50%

Other choices are vimeo and youtube.

.. note::
    Intelligent defaults are used if width and height are not supplied.

Add Help Text From Django Model Fields
======================================

You can alter the docstring process to add the ``help_text`` from Django model fields:

.. code-block:: python

    # conf.py

    # Register the docstring processor with sphinx
    from sphinx_helpers import process_help_text

    def setup(app):
        app.connect("autodoc-process-docstring", process_help_text)

Extract Comments from Templates
===============================

Create a script in the same directory as the docs Makefile:

.. code-block:: python

    # extract_template_comments.py

    # Import the helper.
    from sphinx_helpers.utils import extract_template_comments

    # Get the template comments.
    output = extract_template_comments("../app_name/templates/app_name")

    # Write the templates documentation. Make sure it's added to your docs in a table of contents.
    path = "source/templates.rst"
    with open(path, "wb") as f:
        f.write(output)
        f.close()

You can also manually include template output:

.. code-block:: python

    # extract_template_comments.py

    # Import the helper.
    from sphinx_helpers.utils import extract_template_comments

    # Get the template comments. Suppress the heading and set the rst level to 3 for templates.
    output = extract_template_comments("../app_name/templates/app_name", heading=None, level="-")

    # Write the templates documentation.
    path = "source/_includes/templates.rst"
    with open(path, "wb") as f:
        f.write(output)
        f.close()

Then in an rst file:

.. code-block:: text

    .. include:: _includes/templates.rst

Template documentation is expected to take the following form:

.. code-block:: text

    {% comment %}
    Display an alert.

    **enable_close** (bool) Make it possible to close the alert.

    **label** (str) Optional. Introduces the message.

    **message** (str) The message to be displayed.

    **status** (str) The nature of the alert: ``info``, ``success``, ``warning``, or ``error``. Defaults to ``error``.
    {% endcomment %}

    <!-- template code goes here -->

The comment tag *must* appear at the top of the file.

You may also use param/type for documenting a template.

.. code-block:: text

    {% comment %}
    Display an alert.

    :param enable_close: Make it possible to close the alert.
    :type enable_close: bool

    :param label: Optional. Introduces the message.
    :type label: str

    :param mesage: Required. The message to be displayed.
    :type message: str

    :param status: The nature of the alert: ``info``, ``success``, ``warning``, or ``error``. Defaults to ``error``.
    :type status: str

    {% endcomment %}

    <!-- template code goes here -->