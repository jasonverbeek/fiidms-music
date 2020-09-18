#!/usr/bin/env python

import os

from setuptools import find_packages, setup

NAME = "package"
DESCRIPTION = ""
LONG_DESCRIPTION = ""
URL = ""
EMAIL = ""
AUTHOR = ""
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "0.0.1"

# packages
REQUIRED = []
EXTRAS = {
    # 'feature': ['packageA', 'packageB'],
}


here = os.path.abspath(os.path.dirname(__file__))


setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
    ],
)
