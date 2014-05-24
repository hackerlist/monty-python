monty-python
============

Python API Bindings for the Monty server monitoring Go library

## Installation

For instructions on installing Monty, please refer to the Monty setup
guide at https://github.com/hackerlist/monty. To install the Python
API bindings via pypi run the command:

    sudo pip install monty-python

## Usage

    >>> from montypy import Monty
    >>> m = Monty('http://monty.criticalpha.se', token='XXX')
    >>> print m.nodes()