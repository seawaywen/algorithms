#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def merge_sort(data_list):
    if data_list:
        length = len(data_list)
        if length < 2:
            return

        mid = length // 2

        left_part = data_list[:mid]
        right_part = data_list[mid:]
        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                data_list[k] = left_part[i]
                i += 1
            else:
                data_list[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            data_list[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            data_list[k] = right_part[j]
            j += 1
            k += 1

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(merge_sort(copy.copy(data)))
