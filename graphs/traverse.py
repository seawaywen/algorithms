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

def traversal(g, end_key, parent):
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

def topological_sort(g):
    stack = []
    parent = {}

    for i in g:
        print(f'{i}-in:{i.in_degree} out:{i.out_degree}')
        if i.in_degree == 0:
            topological_visit(i, stack, parent)

    print('->'.join([str(s.key) for s in stack]))

def topological_visit(u, stack, parent):
    for v in u.get_connections():
        if v not in parent:
            parent[v] = u
            topological_visit(v, stack, parent)

    stack.insert(0, u)

def all_topological_sort(g):
    """Get all the topological sortings in a DAG(Directed Acylic Graph)
    """
    visited = []
    in_degree = {}
    for i in g:
        in_degree[i] = i.in_degree
        for v in i.get_connections():
            in_degree[v] = v.in_degree

    all_topological_visit(g, in_degree, visited)

def all_topological_visit(g, in_degree, visited):
    flag = False
    for i in g:
        # choose those vertex has 0 degree and not visted yet
        if i not in visited and in_degree[i] == 0:
            visited.append(i)

            for v in i.get_connections():
                in_degree[v] -= 1

            all_topological_visit(g, in_degree, visited)

            # resetting here for backtracking
            visited.remove(i)
            for v in i.get_connections():
                in_degree[v] += 1
            flag = True

    if not flag:
        print('->'.join([str(s.key) for s in visited]))

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
    print(traversal(g, 'e', parent))

    g = init_graph()
    print('*** BFS')
    parent = bfs(g, 'd')
    print(traversal(g, 'e', parent))

    print('*** BFS with queue')
    parent = bfs_with_queue(g, 'd')
    print(traversal(g, 'e', parent))

    print('*' * 40)
    print('*** Topological sort')
    g = Graph()
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    topological_sort(g)
    print('-' * 20)
    print('*** All topological sorts')
    all_topological_sort(g)

