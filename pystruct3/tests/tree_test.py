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


import random
import unittest

class TestTreeMethods(unittest.TestCase):

    def setUp(self):
        self.empty_tree = Tree()

        self.unit_tree = Tree()
        self.unit_tree.push(2)

        self.some_tree = Tree()
        self.some_tree.push(4)
        self.some_tree.push(5)
        self.some_tree.push(2)

    def test_push_pop_ok(self):
        a = Tree()
        for i in range(1000):
            for j in range(50):
                a.push(random.randint(1,100))
                self.assertTrue(a._is_heap())
            for j in range(50):
                a.pop()
                self.assertTrue(a._is_heap())

            self.assertTrue(a.is_empty())


if __name__ == '__main__':
    from pystruct3.tree import Heap as Tree
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTreeMethods))
