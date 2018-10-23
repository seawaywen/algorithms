#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random


def buckets_sort(data_list, mod_number=10):
    if data_list:
        max_number = max(data_list)

        buckets = [[] for i in range(max_number // mod_number + 1)]
        for number in data_list:
            buckets[number // mod_number].append(number)

        for i, bucket in enumerate(buckets):
            buckets[i] = sorted(bucket)

        result = []
        for bucket in buckets:
            if bucket:
                result.extend([i for i in bucket])
        return result

    return data_list


RANDOM_LENGTH = 10
RANDOM_RANGE = 100

data = random.sample(range(RANDOM_RANGE), RANDOM_LENGTH)
print(data)
print(buckets_sort(copy.copy(data)))
