#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

class Vertex:
    def __init__(self, key):
        self.key = key
        self.adjacency = {}
        self.in_degree= 0
        self.out_degree= 0
        self.distance = float('inf')
        self.previous = None
        self.visited = False
        self.f_visited = False
        self.b_visited = False

    def add_neighbor(self, neighbor, weight=1):
        if neighbor:
            neighbor.in_degree += 1
            self.adjacency[neighbor] = weight
            self.out_degree += 1

    def get_connections(self):
        return self.adjacency.keys()

    def get_weight(self, neighbor):
        return self.adjacency.get(neighbor)

    def is_connected_to(self, dest):
        return dest in self.adjacency

    def __str__(self):
        #connections = str([item.key for item in self.adjacency])
        #return str(self.key) + ' connected to: {}'.format(connections)
        return str(self.key)


if __name__ == '__main__':
    v1 = Vertex(1)
    v2 = Vertex(2)
    v3 = Vertex(3)
    v4 = Vertex(4)

    neighbours = []
    neighbours.extend([v2, v3, v4])

    for item in neighbours:
        v1.add_neighbor(item, 10)

    print(v1)


