#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def selection_sort(data_list):
    if data_list:
        length = len(data_list)
        for i in range(length):
            i_min = i
            for j in range(i+1, length):
                if data_list[j] < data_list[i_min]:
                    i_min = j
            if data_list[i] > data_list[i_min]:
                data_list[i], data_list[i_min] = data_list[i_min], data_list[i]

    return data_list

def selection_recursive_sort(data_list, i):
    if data_list:
        if i == 0: return

        i_max = i
        for j in range(i):
            if data_list[j] > data_list[i_max]:
                i_max = j

        if data_list[i] < data_list[i_max]:
            data_list[i], data_list[i_max] = data_list[i_max], data_list[i]

        selection_recursive_sort(data_list, i - 1)

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(selection_sort(copy.copy(data)))
print(selection_recursive_sort(copy.copy(data), RANDOM_LENGTH - 1))
