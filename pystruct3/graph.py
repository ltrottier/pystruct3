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

    def __del__(self):
        """Destroy the graph.
        """
        self.clear()

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
        """Lists all vertices that are adjacent to the given vertice.

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

    def is_empty(self):
        """Verify if the graph contains vertices.

        Does not modify the graph.

        Args:
            Nothing.

        Returns:
            bool: True if the graph contains no vertices, False otherwise.

        Raises:
            Nothing.
        """
        return self._n_vertices == 0

    def equal(self, other_graph):
        """Graph equality.

        The graphs are equal if they have 1. the same vertices and 2. the same
        adjacency matrix.

        Args:
            other_graph (Graph): The other graph.

        Returns:
            bool: True if the two graphs are equal, False otherwise.

        Raises:
            Nothing.
        """
        vertices1 = self.vertices()
        vertices2 = other_graph.vertices()
        if len(vertices1) != len(vertices2):
            return False
        for vi in vertices1:
            if vi not in vertices2:
                return False
        for vi in vertices1:
            for vj in vertices1:
                if self.adjacent(vi,vj) != other_graph.adjacent(vi,vj):
                    return False
        return True

    def copy(self):
        """Deep copy of the graph.

        Args:
            Nothing.

        Returns:
            Graph: A deep copy of the graph

        Raises:
            Nothing.
        """
        copy_graph = self.__class__()
        for v in self.vertices():
            copy_graph.insert(v)
        for vi in self.vertices():
            for vj in self.vertices():
                if copy_graph.adjacent(vi,vj) != self.adjacent(vi,vj):
                    copy_graph.connect(vi,vj)
        return copy_graph

    def clear(self):
        """Remove all vertices from the graph.

        Args:
            Nothing.

        Returns:
            Nothing.

        Raises:
            Nothing.
        """
        for v in self.vertices():
            self.remove(v)

    def __len__(self):
        return self._n_vertices

    def __eq__(self, other_graph):
        return self.equal(other_graph)

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
        for v in node1.neighbors:
            if v == node2.vertice:
                V1toV2 = True
        for v in node2.neighbors:
            if v == node1.vertice:
                V2toV1 = True

        return V1toV2 or V2toV1

    def neighbors(self, vertice):
        node = self._get_node_from_vertice(vertice)
        neig = [v for v in node.neighbors]
        for node in self.nodes:
            if ((node.vertice != vertice) and (vertice in node.neighbors)
                and (node.vertice not in neig)):
                neig.append(node.vertice)
        return neig

    def vertices(self):
        return [node.vertice for node in self.nodes]

    def insert(self, vertice):
        new_node = self._Node(vertice)
        if new_node in self.nodes:
            raise ValueError('Vertice already in the graph.')
        self.nodes.append(new_node)
        self._n_vertices = self._n_vertices + 1

    def remove(self, vertice):
        try:
            self.nodes.remove(self._Node(vertice))
        except ValueError as err:
            raise ValueError('Vertice not in the graph.') from err
        for node in self.nodes:
            try:
                node.neighbors.remove(vertice)
            except ValueError:
                pass
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