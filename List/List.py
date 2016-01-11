#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
__author__ = "Ludovic Trottier"
__license__ = "MIT"
__date__ = "Sun Jan 10 12:47:32 2016"


class List:
    def __init__(self):
        self._size = 0
        self._head = None
    
    def insert(self, item, pos):
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
    
    def isEmpty(self):
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
        if not self.isEmpty():
            s = s[:-2]
        s = s + "]"           
        return s


class ForwardIterator:
    def __init__(self, node):
        self.node = node
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.node == None:
            raise StopIteration
            
        item = self.node.item
        self.node = self.node.nextNode
        
        return item
        
class SingleLinkedList(List):
    
    class Node:
        def __init__(self, item, nextNode=None):
            self.item = item
            self.nextNode = nextNode    
            
    def __init__(self):
        List.__init__(self)
    
    def insert(self, item, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")
        
        if pos > self.size():
            raise ValueError("Argument pos must be lower than or equal to the list size.")
        
        if self.isEmpty():
            self._head = SingleLinkedList.Node(item)
        else:            
            sentinel = self._head
            if pos == 0:
                newNode = SingleLinkedList.Node(item, self._head)
                self._head = newNode
            else:                
                for i in range(pos-1):
                    sentinel = sentinel.nextNode
                
                newNode = SingleLinkedList.Node(item, sentinel.nextNode)
                sentinel.nextNode = newNode
        
        self._size = self._size + 1

    def remove(self, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")
        
        if pos >= self.size():
            raise ValueError("Argument pos must be lower than the list size.")
        
        if pos == 0:
            temp = self._head
            self._head = self._head.nextNode
            temp.nextNode = None
            temp = None
        else:
            sentinel = self._head
            for i in range(pos-1):
                sentinel = sentinel.nextNode
            temp = sentinel.nextNode
            sentinel.nextNode = sentinel.nextNode.nextNode
            temp.nextNode = None
            temp = None
    
        self._size = self._size - 1
        
    def read(self, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")
        
        if pos >= self.size():
            raise ValueError("Argument pos must be lower than the list size.")
        
        sentinel = self._head
        for i in range(pos):
            sentinel = sentinel.nextNode
        
        return sentinel.item

    def index(self, item):
        sentinel = self._head
        if self.isEmpty():
            raise ValueError("Item not found.")
        i = 0
        while sentinel.item != item:
            sentinel = sentinel.nextNode
            i = i + 1
            if sentinel == None:
                raise ValueError("Item not found.")
        
        return i
    
    def write(self, item, pos):
        if pos < 0:
            raise ValueError("Argument pos must be positive.")
        
        if pos >= self.size():
            raise ValueError("Argument pos must be lower than the list size.")
        
        sentinel = self._head
        for i in range(pos):
            sentinel = sentinel.nextNode
        
        sentinel.item = item
    
class DoubleLinkedList(List):
    
    class Node:
        def __init__(self, item, nextNode):
            self.item = item
            self.nextNode = nextNode
            
    def __init__(self):
        List.__init__(self)
    
    def insert(self, item, pos):
        print("dll")
        if pos < 0:
            raise ValueError("Argument pos must be positive.")
        
        if pos > self.size():
            raise ValueError("Argument pos must be lower than the list size.")

    