#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def cocktail_sort(data_list):
    if data_list:
        length = len(data_list)
        left = 0
        right = length - 1

        while left < right:
            last_right_swap = 0
            for i in range(left, right):
                if data_list[i] > data_list[i+1]:
                    data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
                    last_right_swap = i
            right = last_right_swap

            last_left_swap = 0
            for i in range(right, left, -1):
                if data_list[i] < data_list[i-1]:
                    data_list[i], data_list[i-1] = data_list[i-1], data_list[i]
                    last_left_swap = i
            left = last_left_swap

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(cocktail_sort(copy.copy(data)))

