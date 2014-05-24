#-*- coding: utf-8 -*-

"""
    montypy.test
    ~~~~~~~~~~~~

    Test cases for monty-python
"""

import unittest
import os
from montypy import Monty

TEST_SRV = 'https://monty.criticalpha.se'

class TestMontyPy(unittest.TestCase):
    
    def test_instantiation(self):
        m = Monty(TEST_SRV)

    def test_nodes(self):
        m = Monty(TEST_SRV)
        nodes = m.nodes()
        
    def test_probes(self):
        m = Monty(TEST_SRV)
        probes = m.probes()
        
    def test_scripts(self):
        m = Monty(TEST_SRV)
        scripts = m.scripts()
        
    def test_results(self):
        m = Monty(TEST_SRV)
        results = m.results()
        
    def test_status(self):
        m = Monty(TEST_SRV)
        statuses = m.status()
