# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
from setuptools import setup, find_packages


# Helpers
def read(*paths):
    """Read a text file."""
    basedir = os.path.dirname(__file__)
    fullpath = os.path.join(basedir, *paths)
    contents = io.open(fullpath, encoding='utf-8').read().strip()
    return contents


# Prepare
PACKAGE = 'hatool_compiler'
NAME = PACKAGE.replace('_', '-')
INSTALL_REQUIRES = [
    'awesome-slugify',
    'requests',
    'PyYAML',
]
LINT_REQUIRES = [
    'pylama',
]
TESTS_REQUIRE = [
    'tox',
]
README = read('README.md')
VERSION = read(PACKAGE, 'VERSION')
PACKAGES = find_packages(exclude=['examples', 'tests', '.tox'])

# Run
setup(
    name=NAME,
    version=VERSION,
    packages=PACKAGES,
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRE,
    extras_require={
        'develop': LINT_REQUIRES + TESTS_REQUIRE,
    },
    zip_safe=False,
    long_description=README,
    long_description_content_type='text/markdown',
    description='Compiler for hatool, a versatile scriptable chatbot-like interface for Angular',
    author='Adam Kariv',
    author_email='adam.kariv@gmail.com',
    url='https://github.com/akariv/hatool-compiler',
    license='MIT',
    keywords=[
        'data', 'ui', 'chatbot'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
      'console_scripts': [
        'hatool = hatool_compiler.compiler:main',
      ]
    }
)
