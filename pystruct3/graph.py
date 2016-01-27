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


Graph (abstract) -->

    Undirected Graph -->

        AdjacencyListUndirectedGraph

        Tree -->



    Directed Graph -->

        AdjacencyListDirectedGraph

        DirectedRootedTree -->

            BinaryDirectedRootedTree -->

                Heap -->

                    LinkedNodeHeap
                    ArrayHeap



"""

class Graph(object):
    """
    """

    def __init__(self):
        self._n_nodes = 0

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
        """Insert an edge between vertice1 and vertice2.

        If the graph is directed, the edge goes from vertices 1 to vertice2.

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
        """Remove the edge between vertice1 and vertice2.

        If the graph is directed, the edge goes from vertices1 to vertice2.

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

    def n_nodes(self):
        """Return the number of nodes in the graph.

        Args:
            Nothing.

        Returns:
            int: Number of nodes in the graph.

        Raises:
            Nothing.
        """
        return self._n_nodes

    def n_edges(self):
        """Return the number of edges in the graph.

        Args:
            Nothing.

        Returns:
            int: Number of egdes in the graph.

        Raises:
            Nothing.
        """
        raise NotImplementedError



class AdjacencyListGraph(Graph):
    """An adjacency list graph is a graph where every vertex stores a
       list of adjacent vertices.
    """

    def __init__(self):
        Graph.__init__(self)


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