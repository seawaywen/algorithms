#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def insert_sort(data_list):
    if data_list:
        length = len(data_list)
        for i in range(length):
            key = data_list[i]
            j = i - 1
            while j >= 0:
                if data_list[j] > key:
                    data_list[j], data_list[j+1] = key, data_list[j]
                j -= 1
    return data_list

def insert_recursive_sort(data_list, i):
    if data_list:
        if i == 0:
            return

        insert_recursive_sort(data_list, i - 1)

        j = i
        while j > 0:
            if data_list[j] < data_list[j-1]:
                data_list[j], data_list[j-1] = data_list[j-1], data_list[j]
            j -= 1

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(insert_sort(copy.copy(data)))
print(insert_recursive_sort(copy.copy(data), RANDOM_LENGTH - 1))
