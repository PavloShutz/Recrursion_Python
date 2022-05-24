from typing import Union


def refactored_sum_of_lists(lists: list) -> Union[int, float]:
    return sum([number if not isinstance(number, list)
                else refactored_sum_of_lists(number)
                for number in lists])
