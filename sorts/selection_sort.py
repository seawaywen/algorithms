#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def quick_sort(data_list, left, right):
    if data_list:
        if left >= right:
            return
        low = left
        high = right
        pivot = data_list[left]

        while left < right:
            while left < right and data_list[right] >= pivot:
                right -= 1
            data_list[left] = data_list[right]

            while left < right and data_list[left] <= pivot:
                left += 1
            data_list[right] = data_list[left]

        data_list[left] = pivot

        quick_sort(data_list, low, left - 1)
        quick_sort(data_list, left + 1, high)

    return data_list


def partition(data_list, left, right):
    pivot = left
    for i in range(left+1, right+1):
        if data_list[i] < data_list[left]:
            pivot += 1
            data_list[i], data_list[pivot] = data_list[pivot], data_list[i]
    data_list[left], data_list[pivot] = data_list[pivot], data_list[left]
    return pivot

def quick_sort1(data_list, left, right):
    if data_list:
        if left >= right:
            return

        pivot = partition(data_list, left, right)
        quick_sort1(data_list, left, pivot - 1)
        quick_sort1(data_list, pivot + 1, right)

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(quick_sort(copy.copy(data), 0, RANDOM_LENGTH - 1))
print(quick_sort1(copy.copy(data), 0, RANDOM_LENGTH - 1))
