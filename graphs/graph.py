#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from vertex import Vertex


class Graph:
    def __init__(self):
        self.vertices = {}
        self.vertices_num = 0
        self.edge_num = 0

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        return None

    def add_vertex(self, key):
        vertex = self.get_vertex(key)
        if vertex is None:
            new_vertex = Vertex(key)
            self.vertices[key] = new_vertex
            self.vertices_num += 1
            return new_vertex
        return vertex

    def add_edge(self, src_key, dest_key, weight=1):
        src = self.add_vertex(src_key)
        dest = self.add_vertex(dest_key)

        src.add_neighbor(dest, weight)
        return src, dest

    def has_edge(self, src_key, dest_key):
        src = self.add_vertex(src_key)
        dest = self.add_vertex(dest_key)
        if src and dest:
            return src.is_connected_to(dest)

    def get_vertices(self):
        return self.vertices.keys()

    def __contains__(self, n):
        return n in self.vertices

    def __iter__(self):
        return iter(self.vertices.values())


class UnDirectGraph(Graph):

    def add_edge(self, src_key, dest_key, weight=-1):
        src, dest = super().add_edge(src_key, dest_key, weight)

        dest.add_neighbor(src, weight)
        self.edge_num += 1


if __name__ == '__main__':
    g = Graph()
    for i in range(10):
        g.add_vertex(i)

    print(g.vertices)
    print('-' * 10)

    g.add_edge(0, 1, 4)
    g.add_edge(0, 5, 2)
    g.add_edge(1, 2, 7)
    g.add_edge(2, 3, 3)
    g.add_edge(2, 5, 9)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 5, 1)

    for v in g:
        for w in v.get_connections():
            print('(%s, %s)' % (v.key, w.key))

    print('verteice num:%s' % g.vertices_num)
