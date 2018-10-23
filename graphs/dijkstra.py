#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq
import time

from graph import (
    UnDirectGraph
)


def relax(current_vertex, neighbor, enable_log=False):
    weight = current_vertex.get_weight(neighbor)
    new_distance = current_vertex.distance + weight
    if neighbor.distance > new_distance:
        if enable_log:
            print(f'update current={current_vertex.key}:{current_vertex.distance} next={neighbor.key}:{neighbor.distance} new_distance:{new_distance}')
        neighbor.distance = new_distance
        neighbor.previous = current_vertex
    else:
        if enable_log:
            print(f'NOT update current={current_vertex.key}:{current_vertex.distance} next={neighbor.key}:{neighbor.distance} new_distance:{new_distance}')


def dijkstra(g, start_key, end_key=None):
    start = g.get_vertex(start_key)
    start.distance = 0
    if start is None:
        return

    end = None
    if end_key:
        end = g.get_vertex(end_key)

    pq = [(v.distance, v.key) for v in g]
    heapq.heapify(pq)

    visited_path = []
    while len(pq):
        min_vertex_distance, min_vertex_key = heapq.heappop(pq)
        min_vertex = g.get_vertex(min_vertex_key)

        # if we already found the target, quit the loop safely here now
        if end is not None and min_vertex is end:
            break

        if min_vertex.visited:
            continue

        min_vertex.visited = True
        visited_path.append(min_vertex_key)

        for neighbor in min_vertex.get_connections():
            if neighbor.visited:
                #print(f'neighbor {neighbor.key} is visited!')
                continue

            relax(min_vertex, neighbor)

        while len(pq):
            heapq.heappop(pq)

        pq = [(v.distance, v.key) for v in g if not v.visited]
        heapq.heapify(pq)

    return visited_path



def dijkstra_improved(g, start_key, end_key=None):
    start = g.get_vertex(start_key)
    start.distance = 0
    if start is None:
        return

    end = None
    if end_key:
        end = g.get_vertex(end_key)

    # only put the start vertex initally
    pq = [(start.distance, start_key)]
    heapq.heapify(pq)

    visited_path = []
    while len(pq):
        min_vertex_distance, min_vertex_key = heapq.heappop(pq)
        min_vertex = g.get_vertex(min_vertex_key)

        # if we already found the target, quit the loop safely here now
        if end is not None and min_vertex is end:
            break

        if min_vertex.visited:
            continue

        min_vertex.visited = True
        visited_path.append(min_vertex_key)

        for neighbor in min_vertex.get_connections():
            if neighbor.visited:
                #print(f'neighbor {neighbor.key} is visited!')
                continue

            relax(min_vertex, neighbor)

            # push the updated nodes with the new distance, although we have the
            # duplicated nodes in the priority queue, but we only interested in the low
            # priority nodes
            heapq.heappush(pq, (neighbor.distance, neighbor.key))

    return visited_path

def shortest(v, path):
    if v.previous:
        path.append(v.previous)
        shortest(v.previous, path)
    return


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


    print('\n')
    print('*' * 20)
    print("Dijkstra")
    print('*' * 20)
    g = init_graph()
    target = g.get_vertex(end_vertex_key)
    path = [target]

    start = time.time()
    visited_path = dijkstra(g, start_vertex_key, end_vertex_key)
    shortest(target, path)
    path = [i.key for i in path]
    print(f'The shortest path: {path[::-1]}, cost:{target.distance}')
    visited_path = '->'.join(visited_path)
    print(f'visited path: {visited_path}')
    end = time.time() - start
    print(f'run time:{end}')


    print('*' * 20)
    print("Improved Dijkstra")
    print('*' * 20)
    g = init_graph()
    target = g.get_vertex(end_vertex_key)
    path = [target]

    start = time.time()
    visited_path = dijkstra_improved(g, start_vertex_key, end_vertex_key)
    shortest(target, path)
    path = [i.key for i in path]
    print(f'The shortest path: {path[::-1]}, cost:{target.distance}')
    visited_path = '->'.join(visited_path)
    print(f'visited path: {visited_path}')
    end = time.time() - start
    print(f'run time:{end}')
