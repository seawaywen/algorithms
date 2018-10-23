#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import UnDirectGraph, Graph
from traverse import (
    bfs_with_queue,
    dfs,
    traversal
)


words = [
    'foul', 'fool', 'cool', 'pool', 'poll', 'pole', 'pall',
    'fall', 'fail', 'foil', 'pope', 'pale', 'sale', 'page',
    'sage'
]

def build_word_ladder_graph(words):
    """each word in list we compare the word with each bucket,
    using the ‘_’ as a wildcard, so both “pope” and “pops” would match “pop_.”
    """
    d = {}
    g = UnDirectGraph()

    for word in words:
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    #for k, v in d.items():
    #    print('%s=%s' % (k, v))

    for bucket in d.keys():
        for w1 in d[bucket]:
            for w2 in d[bucket]:
                if w1 != w2:
                    g.add_edge(w1, w2)
    return g



if __name__ == '__main__':

    g = build_word_ladder_graph(words)

    for v in g:
        for w in v.get_connections():
            print('(%s, %s)' % (v.key, w.key))

    print('vertices num:%s' % g.vertices_num)
    print('edge num:%s' % g.edge_num)

    # from `sage` to `fool`
    parent = bfs_with_queue(g, 'fool')
    for k, v in parent.items():
        print('{} - parent:{}'.format(k.key, v))
    print(traversal(g, 'sage', parent))

    print('*' * 40)
    parent = dfs(g, 'fool')
    print(traversal(g, 'sage', parent))
