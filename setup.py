#!/usr/bin/env python2

##
# PySub
# https://github.com/leosartaj/PySub.git
#
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PySub",
    version = "0.0.1",
    author = "Sartaj Singh",
    author_email = "singhsartaj94@gmail.com",
    description = ("Simple Tool to download Subtitles."),
    license = "MIT",
    keywords = "subtitles download movies tv shows",
    url = "http://github.com/leosartaj/PySub",
    packages = ['PySub'],
    scripts = ['bin/pysub'],
    requires = ['requests'],
    long_description = read('README.md'),
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
