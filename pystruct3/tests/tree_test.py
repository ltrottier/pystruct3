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

class TestTreeMethods(unittest.TestCase):

    def setUp(self):
        self.empty_tree = Tree()

        self.unit_tree = Tree()
        self.unit_tree.insert(2)

        self.some_tree = Tree()
        self.some_tree.push(4)
        self.some_tree.push(5)
        self.some_tree.push(2)


if __name__ == '__main__':
    from pystruct3.tree import Heap as Tree
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestTreeMethods))

    a = Tree()
    a.push(4)
    a.push(2)
    a.push(6)
    a.push(8)
    a.push(1)
    a.push(2)
    # a.push(3)