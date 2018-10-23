#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import deque

from graph import UnDirectGraph, Graph


def bfs(g, start_key):
    start = g.get_vertex(start_key)
    if start is None:
        return

    level = {start: 0}
    parent = {start: None}
    frontier = [start]
    i = 1

    while frontier:
        next = []
        for u in frontier:
            for v in u.get_connections():
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
            #print('next:{}'.format(str([j.key for j in next])))

        frontier = next
        i += 1

    return parent


def bfs_with_queue(g, start_key):
    start = g.get_vertex(start_key)
    if start is None:
        return

    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)

    parent = {start: None}
    levels = {start: 0}
    while len(q) > 0:
        current = q.popleft()
        for neighbour in current.get_connections():
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = current
                levels[neighbour] = levels[current] + 1
                q.append(neighbour)

    return parent


def dfs(g, start_key):
    start = g.get_vertex(start_key)
    if start is None:
        return

    parent = {start: None}
    dfs_visit(start, parent)
    return parent

def dfs_visit(start, parent):
    for v in start.get_connections():
        if v not in parent:
            parent[v] = start
            dfs_visit(v, parent)

def traversal(end_key, parent):
    end = g.get_vertex(end_key)

    path = []
    while parent.get(end):
        path.append(end)
        end = parent.get(end)
    path.append(end)

    shortest_path = []
    while len(path) > 0:
       shortest_path.append(path.pop().key)
    return '->'.join(shortest_path)


def init_graph():
    g = UnDirectGraph()
    with open('g_data.txt') as f:
        for line in f:
            s, t, w = (line.strip().split(' '))
            g.add_edge(s, t, int(w))
    return g

if __name__ == '__main__':

    print('-' * 40)
    g = init_graph()
    parent = dfs(g, 'd')
    print(traversal('e', parent))

    g = init_graph()
    print('*** BFS')
    parent = bfs(g, 'd')
    print(traversal('e', parent))

    print('*** BFS with queue')
    parent = bfs_with_queue(g, 'd')
    print(traversal('e', parent))
