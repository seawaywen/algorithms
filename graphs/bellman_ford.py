#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import (
    Graph,
    UnDirectGraph
)


def relax(current_vertex, neighbor):
    weight = current_vertex.get_weight(neighbor)
    new_distance = current_vertex.distance + weight
    if neighbor.distance > new_distance:
        print(f'update current={current_vertex.key}:{current_vertex.distance} next={neighbor.key}:{neighbor.distance} new_distance:{new_distance}')
        neighbor.distance = new_distance
        neighbor.previous = current_vertex
    else:
        print(f'NOT update current={current_vertex.key}:{current_vertex.distance} next={neighbor.key}:{neighbor.distance} new_distance:{new_distance}')


def shortest(v, path):
    if v.previous:
        path.append(v.previous.key)
        shortest(v.previous, path)
    return


def bellman_ford(g, start_key):
    start = g.get_vertex(start_key)
    start.distance = 0
    if start is None:
        return

    for i in range(g.vertices_num):
        for current_vertex in g:
            for neighbor in current_vertex.get_connections():
                relax(current_vertex, neighbor)

    for u in g:
        print(f'{u.key}:{u.distance}')
        for neighbor in u.get_connections():
            weight = u.get_weight(neighbor)
            #print(f'----{neighbor.key}:{neighbor.distance} - weight:{weight}')
            if neighbor.distance > u.distance + weight:
                print(f'!!!!{u.key}:{u.distance} - {neighbor.key}:{neighbor.distance} - weight:{weight}')
                print('There\'s negative weight cycle')
                return True
        return False


if __name__ == '__main__':

    #g = Graph()
    g = UnDirectGraph()
    with open('g_data.txt') as f:
        for line in f:
            s, t, w = (line.strip().split(' '))
            g.add_edge(s, t, int(w))
    """
    g = UnDirectGraph()
    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)
    """

    #Example test data:
    #'a': {'b': -1, 'c':  4},
    #'b': {'c':  3, 'd':  2, 'e':  2},
    #'c': {},
    #'d': {'b':  1, 'c':  5},
    #'e': {'d': -3}
    """
    g = Graph()
    g.add_edge('a', 'b', -1)
    g.add_edge('a', 'c', 4)
    g.add_edge('b', 'c', 3)
    g.add_edge('b', 'd', 2)
    g.add_edge('b', 'e', 2)
    g.add_edge('d', 'b', 1)
    g.add_edge('d', 'c', 5)
    g.add_edge('e', 'd', -3)
    """

    print('*' * 20)
    print("Bellman Ford ")
    print('*' * 20)
    negative_cycle = bellman_ford(g, 'a')

    if not negative_cycle:
        target = g.get_vertex('j')
        if target is None:
            print('j not exits')
        else:
            path = [target.key]
            shortest(target, path)
            print(path)
            print(f'Short path BF: {path[::-1]}')
