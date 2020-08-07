#! /usr/bin/env python

# Imports

import argparse
from json import loads as json_loads
from markdown import markdown
import os
import sys
from urllib import request

# Administrivia

__author__ = "Shawn Davis <shawn@ptltd.co>"
__command__ = os.path.basename(sys.argv[0])
__date__ = "2019-10-29"
__version__ = "0.3.2-d"

# Constants

EXIT_OK = 0
EXIT_USAGE = 1
EXIT_INPUT = 2
EXIT_ENV = 3
EXIT_OTHER = 4

# Functions


def get_issues(user, repo, milestone=None):
    url = "https://api.github.com/repos/%s/%s/issues" % (user, repo)
    if milestone is not None:
        url += "?milestone=%s" % milestone.number

    output = request.urlopen(url).read()
    response = json_loads(output)

    issues = list()
    for i in response:
        issues.append(Issue(**i))

    return issues


def get_milestones(user, repo, include_issues=False):
    # headers = {
    #     'Accept': "application/vnd.github.v3+json",
    # }
    url = "https://api.github.com/repos/%s/%s/milestones" % (user, repo)
    output = request.urlopen(url).read()
    response = json_loads(output)

    milestones = list()
    for m in response:
        milestones.append(Milestone(**m))

    if include_issues:
        for milestone in milestones:
            milestone.issues = get_issues(user, repo, milestone=milestone)

    return milestones


def main():
    """Get and output GitHub milestones."""

    # Define options and arguments.
    parser = argparse.ArgumentParser(description=__doc__)

    parser.add_argument(
        "user",
        help="Your GitHub user name."
    )

    parser.add_argument(
        "repo",
        help="The GitHub repo."
    )

    parser.add_argument(
        "-i",
        "--include-issues",
        action="store_true",
        dest="include_issues",
        help="Also load issues for each milestone."
    )

    parser.add_argument(
        "-O=",
        "--output-format=",
        choices=["html", "md", "rst"],
        default="rst",
        dest="output_format",
        help="The output format."
    )

    # Access to the version number requires special consideration, especially
    # when using sub parsers. The Python 3.3 behavior is different. See this
    # answer: http://stackoverflow.com/questions/8521612/argparse-optional-subparser-for-version
    # parser.add_argument('--version', action='version', version='%(prog)s 2.0')
    parser.add_argument(
        "-v",
        action="version",
        help="Show version number and exit.",
        version=__version__
    )
    parser.add_argument(
        "--version",
        action="version",
        help="Show verbose version information and exit.",
        version="%(prog)s" + " %s %s" % (__version__, __date__)
    )
    # parser.add_argument("argument_name", help="argument_help.")
    # parser.add_argument("argument_name", default="default", nargs="?", help="argument_help")
    # parser.add_argument("-switch", dest="switch_name", help="switch_help")
    # parser.add_argument("--long-switch=", dest="switch_name", help="switch_help")

    # This will display help or input errors as needed.
    args = parser.parse_args()
    # print args

    # headers = {
    # 	'Accept': "application/vnd.github.v3+json",
    # }
    # url = "https://api.github.com/repos/develmaycare/superpython/milestones"
    #
    # output = request.urlopen(url).read()
    # response = json_loads(output)
    _milestones = get_milestones(args.user, args.repo, include_issues=args.include_issues)
    for _milestone in _milestones:
        if args.output_format == "html":
            print(_milestone.to_html())
        elif args.output_format == "md":
            print(_milestone.to_markdown())
        else:
            print(_milestone.to_rst())

    # Quit.
    exit(EXIT_OK)

# Classes


class Issue(object):

    def __init__(self, **kwargs):
        self.attributes = kwargs

    def __getattr__(self, item):
        return self.attributes.get(item)

    def to_html(self):
        return markdown(self.to_markdown())

    def to_markdown(self):
        return "- [%s](%s) (%s) %s" % (self.title, self.url, self.state, self.body)

    def to_rst(self):
        return "- `%s <%s>`_ (%s) %s" % (self.title, self.url, self.state, self.body)


class Milestone(object):

    def __init__(self, **kwargs):
        self.issues = list()
        self.attributes = kwargs

    def __getattr__(self, item):
        return self.attributes.get(item)

    def to_html(self):
        return markdown(self.to_markdown())

    def to_markdown(self):
        a = list()
        a.append("### %s" % self.title)
        a.append("")

        a.append("- **Status:** %s" % self.state)
        a.append("- **Due:** %s" % self.due_one)
        a.append("- **Close/Open Issues:** %s/%s" % (self.closed_issues, self.open_issues))
        a.append("")

        a.append(self.description)
        a.append("")

        if self.issues:
            for i in self.issues:
                a.append(i.to_markdown())

            a.append("")

        return "\n".join(a)

    def to_rst(self):
        a = list()
        a.append(self.title)
        a.append("-" * len(self.title))

        a.append("- **Status:** %s" % self.state)
        a.append("- **Due:** %s" % self.due_one)
        a.append("- **Close/Open Issues:** %s/%s" % (self.closed_issues, self.open_issues))
        a.append("")

        a.append(self.description)
        a.append("")

        if self.issues:
            for i in self.issues:
                a.append(i.to_rst())

            a.append("")

        return "\n".join(a)


# Kickoff
if __name__ == "__main__":
    main()
