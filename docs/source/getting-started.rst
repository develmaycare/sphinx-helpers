.. _getting-started:

***************
Getting Started
***************

System Requirements
===================

Python 2.7+ or 3.0+ is required.

Sphinx Helpers requires that Sphinx be installed, but it is *not* included in ``setup.py``.

Install
=======

To install:

.. code-block:: bash

    pip install sphinx
    pip install git+https://github.com/develmaycare/sphinx-helpers

Examples
========

See :ref:`how-to` and :ref:`topics`.

See also the example scripts in the ``examples/`` directory.

Next Steps
==========

Create your ``docs/`` directory, and run ``sphinx-quickstart`` from that directory. Edit the ``conf.py`` to import resources from Sphinx Helpers.

We also like to add a target to the package's top-level Makefile:

.. code-block:: bash

    .PHONY: docs

    # The path to source code to be counted with cloc.
    CLOC_PATH := package_name

    #> docs - Generate documentation.
    docs: lines
        cd docs && make html;
        cd docs && make coverage;
        open docs/build/coverage/python.txt;
        open docs/build/html/index.html;

    # lines - Generate lines of code report.
    lines:
        rm -f docs/source/_data/cloc.csv;
        echo "files,language,blank,comment,code" > docs/source/_data/cloc.csv;
        cloc $(CLOC_PATH) --csv --quiet --unix --report-file=tmp.csv
        tail -n +2 tmp.csv >> docs/source/_data/cloc.csv;
        rm tmp.csv;

This allows you to build docs from project root with: ``make docs``

Resources
=========

- `Sphinx Home Page`_
- `reStructuredText Home Page`_
- `reStructuredText Quick Reference`_

.. _reStructuredText Home Page: https://docutils.sourceforge.io/rst.html
.. _reStructuredText Quick Reference: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _Sphinx Home Page: https://www.sphinx-doc.org

FAQs
====

Have a question? `Just ask`_!

.. _Just ask: https://develmaycare.com/contact/?support=1&product=Sphinx%20Helpers
