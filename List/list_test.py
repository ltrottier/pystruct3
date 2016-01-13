#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Ludovic Trottier
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import unittest
import random

class TestListMethods(unittest.TestCase):

    def setUp(self):
        self.empty_list = List()

        self.unit_list = List()
        self.unit_list.append(4)

        # [3, 1, 2]
        self.some_list = List()
        self.some_list.insert(1, 0)
        self.some_list.insert(2, 1)
        self.some_list.insert(3, 0)

    def test_read_ok(self):
        self.assertEqual(self.some_list.read(0), 3)
        self.assertEqual(self.some_list[0], 3)
        self.assertEqual(self.some_list.read(1), 1)
        self.assertEqual(self.some_list[1], 1)
        self.assertEqual(self.some_list.read(2), 2)
        self.assertEqual(self.some_list[2], 2)

    def test_read_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.read(-1)
        with self.assertRaises(ValueError):
            self.empty_list.read(0)
        with self.assertRaises(ValueError):
            self.some_list.read(4)
        with self.assertRaises(ValueError):
            self.some_list.read(-1)

    def test_contains_ok(self):
        self.assertTrue(1 in self.some_list)
        self.assertTrue(self.some_list.contains(1))
        self.assertTrue(2 in self.some_list)
        self.assertTrue(self.some_list.contains(2))
        self.assertTrue(3 in self.some_list)
        self.assertTrue(self.some_list.contains(3))

        self.assertFalse(1 in self.empty_list)
        self.assertFalse(self.empty_list.contains(1))
        self.assertFalse(0 in self.some_list)
        self.assertFalse(self.some_list.contains(0))
        self.assertFalse(4 in self.some_list)
        self.assertFalse(self.some_list.contains(4))

    def test_insert_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.insert(1, -1)
        with self.assertRaises(ValueError):
            self.empty_list.insert(1, 1)
        with self.assertRaises(ValueError):
            self.some_list.insert(-1, 4)

    def test_insert_ok(self):
        a_list = List()
        a_list.append(1)
        a_list.append(1)
        a_list.append(1)
        self.assertEqual(1, a_list[0])
        self.assertEqual(1, a_list[1])
        self.assertEqual(1, a_list[2])

    def test_pop_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.pop(0)
        with self.assertRaises(ValueError):
            self.some_list.pop(-1)
        with self.assertRaises(ValueError):
            self.some_list.pop(3)

    def test_pop_ok(self):
        self.some_list.pop(0)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(2, self.some_list[1])
        self.assertEqual(2, self.some_list.size())
        self.some_list.pop(1)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(1, self.some_list.size())
        self.some_list.pop(0)
        self.assertEqual(0, self.some_list.size())

    def test_random_insert_remove(self):
        a_list = List()
        for i in range(10000):
             item = random.randint(-100,100)
             pos = random.randint(0, len(a_list))
             if item not in a_list:
                 a_list.insert(item,pos)
             else:
                 a_list.remove(item)

    def test_is_empty_ok(self):
        self.assertEqual(self.empty_list.size(), 0)
        self.assertTrue(self.empty_list.is_empty())
        self.assertFalse(self.some_list.is_empty())

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
    from list import SingleLinkedList as List
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestListMethods))

    #from List import DoubleLinkedList as List
    #unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestListMethods))