from typing import List
from operator import lt, gt


def sort(container: List[int], asc: bool = True, inplace=True) -> List[int]:
    """
    Sort input container with bubble sort
    :param asc если тру по возрастанию если фолс по убыванию
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not inplace:
        container = container.copy()
    offset = 1  # смещение относительно конца списка
    compare_operator = gt if asc else lt
    for i in range(len(container)):
        is_exchange = False  # не было замены элементов
        for j in range(len(container) - offset):
            if compare_operator(container[j], container[j + 1]):
                container[j], container[j + 1] = container[j + 1], container[j]
                is_exchange = True
        if not is_exchange:
            break
        offset += 1
    return container


if __name__ == '__main__':
    print(sort([1, 2, 3], asc=False))

    list_ = [3, 2, 1]
    sorted_copy = sort(list_, inplace=False)
    print(list_)
    print(sorted_copy)
