#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re
import sys

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


package = 'tapioca_amarilis'
requirements = [
    'tapioca-wrapper<2',
]
test_requirements = [
    'ipdb'
]


setup(
    name='tapioca-amarilis',
    version='0.1.0',
    description='Amarilis API wrapper using tapioca',
    long_description=readme,
    author='Daniel Bastos',
    author_email='danielfloresbastos@gmail.com',
    url='https://github.com/daniellbastos/tapioca-amarilis',
    packages=[
     'tapioca_amarilis',
    ],
    package_dir={'tapioca_amarilis': 'tapioca_amarilis'},
    include_package_data=True,
    install_requires=requirements,
    keywords='amarilis',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
