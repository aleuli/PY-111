from typing import List
from random import choice


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not container:
        return container

    pivot_element = choice(container)

    return sort([value for value in container if value < pivot_element])\
           + [value for value in container if value == pivot_element]\
           + sort([value for value in container if value > pivot_element])
