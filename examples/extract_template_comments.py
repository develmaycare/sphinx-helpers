#! /usr/bin/env python

# Import the helper.
from sphinx_helpers.utils import extract_template_comments

# Get the template comments.
output = extract_template_comments("../app_name/templates/app_name")

# Write the templates documentation.
path = "source/templates.rst"
with open(path, "wb") as f:
    f.write("\n".join(output))
    f.close()

# Add this to the html target in the Makefile:
# ./extract_template_comments.py
