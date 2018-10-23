#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random

def heapify(data_list, index, heap_size):
    i_max = index
    i_left = 2 * index + 1
    i_right = 2 * index + 2

    if i_left < heap_size and data_list[i_left] > data_list[index]:
        i_max = i_left
    if i_right < heap_size and data_list[i_right] > data_list[i_max]:
        i_max = i_right

    if i_max != index:
        data_list[i_max], data_list[index] = data_list[index], data_list[i_max]
        heapify(data_list, i_max, heap_size)


def build_heap(data_list):
    heap_size = len(data_list)
    parent = (heap_size - 1) // 2
    for i in range(parent - 1, -1, -1):
        heapify(data_list, i, heap_size)

def heap_sort(data_list):
    if data_list:
        heap_size = len(data_list)

        build_heap(data_list)

        for i in range(heap_size - 1, 0, -1):
            data_list[0], data_list[i] = data_list[i], data_list[0]
            heapify(data_list, 0, i)

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(heap_sort(copy.copy(data)))
