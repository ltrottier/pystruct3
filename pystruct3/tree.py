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

"""
"""

class Tree(object):
    """A tree is a directed graph in which: 1. any two vertices are
       connected by exactly one path, 2. there is a node call the source, and
       3. all nodes point away from the source.
    """
    def __init__(self):
        pass


class Heap(Tree):
    """A heap is a tree that satisfies the heap property.
    """
    def __init__(self, compare=None):
        Tree.__init__(self)
        self._vertices = [None]
        self._capacity = 1
        self._n_vertices = 0
        if compare is None:
            self._compare = lambda x1,x2 : x1 >= x2
        else:
            self._compare = compare

    def push(self, vertice):
        """Insert a vertice in the heap.

        Args:
            vertice (object): The vertice to insert.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        if self._capacity == self._n_vertices + 1:
            self._augment_capacity(2*len(self._vertices) + 1)
        self._vertices[self._n_vertices + 1] = vertice
        self._shift_up(self._n_vertices + 1)
        self._n_vertices = self._n_vertices + 1

    def _augment_capacity(self, new_capacity):
        increment = new_capacity - self._capacity
        self._capacity = new_capacity
        self._vertices.extend([None for _ in range(increment)])

    def _shift_up(self, start_index):
        index = start_index
        if index == 1:
            return
        parent = index // 2
        heap_condition = self._compare(self._vertices[parent],
                                       self._vertices[index])
        while not heap_condition:
            self._vertices[index], self._vertices[parent] = (
               self._vertices[parent], self._vertices[index])

            index = parent
            if index == 1:
                return
            parent = index // 2
            heap_condition = self._compare(self._vertices[parent],
                                           self._vertices[index])


    def clear(self):
        """Remove all vertices from the heap.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        self._vertices.clear()
        self._n_vertices = 0

    def peek(self):
        """Inspect the root of the heap.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs when the heap is empty.
        """
        pass

    def pop(self):
        """Extract the root of the heap and return it.

        Args:
            Nothing.

        Returns:
            object: Vertice at the root.

        Raises:
            ValueError: An error occurs when the heap is empty.
        """
        pass

    def replace(self, vertice):
        """Pop the root then push a vertice.

        This is more efficient than pop followed by push because only
        one balancing is done instead of two.

        Args:
            vertice (object): The vertice to insert.

        Returns:
            object: Vertice at the root.

        Raises:
            ValueError: An error occurs when the heap is empty.
        """
        pass

    def heapify(self, elements):
        """Create a heap out of elements.

        Args:
            elements (python list (object)): A list containing elements
                                             to form the heap.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs when elements is not a list.
        """
        pass

    def is_empty(self):
        """Verify if the heap contains vertices.

        Does not modify the heap.

        Args:
            Nothing.

        Returns:
            bool: True if the heap contains no vertices, False otherwise.

        Raises:
            Nothing.
        """
        return self._n_vertices == 0

    def size(self):
        """Get the number of vertices in the heap.

        Does not modify the heap.

        Args:
            Nothing.

        Returns:
            int: The number of vertices.

        Raises:
            Nothing.
        """
        return self._n_vertices

    def contains(self, vertice):
        """Verify if a vertice is in the heap.

        Args:
            vertice (object): The queried vertice.

        Returns:
            bool: True if the vertice is in the heap, False otherwise.

        Raises:
            Nothing.
        """
        return vertice in self._vertices

    def merge(self, other_heap):
        """Join other_heap to the current one.

        Args:
            other_heap (Heap): The heap to join.

        Returns:
            Nothing.

        Raises:
            Nothing
        """
        pass

    def __contains__(self, vertice):
        return self.contains(vertice)

    def __len__(self):
        return self._n_vertices

    def __repr__(self):
        items = ['[']
        for i in range(1, self._n_vertices + 1):
            items.append(str(self._vertices[i]))
            items.append(', ')
        if self.size() != 0:
            items.pop()
        items.append(']')
        return ''.join(items)

    def __add__(self, other_heap):
        new_heap = self.__class__()
        new_heap.merge(self)
        new_heap.merge(other_heap)
        return new_heap


class AVLTree(Tree):
    """Self-balancing tree based on AVL.
    """
    def __init__(self):
        Tree.__init__(self)


class RedBlackTree(Tree):
    """Self-balancing tree based on red-black.
    """
    def __init__(self):
        Tree.__init__(self)

