#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search_recursive(data_list, key):
    """Recursive binary search for the given sorted integer list

    Args:
        data_list: sorted integer list
        key: the integer to be searched
    Returns:
        the first found key's index in the list
    """
    length = len(data_list)
    if length == 0:
        return -1

    mid = length // 2
    if key == data_list[mid]:
        return mid

    if key < data_list[mid]:
        return binary_search_recursive(data_list[:mid], key)
    else:
        return mid + 1 + binary_search_recursive(data_list[mid+1:], key)


def binary_search_iterative(data_list, key):
    """Iterative binary search for the given sorted integer list

    Args:
        data_list: sorted integer list
        key: the integer to be searched
    Returns:
        the first found key's index in the list
    """
    length = len(data_list)
    if length == 0:
        return -1

    low = 0
    high = length - 1
    while low <= high:
        mid = (low + high) // 2

        if data_list[mid] == key:
            return mid
        else:
            if key < data_list[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return -1


if __name__ == '__main__':

    data = [2, 3, 4, 5, 7, 7, 12, 15, 32, 53, 60, 100]

    #case1: normal case
    print(binary_search_recursive(data, 60))
    print(binary_search_iterative(data, 60))

    #case2: duplicated elements
    print(binary_search_recursive(data, 7))
    print(binary_search_iterative(data, 7))

    #case3: non-existed element
    print(binary_search_recursive(data, -100))
    print(binary_search_iterative(data, -100))

