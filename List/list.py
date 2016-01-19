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
List data structures.

This module contains class implementations of several List types.
The available lists are:
    SingleLinkedList
    DoubleLinkedList
    CircularSingleLinkedList
    CircularDoubleLinkedList
    ArrayList
"""

class List(object):
    """List data structure interface.

    This is the interface of a list data structure. All list classes are
    sub-classes of List.

    Args:
        Nothing.

    Attributes (public):
        Nothing.
    """

    def __init__(self):
        """Create an empty list.
        """
        self._size = 0

    def __del__(self):
        """Destroy the list.
        """
        while self._size > 0:
            self.pop(0)

    def insert(self, item, index):
        """Insert an item at a certain index.

        The inserted item will be accessible at position index. All items that
        were formally positioned at index, index+1, index+2 ... will be
        positioned at index+1, index+2, index+3, ...

        Args:
            item (object): An item.
            index (int): The index in the list.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs if index is out of range, i.e.
                        if index < -1 * list size or if index > list size.
        """
        raise NotImplementedError

    def remove(self, item):
        """Remove an item of the list.

        Args:
            item (object): The item to remove.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs when item is not in the list.
        """
        raise NotImplementedError

    def pop(self, index=None):
        """Remove the item at a certain index and returns it.

        The item at position index will be removed. All items that were
        formally positioned at index+1, index+2, index+3, ... will be
        positioned at index, index+1, index+2, ...

        Args:
            index (Optional[int]): The index in the list. If not provided,
                                   pop the last item.

        Returns:
            object: The item at the given index.

        Raises:
            ValueError: An error occurs if index is out of range, i.e.
                        if index < -1 * list size or if index > list size.
        """
        raise NotImplementedError

    def read(self, index):
        """Read the list at a certain index.

        Does not modify the list.

        Args:
            index (int): The index in the list.

        Returns:
            object: The item at position index.

        Raises:
            ValueError: An error occurs if index is out of range, i.e.
                        if index < -1 * list size or if index >= list size.
        """
        raise NotImplementedError

    def index(self, item):
        """Return the index of the first occurence of item.

        Does not modify the list.

        Args:
            item (object): The queried item.

        Returns:
            int: The index in the list.

        Raises:
            ValueError: An error occurs if item is not in the list.
        """
        raise NotImplementedError

    def write(self, item, index):
        """Modify the list at a certain index.

        Object item will be accessible at position index.

        Args:
            item (object): The item to write.
            index (int): The index in the list

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs if index is out of range, i.e.
                        if index < -1 * list size or if index >= list size.
        """
        raise NotImplementedError

    def size(self):
        """Get the size of the list.

        Does not modify the list.

        Args:
            Nothing.

        Returns:
            int: The size of the list.

        Raises:
            Nothing.
        """
        return self._size

    def contains(self, item):
        """Verify if an item is in the list.

        Does not modify the list.

        Args:
            item (object): The queried item.

        Returns:
            bool: True if item is in the list, False otherwise.

        Raises:
            Nothing
        """
        try:
            self.index(item)
            return True
        except ValueError:
            return False

    def append(self, item):
        """Insert an item at the end of the list.

        Args:
            item (object): The item to add.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        self.insert(item, self._size)


    def is_empty(self):
        """Verify if the list is empty.

        Does not modify the list

        Args:
            Nothing.

        Returns:
            bool: True if the list is empty, False otherwise.

        Raises:
            Nothing.
        """
        return self._size == 0

    def copy(self):
        """Deep copy of the list.

        Args:
            Nothing.

        Returns:
            List: A deep copy of the list

        Raises:
            Nothing.
        """
        copy_list = self.__class__()
        for item in self:
            copy_list.append(item)
        return copy_list

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if isinstance(index, slice):
            sliced_list = self.__class__()
            for i in range(index.start, index.stop, index.step or 1):
                sliced_list.append(self.read(i))
            return sliced_list
        else:
            return self.read(index)

    def __setitem__(self, index, item):
        if isinstance(index, slice):
            for i in range(index.start, index.stop, index.step or 1):
                self.write(item[i], i)
        else:
            self.write(item, index)

    def __delitem__(self, index):
        if isinstance(index, slice):
            decrement = 0
            for i in range(index.start, index.stop, index.step or 1):
                self.pop(i - decrement)
                decrement = decrement + 1
        else:
            self.pop(index)

    def __contains__(self, item):
        return self.contains(item)

    def __add__(self, other_list):
        new_list = self.__class__()
        for item in self:
            new_list.append(item)
        for item in other_list:
            new_list.append(item)
        return new_list

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
            del items[-1]
        items.append(']')
        return ''.join(items)


class SingleLinkedList(List):
    """Single linked list data structure.

    Linked list where a node contains a pointer to its adjacent neighbor.

    Args:
        Nothing.

    Attributs (public):
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
            # print('deleted', self.item, self.next_node)
            self.item = None
            self.next_node = None

    class _ForwardIterator(object):
        """Iterator for SingleLinkedList.

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
        List.__init__(self)
        self._head = None

    def __iter__(self):
        return self._ForwardIterator(self._head)

    def insert(self, item, index):
        if (index < -self._size) or (index > self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if self.is_empty():
            self._head = self._Node(item)
        else:
            sentinel = self._head
            if index == 0:
                newNode = self._Node(item, self._head)
                self._head = newNode
            else:
                for i in range(index-1):
                    sentinel = sentinel.next_node

                newNode = self._Node(item, sentinel.next_node)
                sentinel.next_node = newNode

        self._size = self._size + 1

    def remove(self, item):
        if self.is_empty():
            raise ValueError('Item not found.')

        if self._head.item == item:
            self._head = self._head.next_node
        else:
            previous = self._head
            sentinel = self._head.next_node
            if sentinel is None:
                raise ValueError('Item not found.')
            while sentinel.item != item:
                previous = sentinel
                sentinel = sentinel.next_node
                if sentinel is None:
                    raise ValueError('Item not found.')

            previous.next_node = sentinel.next_node

        self._size = self._size - 1

    def pop(self, index=None):
        if index is None:
            index = self._size - 1

        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if index == 0:
            item = self._head.item
            self._head = self._head.next_node
        else:
            sentinel = self._head
            for i in range(index-1):
                sentinel = sentinel.next_node
            item = sentinel.next_node.item
            sentinel.next_node = sentinel.next_node.next_node

        self._size = self._size - 1
        return item

    def read(self, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        for i in range(index):
            sentinel = sentinel.next_node

        return sentinel.item

    def index(self, item):
        sentinel = self._head
        if self.is_empty():
            raise ValueError('Item not found.')
        i = 0
        while sentinel.item != item:
            sentinel = sentinel.next_node
            i = i + 1
            if sentinel is None:
                raise ValueError('Item not found.')

        return i

    def write(self, item, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        for i in range(index):
            sentinel = sentinel.next_node

        sentinel.item = item


class DoubleLinkedList(List):
    """Double linked list data structure.

    Linked list where a node contains a pointer to its adjacent neighbors
    (previous and next ones).

    Args:
        Nothing.

    Attributs (public):
        Nothing.
    """

    class _Node(object):
        """Node class for linked list.

        Args:
            item (object): Item contained in the node.
            next_node (_Node): Pointer to next neighbor node.
            prev_node (_Node): Pointer to previous neighbor node.

        Attributes (public):
            item (object): Item contained in the node.
            next_node (_Node): Pointer to next neighbor node.
            prev_node (_Node): Pointer to previous neighbo node.
        """
        def __init__(self, item, next_node=None, prev_node=None):
            self.item = item
            self.next_node = next_node
            self.prev_node = prev_node

        def __del__(self):
            self.item = None
            self.next_node = None
            self.prev_node = None

    class _ForwardIterator(object):
        """Iterator for DoubleLinkedList.

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
        List.__init__(self)
        self._head = None
        self._tail = None

    def __iter__(self):
        return self._ForwardIterator(self._head)

    def insert(self, item, index):
        if (index < -self._size) or (index > self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if self.is_empty():
            self._head = self._Node(item)
            self._tail = self._head
        else:
            if index == 0:
                new_node = self._Node(item, self._head)
                self._head.prev_node = new_node
                self._head = new_node
            elif index == self._size:
                new_node = self._Node(item, None, self._tail)
                self._tail.next_node = new_node
                self._tail = new_node
            else:
               if index < self._size / 2:
                   sentinel = self._head
                   for i in range(index):
                       sentinel = sentinel.next_node
               else:
                   sentinel = self._tail
                   for i in range(self._size - 1, index, -1):
                       sentinel = sentinel.prev_node

               new_node = self._Node(item, sentinel, sentinel.prev_node)
               sentinel.prev_node.next_node = new_node
               sentinel.prev_node = new_node

        self._size = self._size + 1

    def remove(self, item):
        if self.is_empty():
            raise ValueError('Item not found.')

        sentinel = self._head
        while sentinel.item != item:
            sentinel = sentinel.next_node
            if sentinel is None:
                raise ValueError('Item not found.')

        if self._size == 1:
            self._head = None
            self._tail = None
        elif sentinel is self._head:
            self._head.next_node.prev_node = None
            self._head = self._head.next_node
        elif sentinel is self._tail:
            self._tail.prev_node.next_node = None
            self._tail = self._tail.prev_node
        else:
            sentinel.prev_node.next_node = sentinel.next_node
            sentinel.next_node.prev_node = sentinel.prev_node

        self._size = self._size - 1

    def pop(self, index=None):
        if index is None:
            index = self._size - 1

        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if self._size == 1:
            item = self._head.item
            self._head = None
            self._tail = None
        else:
            if index == 0:
                item = self._head.item
                self._head.next_node.prev_node = None
                self._head = self._head.next_node
            elif index == self._size - 1:
                item = self._tail.item
                self._tail.prev_node.next_node = None
                self._tail = self._tail.prev_node
            else:
               if index < self._size / 2:
                   sentinel = self._head
                   for i in range(index):
                       sentinel = sentinel.next_node
               else:
                   sentinel = self._tail
                   for i in range(self._size - 1, index, -1):
                       sentinel = sentinel.prev_node

               sentinel.next_node.prev_node = sentinel.prev_node
               sentinel.prev_node.next_node = sentinel.next_node
               item = sentinel.item

        self._size = self._size - 1

        return item

    def read(self, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if index < self._size / 2:
            sentinel = self._head
            for i in range(index):
                sentinel = sentinel.next_node
        else:
            sentinel = self._tail
            for i in range(self._size - 1, index, -1):
                sentinel = sentinel.prev_node

        return sentinel.item

    def index(self, item):
        sentinel = self._head
        if self.is_empty():
            raise ValueError('Item not found.')
        i = 0
        while sentinel.item != item:
            sentinel = sentinel.next_node
            i = i + 1
            if sentinel is None:
                raise ValueError('Item not found.')

        return i

    def write(self, item, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if index < self._size / 2:
            sentinel = self._head
            for i in range(index):
                sentinel = sentinel.next_node
        else:
            sentinel = self._tail
            for i in range(self._size - 1, index, -1):
                sentinel = sentinel.prev_node

        sentinel.item = item


class CircularSingleLinkedList(List):
    """Circular single linked list data structure.

    Args:
        Nothing.

    Attributs (public):
        Nothing.
    """

    class _Node(object):
        """Node class for circular single linked list.

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
        """Iterator for SingleLinkedList.

        Args:
            head (_Node): The head node of the circular list.
            current (_Node): The first element of the circular list.

        Attributs (public):
            head (_Node): The head node of the circular list.
            current (_Node): The first element of the circular list.
        """

        def __init__(self, head, current):
            self.head = head
            self.current = current

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is self.head:
                raise StopIteration

            item = self.current.item
            self.current = self.current.next_node

            return item

    def __init__(self):
        List.__init__(self)
        self._head = self._Node(None,None)
        self._head.next_node = self._head

    def __iter__(self):
        return self._ForwardIterator(self._head, self._head.next_node)

    def insert(self, item, index):
        if (index < -self._size) or (index > self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        for i in range(index):
            sentinel = sentinel.next_node

        new_node = self._Node(item, sentinel.next_node)
        sentinel.next_node = new_node
        self._size = self._size + 1

    def remove(self, item):
        sentinel = self._head
        while sentinel.next_node.item != item:
            sentinel = sentinel.next_node
            if sentinel is self._head:
                raise ValueError('Item not found.')

        sentinel.next_node = sentinel.next_node.next_node
        self._size = self._size - 1

    def pop(self, index=None):
        if index is None:
            index = self._size - 1

        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        for i in range(index):
            sentinel = sentinel.next_node

        item = sentinel.next_node.item
        sentinel.next_node = sentinel.next_node.next_node
        self._size = self._size - 1
        return item

    def read(self, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        for i in range(index):
            sentinel = sentinel.next_node

        return sentinel.next_node.item

    def index(self, item):
        sentinel = self._head
        index = -1
        while sentinel.item != item:
            sentinel = sentinel.next_node
            index = index + 1
            if sentinel is self._head:
                raise ValueError('Item not found.')

        return index

    def write(self, item, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        for i in range(index):
            sentinel = sentinel.next_node

        sentinel.next_node.item = item


class CircularDoubleLinkedList(List):
    """Circular double linked list data structure.

    Args:
        Nothing.

    Attributs (public):
        Nothing.
    """

    class _Node(object):
        """Node class for circular double linked list.

        Args:
            item (object): Item contained in the node.
            next_node (_Node): Pointer to next neighbor node.
            prev_node (_Node): Pointer to previous neighbor node.

        Attributes (public):
            item (object): Item contained in the node.
            next_node (_Node): Pointer to next neighbor node.
            prev_node (_Node): Pointer to previous neighbo node.
        """
        def __init__(self, item, next_node=None, prev_node=None):
            self.item = item
            self.next_node = next_node
            self.prev_node = prev_node

        def __del__(self):
            self.item = None
            self.next_node = None
            self.prev_node = None

    class _ForwardIterator(object):
        """Iterator for CircularDoubleLinkedList.

        Args:
            head (_Node): The head node of the circular list.
            current (_Node): The first element of the circular list.

        Attributs (public):
            head (_Node): The head node of the circular list.
            current (_Node): The first element of the circular list.
        """

        def __init__(self, head, current):
            self.head = head
            self.current = current

        def __iter__(self):
            return self

        def __next__(self):
            if self.current is self.head:
                raise StopIteration

            item = self.current.item
            self.current = self.current.next_node

            return item

    def __init__(self):
        List.__init__(self)
        self._head = self._Node(None,None,None)
        self._head.next_node = self._head
        self._head.prev_node = self._head

    def __iter__(self):
        return self._ForwardIterator(self._head, self._head.next_node)

    def insert(self, item, index):
        if (index < -self._size) or (index > self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        if index < self._size / 2:
            for i in range(index):
                sentinel = sentinel.next_node
        else:
            for i in range(self._size - index + 1):
                sentinel = sentinel.prev_node

        new_node = self._Node(item, sentinel.next_node, sentinel)
        sentinel.next_node.prev_node = new_node
        sentinel.next_node = new_node
        self._size = self._size + 1

    def remove(self, item):
        sentinel = self._head
        while sentinel.item != item:
            sentinel = sentinel.next_node
            if sentinel is self._head:
                raise ValueError('Item not found.')

        sentinel.next_node.prev_node = sentinel.prev_node
        sentinel.prev_node.next_node = sentinel.next_node
        self._size = self._size - 1

    def pop(self, index=None):
        if index is None:
            index = self._size - 1

        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        if index < self._size / 2:
            for i in range(index + 1):
                sentinel = sentinel.next_node
        else:
            for i in range(self._size - index):
                sentinel = sentinel.prev_node

        item = sentinel.item
        sentinel.next_node.prev_node = sentinel.prev_node
        sentinel.prev_node.next_node = sentinel.next_node
        self._size = self._size - 1
        return item

    def read(self, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        if index < self._size / 2:
            for i in range(index + 1):
                sentinel = sentinel.next_node
        else:
            for i in range(self._size - index):
                sentinel = sentinel.prev_node

        return sentinel.item

    def index(self, item):
        sentinel = self._head
        index = -1
        while sentinel.item != item:
            sentinel = sentinel.next_node
            index = index + 1
            if sentinel is self._head:
                raise ValueError('Item not found.')

        return index

    def write(self, item, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = self._head
        if index < self._size / 2:
            for i in range(index + 1):
                sentinel = sentinel.next_node
        else:
            for i in range(self._size - index):
                sentinel = sentinel.prev_node

        sentinel.item = item


class ArrayList(List):
    """Array list data structure.

    Args:
        capacity (int): Initial capacity of the array.

    Attributs (public):
        Nothing.
    """

    class _ForwardIterator(object):
        """Iterator for ArrayList.

        Args:
            array (python list): Container of ArrayList
            head (int): Begining of the ArrayList
            tail (int): End of the ArrayList

        Attributs (public):
            array (python list): Container of ArrayList
            head (int): Begining of the ArrayList
            tail (int): End of the ArrayList
        """

        def __init__(self, array, head, tail):
            self.array = array
            self.head = head
            self.tail = tail

        def __iter__(self):
            return self

        def __next__(self):
            if self.head == self.tail:
                raise(StopIteration)
            item = self.array[self.head]
            self.head = (self.head + 1) % len(self.array)
            return item

    def __init__(self, capacity=2):
        List.__init__(self)
        self._capacity = capacity
        self._array = [None] * self._capacity
        self._head = 0
        self._tail = 0

    def __iter__(self):
        return self._ForwardIterator(self._array, self._head, self._tail)

    def _resize(self):
        new_array = [None] * self._capacity * 2
        i = self._head
        pos = 0
        while i != self._tail:
            new_array[pos] = self._array[i]
            self._array[i] = None
            i = (i + 1) % self._capacity
            pos = pos + 1

        self._capacity = self._capacity * 2
        self._head = 0
        self._tail = self._size
        self._array = new_array

    def capacity(self):
        return self._capacity

    def insert(self, item, index):
        if (index < -self._size) or (index > self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        if self._size + 1 == self._capacity:
            self._resize()

        if index < self._size / 2:
            self._head = (self._head - 1) % self._capacity
            sentinel = self._head
            for i in range(index):
                self._array[sentinel] = self._array[(sentinel + 1) % self._capacity]
                sentinel = (sentinel + 1) % self._capacity
        else:
            sentinel = self._tail
            self._tail = (self._tail + 1) % self._capacity
            for i in range(self._size - index):
                self._array[sentinel] = self._array[(sentinel - 1) % self._capacity]
                sentinel = (sentinel - 1) % self._capacity

        self._array[sentinel] = item
        self._size = self._size + 1

    def remove(self, item):
        self.pop(self.index(item))

    def pop(self, index=None):
        if index is None:
            index = self._size - 1

        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = (self._head + index) % self._capacity
        item = self._array[sentinel]
        if sentinel < self._size / 2:
            while sentinel != self._head:
                self._array[sentinel] = self._array[(sentinel - 1) % self._capacity]
                sentinel = (sentinel - 1) % self._capacity
            self._head = (self._head + 1) % self._capacity
        else:
            self._tail = (self._tail - 1) % self._capacity
            while sentinel != self._tail:
                self._array[sentinel] = self._array[(sentinel + 1) % self._capacity]
                sentinel = (sentinel + 1) % self._capacity

        self._size = self._size - 1
        return item

    def read(self, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = (self._head + index) % self._capacity
        return self._array[sentinel]

    def index(self, item):
        if self.is_empty():
            raise ValueError('Item not found.')

        sentinel = self._head
        index = 0
        while self._array[sentinel] != item:
            sentinel = (sentinel + 1) % self._capacity
            index = index + 1
            if sentinel == self._tail:
                raise ValueError('Item not found.')

        return index

    def write(self, item, index):
        if (index < -self._size) or (index >= self._size):
            raise ValueError('Argument index out of range.')

        if index < 0:
            index = self._size + index

        sentinel = (self._head + index) % self._capacity
        self._array[sentinel] = item