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

"""
Queue data structures.

This module contains class implementations of several Queue types.
The available queues are:

"""

from pystruct3.list import DoubleLinkedList

class Queue(object):
    """Queue data structure interface.

    This is the interface of a queue data structure. All queue classes are
    sub-classes of Queue.

    Args:
        Nothing.

    Attributes (public):
        Nothing.
    """
    def __init__(self):
        """Create an empty queue.
        """
        self.items = DoubleLinkedList()

    def __del__(self):
        """Destroy the queue.
        """
        self.clear()


    def enqueue(self, item):
        """Add an item to the queue

        Args:
            item (object): Item to add to the queue.

        Return:
            Nothing.

        Raises:
            Nothing.
        """
        self.items.append(item)

    def dequeue(self):
        """Remove the first item of the queue

        Args:
            Nothing.

        Return:
            object: first item of the queue

        Raises:
            ValueError: An error occurs when the list is empty.
        """
        return self.items.pop()

    def first(self):
        """Read the first item of the queue

        Does not modify the queue.

        Args:
            Nothing.

        Return:
            object: first item of the queue

        Raises:
            ValueError: An error occurs when the list is empty.
        """
        return self.items[0]

    def last(self):
        """Read the last item of the queue

        Does not modify the queue.

        Args:
            Nothing.

        Return:
            object: last item of the queue

        Raises:
            ValueError: An error occurs when the list is empty.
        """
        return self.items[-1]

    def contains(self, item):
        """Verify if an item is in the queue.

        Does not modify the queue.

        Args:
            item (object): The queried item.

        Returns:
            bool: True if item is in the queue, False otherwise.

        Raises:
            Nothing
        """
        return (item in self.items)

    def copy(self, ):
        """Deep copy of the queue.

        Args:
            Nothing.

        Returns:
            Queue: A deep copy of the queue.

        Raises:
            Nothing.
        """
        return self.items.copy()

    def clear(self):
        """Remove all items from the queue.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        self.items.clear()

    def size(self):
        """Get the size of the queue.

        Does not modify the queue.

        Args:
            Nothing.

        Returns:
            int: The size of the queue.

        Raises:
            Nothing.
        """
        return self.items.size()

    def is_empty(self):
        """Verify if the queue is empty.

        Does not modify the queue.

        Args:
            Nothing.

        Returns:
            bool: True if the queue is empty, False otherwise.

        Raises:
            Nothing.
        """
        return self.items.is_empty()

    def __len__(self):
        return self.items.size()

    def __contains__(self, item):
        return self.contains(item)

    def __eq__(self, other_queue):
        return self.items == other_queue.items

    def __iter__(self):
        return self.items.__iter__()

    def __repr__(self):
        return self.items.__repr__()