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

    def test_adjacent_to_self(self):
        self.unit_graph.connect(2,2)
        self.assertTrue(self.unit_graph.adjacent(2,2))
        self.assertFalse(self.some_graph.adjacent(2,2))
        self.assertFalse(self.some_graph.adjacent(4,4))
        self.assertFalse(self.some_graph.adjacent(5,5))
        self.some_graph.connect(5,5)
        self.assertTrue(self.some_graph.adjacent(5,5))

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
        self.some_graph.connect(5,5)
        self.assertEqual([2,4,5], sorted(self.some_graph.neighbors(5)))

    def test_vertices_ok(self):
        self.assertEqual([], sorted(self.empty_graph.vertices()))
        self.assertEqual([2], sorted(self.unit_graph.vertices()))
        self.assertEqual([2,4,5], sorted(self.some_graph.vertices()))

    def test_contains_ok(self):
        self.assertFalse(3 in self.empty_graph)
        self.assertFalse(self.empty_graph.contains(3))
        self.assertTrue(2 in self.unit_graph)
        self.assertTrue(self.unit_graph.contains(2))
        self.assertFalse(4 in self.unit_graph)
        self.assertFalse(self.unit_graph.contains(4))
        self.assertTrue(2 in self.some_graph)
        self.assertTrue(self.some_graph.contains(2))
        self.assertTrue(4 in self.some_graph)
        self.assertTrue(self.some_graph.contains(4))
        self.assertTrue(5 in self.some_graph)
        self.assertTrue(self.some_graph.contains(5))
        self.assertFalse(1 in self.some_graph)
        self.assertFalse(self.some_graph.contains(1))

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
        self.empty_graph.insert(4)
        self.assertEqual([4], self.empty_graph.vertices())
        self.empty_graph.insert(2)
        self.assertEqual([2,4], sorted(self.empty_graph.vertices()))
        self.empty_graph.insert(1)
        self.assertEqual([1,2,4], sorted(self.empty_graph.vertices()))

    def test_remove_raises(self):
        with self.assertRaises(ValueError):
            self.empty_graph.remove(4)
        with self.assertRaises(ValueError):
            self.unit_graph.remove(1)
        with self.assertRaises(ValueError):
            self.some_graph.remove(7)

    def test_remove_ok(self):
        self.unit_graph.remove(2)
        self.assertTrue(self.unit_graph.is_empty())

        self.some_graph.remove(5)
        self.assertEqual([], self.some_graph.neighbors(4))
        self.assertEqual([], self.some_graph.neighbors(2))

    def test_remove_when_self_adjacent(self):
        self.some_graph.connect(5,5)
        self.some_graph.remove(5)
        self.assertEqual([], self.some_graph.neighbors(4))
        self.assertEqual([], self.some_graph.neighbors(2))

    def test_remove_no_neighbors(self):
        self.some_graph.connect(5,2)
        self.some_graph.connect(4,2)
        self.some_graph.connect(2,4)
        self.some_graph.connect(5,5)
        self.some_graph.remove(5)
        self.assertTrue(5 not in self.some_graph)
        self.assertTrue(5 not in self.some_graph.neighbors(4))
        self.assertTrue(5 not in self.some_graph.neighbors(2))

    def test_connect_raises(self):
        with self.assertRaises(ValueError):
            self.empty_graph.connect(1,2)
        with self.assertRaises(ValueError):
            self.unit_graph.connect(1,2)
        with self.assertRaises(ValueError):
            self.unit_graph.connect(2,1)
        with self.assertRaises(ValueError):
            self.unit_graph.connect(2,2)
            self.unit_graph.connect(2,2)
        with self.assertRaises(ValueError):
            self.some_graph.connect(4,5)
        with self.assertRaises(ValueError):
            self.some_graph.connect(5,4)
        with self.assertRaises(ValueError):
            self.some_graph.connect(2,5)
        with self.assertRaises(ValueError):
            self.some_graph.connect(1,5)
        with self.assertRaises(ValueError):
            self.some_graph.connect(5,1)

    def test_connect_ok(self):
        self.unit_graph.connect(2,2)
        self.assertTrue(self.unit_graph.adjacent(2,2))
        self.some_graph.connect(5,5)
        self.assertTrue(self.some_graph.adjacent(5,5))
        self.some_graph.connect(2,4)
        self.assertTrue(self.some_graph.adjacent(2,4))
        self.some_graph.connect(4,2)
        self.assertTrue(self.some_graph.adjacent(4,2))

    def test_disconnect_raises(self):
        with self.assertRaises(ValueError):
            self.empty_graph.disconnect(3,2)

        with self.assertRaises(ValueError):
            self.unit_graph.disconnect(2,2)
        with self.assertRaises(ValueError):
            self.unit_graph.disconnect(5,2)
        with self.assertRaises(ValueError):
            self.unit_graph.disconnect(2,5)
        with self.assertRaises(ValueError):
            self.unit_graph.disconnect(5,7)

        with self.assertRaises(ValueError):
            self.some_graph.disconnect(5,2)
        with self.assertRaises(ValueError):
            self.some_graph.disconnect(8,9)
        with self.assertRaises(ValueError):
            self.some_graph.disconnect(4,9)
        with self.assertRaises(ValueError):
            self.some_graph.disconnect(9,5)
        with self.assertRaises(ValueError):
            self.some_graph.disconnect(2,5)
            self.some_graph.disconnect(2,5)

    def test_disconnect_ok(self):
        self.some_graph.disconnect(2,5)
        self.assertFalse(self.some_graph.adjacent(2,5))
        self.assertTrue(self.some_graph.adjacent(5,4))
        self.assertTrue(self.some_graph.adjacent(4,5))

        self.some_graph.connect(5,5)
        self.some_graph.connect(2,5)
        self.some_graph.disconnect(5,5)
        self.assertFalse(self.some_graph.adjacent(5,5))
        self.assertTrue(self.some_graph.adjacent(2,5))
        self.assertTrue(self.some_graph.adjacent(5,4))
        self.assertTrue(self.some_graph.adjacent(4,5))

    def test_n_edges_ok(self):
        self.assertEqual(0, self.empty_graph.n_edges())
        self.assertEqual(0, self.unit_graph.n_edges())
        self.assertEqual(3, self.some_graph.n_edges())

        self.unit_graph.connect(2,2)
        self.assertEqual(1, self.unit_graph.n_edges())

        self.some_graph.connect(4,2)
        self.assertEqual(4, self.some_graph.n_edges())
        self.some_graph.disconnect(2,5)
        self.assertEqual(3, self.some_graph.n_edges())

    def test_n_vertices_ok(self):
        self.assertEqual(0, self.empty_graph.n_vertices())
        self.assertEqual(1, self.unit_graph.n_vertices())
        self.assertEqual(3, self.some_graph.n_vertices())

        self.empty_graph.insert(5)
        self.assertEqual(1, self.empty_graph.n_vertices())

        self.some_graph.remove(5)
        self.assertEqual(2, self.some_graph.n_vertices())

    def test_is_empty_ok(self):
        self.assertTrue(self.empty_graph.is_empty())
        self.assertFalse(self.unit_graph.is_empty())
        self.assertFalse(self.some_graph.is_empty())

    def test_equal_self(self):
        self.assertTrue(self.empty_graph.equal(self.empty_graph))
        self.assertEqual(self.empty_graph, self.empty_graph)

        self.assertTrue(self.unit_graph.equal(self.unit_graph))
        self.assertEqual(self.unit_graph, self.unit_graph)

        self.assertTrue(self.some_graph.equal(self.some_graph))
        self.assertEqual(self.some_graph, self.some_graph)

    def test_equal_ok(self):
        g = Graph()
        self.assertEqual(g, self.empty_graph)
        self.assertFalse(g is self.empty_graph)

        g.insert(2)
        self.assertEqual(g, self.unit_graph)
        self.assertFalse(g is self.unit_graph)

        g.insert(4)
        g.insert(5)
        g.connect(4,5)
        g.connect(5,4)
        g.connect(2,5)
        self.assertEqual(g, self.some_graph)
        self.assertFalse(g is self.some_graph)

    def test_copy_ok(self):
        g = self.empty_graph.copy()
        self.assertEqual(g, self.empty_graph)
        self.assertFalse(g is self.empty_graph)

        g = self.unit_graph.copy()
        self.assertEqual(g, self.unit_graph)
        self.assertFalse(g is self.unit_graph)

        g = self.some_graph.copy()
        self.assertEqual(g, self.some_graph)
        self.assertFalse(g is self.some_graph)

    def test_clear_ok(self):
        self.empty_graph.clear()
        self.assertEqual(0, self.empty_graph.n_vertices())
        self.assertEqual(0, self.empty_graph.n_edges())

        self.unit_graph.clear()
        self.assertEqual(0, self.unit_graph.n_vertices())
        self.assertEqual(0, self.unit_graph.n_edges())

        self.some_graph.clear()
        self.assertEqual(0, self.some_graph.n_vertices())
        self.assertEqual(0, self.some_graph.n_edges())

if __name__ == '__main__':
    from pystruct3.graph import AdjacencyListGraph as Graph
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestGraphMethods))
