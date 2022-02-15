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
    value = 0
    for index, current_value in enumerate(arr):
        if value < current_value:
            value += current_value
        else:
            return index

if __name__ == '__main__':
    min_search([1, 2, 3])