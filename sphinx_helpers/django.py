"""
Helpers specific to Django.

"""

import inspect
# noinspection PyUnresolvedReferences
from django.utils.html import strip_tags
# noinspection PyUnresolvedReferences
from django.utils.encoding import force_unicode

__all__ = (
    "process_help_text",
)

# Functions


# noinspection PyUnusedLocal
def process_help_text(app, what, name, obj, options, lines):
    """Automatically document the fields for Django models.

    Example:

    .. code-block:: py

        from sphinx_helpers import process_docstring

        def setup(app):
            app.connect("autodoc-process-docstring", process_docstring)

    """

    # This causes import errors if left outside the function.
    # noinspection PyUnresolvedReferences
    from django.db import models

    # Only look at objects that inherit from Django's base model class
    if inspect.isclass(obj) and issubclass(obj, models.Model):

        # Grab the field list from the meta class
        # noinspection PyProtectedMember
        fields = obj._meta._fields()

        for field in fields:
            # Decode and strip any html out of the field's help text
            help_text = strip_tags(force_unicode(field.help_text))

            # Decode and capitalize the verbose name, for use if there isn't
            # any help text
            verbose_name = force_unicode(field.verbose_name).capitalize()

            if help_text:
                # Add the model field to the end of the docstring as a param
                # using the help text as the description
                lines.append(u':param %s: %s' % (field.attname, help_text))
            else:
                # Add the model field to the end of the docstring as a param
                # using the verbose name as the description
                lines.append(u':param %s: %s' % (field.attname, verbose_name))

            # Add the field's type to the docstring
            lines.append(u':type %s: %s' % (
                field.attname,
                type(field).__name__)
            )

    # Return the extended docstring
    return lines
