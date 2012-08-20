#!/usr/bin/env python

import os
import sys

import bllbrd

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
    'bllbrd',
]

setup(
    name='bllbrd',
    version=bllbrd.__version__,
    description='Python client for bllbrd.io',
    long_description=open('README.md').read(),
    author='Philipp Bosch',
    author_email='hello@pb.io',
    url='http://bllbrd.io/',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'bllbrd': 'bllbrd'},
    include_package_data=True,
    install_requires=['requests'],
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
)