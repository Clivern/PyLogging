"""
Python Logging Library

@author: Clivern U{support@clivern.com}
"""

from setuptools import setup
from pylogging import __VERSION__
import os

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pylogging",
    version = __VERSION__,
    author = "Clivern",
    author_email = "support@clivern.com",
    description="Python Logging Library",
    license = "MIT",
    keywords = "logging,pylogger",
    url = "http://clivern.com/portfolio/pylogging",
    packages = ['pylogging'],
    long_description = read('README.md'),
    classifiers = [
        # Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Package is intended for
        "Topic :: Utilities",

        'License :: OSI Approved :: MIT License',

        # Support Python-2.x and Python-3.x
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)