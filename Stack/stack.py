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
Stack data structures.

This module contains a class implementation of a stack type.
"""

class Stack(object):
    """Stack data structure.

    This stack is based on a single liked list.

    Args:
        Nothing.

    Attributes (public):
        Nothing.
    """

    class _Node(object):
        """Node class for linked list.

        Args:
            item (object): Item contained in the node.
            next_node (_Node): Pointer to neighbor node.

        Attributes (public):
            item (object): Item contained in the node.
            next_node (_Node): Pointer to neighbor node.
        """

        def __init__(self, item, next_node=None):
            self.item = item
            self.next_node = next_node

        def __del__(self):
            self.item = None
            self.next_node = None

    class _ForwardIterator(object):
        """Iterator for Stack.

        Args:
            node (Node): A linked list node.

        Attributs (public):
            node (Node): A linked list node.
        """

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

    def __init__(self):
        """Create an empty stack.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        self._size = 0
        self._head = None


    def __del__(self):
        """Destroy the stack.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        self.clear()

    def push(self, item):
        """Push an item at the top of the stack.

        Args:
            item (object): The item to add to the stack.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        new_node = self._Node(item, self._head)
        self._head = new_node
        self._size = self._size + 1

    def pop(self):
        """Removes and return the item at the top of the stack

        Args:
            Nothing.

        Returns:
            object: The item at the top of the list.

        Raises:
            ValueError: An error occurs when the list is empty.
        """
        if self.is_empty():
            raise ValueError('The stack is empty.')

        item = self._head.item
        self._head = self._head.next_node
        self._size = self._size - 1
        return item

    def peek(self):
        """Returns the element at the top of the stack.

        Args:
            Nothing.

        Returns:
            object: The item at the top of the list.

        Raises:
            ValueError: An error occurs when the list is empty.
        """
        if self.is_empty():
            raise ValueError('The stack is empty.')

        return self._head.item

    def write(self, item):
        """Write an item at the top of the stack.

        Args:
            item (object): Item to be written.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs if the stack is empty.
        """
        if self.is_empty():
            raise ValueError('The stack is empty.')

        self._head.item = item

    def contains(self, item):
        """Verify if an item is in the stack.

        Does not modify the stack.

        Args:
            item (object): The queried item.

        Returns:
            bool: True if item is in the stack, False otherwise.

        Raises:
            Nothing
        """
        sentinel = self._head
        while sentinel is not None:
            if sentinel.item == item:
                return True
            sentinel = sentinel.next_node
        return False

    def clear(self):
        """Remove all items from the stack.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        while self._size > 0:
            self.pop()

    def is_empty(self):
        """Verify if the stack is empty.

        Does not modify the stack.

        Args:
            Nothing.

        Returns:
            bool: True if the stack is empty, False otherwise.

        Raises:
            Nothing.
        """
        return self._size == 0

    def size(self):
        """Get the size of the stack.

        Does not modify the stack.

        Args:
            Nothing.

        Returns:
            int: The size of the stack.

        Raises:
            Nothing.
        """
        return self._size

    def copy(self):
        """Deep copy of the stack.

        Args:
            Nothing.

        Returns:
            Stack: A deep copy of the stack

        Raises:
            Nothing.
        """
        tmp_stack = self.__class__()
        copy_stack = self.__class__()
        for item in self:
            tmp_stack.push(item)

        while not tmp_stack.is_empty():
            copy_stack.push(tmp_stack.pop())

        return copy_stack

    def __len__(self):
        return self._size

    def __iter__(self):
        return self._ForwardIterator(self._head)

    def __contains__(self, item):
        return self.contains(item)

    def __eq__(self, other_list):
        if self._size != other_list.size():
            return False

        for item1,item2 in zip(self,other_list):
            if item1 != item2:
                return False

        return True

    def __repr__(self):
        items = ['[']
        for item in self:
            items.append(str(item))
            items.append(', ')
        if not self.is_empty():
            items.insert(2, ')')
            items.insert(1, '(')
            del items[-1]
        items.append(']')
        return ''.join(items)