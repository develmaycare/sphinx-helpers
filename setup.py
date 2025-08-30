# See https://packaging.python.org/en/latest/distributing.html
# and https://docs.python.org/2/distutils/setupscript.html
# and https://pypi.python.org/pypi?%3Aaction=list_classifiers

import os
from setuptools import setup, find_packages


def read_file(path):
    with open(path, "r") as f:
        contents = f.read()
        f.close()
    return contents.strip()


def get_description():
    files = ("README", "COPYING", "CHANGES", "TODO")
    extensions = ("markdown", "md", "rst", "txt")

    description = ""
    for file_name in files:
        for ext in extensions:
            path = "%s.%s" % (file_name, ext)
            if os.path.exists(path):
                description += read_file(path)

    return description


setup(
    name='sphinx_helpers',
    version=read_file("VERSION.txt"),
    description='Common helpers for creating documentation with Sphinx.',
    long_description=get_description(),
    author='Shawn Davis',
    author_email='shawn@develmaycare.com',
    url='https://github.com/develmaycare/sphinx-helpers',
    packages=find_packages(exclude=["examples", "examples.*"]),
    install_requires=[
        "docutils",
    ],
    classifiers=[
        'Development Status :: 2 - Pre Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    zip_safe=False,
    #tests_require=[
    #    "django",
    #    "docutils",
    #],
    #test_suite='runtests.runtests'
)
