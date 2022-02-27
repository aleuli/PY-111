from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    def lazy_stair_way_path(stair_number: int) -> Union[int, float]:
        """Принимаем номер ступени.Возвращаем ступень до нее."""

        if stair_number == 0:
            return stairway[stair_number]
        if stair_number == 1:
            return stairway[stair_number]

        current_cost = stairway[stair_number]
        return current_cost + min(lazy_stair_way_path(stair_number - 1),
                                  lazy_stair_way_path(stair_number - 2))

    return lazy_stair_way_path(len(stairway) - 1)


    # return reverse_stairway_path(stairway)

def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    count_stars = len(stairway)
    total_coast = [0] * count_stars

    total_coast[0] = stairway[0]
    total_coast[1] = stairway[1]

    for i in range(2, count_stars):
        total_coast[i] = stairway[i] + min(total_coast[i - 1], total_coast[i - 2])

    return total_coast[-1]


def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    count_stars = len(stairway)
    total_coast: list[float] = [float("inf")] * count_stars

    total_coast[0] = stairway[0]
    total_coast[1] = stairway[1]

    for i in range(0, count_stars):
        if i + 1 < count_stars:
            total_coast[i + 1] = min(total_coast[i] + stairway[i + 1], total_coast[i + 1])

        if i + 2 < count_stars:
            total_coast[i + 2] = min(total_coast[i] + stairway[i + 2], total_coast[i + 2])

    return total_coast[-1]
