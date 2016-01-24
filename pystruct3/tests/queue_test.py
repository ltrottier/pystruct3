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

class TestQueueMethods(unittest.TestCase):

    def setUp(self):
        # []
        self.empty_queue = Queue()

        # [4]
        self.unit_queue = Queue()
        self.unit_queue.enqueue(4)

        # [3, 1, 2]
        self.some_queue = Queue()
        self.some_queue.enqueue(3)
        self.some_queue.enqueue(1)
        self.some_queue.enqueue(2)

    def test_size_ok(self):
        self.assertEqual(self.empty_queue.size(), 0)
        self.assertEqual(len(self.empty_queue), 0)
        self.assertEqual(self.unit_queue.size(), 1)
        self.assertEqual(len(self.unit_queue), 1)
        self.assertEqual(self.some_queue.size(), 3)
        self.assertEqual(len(self.some_queue), 3)

    def test_is_empty_ok(self):
        self.assertTrue(self.empty_queue.is_empty())
        self.assertFalse(self.unit_queue.is_empty())
        self.assertFalse(self.some_queue.is_empty())

    def test_dequeue_raises(self):
        with self.assertRaises(ValueError):
            self.empty_queue.dequeue()

        self.unit_queue.dequeue()
        with self.assertRaises(ValueError):
            self.unit_queue.dequeue()

        self.some_queue.dequeue()
        self.some_queue.dequeue()
        self.some_queue.dequeue()
        with self.assertRaises(ValueError):
            self.some_queue.dequeue()

    def test_dequeue_ok(self):
        self.assertEqual(4, self.unit_queue.dequeue())
        self.assertEqual(0, self.unit_queue.size())

        self.assertEqual(3, self.some_queue.dequeue())
        self.assertEqual(2, self.some_queue.size())
        self.assertEqual(1, self.some_queue.dequeue())
        self.assertEqual(1, self.some_queue.size())
        self.assertEqual(2, self.some_queue.dequeue())
        self.assertEqual(0, self.some_queue.size())

    def test_first_raises(self):
        with self.assertRaises(ValueError):
            self.empty_queue.first()

    def test_first_ok(self):
        self.assertEqual(4, self.unit_queue.first())
        self.assertEqual(3, self.some_queue.first())

    def test_last_raises(self):
        with self.assertRaises(ValueError):
            self.empty_queue.last()

    def test_last_ok(self):
        self.assertEqual(4, self.unit_queue.last())
        self.assertEqual(2, self.some_queue.last())

    def test_contains_ok(self):
        self.assertTrue(self.unit_queue.contains(4))
        self.assertTrue(4 in self.unit_queue)
        self.assertTrue(self.some_queue.contains(1))
        self.assertTrue(1 in self.some_queue)
        self.assertTrue(self.some_queue.contains(2))
        self.assertTrue(2 in self.some_queue)
        self.assertTrue(self.some_queue.contains(3))
        self.assertTrue(3 in self.some_queue)

    def test_clear_ok(self):
        self.empty_queue.clear()
        self.assertTrue(self.empty_queue.is_empty())

        self.unit_queue.clear()
        self.assertTrue(self.unit_queue.is_empty())

        self.some_queue.clear()
        self.assertTrue(self.some_queue.is_empty())

    def test_equal_ok(self):
        a = Queue()
        self.assertEqual(a, self.empty_queue)
        self.assertNotEqual(a, self.unit_queue)
        self.assertNotEqual(a, self.some_queue)
        a.enqueue(4)
        self.assertNotEqual(a, self.empty_queue)
        self.assertEqual(a, self.unit_queue)
        self.assertNotEqual(a, self.some_queue)
        a.dequeue()
        a.enqueue(3)
        a.enqueue(1)
        a.enqueue(2)
        self.assertNotEqual(a, self.empty_queue)
        self.assertNotEqual(a, self.unit_queue)
        self.assertEqual(a, self.some_queue)

    def test_equal_same_queue_ok(self):
        self.assertEqual(self.empty_queue, self.empty_queue)
        self.assertEqual(self.unit_queue, self.unit_queue)
        self.assertEqual(self.some_queue, self.some_queue)

    def test_copy_ok(self):
        a = self.empty_queue.copy()
        self.assertEqual(a.size(), 0)

        a = self.unit_queue.copy()
        self.assertEqual(a.size(), 1)
        self.assertEqual(a.dequeue(), 4)

        a = self.some_queue.copy()
        self.assertEqual(a.size(), 3)
        self.assertEqual(a.dequeue(), 3)
        self.assertEqual(a.dequeue(), 1)
        self.assertEqual(a.dequeue(), 2)

    def test_copy_no_overwrite_ok(self):
        a = self.empty_queue.copy()
        a.enqueue(4)
        self.assertNotEqual(a.size(), self.empty_queue.size())

        a = self.unit_queue.copy()
        a.dequeue()
        a.enqueue(-1)
        self.assertNotEqual(a.first(), self.some_queue.first())

        a = self.some_queue.copy()
        a.dequeue()
        a.enqueue(-1)
        self.assertNotEqual(a.first(), self.some_queue.first())


if __name__ == '__main__':
    from pystruct3.queue import LIFOQueue as Queue
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestQueueMethods))

