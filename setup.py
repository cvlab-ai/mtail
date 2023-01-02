#!/usr/bin/env python3

import os
import sys
from distutils.core import setup

from setuptools import find_packages

if sys.version_info.major <= 2:
    raise Exception("Only python 3+ is supported!")

__version__ = "0.9"
package_name = "mtail"

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

description = long_description.splitlines()[0].strip()

setup(
    name=package_name,
    version=__version__,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jan Cychnerski',
    url='https://github.com/cvlab-ai/mtail',
    packages=find_packages("."),
    entry_points={'console_scripts': ['mtail=mtail.mtail:main']},
    license="GPL-3.0+",
    python_requires='>=3.6',
)
