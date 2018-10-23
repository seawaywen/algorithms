#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import Graph


def is_cyclic_direct_graph(g):
    visited = set()
    parent = set()
    for node in g:
        if node not in visited:
            if is_cyclic_visit(g, node, visited, parent) == True:
                return True

    return False

def is_cyclic_visit(g, node, visited, parent):
    visited.add(node)
    parent.add(node)

    for neighbor in node.get_connections():
        if neighbor not in visited:
            if is_cyclic_visit(g, neighbor, visited, parent) == True:
                return True
        # we can say if the adjacent vertex is visited and
        # it's not parent of the current vertex
        elif neighbor in parent:
            return True

    parent.remove(node)
    return False

def is_cyclic_direct_graph_with_color(g):
    """
    WHITE : Vertex is not processed yet.  Initially
        all vertices are WHITE.

    GRAY : Vertex is being processed (DFS for this
        vertex has started, but not finished which means
        that all descendants (ind DFS tree) of this vertex
        are not processed yet (or this vertex is in function
        call stack)

    BLACK : Vertex and all its descendants are
            processed.

    While doing DFS, if we encounter an edge from current
    vertex to a GRAY vertex, then this edge is back edge
    and hence there is a cycle.
    """
    color = ['WHITE'] * g.vertices_num

    for i in range(g.vertices_num):
        if color[i] == 'WHITE':
            if cyclic_util(g, i, color) == True:
                return True
    return False

def cyclic_util(g, u, color):
    color[u] = 'GRAY'

    for v in g.get_vertex(u).get_connections():
        if color[v.key] == 'GRAY':
            return True

        if color[v.key] == 'WHITE' and cyclic_util(g, v.key, color) == True:
            return True

    color[u] = 'BLACK'
    #print(color)
    return False


if __name__ == '__main__':

    g = Graph()
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    #g.add_edge(2, 1)
    #g.add_edge(2, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    print(is_cyclic_direct_graph(g))
    print(is_cyclic_direct_graph_with_color(g))
