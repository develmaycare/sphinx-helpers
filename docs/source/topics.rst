.. _topics:

******
Topics
******

The topics below are *not* specific to Sphinx Helpers, but you may find them useful when working with Sphinx documentation.

Working with Django
===================

To work with Django projects, you need some extra settings in the ``conf.py`` file:

.. code-block:: python

    # Be sure to import django.
    import django

    # Assuming docs/source/conf.py is the location and that docs is in project root (same level as source/).
    sys.path.insert(0, os.path.abspath("../../source"))

    # Load the environment and call Django setup. The project name is "main".
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
    django.setup()

If you are working with a Django app or library, and use have a project that you use for testing, the configuration might look like this:

.. code-block:: python

    # Be sure to import django.
    import django

    # Add the path to your source code.
    sys.path.append(os.path.abspath(os.path.join("../", "../")))

    # Add the example project path.
    sys.path.insert(0, os.path.abspath(os.path.join("../", "../", "tests", "example_project", "source")))

    # Load the environment and call Django setup. The project name is "main".
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
    django.setup()

RST Prolog
==========

The ``rst_prolog`` setting may be used to add role and replace definitions that may be used across all of your RST files. See:

- `Roles`_
- `Substitutions`_

.. _Roles: http://docutils.sourceforge.net/docs/ref/rst/directives.html#custom-interpreted-text-roles
.. _Substitutions: http://docutils.sourceforge.net/docs/ref/rst/directives.html#directives-for-substitution-definitions

Here is an example using roles and substitutions together:

.. code-block:: python

    # conf.py
    # The ``rst_prolog`` is added to the beginning of the output, allowing you to
    # create custom roles, text replacement, and so on.

    html_style = "custom.css"

    rst_prolog = """
    .. role:: hp
        :class: badge high-priority

    .. role:: np
        :class: badge normal-priority

    .. role:: lp
        :class: badge low-priority

    .. |MUSTHAVE| replace:: :hp:`Priority: Must Have`
    .. |NICETOHAVE| replace:: :np:`Priority: Nice to Have`
    .. |OPTIONAL| replace:: :lp:`Priority: Optional`

    .. |FSD| replace:: Shawn Davis
    .. |ACME| replace:: Acme, Inc.

    .. stage images

    .. |planning| image:: https://img.shields.io/badge/stage-planning-lightgray.svg

    .. |experimental| image:: https://img.shields.io/badge/stage-experimental-red.svg

    .. |development| image:: https://img.shields.io/badge/stage-development-blue.svg

    .. |alpha| image:: https://img.shields.io/badge/stage-alpha-orange.svg

    .. |beta| image:: https://img.shields.io/badge/stage-beta-yellow.svg

    .. |release| image:: https://img.shields.io/badge/stage-release-yellowgreen.svg

    .. |live| image:: https://img.shields.io/badge/stage-live-green.svg

    .. |obsolete| image:: https://img.shields.io/badge/stage-obsolete-000000.svg

    """

And the supporting CSS ...

.. code-block:: css

    /* _static/custom.css */

    .badge {
        padding: 5px;
        -webkit-border-radius: 10px 10px 10px 10px;
        -moz-border-radius: 10px 10px 10px 10px;
        border-radius: 10px 10px 10px 10px;
    }

    .high-priority {
        color: #ffffff;
        background: #cc0000;
    }

    .normal-priority {
        color: #ffffff;
        background: #006600;
    }

    .low-priority {
        color: #111111;
        background: #cccccc;
    }

Sync Documentation to Remove Server
===================================

If you keep your documentation on a separate site, this is a way to sync to the remote from the ``Makefile``:

.. code-block:: bash

    SSH_HOST := example.com
    SSH_KEY_FILE := /path/to/ssh/key_file
    SSH_USER := docs
    SSH_PATH := example_docs/www
    SSH_PORT := 22

    #> drysync - Preview syncing documentation to remote Web server.
    drysync:
        @make rsync DRY="--dry-run";

    #> rsync - Sync documentation to remote Web server.
    rsync:
        rsync -av --delete --progress --human-readable $(DRY) -e "ssh -i $(SSH_KEY_FILE) -p $(SSH_PORT)" $(BUILDDIR)/html/ $(SSH_USER)@$(SSH_HOST):$(SSH_PATH);

Graph Django Models
===================

`Django Extensions`_ comes with a handy management command or graphing models.

.. _Django Extensions: http://django-extensions.readthedocs.io/en/latest/index.html

.. note::
    You'll need GraphViz to make this work. On a Mac, you can install this with Homebrew: ``brew install graphviz``. On Ubuntu you can use ``apt-get install graphviz``.

Install Django Extensions and PyGraphViz:

.. code-block:: bash

    pip install django-extensions;
    pip install pygraphviz;

Add ``'django_extensions',`` to ``INSTALLED_APPS``.

Now you can add something like this to the ``Makefile``:

.. code-block:: bash

    #> graphmodels: Generate graphs of Django models.
    graphmodels:
        (cd .. && source $(PYTHON_ACTIVATE) && ./manage.py graph_models --output=docs/source/_static/example_app.jpg example_app);

If the diagram is too big, you can choose which models to show:

.. code-block:: bash

    graphmodels:
        (cd .. && source $(PYTHON_ACTIVATE) && ./manage.py graph_models --output=docs/source/_static/example_app.jpg --include-models=ModelA,ModelB,ModelC example_app);

