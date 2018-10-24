#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search_recursive(data_list, key):
    """Recursive binary search for the given sorted integer list.
    Simple call the recursive helper
    Args:
        data_list: sorted integer list
        key: the integer to be searched
    Returns:
        the first found key's index in the list
    """
    if not isinstance(data_list, (list, tuple)):
        print('invalid data list')
        return -1

    return binary_search_recursive_helper(
        data_list, key, 0, len(data_list) - 1)

def binary_search_recursive_helper(data_list, key, low, high):
    """Recursive binary search helper for the given sorted integer list

    Args:
        data_list: sorted integer list
        key: the integer to be searched
        low: list lowest index
        high: list highest index
    Returns:
        the first found key's index in the list
    """
    if low > high:
        return -1

    mid = low + ((high - low) >> 1)
    if data_list[mid] == key:
        return mid
    else:
        if data_list[mid] < key:
            return binary_search_recursive_helper(
                data_list, key, mid + 1, high)
        else:
            return binary_search_recursive_helper(
                data_list, key, low, mid - 1)



def binary_search_iterative(data_list, key):
    """Iterative binary search for the given sorted integer list

    Args:
        data_list: sorted integer list
        key: the integer to be searched
    Returns:
        the first found key's index in the list
    """
    if not isinstance(data_list, (list, tuple)):
        print('invalid data list')
        return -1

    length = len(data_list)
    if length == 0:
        return -1

    low = 0
    high = length - 1
    while low <= high:
        # following calc may cause the overflow if number is big enough
        #mid = (low + high) // 2
        # alternitive 1:
        #mid = low + (high - low) // 2
        # alternitive 2:
        mid = low + ((high - low) >> 1)

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

    #case3: non-existed element(low bound number)
    print(binary_search_recursive(data, -100))
    print(binary_search_iterative(data, -100))

    #case4: non-existed element(high bound number)
    print(binary_search_iterative(data, 1001))
    print(binary_search_recursive(data, 1001))

    #case5: invalid data list
    print(binary_search_iterative(12, 1001))
    print(binary_search_recursive(12, 1001))

