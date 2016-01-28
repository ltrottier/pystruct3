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

class TestGraphMethods(unittest.TestCase):

    def setUp(self):
        self.empty_graph = Graph()

        self.unit_graph = Graph()
        self.unit_graph.insert(2)

        self.some_graph = Graph()
        self.some_graph.insert(4)
        self.some_graph.insert(5)
        self.some_graph.insert(2)
        self.some_graph.connect(4,5)
        self.some_graph.connect(5,4)
        self.some_graph.connect(2,5)

    def test_adjacent_raises(self):
        with self.assertRaises(ValueError):
            self.empty_graph.adjacent(1,2)
        with self.assertRaises(ValueError):
            self.unit_graph.adjacent(1,2)
        with self.assertRaises(ValueError):
            self.some_graph.adjacent(2,6)
        with self.assertRaises(ValueError):
            self.some_graph.adjacent(1,2)

    def test_adjacent_ok(self):
        self.assertTrue(self.some_graph.adjacent(4,5))
        self.assertTrue(self.some_graph.adjacent(5,4))
        self.assertTrue(self.some_graph.adjacent(2,5))
        self.assertTrue(self.some_graph.adjacent(5,2))
        self.assertFalse(self.some_graph.adjacent(2,4))
        self.assertFalse(self.some_graph.adjacent(4,2))

    def test_neighbors_raises(self):
        with self.assertRaises(ValueError):
            self.empty_graph.neighbors(2)
        with self.assertRaises(ValueError):
            self.unit_graph.neighbors(5)
        with self.assertRaises(ValueError):
            self.some_graph.neighbors(1)

    def test_neighbors_ok(self):
        self.assertEqual([], self.unit_graph.neighbors(2))
        self.assertEqual([2,4], sorted(self.some_graph.neighbors(5)))
        self.assertEqual([5], sorted(self.some_graph.neighbors(4)))
        self.assertEqual([5], sorted(self.some_graph.neighbors(2)))

    def test_vertices_ok(self):
        self.assertEqual([], sorted(self.empty_graph.vertices()))
        self.assertEqual([2], sorted(self.unit_graph.vertices()))
        self.assertEqual([2,4,5], sorted(self.some_graph.vertices()))

    def test_insert_raises(self):
        with self.assertRaises(ValueError):
            self.unit_graph.insert(2)
        with self.assertRaises(ValueError):
            self.some_graph.insert(2)
        with self.assertRaises(ValueError):
            self.some_graph.insert(4)
        with self.assertRaises(ValueError):
            self.some_graph.insert(5)

    def test_insert_ok(self):
        pass


if __name__ == '__main__':
    from pystruct3.graph import AdjacencyListGraph as Graph
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestGraphMethods))
