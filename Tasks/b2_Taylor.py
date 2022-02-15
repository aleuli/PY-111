"""
Taylor series
"""
from typing import Union
import math
from itertools import count


EPSILON = 0.0001


def get_item(x, n):
    return x ** n / math.factorial(n)


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    summ = 1
    for n in count(1, 1):
        current_item = get_item(x, n)
        summ += current_item
        if current_item <= EPSILON:
            break
    return summ


def get_item_sin(x, n):
    return -1 ** (n - 1) * x ** (2 * (n - 1) / math.factorial(2 * (n - 1))


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    summ = 1
    for n in count(1, 1):
        current_item = get_item_sin(x, n)
        summ += current_item
        print(summ)
        if current_item <= EPSILON:
            return summ

if __name__ == '__main__':
    print(sinx(5))
    print(math.sin(5))