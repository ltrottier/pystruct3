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
from stack import Stack

class TestStackMethods(unittest.TestCase):

    def setUp(self):
        # []
        self.empty_stack = Stack()

        # [4]
        self.unit_stack = Stack()
        self.unit_stack.push(4)

        # [3, 1, 2]
        self.some_stack = Stack()
        self.some_stack.push(3)
        self.some_stack.push(1)
        self.some_stack.push(2)

    def test_size_ok(self):
        self.assertEqual(self.empty_stack.size(), 0)
        self.assertEqual(len(self.empty_stack), 0)
        self.assertEqual(self.unit_stack.size(), 1)
        self.assertEqual(len(self.unit_stack), 1)
        self.assertEqual(self.some_stack.size(), 3)
        self.assertEqual(len(self.some_stack), 3)

    def test_is_empty_ok(self):
        self.assertTrue(self.empty_stack.is_empty())
        self.assertFalse(self.unit_stack.is_empty())
        self.assertFalse(self.some_stack.is_empty())

    def test_pop_raises(self):
        with self.assertRaises(ValueError):
            self.empty_stack.pop()

        self.unit_stack.pop()
        with self.assertRaises(ValueError):
            self.unit_stack.pop()

        self.some_stack.pop()
        self.some_stack.pop()
        self.some_stack.pop()
        with self.assertRaises(ValueError):
            self.some_stack.pop()

    def test_pop_ok(self):
        self.assertEqual(4, self.unit_stack.pop())
        self.assertEqual(0, self.unit_stack.size())

        self.assertEqual(2, self.some_stack.pop())
        self.assertEqual(2, self.some_stack.size())
        self.assertEqual(1, self.some_stack.pop())
        self.assertEqual(1, self.some_stack.size())
        self.assertEqual(3, self.some_stack.pop())
        self.assertEqual(0, self.some_stack.size())

    def test_peek_raises(self):
        with self.assertRaises(ValueError):
            self.empty_stack.peek()

    def test_peek_ok(self):
        self.assertEqual(4, self.unit_stack.peek())
        self.assertEqual(2, self.some_stack.peek())

    def test_write_raises(self):
        with self.assertRaises(ValueError):
            self.empty_stack.write(4)

    def test_write_ok(self):
        self.unit_stack.write(-1)
        self.assertEqual(-1, self.unit_stack.peek())

        self.some_stack.write(-1)
        self.assertEqual(-1, self.some_stack.peek())

    def test_contains_ok(self):
        self.assertTrue(self.unit_stack.contains(4))
        self.assertTrue(4 in self.unit_stack)
        self.assertTrue(self.some_stack.contains(1))
        self.assertTrue(1 in self.some_stack)
        self.assertTrue(self.some_stack.contains(2))
        self.assertTrue(2 in self.some_stack)
        self.assertTrue(self.some_stack.contains(3))
        self.assertTrue(3 in self.some_stack)

    def test_clear_ok(self):
        self.empty_stack.clear()
        self.assertTrue(self.empty_stack.is_empty())

        self.unit_stack.clear()
        self.assertTrue(self.unit_stack.is_empty())

        self.some_stack.clear()
        self.assertTrue(self.some_stack.is_empty())

    def test_equal_ok(self):
        a = Stack()
        self.assertEqual(a, self.empty_stack)
        self.assertNotEqual(a, self.unit_stack)
        self.assertNotEqual(a, self.some_stack)
        a.push(4)
        self.assertNotEqual(a, self.empty_stack)
        self.assertEqual(a, self.unit_stack)
        self.assertNotEqual(a, self.some_stack)
        a.pop()
        a.push(3)
        a.push(1)
        a.push(2)
        self.assertNotEqual(a, self.empty_stack)
        self.assertNotEqual(a, self.unit_stack)
        self.assertEqual(a, self.some_stack)

    def test_equal_same_stack_ok(self):
        self.assertEqual(self.empty_stack, self.empty_stack)
        self.assertEqual(self.unit_stack, self.unit_stack)
        self.assertEqual(self.some_stack, self.some_stack)

    def test_copy_ok(self):
        a = self.empty_stack.copy()
        self.assertEqual(a.size(), 0)

        a = self.unit_stack.copy()
        self.assertEqual(a.size(), 1)
        self.assertEqual(a.pop(), 4)

        a = self.some_stack.copy()
        self.assertEqual(a.size(), 3)
        self.assertEqual(a.pop(), 2)
        self.assertEqual(a.pop(), 1)
        self.assertEqual(a.pop(), 3)



    def test_copy_no_overwrite_ok(self):
        a = self.empty_stack.copy()
        a.push(4)
        self.assertNotEqual(a.size(), self.empty_stack.size())

        a = self.unit_stack.copy()
        a.write(-1)
        self.assertNotEqual(a.peek(), self.some_stack.peek())

        a = self.some_stack.copy()
        a.write(-1)
        self.assertNotEqual(a.peek(), self.some_stack.peek())


if __name__ == '__main__':
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestStackMethods))
