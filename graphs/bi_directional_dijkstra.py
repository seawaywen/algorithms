#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import heapq
from itertools import cycle
import time

from graph import (
    UnDirectGraph
)
from dijkstra import relax, shortest


def idijkstra(g, start_key):
    start = g.get_vertex(start_key)
    start.distance = 0
    if start is None:
        return

    pq = [(start.distance, start_key)]
    heapq.heapify(pq)

    while len(pq):
        min_vertex_distance, min_vertex_key = heapq.heappop(pq)
        min_vertex = g.get_vertex(min_vertex_key)
        if min_vertex.visited:
            continue

        min_vertex.visited = True
        yield min_vertex

        for neighbor in min_vertex.get_connections():
            if neighbor.visited:
                #print(f'neighbor {neighbor.key} is visited!')
                continue

            relax(min_vertex, neighbor, enable_log=False)
            heapq.heappush(pq, (neighbor.distance, neighbor.key))


def bi_directional_dijstra(g, start_key, end_key=None):
    Ds, Dt = {}, {}

    g1 = copy.deepcopy(g)
    g2 = copy.deepcopy(g)
    forward = idijkstra(g1, start_key)
    backward = idijkstra(g2, end_key)

    dirs = (Ds, Dt, forward), (Dt, Ds, backward)

    try:
        for D, other, step in cycle(dirs):
            v = next(step)

            D[v.key] = v.distance

            if v.key in other:
                break
    except StopIteration:
        return float('inf')

    intermediate_node = None
    cost = float('Inf')
    for u_key in Ds:
        u = g1.get_vertex(u_key)
        if u:
            for v in u.get_connections():
                if v.key not in Dt:
                    continue

                if cost > Ds[u.key] + u.get_weight(v) + Dt[v.key]:
                    cost = min(cost, Ds[u.key] + u.get_weight(v) + Dt[v.key])
                    # record the meeting node with lowest distance
                    intermediate_node = u
                    #print(intermediate_node.key, v.key, cost)

    print(f'Forward and Backward meet at node:{intermediate_node.key}!')

    # shortest path in forward list part(including the intermediate node)
    forward_path = []
    node = g1.get_vertex(intermediate_node.key)
    forward_path.append(node)
    shortest(node, forward_path)
    forward_path.reverse()
    print(f'forward path:{[i.key for i in forward_path]}')

    # skip the intermediate_node since it's already in forward list
    backward_path = []
    node = g2.get_vertex(intermediate_node.key)
    shortest(node, backward_path)
    print(f'backward path:{[i.key for i in backward_path]}')

    forward_path.extend(backward_path)

    return forward_path, cost


def init_graph():
    g = UnDirectGraph()
    with open('g_data.txt') as f:
        for line in f:
            s, t, w = (line.strip().split(' '))
            g.add_edge(s, t, int(w))
    return g


if __name__ == '__main__':
    start_vertex_key = 'a'
    end_vertex_key = 'j'

    print('*' * 20)
    print("iDijkstra")
    print('*' * 20)
    g = init_graph()


    start = time.time()
    j = idijkstra(g, start_vertex_key)

    while True:
        try:
            v = next(j)
        except StopIteration:
            break

    target = g.get_vertex(end_vertex_key)
    path = [target]
    shortest(target, path)
    path = [i.key for i in path]
    print('The shortest path : %s' %(path[::-1]))
    end = time.time() - start
    print(f'run time:{end}')


    print('\n')
    print('*' * 20)
    print("bi_directional Dijkstra")
    print('*' * 20)
    g = init_graph()

    start = time.time()
    path, cost = bi_directional_dijstra(g, start_vertex_key, end_vertex_key)
    print(f'The shotest path-->{[i.key for i in path]}, cost is {cost}')
    end = time.time() - start
    print(f'run time:{end}')
