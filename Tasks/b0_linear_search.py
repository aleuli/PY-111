"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_value = arr[0]
    index_ = 0
    for index, value in enumerate(arr):
        if value < min_value:
            min_value = value
            index_ = index
            continue
    return index_
