#!/usr/bin/env python
import setuptools
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import os
import re

with open("README.md", "r") as fh:
    readme = fh.read()

with open(os.path.join(os.path.dirname(__file__), 'outlier_detection', '__init__.py')) as f:
    version = re.search("__version__ = '([^']+)'", f.read()).group(1)

setup(
    name='outlier_detection',
    version=version,
    author="mvadu",
    author_email="mvadu@adystech.com",
    description="Outlier Detection in Time Series",
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/adystech/outlier-detection',
    license='MIT License',
    packages=find_packages(),
    # test_suite='tests',
    # tests_require=test_requires,
    install_requires=[
        'pandas'
    ],
    # extras_require={'test': test_requires},
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
