#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def gap_insert_sort(data_list, start, gap):
    if data_list:
        for i in range(start+gap, len(data_list), gap):
            key = data_list[i]
            j = i - gap
            while j >= 0:
                if data_list[j] > key:
                    data_list[j], data_list[j+gap] = key, data_list[j]
                j -= gap
    return data_list


def shell_sort(data_list, step=2):
    if data_list:
        length = len(data_list)

        sub_list_count = length // step

        while sub_list_count > 0:
            for i in range(sub_list_count):
                gap_insert_sort(data_list, i, sub_list_count)

            sub_list_count //= step

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(shell_sort(copy.copy(data)))
