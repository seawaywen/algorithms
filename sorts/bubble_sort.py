#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def forward_bubble_sort(data_list):
    if data_list:
        length = len(data_list)
        for i in range(length):
            for j in range(i+1, length):
                if data_list[i] > data_list[j]:
                    data_list[i], data_list[j] = data_list[j], data_list[i]

    return data_list

def backward_bubble_sort(data_list):
    if data_list:
        length = len(data_list)
        for i in range(length - 1, 1, -1):
            for j in range(0, i):
                if data_list[i] < data_list[j]:
                    data_list[i], data_list[j] = data_list[j], data_list[i]
    return data_list

RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(forward_bubble_sort(copy.copy(data)))
print(backward_bubble_sort(copy.copy(data)))

