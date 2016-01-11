#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Ludovic Trottier"
__license__ = "GPL"
__date__ = "Sun Jan 10 12:55:14 2016"

import unittest

class TestStringMethods(unittest.TestCase):

    def test_isEmpty(self):
        l = List()
        self.assertEqual(l.size(), 0)
        self.assertTrue(l.isEmpty())

    def test_insertRaises(self):
        l = List()
        with self.assertRaises(ValueError):
            l.insert(1, -1)
        
        with self.assertRaises(ValueError):
            l.insert(1, 1)
            
    def test_insertOk(self):
        l = List()
        l.insert(1, 0)
        l.insert(2, 1)
        l.insert(3, 0)
        self.assertEqual(3, l[0])
        self.assertEqual(1, l[1])
        self.assertEqual(2, l[2])
    
    def test_removeRaises(self):
        l = List()
        with self.assertRaises(ValueError):
            l.remove(0)
        
        l.insert(1, 0)
        l.insert(2, 1)
        l.insert(3, 0)
        with self.assertRaises(ValueError):
            l.remove(-1)
        with self.assertRaises(ValueError):
            l.remove(3)
        
    def test_removeOk(self):
        l = List()
        l.insert(1, 0)
        l.insert(2, 1)
        l.insert(3, 0)
        l.remove(0)
        self.assertEqual(1, l[0])
        self.assertEqual(2, l[1])
        self.assertEqual(2, l.size())
        l.remove(1)        
        self.assertEqual(1, l[0])
        self.assertEqual(1, l.size())
        l.remove(0)
        self.assertEqual(0, l.size())
    
    def test_indexRaises(self):
        l = List()
        with self.assertRaises(ValueError):
            l.index(2)
        
        l.insert(1, 0)
        l.insert(2, 1)
        l.insert(3, 0)
        
        with self.assertRaises(ValueError):
            l.index(-3)
        
        
    def test_indexOk(self):
        l = List()
        l.insert(1, 0)
        l.insert(2, 1)
        l.insert(3, 0)
        self.assertEqual(l.index(3), 0)
        self.assertEqual(l.index(2), 2)
        self.assertEqual(l.index(1), 1)
      
if __name__ == '__main__':
    from List import SingleLinkedList as List
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))
    
    #from List import DoubleLinkedList as List
    #unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestStringMethods))