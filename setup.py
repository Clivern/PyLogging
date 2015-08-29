"""
Python Logging Library

@author: Clivern U{support@clivern.com}
"""

from setuptools import setup
from pylogging import __VERSION__
import os

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
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
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        "Topic :: Utilities",

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)