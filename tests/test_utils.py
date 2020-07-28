from sphinx_helpers.utils import *

# Tests


def test_extract_template_comments():
    output = extract_template_comments("tests/example_project/templates")
    # print(output)
    assert "Display an alert." in output
    assert "Generate breadcrumbs." in output
    assert "Display a standard page header." in output


def test_get_release():
    v = get_release("tests/example_project/VERSION-1.txt")
    assert v == "1.1.2-d"

    v = get_release("tests/example_project/VERSION-2.txt")
    assert v == "2"


def test_get_version():
    v = get_version("tests/example_project/VERSION-1.txt")
    assert v == "1.1"

    v = get_version("tests/example_project/VERSION-2.txt")
    assert v == "2.0"
