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
    keywords = "logging,debugging",
    url="http://clivern.com/portfolio/pylogging",
    packages=['pylogging'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)