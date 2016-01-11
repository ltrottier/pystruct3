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

class List:

    def __init__(self):
        self._size = 0
        self._head = None

    def insert(self, item, pos):
        """Insert an item at a certain position.

        The inserted item will be accessible at position pos. All items that
        were formally positioned at pos, pos+1, pos+2... will be positioned at
        pos+1, pos+2, pos+3, ...

        Args:
            item: An item.
            pos: An integer of the position in the list.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs if pos is out of range, i.e. if pos < 0
                        or if pos > list size.
        """
        raise NotImplementedError

    def remove(self, pos):
        raise NotImplementedError

    def read(self, pos):
        raise NotImplementedError

    def index(self, item):
        raise NotImplementedError

    def write(self, item, pos):
        raise NotImplementedError

    def size(self):
        return self._size

    def contains(self, item):
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def append(self, item):
        self.insert(item, self.size())

    def pop(self):
        self.remove(self.size() - 1)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def __getitem__(self, pos):
        return self.read(pos)

    def __setitem__(self, pos, item):
        self.write(item, pos)

    def __delitem__(self, pos):
        self.remove(pos)

    def __contains__(self, item):
        return self.contains(item)

    def __iter__(self):
        return ForwardIterator(self._head)

    def __repr__(self):
        s = "["
        for item in self:
            s = s + str(item) + ", "
        if not self.is_empty():
            s = s[:-2]
        s = s + "]"
        return s


class ForwardIterator:

    def __init__(self, node):
        self.node = node

    def __iter__(self):
        return self

    def __next__(self):
        if self.node is None:
            raise StopIteration

        item = self.node.item
        self.node = self.node.next_node

        return item


class SingleLinkedList(List):

    class Node:

        def __init__(self, item, next_node=None):
            self.item = item
            self.next_node = next_node

    def __init__(self):
        List.__init__(self)

    def insert(self, item, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")

        if pos > self.size():
            raise ValueError("Argument pos must be lower than or equal to the list size.")

        if self.is_empty():
            self._head = SingleLinkedList.Node(item)
        else:
            sentinel = self._head
            if pos == 0:
                newNode = SingleLinkedList.Node(item, self._head)
                self._head = newNode
            else:
                for i in range(pos-1):
                    sentinel = sentinel.next_node

                newNode = SingleLinkedList.Node(item, sentinel.next_node)
                sentinel.next_node = newNode

        self._size = self._size + 1

    def remove(self, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")

        if pos >= self.size():
            raise ValueError("Argument pos must be lower than the list size.")

        if pos == 0:
            temp = self._head
            self._head = self._head.next_node
            temp.next_node = None
            temp = None
        else:
            sentinel = self._head
            for i in range(pos-1):
                sentinel = sentinel.next_node
            temp = sentinel.next_node
            sentinel.next_node = sentinel.next_node.next_node
            temp.next_node = None
            temp = None

        self._size = self._size - 1

    def read(self, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")

        if pos >= self.size():
            raise ValueError("Argument pos must be lower than the list size.")

        sentinel = self._head
        for i in range(pos):
            sentinel = sentinel.next_node

        return sentinel.item

    def index(self, item):
        sentinel = self._head
        if self.is_empty():
            raise ValueError("Item not found.")
        i = 0
        while sentinel.item != item:
            sentinel = sentinel.next_node
            i = i + 1
            if sentinel is None:
                raise ValueError("Item not found.")

        return i

    def write(self, item, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")

        if pos >= self.size():
            raise ValueError("Argument pos must be lower than the list size.")

        sentinel = self._head
        for i in range(pos):
            sentinel = sentinel.next_node

        sentinel.item = item


class DoubleLinkedList(List):

    class Node:

        def __init__(self, item, next_node):
            self.item = item
            self.next_node = next_node

    def __init__(self):
        List.__init__(self)

    def insert(self, item, pos):
        print("dll")
        if pos < 0:
            raise ValueError("Argument pos must be positive.")

        if pos > self.size():
            raise ValueError("Argument pos must be lower than the list size.")

