#-*- coding: utf-8 -*-

"""
    montypy
    ~~~~~~~

    Setup
    `````
    $ sudo pip install monty-python
"""

from distutils.core import setup
import os

setup(
    name='monty-python',
    version='0.0.01',
    url='https://github.com/hackerlist/monty-python',
    author='hackerlist',
    author_email='m@hackerlist.net',
    packages=[
        'montypy',
        ],
    platforms='any',
    license='LICENSE',
    install_requires=[
        'requests >= 1.1.0',
        'simplejson >= 2.5.2'
    ],
    description="Python API Bindings for the Monty server monitoring Go library",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
