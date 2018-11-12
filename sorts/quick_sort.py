#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import random

"""
Quicksort is one of the divide and conquer algorithm.

A pivot will be selected in the array to do the partition:
    1. All elements that smaller than pivot will be moved before the pivot
    2. All elements that greater than pivot will be moved after the pivot
Above 2 steps can be done in linear time. O(N)
Recursively apply above steps to the above 2 sub-arrays(one containes
all the smaller values than pivot, the other one contains the greater
values than pivot)

Quicksort is unstable sort.


* Average time complexity: O(n*logn)
* Best time complexity: O(n*logn)
* Bad time complexity: O(n*n)

Although the worst-case performace is O(n*n), but it's rare.

Recurrence relation:
    T(n) = O(n) + T(0) + T(n-1) = O(n) + T(n-1)
A single quicksort call involves O(n) work + 2 recursive call on 0 and n-1)
    T(n) = O(n) + 2T(n/2)
         = O(nlgn)

Quicksort is faster on average compare to the heapsort and mergesort, but worse
than them in worst case.
Although they(quicksort, heapsort and mergesort) have the same asymptotic complexity.
because:
    1. operations in the innermost loop are simpler in quicksort
    2. it can make excellent usage of memory hierachy, take perfect advantage of virutal memory
    and available caches.
    3. quicksort makes more recursive calls ,but allocating stack space is cheap than allocate
    a giant block on the heap.


In Don Knuth's "The Art of Computer Programming", he found the average case
results for the many algorithms, e.g.

Quicksort: 11.667(n+1)log(n)−1.74n−18.74
Mergesort: 12.5nlg(n)
Heapsort: 16nlg(n)+0.01n
Insertionsort: 2.25n2+7.75n−3lg(n)

Analyse the swap and key comparisions:
    In Robert Swdgewicks' "Algorithms" book:

Quicksort: 2nlg(n) comparisons and 13nlg(n) swaps on average
Mergesort: 1.44nlg(n) comparisons, but up to 8.66nlg(n) array accesses
    (mergesort is not swap based, so we cannot count that).
Insertionsort: 14lg2 comparisons and 14n2 swaps on average.

"""

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
