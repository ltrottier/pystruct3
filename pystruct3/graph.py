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

"""

from pystruct3.list import DoubleLinkedList as _DoubleLinkedList

class Graph(object):
    """
    """

    def __init__(self):
        self._n_vertices = 0
        self._n_edges = 0

    def adjacent(self, vertice1, vertice2):
        """Verify if there is an edge between vertice1 and vertice2

        Args:
            vertice1 (object): The first vertice.
            vertice2 (object): The second vertice.

        Returns:
            bool: True if there is an edge between vertice1 and vertice2,
                  False otherwise.

        Raises:
            ValueError: An error occurs if one of the vertices is not in the
                        Graph.
        """
        raise NotImplementedError

    def neighbors(self, vertice):
        """Lists all vertices that are connected to the given vertice.

        Args:
            vertice (object): The given vertice.

        Returns:
            python list: The list of adjacent neighbors to the given vertice.

        Raises:
            ValueError: An error occurs if vertice is not in the graph.
        """
        raise NotImplementedError

    def vertices(self):
        """Lists all vectices in the graph.

        Args:
            Nothing.

        Returns:
            python list: The list of graph vertices.

        Raises:
            Nothing.
        """
        raise NotImplementedError

    def insert(self, vertice):
        """Insert a vertice to the Graph.

        After insertion, the new vertice is not connected to any nodes.

        Args:
            vertice (object): The given vertice.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs when vertice is already in the graph.
        """
        raise NotImplementedError

    def remove(self, vertice):
        """Remove a vertice from the Graph.

        All connections from/to vertice are deleted.

        Args:
            vertice (object): The given vertice.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs when vertice is not in the graph.
        """
        raise NotImplementedError

    def connect(self, vertice1, vertice2):
        """Insert an edge that goes from vertice1 to vertice2.

        Args:
            vertice1 (object): The first vertice.
            vertice2 (object): The second vertice.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs if one of the vertices is not in the
                        Graph.
        """
        raise NotImplementedError

    def disconnect(self, vertice1, vertice2):
        """Remove the edge that goes from vertice1 to vertice2.

        Args:
            vertice1 (object): The first vertice.
            vertice2 (object): The second vertice.

        Returns:
            Nothing.

        Raises:
            ValueError: An error occurs if one of the vertices is not in the
                        Graph.
            ValueError: An error occurs if the two vertices are not connected.
        """
        raise NotImplementedError

    def n_edges(self):
        """Return the number of edges in the graph.

        Args:
            Nothing.

        Returns:
            int: Number of egdes in the graph.

        Raises:
            Nothing.
        """
        return self._n_edges

    def n_vertices(self):
        """Return the number of vertices in the graph.

        Args:
            Nothing.

        Returns:
            int: Number of vertices in the graph.

        Raises:
            Nothing.
        """
        return self._n_vertices

    def __len__(self):
        return self._n_vertices

    def __repr__(self):
        items = ['{']
        for vertice in self.vertices():
            items.append('[')
            items.append(str(vertice))
            items.append(' -> ')
            for neighbor in self.neighbors(vertice):
                items.append(str(neighbor))
                items.append(', ')
            items.pop()
            items.append(']')
            items.append(',\n ')
        if self.n_vertices() > 0:
            items.pop()
        items.append('}')
        return "".join(items)


class AdjacencyListGraph(Graph):
    """An adjacency list graph is a graph where every vertex stores a
       list of adjacent vertices.
    """

    class _Node(object):
        """Internal node of the graph to save the item and its neighbors.
        """
        def __init__(self, vertice):
            self.vertice = vertice
            self.neighbors = _DoubleLinkedList()

        def __del__(self):
            self.vertice = None
            self.neighbors.clear()

        def __eq__(self, other_node):
            return self.vertice == other_node.vertice

    def __init__(self):
        Graph.__init__(self)
        self.nodes = _DoubleLinkedList()

    def _get_node_from_vertice(self, vertice):
        """Get the node given the vertice.

        This is a private method.

        Args:
            vertice (object): A vertice.

        Returns:
            _Node: The node containing the vertice

        Raises:
            ValueError: An error occurs when vertice is not in the graph.
        """
        for node in self.nodes:
            if node.vertice == vertice:
                return node
        raise ValueError('The vertice is not in the graph.')

    def adjacent(self, vertice1, vertice2):
        node1 = self._get_node_from_vertice(vertice1)
        node2 = self._get_node_from_vertice(vertice2)

        V1toV2 = False
        V2toV1 = False
        for node in node1.neighbors:
            if node == node2:
                V1toV2 = True
        for node in node2.neighbors:
            if node == node1:
                V2toV1 = True

        return V1toV2 or V2toV1

    def neighbors(self, vertice):
        node = self._get_node_from_vertice(vertice)
        return [v for v in node.neighbors]

    def vertices(self):
        return [node.vertice for node in self.nodes]

    def insert(self, vertice):
        self.nodes.append(self._Node(vertice))
        self._n_vertices = self._n_vertices + 1

    def remove(self, vertice):
        self.nodes.remove(self._Node(vertice))
        for node in self.nodes:
            node.neighbors.remove(vertice)
        self._n_vertices = self._n_vertices - 1

    def connect(self, vertice1, vertice2):
        node1 = self._get_node_from_vertice(vertice1)
        self._get_node_from_vertice(vertice2)
        if vertice2 in node1.neighbors:
            raise ValueError('Edge already exists.')
        node1.neighbors.append(vertice2)
        self._n_edges = self._n_edges + 1

    def disconnect(self, vertice1, vertice2):
        node1 = self._get_node_from_vertice(vertice1)
        self._get_node_from_vertice(vertice2)
        try:
            node1.neighbors.remove(vertice2)
        except ValueError as err:
            raise ValueError('Edge does not exists.') from err
        self._n_edges = self._n_edges - 1


class AdjacencyMatrixGraph(Graph):
    """An adjacency matrix graph is a graph where a two-dimensional matrix
       stores edges information, in which the rows represent
       source vertices and columns represent destination vertices.
    """

    def __init__(self):
        Graph.__init__(self)

class IncidenceMatrixGraph(Graph):
    """ An incidence matrix graph is a graph where a two-dimensional matrix
       stores edges information, in which the rows represent the vertices
       and columns represent the edges.
    """

    def __init__(self):
        Graph.__init__(self)

class Tree(Graph):
    """A tree is a directed graph in which: 1. any two vertices are
       connected by exactly one path, 2. there is a node call the source, and
       3. all nodes point away from the source.
    """
    def __init__(self):
        Graph.__init__(self)


class Heap(Tree):
    """A heap is a tree that satisfies the heap property.
    """
    def __init__(self):
        Tree.__init__(self)


class LinkedNodeHeap(Heap):
    """A heap implement with linked nodes.
    """
    def __init__(self):
        Heap.__init__(self)


class ArrayHeap(Heap):
    """A heap implement with an array.
    """
    def __init__(self):
        Heap.__init__(self)