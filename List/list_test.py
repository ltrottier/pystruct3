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
        # []
        self.empty_list = List()

        # [4]
        self.unit_list = List()
        self.unit_list.append(4)

        # [3, 1, 2]
        self.some_list = List()
        self.some_list.insert(1, 0)
        self.some_list.insert(2, 1)
        self.some_list.insert(3, 0)

    def test_read_ok(self):
        self.assertEqual(self.unit_list[0], 4)
        self.assertEqual(self.unit_list[-1], 4)

        self.assertEqual(self.some_list.read(0), 3)
        self.assertEqual(self.some_list[0], 3)
        self.assertEqual(self.some_list[-3], 3)

        self.assertEqual(self.some_list.read(1), 1)
        self.assertEqual(self.some_list[1], 1)
        self.assertEqual(self.some_list[-2], 1)

        self.assertEqual(self.some_list.read(2), 2)
        self.assertEqual(self.some_list[2], 2)
        self.assertEqual(self.some_list[-1], 2)

    def test_read_raises(self):
        with self.assertRaises(ValueError):
            self.unit_list.read(1)
        with self.assertRaises(ValueError):
            self.empty_list.read(-1)
        with self.assertRaises(ValueError):
            self.empty_list.read(0)
        with self.assertRaises(ValueError):
            self.some_list.read(4)
        with self.assertRaises(ValueError):
            self.some_list.read(-4)

    def test_contains_ok(self):
        self.assertFalse(1 in self.empty_list)
        self.assertFalse(self.empty_list.contains(1))

        self.assertFalse(0 in self.unit_list)
        self.assertTrue(4 in self.unit_list)

        self.assertTrue(1 in self.some_list)
        self.assertTrue(self.some_list.contains(1))
        self.assertTrue(2 in self.some_list)
        self.assertTrue(self.some_list.contains(2))
        self.assertTrue(3 in self.some_list)
        self.assertTrue(self.some_list.contains(3))
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
            self.unit_list.insert(5,2)
        with self.assertRaises(ValueError):
            self.unit_list.insert(5,-3)
        with self.assertRaises(ValueError):
            self.some_list.insert(-1, 4)

    def test_insert_ok(self):
        a_list = List()
        a_list.insert(4,0)
        self.assertEqual(4, a_list[0])
        self.assertEqual(4, a_list[-1])

        a_list.insert(3, -1)
        self.assertEqual(4, a_list[-1])
        self.assertEqual(3, a_list[0])
        self.assertEqual(4, a_list[1])

        a_list.insert(5, 2)
        self.assertEqual(3, a_list[-3])
        self.assertEqual(4, a_list[-2])
        self.assertEqual(5, a_list[-1])
        self.assertEqual(3, a_list[0])
        self.assertEqual(4, a_list[1])
        self.assertEqual(5, a_list[2])

        a_list.insert(6,-3)
        self.assertEqual(6, a_list[-4])
        self.assertEqual(3, a_list[-3])
        self.assertEqual(4, a_list[-2])
        self.assertEqual(5, a_list[-1])
        self.assertEqual(6, a_list[0])
        self.assertEqual(3, a_list[1])
        self.assertEqual(4, a_list[2])
        self.assertEqual(5, a_list[3])

    def test_append_ok(self):
        a_list = List()
        a_list.append(2)
        a_list.append(6)
        a_list.append(7)
        a_list.append(9)
        self.assertEqual(2, a_list[0])
        self.assertEqual(6, a_list[1])
        self.assertEqual(7, a_list[2])
        self.assertEqual(9, a_list[3])

    def test_pop_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.pop(0)
        with self.assertRaises(ValueError):
            del self.empty_list[0]

        with self.assertRaises(ValueError):
            self.unit_list.pop(1)
        with self.assertRaises(ValueError):
            del self.unit_list[1]

        with self.assertRaises(ValueError):
            self.unit_list.pop(-2)
        with self.assertRaises(ValueError):
            del self.unit_list[-2]

        with self.assertRaises(ValueError):
            self.some_list.pop(-4)
        with self.assertRaises(ValueError):
            del self.some_list[-4]

        with self.assertRaises(ValueError):
            self.some_list.pop(3)
        with self.assertRaises(ValueError):
            del self.some_list[3]

    def test_pop_ok(self):
        item = self.some_list.pop(0)
        self.assertEqual(item, 3)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(2, self.some_list[1])
        self.assertEqual(2, self.some_list.size())

        item = self.some_list.pop(1)
        self.assertEqual(item, 2)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(1, self.some_list.size())

        item = self.some_list.pop(0)
        self.assertEqual(item, 1)
        self.assertEqual(0, self.some_list.size())

        self.unit_list.pop(0)
        self.assertTrue(self.unit_list.is_empty())

    def test_pop_neg_ok(self):
        item = self.some_list.pop(-3)
        self.assertEqual(item, 3)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(2, self.some_list[1])
        self.assertEqual(2, self.some_list.size())

        item = self.some_list.pop(-1)
        self.assertEqual(item, 2)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(1, self.some_list.size())

    def test_remove_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.remove(0)
        with self.assertRaises(ValueError):
            self.unit_list.remove(2)
        with self.assertRaises(ValueError):
            self.some_list.remove(5)

    def test_remove_ok(self):
        self.unit_list.remove(4)
        self.assertTrue(self.unit_list.is_empty())

        self.some_list.remove(3)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(2, self.some_list[1])
        self.assertEqual(2, self.some_list.size())
        self.some_list.remove(2)
        self.assertEqual(1, self.some_list[0])
        self.assertEqual(1, self.some_list.size())
        self.some_list.remove(1)
        self.assertEqual(0, self.some_list.size())

    def test_random_insert_remove_ok(self):
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

    def test_index_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.index(2)
        with self.assertRaises(ValueError):
            self.unit_list.index(5)
        with self.assertRaises(ValueError):
            self.some_list.index(-3)

    def test_index_ok(self):
        self.assertEqual(self.unit_list.index(4), 0)

        self.assertEqual(self.some_list.index(3), 0)
        self.assertEqual(self.some_list.index(2), 2)
        self.assertEqual(self.some_list.index(1), 1)

    def test_write_raises(self):
        with self.assertRaises(ValueError):
            self.empty_list.write(2,0)
        with self.assertRaises(ValueError):
            self.empty_list[0] = 2
        with self.assertRaises(ValueError):
            self.empty_list[-1] = 2
        with self.assertRaises(ValueError):
            self.unit_list.write(5,1)
        with self.assertRaises(ValueError):
            self.unit_list[1] = 5
        with self.assertRaises(ValueError):
            self.unit_list[-2] = 5
        with self.assertRaises(ValueError):
            self.some_list.write(10,3)
        with self.assertRaises(ValueError):
            self.some_list[3] = 10
        with self.assertRaises(ValueError):
            self.some_list[-4] = 10

    def test_write_ok(self):
        self.some_list.write(12, -1)
        self.assertEqual(self.some_list[-1], 12)
        self.some_list.write(22, -2)
        self.assertEqual(self.some_list[-2], 22)
        self.some_list.write(17, -3)
        self.assertEqual(self.some_list[-3], 17)

        self.some_list.write(6,0)
        self.assertEqual(self.some_list[0], 6)
        self.some_list.write(7,1)
        self.assertEqual(self.some_list[1], 7)
        self.some_list.write(10,2)
        self.assertEqual(self.some_list[2], 10)

        self.some_list[-1] = 10
        self.assertEqual(self.some_list[-1], 10)
        self.some_list[-2] = 90
        self.assertEqual(self.some_list[-2], 90)
        self.some_list[-3] = 140
        self.assertEqual(self.some_list[-3], 140)

        self.some_list[0] = 1
        self.assertEqual(self.some_list[0], 1)
        self.some_list[1] = 9
        self.assertEqual(self.some_list[1], 9)
        self.some_list[2] = 14
        self.assertEqual(self.some_list[2], 14)

        self.unit_list.write(3,0)
        self.assertEqual(self.unit_list[0], 3)
        self.unit_list[0] = 5
        self.assertEqual(self.unit_list[0], 5)

    def test_concat_empty_ok(self):
        p = List()
        l = List()
        q = p + l
        self.assertTrue(q.is_empty())

    def test_concat_unit_ok(self):
        p = List()
        l = List()
        p.append(3)
        l.append(6)
        q = p + l
        self.assertEqual(q[0], 3)
        self.assertEqual(q[1], 6)

    def test_concat_some_list_ok(self):
        p = List()
        l = List()

        p.append(3)
        p.append(7)
        p.append(1)
        l.append(6)
        l.append(2)
        l.append(4)

        q = p + l
        self.assertEqual(q[0], 3)
        self.assertEqual(q[1], 7)
        self.assertEqual(q[2], 1)
        self.assertEqual(q[3], 6)
        self.assertEqual(q[4], 2)
        self.assertEqual(q[5], 4)

    def test_concat_self_ok(self):
        q = self.some_list + self.some_list
        self.assertEqual(q[0], 3)
        self.assertEqual(q[1], 1)
        self.assertEqual(q[2], 2)
        self.assertEqual(q[3], 3)
        self.assertEqual(q[4], 1)
        self.assertEqual(q[5], 2)

    def test_concat_no_overwrite(self):
        p = List()

        p.append(9)
        p.append(7)
        p.append(1)

        l = self.some_list + p
        l[0] = 12
        l[1] = 56
        l[2] = 43
        l[3] = 41
        l[4] = 98
        l[5] = 32
        self.assertEqual(self.some_list[0],3)
        self.assertEqual(self.some_list[1],1)
        self.assertEqual(self.some_list[2],2)
        self.assertEqual(p[0],9)
        self.assertEqual(p[1],7)
        self.assertEqual(p[2],1)

    def test_equal_ok(self):
        p = List()
        l = List()
        self.assertTrue(p == l)
        self.assertFalse(p is l)
        for i in range(5):
            p.append(i)
            l.append(i)
            self.assertTrue(p == l)
            self.assertFalse(p is l)

        q = List()
        m = List()
        for i in range(1,5):
            q.append(i)
            m.append(-i)
            self.assertTrue(q != m)
            self.assertFalse(q is m)

if __name__ == '__main__':
    from list import SingleLinkedList as List
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestListMethods))

    from list import DoubleLinkedList as List
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestListMethods))