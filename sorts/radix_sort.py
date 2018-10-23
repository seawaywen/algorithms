#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def radix_sort(data_list, base=10):
    def list_to_buckets(data_list, base, iteration):
        buckets = [[] for i in range(base)]
        for number in data_list:
            digit = (number // (base ** iteration)) % base
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        result = []
        for bucket in buckets:
            if bucket:
                result.extend([i for i in bucket])
        return result

    if data_list:
        max_number = max(data_list)
        iteration = 0
        while base ** iteration < max_number:
            buckets = list_to_buckets(data_list, base, iteration)
            data_list = buckets_to_list(buckets)
            iteration += 1

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(radix_sort(copy.copy(data)))
