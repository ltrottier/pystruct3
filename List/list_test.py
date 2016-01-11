#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2016 Ludovic Trottier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import unittest

class TestStringMethods(unittest.TestCase):

    def test_is_empty(self):
        l = List()
        self.assertEqual(l.size(), 0)
        self.assertTrue(l.is_empty())

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